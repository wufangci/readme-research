"""依時期把 04_screenshots 的截圖排成對照頁（需要 Pillow）。輸出到 04_screenshots/_by_period/，不進 git。"""
import os, re, sys
from PIL import Image, ImageDraw, ImageFont
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); SS=os.path.join(R,'04_screenshots'); OUT=os.path.join(SS,'_by_period')
PERIODS=[('1_formosa','福爾摩沙',range(1,9)),('2_seiban','生番',range(9,20)),('3_takasago','高砂族',range(20,29))]
os.makedirs(OUT,exist_ok=True)
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',22)
except Exception: font=ImageFont.load_default()
W,H,C,PER=300,420,8,40
def key(f): return [int(x) for x in re.findall(r'\d+',f)]
for slug,name,nums in PERIODS:
    files=[]
    for d in sorted(os.listdir(SS)):
        m=re.match(r'(\d+)_',d)
        if m and int(m.group(1)) in nums and os.path.isdir(os.path.join(SS,d)):
            files+=[os.path.join(SS,d,f) for f in sorted(os.listdir(os.path.join(SS,d)),key=key) if f.endswith('.jpg')]
    for k in range(0,len(files),PER):
        chunk=files[k:k+PER]; rows=(len(chunk)+C-1)//C
        sh=Image.new('RGB',(C*W,rows*(H+30)),'white'); dr=ImageDraw.Draw(sh)
        for j,f in enumerate(chunk):
            im=Image.open(f); im.thumbnail((W-6,H)); x=(j%C)*W; y=(j//C)*(H+30)
            sh.paste(im,(x+3,y+30)); b=os.path.basename(f); lab=b.split('_')[0]+'_'+b.rsplit('_',1)[-1].replace('.jpg','')
            dr.text((x+6,y+4),lab,fill='red',font=font)
        out=os.path.join(OUT,f'{slug}_{k//PER+1:02d}.jpg'); sh.save(out,quality=80); print(out,len(chunk))
