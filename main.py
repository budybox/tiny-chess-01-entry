
import sys,time
P=1;N=2;B=3;R=4;Q=5;K=6;W=8;B0=16
V={P:100,N:320,B:330,R:500,Q:900,K:20000}
MT={
 P:{0:[-8],1:[8]},
 N:{0:[-17,-15,-10,-6,6,10,15,17],
   1:[-17,-15,-10,-6,6,10,15,17]},
 B:{0:[-9,-7,7,9],1:[-9,-7,7,9]},
 R:{0:[-8,-1,1,8],1:[-8,-1,1,8]},
 Q:{0:[-9,-8,-7,-1,1,7,8,9],1:[-9,-8,-7,-1,1,7,8,9]},
 K:{0:[-9,-8,-7,-1,1,7,8,9],1:[-9,-8,-7,-1,1,7,8,9]}
}
def I(p):return 0<=p<64
def K_saf(v,p):
 f=(v[p]>>4)&1;q=v[p]&7
 if q!=K:return True
 f2=(v[p]>>4)&1
 for d in MT[q][f]:
  n=p+d
  if I(n):
   c=v[n]
   if c and ((c>>4)&1)==f2 and (c&7)!=K:
    # Check if this piece attacks p
    for d2 in MT[(c&7)][(c>>4)&1]:
     if p==n+d2:return False
 return True
def E(v):
 s=0
 for p in range(64):
  c=v[p]
  if c:
   f=(c>>4)&1;q=c&7
   s+=V[q]*(1 if f==0 else -1)
 return s
b=[0]*64
b[0]=W|R;b[1]=W|N;b[2]=W|B;b[3]=W|Q;b[4]=W|K
for i in range(8):b[i+8]=W|P
b[56]=B0|R;b[57]=B0|N;b[58]=B0|B;b[59]=B0|Q;b[60]=B0|K
for i in range(8):b[i+48]=B0|P
print("uci",flush=True)
print("id name TinyChess",flush=True)
print("id author Budiyanto",flush=True)
print("uciok",flush=True)
while 1:
 l=sys.stdin.readline().strip()
 if not l:continue
 if l=="isready":print("readyok",flush=True)
 elif l=="go":
  mm=None;mv=-30000
  for p in range(64):
   c=b[p]
   if not c:continue
   f=(c>>4)&1;q=c&7
   for d in MT[q][f]:
    n=p+d
    if I(n):
     tg=b[n]
     if not tg or((tg>>4)&1)!=f:
      b[p],b[n]=0,c;v=E(b);b[p],b[n]=c,tg
      if v>mv:mv=v;mm=(p,n)
  if mm:print(f"bestmove {chr(97+mm[0]%8)}{8-mm[0]//8}{chr(97+mm[1]%8)}{8-mm[1]//8}",flush=True)
 elif l=="quit":break
