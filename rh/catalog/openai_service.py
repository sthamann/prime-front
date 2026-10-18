#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OpenAI helper for the RH semantic catalog (stdlib urllib + json).

Loads OPENAI_API_KEY from the environment, else ~/.config/tfpt/openai.env,
else a repo-root .env only when `git check-ignore -q .env` succeeds.

Assumed prices (USD per 1M tokens; edit PRICE_TABLE / EMBED_PRICE_TABLE):
  gpt-5-nano / gpt-4.1-nano          in 0.10  out 0.40
  gpt-4o-mini                        in 0.15  out 0.60
  gpt-5-mini                         in 0.25  out 2.00
  gpt-4.1-mini                       in 0.40  out 1.60
  o4-mini / o3-mini                  in 1.10  out 4.40
  text-embedding-3-small             0.02
  text-embedding-3-large             0.13
Unknown chat ids use in 0.15 / out 0.60. Cached hits are free.

NO RH CLAIM. Never print the API key.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(CATALOG_DIR, "..", ".."))
HOME_ENV = os.path.join(os.path.expanduser("~"), ".config", "tfpt", "openai.env")
API_ROOT = "https://api.openai.com"
DEFAULT_CACHE_DIR = os.path.join(CATALOG_DIR, "cache")
CACHE_NAME = "llm_cache.jsonl"
KEY_RE = re.compile(r"sk-[A-Za-z0-9_-]{20,}")
RETRY_AFTER_RE = re.compile(r"try again in ([0-9.]+)\s*(ms|s)", re.I)
MINI_NANO_RE = re.compile(r"(mini|nano)", re.I)
CHAT_EXCLUDE = (
    "embed",
    "whisper",
    "tts",
    "dall-e",
    "dall-e",
    "davinci",
    "babbage",
    "ada-",
    "audio",
    "realtime",
    "image",
    "moderation",
    "transcribe",
    "sora",
    "search",
    "computer-use",
    "codex",
)
# USD per 1M tokens: (input, output). Edit when prices change.
PRICE_TABLE = {
    "gpt-5-nano": (0.10, 0.40),
    "gpt-4.1-nano": (0.10, 0.40),
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-5-mini": (0.25, 2.00),
    "gpt-4.1-mini": (0.40, 1.60),
    "o4-mini": (1.10, 4.40),
    "o3-mini": (1.10, 4.40),
}
DEFAULT_CHAT_PRICE = (0.15, 0.60)
EMBED_PRICE_TABLE = {
    "text-embedding-3-small": 0.02,
    "text-embedding-3-large": 0.13,
}
DEFAULT_EMBED_PRICE = 0.02
CLASSIFY_IN_TOKENS = 700
CLASSIFY_OUT_TOKENS = 180
EMBED_TOKENS_PER_RECORD = 80
CHARS_PER_TOKEN = 4.0
EMBED_BATCH = 96
TIMEOUT_S = 60
MAX_RETRIES = 8
MIN_REQUEST_INTERVAL_S = 0.85
WORD_LIMIT_RATIONALE = 40
WORD_LIMIT_SHORT = 30


class RateLimiter:
    def __init__(self, min_interval):
        self.min_interval = float(min_interval)
        self._next = 0.0
        self._lock = threading.Lock()

    def wait(self):
        with self._lock:
            now = time.time()
            delay = max(0.0, self._next - now)
            self._next = now + delay + self.min_interval
        if delay > 0:
            time.sleep(delay)

    def backoff(self, seconds):
        with self._lock:
            self._next = max(self._next, time.time() + float(seconds))


class BudgetExceeded(RuntimeError):
    """Raised when the running cost estimate would exceed budget_usd."""


class OpenAIError(RuntimeError):
    """HTTP or protocol failure (key already redacted)."""


def redact(text):
    return KEY_RE.sub("sk-[REDACTED]", str(text))


def clip_words(text, limit):
    words = (text or "").split()
    return " ".join(words[:limit])


def _read_env_file(path):
    if not path or not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for raw in fh:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("export "):
                    line = line[7:].strip()
                if not line.startswith("OPENAI_API_KEY="):
                    continue
                value = line.split("=", 1)[1].strip().strip("'").strip('"')
                return value or None
    except OSError:
        return None
    return None


def _repo_dotenv_allowed():
    env_path = os.path.join(REPO, ".env")
    if not os.path.isfile(env_path):
        return False
    try:
        rc = subprocess.call(
            ["git", "check-ignore", "-q", ".env"],
            cwd=REPO,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        return False
    return rc == 0


def resolve_api_key():
    """Return (key, source) or (None, None). Never prints the key."""
    env = os.environ.get("OPENAI_API_KEY") or ""
    if env.strip():
        return env.strip(), "env"
    home = _read_env_file(HOME_ENV)
    if home:
        return home, "home"
    if _repo_dotenv_allowed():
        repo_key = _read_env_file(os.path.join(REPO, ".env"))
        if repo_key:
            return repo_key, "repo-dotenv"
    return None, None


def key_resolves():
    key, _src = resolve_api_key()
    return bool(key)


def _sha256_json(obj):
    blob = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def estimate_tokens(text):
    return max(1, int(len(text or "") / CHARS_PER_TOKEN))


def chat_price(model):
    return PRICE_TABLE.get(model, DEFAULT_CHAT_PRICE)


def embed_price(model):
    return EMBED_PRICE_TABLE.get(model, DEFAULT_EMBED_PRICE)


def is_chat_candidate(model_id):
    low = (model_id or "").lower()
    if not MINI_NANO_RE.search(low):
        return False
    if any(tok in low for tok in CHAT_EXCLUDE):
        return False
    if "embed" in low:
        return False
    return True


def pick_chat_model(model_ids):
    candidates = [m for m in model_ids if is_chat_candidate(m)]
    if not candidates:
        return None

    def rank(mid):
        inp, out = chat_price(mid)
        nano = 0 if "nano" in mid.lower() else 1
        known = 0 if mid in PRICE_TABLE else 1
        return (known, inp, out, nano, mid)

    return sorted(candidates, key=rank)[0]


def pick_embed_model(model_ids):
    found = [m for m in model_ids if m.startswith("text-embedding-3-")]
    if not found:
        found = [m for m in model_ids if "embedding" in m.lower()]
    if not found:
        return None
    if "text-embedding-3-small" in found:
        return "text-embedding-3-small"
    return sorted(found, key=lambda m: (embed_price(m), len(m), m))[0]


def taxonomy_schema(taxonomy):
    kinds = sorted((taxonomy.get("kinds") or {}).keys())
    families = sorted((taxonomy.get("families") or {}).keys())
    outcomes = sorted((taxonomy.get("outcomes") or {}).keys())
    failures = sorted((taxonomy.get("failure_classes") or {}).keys())
    relevances = sorted((taxonomy.get("rh_relevances") or {}).keys())
    confidences = sorted((taxonomy.get("confidence") or {}).keys())
    props = {
        "kind": {"type": "string", "enum": kinds},
        "family": {"type": "string", "enum": families},
        "family_secondary": {
            "type": "array",
            "items": {"type": "string", "enum": families},
        },
        "outcome": {"type": "string", "enum": outcomes},
        "failure_class": {"type": "string", "enum": failures},
        "rh_relevance": {"type": "string", "enum": relevances},
        "question": {"type": "string"},
        "mechanism": {"type": "string"},
        "reusable": {"type": "string"},
        "confidence": {"type": "string", "enum": confidences},
        "rationale": {"type": "string"},
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": props,
        "required": list(props.keys()),
    }


def classify_system_prompt(taxonomy):
    def enum_block(title, mapping):
        lines = [title + ":"]
        for key, desc in (mapping or {}).items():
            lines.append("- %s: %s" % (key, desc))
        return "\n".join(lines)

    return (
        "Classify one RH-corpus catalogue record. Research documentation only. "
        "NO RH CLAIM in either direction. Use only the supplied enums.\n\n"
        + enum_block("kind", taxonomy.get("kinds"))
        + "\n\n"
        + enum_block("family", taxonomy.get("families"))
        + "\n\n"
        + enum_block("outcome", taxonomy.get("outcomes"))
        + "\n\n"
        + enum_block("failure_class", taxonomy.get("failure_classes"))
        + "\n\n"
        + enum_block("rh_relevance", taxonomy.get("rh_relevances"))
        + "\n\n"
        "question and mechanism: <=30 words each. reusable: <=30 words or empty. "
        "rationale: <=40 words. family_secondary: 0-4 other families, no duplicate of family. "
        "confidence: low if inferred, med if artefact-backed, high only if verbatim."
    )


def classify_user_prompt(record):
    keys = (
        "path",
        "round",
        "role",
        "status_raw",
        "kind",
        "family",
        "outcome",
        "failure_class",
        "rh_relevance",
        "question",
        "mechanism",
        "result_verdict",
        "solved",
        "failed_because",
        "reusable",
    )
    lines = ["Classify this catalogue record. Do not invent ledger ids."]
    for key in keys:
        val = record.get(key)
        if val is None or val == "" or val == []:
            continue
        lines.append("%s: %s" % (key, val))
    return "\n".join(lines)


def normalize_classification(payload, taxonomy):
    kinds = set((taxonomy.get("kinds") or {}))
    families = set((taxonomy.get("families") or {}))
    outcomes = set((taxonomy.get("outcomes") or {}))
    failures = set((taxonomy.get("failure_classes") or {}))
    relevances = set((taxonomy.get("rh_relevances") or {}))
    confidences = set((taxonomy.get("confidence") or {}))
    family = payload.get("family") if payload.get("family") in families else "OTHER"
    secondary = []
    for item in payload.get("family_secondary") or []:
        if item in families and item != family and item not in secondary:
            secondary.append(item)
    out = {
        "kind": payload.get("kind") if payload.get("kind") in kinds else "OTHER",
        "family": family,
        "family_secondary": secondary[:4],
        "outcome": payload.get("outcome") if payload.get("outcome") in outcomes else "OPEN",
        "failure_class": (
            payload.get("failure_class")
            if payload.get("failure_class") in failures
            else "NOT_APPLICABLE"
        ),
        "rh_relevance": (
            payload.get("rh_relevance")
            if payload.get("rh_relevance") in relevances
            else "INFRASTRUCTURE"
        ),
        "question": clip_words(payload.get("question") or "", WORD_LIMIT_SHORT),
        "mechanism": clip_words(payload.get("mechanism") or "", WORD_LIMIT_SHORT),
        "reusable": clip_words(payload.get("reusable") or "", WORD_LIMIT_SHORT),
        "confidence": (
            payload.get("confidence") if payload.get("confidence") in confidences else "low"
        ),
        "rationale": clip_words(payload.get("rationale") or "", WORD_LIMIT_RATIONALE),
    }
    return out


class OpenAIService:
    def __init__(
        self,
        model=None,
        embed_model=None,
        budget_usd=5.0,
        cache_dir=None,
        dry_run=False,
    ):
        self.dry_run = bool(dry_run)
        self.budget_usd = float(budget_usd)
        self.spent_usd = 0.0
        self.cache_dir = os.path.abspath(cache_dir or DEFAULT_CACHE_DIR)
        self.cache_path = os.path.join(self.cache_dir, CACHE_NAME)
        self._cache = {}
        self._lock = threading.Lock()
        self._limiter = RateLimiter(MIN_REQUEST_INTERVAL_S)
        self._key, self.key_source = resolve_api_key()
        self._model_ids = []
        env_model = os.environ.get("TFPT_OPENAI_MODEL") or None
        env_embed = os.environ.get("TFPT_OPENAI_EMBED_MODEL") or None
        self.model = model or env_model
        self.embed_model = embed_model or env_embed
        self._load_cache()
        if self.dry_run:
            self.model = self.model or "gpt-4.1-nano"
            self.embed_model = self.embed_model or "text-embedding-3-small"
            sys.stderr.write(
                "openai: dry-run models chat=%s embed=%s budget=%.2f\n"
                % (self.model, self.embed_model, self.budget_usd)
            )
            return
        if not self._key:
            raise OpenAIError(
                "OPENAI_API_KEY not found (env, ~/.config/tfpt/openai.env, "
                "or ignored repo .env)"
            )
        self._select_models()
        sys.stderr.write(
            "openai: chat=%s embed=%s source=%s budget=%.2f\n"
            % (self.model, self.embed_model, self.key_source, self.budget_usd)
        )

    def _load_cache(self):
        if not os.path.isfile(self.cache_path):
            return
        try:
            with open(self.cache_path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    digest = row.get("sha256")
                    if digest:
                        self._cache[digest] = row
        except OSError:
            return

    def _write_cache(self, digest, kind, request, response, usage, cost):
        os.makedirs(self.cache_dir, exist_ok=True)
        row = {
            "sha256": digest,
            "kind": kind,
            "request": request,
            "response": response,
            "usage": usage,
            "cost_usd": cost,
        }
        with self._lock:
            self._cache[digest] = row
            with open(self.cache_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    def _charge(self, cost, label):
        with self._lock:
            projected = self.spent_usd + cost
            if projected > self.budget_usd + 1e-12:
                raise BudgetExceeded(
                    "budget %.4f USD exceeded (spent=%.4f next=%.4f %s)"
                    % (self.budget_usd, self.spent_usd, cost, label)
                )
            self.spent_usd = projected

    def _http(self, method, path, body=None):
        url = API_ROOT + path
        data = None
        headers = {"Authorization": "Bearer " + self._key}
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        last_err = None
        for attempt in range(MAX_RETRIES):
            self._limiter.wait()
            req = urllib.request.Request(url, data=data, method=method, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                    raw = resp.read().decode("utf-8")
                    return json.loads(raw)
            except urllib.error.HTTPError as exc:
                raw = ""
                try:
                    raw = exc.read().decode("utf-8", errors="replace")
                except Exception:
                    raw = ""
                last_err = OpenAIError(
                    redact("HTTP %s %s: %s" % (exc.code, path, raw[:800]))
                )
                last_err.status = exc.code
                last_err.body = redact(raw)
                if exc.code in (429, 500, 502, 503, 504) and attempt + 1 < MAX_RETRIES:
                    wait = min(20.0, 2.0 ** attempt)
                    match = RETRY_AFTER_RE.search(raw)
                    if match:
                        val = float(match.group(1))
                        parsed = val / 1000.0 if match.group(2).lower() == "ms" else val
                        wait = max(wait, parsed + 0.25)
                    header = exc.headers.get("Retry-After") if exc.headers else None
                    if header:
                        try:
                            wait = max(wait, float(header))
                        except ValueError:
                            pass
                    self._limiter.backoff(wait)
                    time.sleep(wait)
                    continue
                raise last_err
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_err = OpenAIError(redact("%s %s: %s" % (type(exc).__name__, path, exc)))
                if attempt + 1 < MAX_RETRIES:
                    time.sleep(min(16.0, 2.0 ** attempt))
                    continue
                raise last_err
        raise last_err or OpenAIError("request failed")

    def list_models(self):
        if self.dry_run:
            ids = [
                "gpt-4.1-nano",
                "gpt-4.1-mini",
                "gpt-4o-mini",
                "text-embedding-3-small",
                "text-embedding-3-large",
            ]
            self._model_ids = ids
            return ids
        payload = self._http("GET", "/v1/models")
        ids = sorted(
            item.get("id")
            for item in (payload.get("data") or [])
            if isinstance(item, dict) and item.get("id")
        )
        self._model_ids = ids
        return ids

    def _select_models(self):
        if not self._model_ids:
            self.list_models()
        if not self.model:
            self.model = pick_chat_model(self._model_ids) or "gpt-4o-mini"
        if not self.embed_model:
            self.embed_model = pick_embed_model(self._model_ids) or "text-embedding-3-small"

    def estimate_cost(self, n_records):
        n = int(n_records)
        if not self.model or not self.embed_model:
            if self.dry_run:
                self.model = self.model or "gpt-4.1-nano"
                self.embed_model = self.embed_model or "text-embedding-3-small"
            elif self._key:
                self._select_models()
        cin, cout = chat_price(self.model)
        chat_usd = n * (CLASSIFY_IN_TOKENS * cin + CLASSIFY_OUT_TOKENS * cout) / 1e6
        embed_usd = n * EMBED_TOKENS_PER_RECORD * embed_price(self.embed_model) / 1e6
        return {
            "n_records": n,
            "chat_model": self.model,
            "embed_model": self.embed_model,
            "assumed_chat_usd_per_1m": {"input": cin, "output": cout},
            "assumed_embed_usd_per_1m": embed_price(self.embed_model),
            "assumed_tokens": {
                "classify_in": CLASSIFY_IN_TOKENS,
                "classify_out": CLASSIFY_OUT_TOKENS,
                "embed_per_record": EMBED_TOKENS_PER_RECORD,
            },
            "chat_usd": round(chat_usd, 6),
            "embed_usd": round(embed_usd, 6),
            "total_usd": round(chat_usd + embed_usd, 6),
            "budget_usd": self.budget_usd,
            "spent_usd": round(self.spent_usd, 6),
        }

    def _usage_cost(self, kind, model, usage, fallback_in, fallback_out):
        usage = usage or {}
        if kind == "embed":
            tokens = int(usage.get("prompt_tokens") or usage.get("total_tokens") or fallback_in)
            return tokens * embed_price(model) / 1e6, tokens, 0
        inp = int(
            usage.get("prompt_tokens")
            or usage.get("input_tokens")
            or fallback_in
        )
        out = int(
            usage.get("completion_tokens")
            or usage.get("output_tokens")
            or fallback_out
        )
        cin, cout = chat_price(model)
        return (inp * cin + out * cout) / 1e6, inp, out

    def _cached_or_call(self, kind, request, invoke, fallback_in, fallback_out):
        digest = _sha256_json({"kind": kind, "request": request})
        with self._lock:
            hit = self._cache.get(digest)
        if hit:
            return hit.get("response"), True, 0.0
        if self.dry_run:
            return None, False, 0.0
        cin, _cout = chat_price(self.model if kind != "embed" else self.embed_model)
        if kind == "embed":
            preview = fallback_in * embed_price(self.embed_model) / 1e6
        else:
            preview = (
                fallback_in * cin + fallback_out * chat_price(self.model)[1]
            ) / 1e6
        self._charge(preview, kind)
        response = invoke()
        usage = response.get("usage") or {}
        actual, _inp, _out = self._usage_cost(
            kind, request.get("model"), usage, fallback_in, fallback_out
        )
        with self._lock:
            self.spent_usd = max(0.0, self.spent_usd - preview + actual)
        self._write_cache(digest, kind, request, response, usage, actual)
        return response, False, actual

    def _parse_chat_content(self, payload):
        choices = payload.get("choices") or []
        if choices:
            msg = choices[0].get("message") or {}
            content = msg.get("content")
            if isinstance(content, list):
                bits = []
                for item in content:
                    if isinstance(item, dict) and item.get("type") in ("text", "output_text"):
                        bits.append(item.get("text") or "")
                    elif isinstance(item, dict) and "text" in item:
                        bits.append(item.get("text") or "")
                content = "".join(bits)
            if content:
                return content
        for item in payload.get("output") or []:
            for block in item.get("content") or []:
                if block.get("type") in ("output_text", "text") and block.get("text"):
                    return block["text"]
        text = payload.get("output_text")
        if text:
            return text
        raise OpenAIError("no JSON content in model response")

    def chat_json(self, system, user, schema, max_tokens=400):
        if not self.model and not self.dry_run:
            self._select_models()
        request = {
            "model": self.model,
            "system": system,
            "user": user,
            "schema_name": (schema or {}).get("title") or "catalog_record",
            "schema": schema,
            "max_tokens": max_tokens,
        }
        fallback_in = estimate_tokens(system) + estimate_tokens(user) + 40
        if self.dry_run:
            self._charge(0.0, "chat-dry-run")
            return {
                "dry_run": True,
                "model": self.model,
                "estimated_input_tokens": fallback_in,
                "estimated_output_tokens": max_tokens,
            }

        def invoke_chat():
            body = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "response_format": {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "catalog_record",
                        "strict": True,
                        "schema": schema,
                    },
                },
            }
            try:
                body["max_tokens"] = int(max_tokens)
                return self._http("POST", "/v1/chat/completions", body)
            except OpenAIError as exc:
                msg = str(exc).lower()
                if "max_tokens" in msg or "max_completion_tokens" in msg:
                    body.pop("max_tokens", None)
                    body["max_completion_tokens"] = int(max_tokens)
                    return self._http("POST", "/v1/chat/completions", body)
                if getattr(exc, "status", None) in (400, 404) or "response_format" in msg:
                    resp_body = {
                        "model": self.model,
                        "input": [
                            {"role": "system", "content": system},
                            {"role": "user", "content": user},
                        ],
                        "max_output_tokens": int(max_tokens),
                        "text": {
                            "format": {
                                "type": "json_schema",
                                "name": "catalog_record",
                                "strict": True,
                                "schema": schema,
                            }
                        },
                    }
                    return self._http("POST", "/v1/responses", resp_body)
                raise

        payload, cached, _cost = self._cached_or_call(
            "chat", request, invoke_chat, fallback_in, max_tokens
        )
        if payload is None:
            return {"dry_run": True, "model": self.model}

        def parse_payload(item):
            raw = self._parse_chat_content(item)
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.strip("`")
                if raw.lower().startswith("json"):
                    raw = raw[4:]
                raw = raw.strip()
            return json.loads(raw)

        try:
            parsed = parse_payload(payload)
        except (json.JSONDecodeError, OpenAIError):
            digest = _sha256_json({"kind": "chat", "request": request})
            with self._lock:
                self._cache.pop(digest, None)
            max_tokens = max(int(max_tokens) * 2, 800)
            payload = invoke_chat()
            try:
                parsed = parse_payload(payload)
            except json.JSONDecodeError as exc:
                raise OpenAIError(redact("invalid JSON from model: %s" % exc))
            cached = False
        parsed["_cached"] = cached
        parsed["_model"] = self.model
        return parsed

    def embed(self, texts):
        if not self.embed_model and not self.dry_run:
            self._select_models()
        vectors = [None] * len(texts)
        pending = []
        for idx, text in enumerate(texts):
            request = {"model": self.embed_model, "input": text}
            digest = _sha256_json({"kind": "embed", "request": request})
            with self._lock:
                hit = self._cache.get(digest)
            if hit:
                vec = ((hit.get("response") or {}).get("data") or [{}])[0].get("embedding")
                if vec:
                    vectors[idx] = vec
                    continue
            pending.append((idx, text, request, digest))
        if self.dry_run:
            dim = 8
            for idx, text, request, digest in pending:
                vectors[idx] = [0.0] * dim
            return vectors
        for start in range(0, len(pending), EMBED_BATCH):
            chunk = pending[start : start + EMBED_BATCH]
            body = {
                "model": self.embed_model,
                "input": [row[1] for row in chunk],
            }
            fallback_in = sum(estimate_tokens(row[1]) for row in chunk)
            preview = fallback_in * embed_price(self.embed_model) / 1e6
            self._charge(preview, "embed")

            def invoke(body=body):
                return self._http("POST", "/v1/embeddings", body)

            payload = invoke()
            usage = payload.get("usage") or {}
            actual, _inp, _out = self._usage_cost(
                "embed", self.embed_model, usage, fallback_in, 0
            )
            with self._lock:
                self.spent_usd = max(0.0, self.spent_usd - preview + actual)
            data = sorted(payload.get("data") or [], key=lambda row: row.get("index", 0))
            if len(data) != len(chunk):
                raise OpenAIError("embed batch size mismatch")
            for local_i, row in enumerate(chunk):
                idx, text, request, digest = row
                vec = data[local_i].get("embedding")
                if not vec:
                    raise OpenAIError("missing embedding vector")
                vectors[idx] = vec
                one = {
                    "object": "list",
                    "data": [{"embedding": vec, "index": 0}],
                    "usage": {"prompt_tokens": estimate_tokens(text)},
                }
                self._write_cache(digest, "embed", request, one, one["usage"], 0.0)
        return vectors

    def classify_record(self, record, taxonomy):
        schema = taxonomy_schema(taxonomy)
        system = classify_system_prompt(taxonomy)
        user = classify_user_prompt(record)
        if self.dry_run:
            return {
                "kind": "OTHER",
                "family": "OTHER",
                "family_secondary": [],
                "outcome": "OPEN",
                "failure_class": "NOT_APPLICABLE",
                "rh_relevance": "INFRASTRUCTURE",
                "question": clip_words(record.get("question") or "", WORD_LIMIT_SHORT),
                "mechanism": clip_words(record.get("mechanism") or "", WORD_LIMIT_SHORT),
                "reusable": clip_words(record.get("reusable") or "", WORD_LIMIT_SHORT),
                "confidence": "low",
                "rationale": "dry-run; no API call",
                "_dry_run": True,
                "_model": self.model,
            }
        payload = self.chat_json(system, user, schema, max_tokens=800)
        classified = normalize_classification(payload, taxonomy)
        classified["_cached"] = bool(payload.get("_cached"))
        classified["_model"] = payload.get("_model") or self.model
        return classified


def load_taxonomy(path=None):
    tax_path = path or os.path.join(CATALOG_DIR, "taxonomy.json")
    with open(tax_path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_catalog_records(path=None):
    cat_path = path or os.path.join(CATALOG_DIR, "rh_semantic_catalog.json")
    with open(cat_path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    if isinstance(payload, list):
        return payload
    return payload.get("records") or []


def find_record(records, needle):
    for rec in records:
        path = rec.get("path") or ""
        if path == needle or path.endswith(needle):
            return rec
    return None


def _print_json(obj):
    sys.stdout.write(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


def main(argv=None):
    argv = list(argv if argv is not None else sys.argv[1:])
    dry = "--dry-run" in argv
    argv = [a for a in argv if a != "--dry-run"]
    if not argv or argv[0] in ("-h", "--help"):
        sys.stdout.write(
            "usage: openai_service.py [--dry-run] --key-ok | --list-models | "
            "--estimate N | --classify PATH\n"
        )
        return 0
    cmd = argv[0]
    if cmd == "--key-ok":
        key, src = resolve_api_key()
        if not key:
            sys.stdout.write("key: missing\n")
            return 1
        sys.stdout.write("key: ok (%s)\n" % src)
        return 0
    svc = OpenAIService(dry_run=dry)
    if cmd == "--list-models":
        ids = svc.list_models()
        if not dry:
            svc._select_models()
        sys.stdout.write(
            "models=%d chat=%s embed=%s\n" % (len(ids), svc.model, svc.embed_model)
        )
        return 0
    if cmd == "--estimate":
        n = int(argv[1]) if len(argv) > 1 else 0
        _print_json(svc.estimate_cost(n))
        return 0
    if cmd == "--classify":
        if len(argv) < 2:
            sys.stderr.write("need a record path\n")
            return 2
        rec = find_record(load_catalog_records(), argv[1])
        if rec is None:
            sys.stderr.write("record not found: %s\n" % argv[1])
            return 2
        out = svc.classify_record(rec, load_taxonomy())
        _print_json(out)
        sys.stderr.write("spent_usd=%.6f\n" % svc.spent_usd)
        return 0
    sys.stderr.write("unknown command\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
