"""Extract closed CAD polygon loops from the user's logo, without modifying the image."""
import json, math
from pathlib import Path
from PIL import Image
import numpy as np
src=Path('product/references/uploads/20260930T145159368Z-3-ishot-2026-09-30-10-50-10.png')
a=np.asarray(Image.open(src).convert('L'))<128
edges={}
for y,x in zip(*np.where(a)):
 for exposed,s,t in [(y==0 or not a[y-1,x],(x,y),(x+1,y)),(x==a.shape[1]-1 or not a[y,x+1],(x+1,y),(x+1,y+1)),(y==a.shape[0]-1 or not a[y+1,x],(x+1,y+1),(x,y+1)),(x==0 or not a[y,x-1],(x,y+1),(x,y))]:
  if exposed: edges.setdefault(s,[]).append(t)
loops=[]
while edges:
 start=next(iter(edges)); cur=start; loop=[]
 while True:
  loop.append(cur); nxt=edges[cur].pop()
  if not edges[cur]: del edges[cur]
  cur=nxt
  if cur==start: break
 if len(loop)>20: loops.append(loop)
def area(p): return sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p)))/2
def rdp(p,eps):
 if len(p)<3: return p
 ax,ay=p[0]; bx,by=p[-1]; dx,dy=bx-ax,by-ay
 den=math.hypot(dx,dy)
 ds=[abs(dx*(ay-y)-(ax-x)*dy)/den if den else math.hypot(x-ax,y-ay) for x,y in p]
 i=max(range(len(ds)),key=ds.__getitem__)
 return rdp(p[:i+1],eps)[:-1]+rdp(p[i:],eps) if ds[i]>eps else [p[0],p[-1]]
loops.sort(key=lambda p:abs(area(p)),reverse=True)
xs=[p[0] for p in loops[0]]; ys=[p[1] for p in loops[0]]
cx=(max(xs)+min(xs))/2; cy=(max(ys)+min(ys))/2; w=max(xs)-min(xs)
out=[]
for loop in loops:
 k=len(loop)//2
 q=rdp(loop[:k+1],1.2)[:-1]+rdp(loop[k:]+[loop[0]],1.2)[:-1]
 out.append([[round((x-cx)/w,7),round((cy-y)/w,7)] for x,y in q])
Path('product/references/logo-trace.json').write_text(json.dumps({'source':str(src),'method':'luminance threshold 128; pixel boundary; RDP 1.2 px','pixel_width':int(w),'max_simplification_mm_at_32mm_width':round(1.2/w*32,4),'loops':out},ensure_ascii=False,indent=2)+'\n')
print('Logo contours:',len(out),'vertices:',[len(p) for p in out], 'original pixel width:',w)
