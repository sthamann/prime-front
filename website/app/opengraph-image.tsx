import { ImageResponse } from "next/og";
export const alt="Prime Front · independent prime-number research";
export const size={width:1200,height:630}; export const contentType="image/png";
export default function Image(){return new ImageResponse(<div style={{display:"flex",flexDirection:"column",justifyContent:"space-between",width:"100%",height:"100%",padding:70,background:"#fcfbf8",color:"#173d38",borderTop:"14px solid #245e53"}}><div style={{fontSize:25,letterSpacing:8}}>INDEPENDENT MATHEMATICAL RESEARCH</div><div style={{fontSize:112,fontFamily:"serif"}}>Prime Front.</div><div style={{fontSize:35,color:"#506267"}}>Primes · Operators · Open questions</div><div style={{fontSize:22}}>Finite evidence, explicit limits. No RH proof claimed.</div></div>,size)}
