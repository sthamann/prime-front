import Lake
open Lake DSL

/--
Per-`lean`-process memory ceiling in MB, handed to Lean as `-M`.

Sizing rationale: Lake 5 has no `-j` flag, so a plain `lake build` fans out
over every core (32 on the reference machine). The generated
`TfptCarrier/WallLadder/RungKz*.lean` certificates each drive a single
kernel `decide` over a packed 66k-limb Cholesky witness and peak at
21-36 GB, so an uncapped parallel build exhausted 512 GB of RAM, saturated
the VM compressor and tripped the kernel's WindowServer watchdog (hard
reset). The default below keeps even a full 32-way fan-out inside physical
RAM at the cost of failing the rung modules, which must instead be built
serially via `scripts/build_wall_ladder.sh`.

Override per invocation, e.g. `lake build -K leanMemoryMb=49152 <target>`,
but only for a build that is known to be serialised.
-/
def leanMemoryMb : String :=
  (get_config? leanMemoryMb).getD "12288"

package «TfptCarrier» where
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩,
    ⟨`autoImplicit, false⟩
  ]
  -- `-M` bounds the elaborator/kernel allocation budget without changing the
  -- emitted olean, so it belongs in `weakLeanArgs`: raising or lowering the
  -- ceiling must not invalidate build traces and force a Mathlib-wide rebuild.
  weakLeanArgs := #["-M", leanMemoryMb]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.29.1"

@[default_target]
lean_lib «TfptCarrier» where
