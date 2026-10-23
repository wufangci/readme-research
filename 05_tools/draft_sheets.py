"""把 draft_selection.tsv 的建議選件依時期排成對照頁，輸出到 04_screenshots/_draft/（不進 git）。需要 Pillow。"""
import os, re, glob
from PIL import Image, ImageDraw, ImageFont
T=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(T); SS=os.path.join(R,'04_screenshots'); OUT=os.path.join(SS,'_draft')
os.makedirs(OUT,exist_ok=True)
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',26)
except Exception: font=ImageFont.load_default()
groups={}
for l in open(os.path.join(T,'draft_selection.tsv')):
    if not l.strip(): continue
    per,num,pages=l.rstrip('\n').split('\t')
    for p in pages.split(','):
        hit=glob.glob(os.path.join(SS,f'{num}_*',f'{num}_*_n{p}.jpg'))
        if hit: groups.setdefault(per,[]).append((f'{num}_n{p}',hit[0]))
        else: print('missing',num,p)
W,H,C=380,540,6
for per,items in groups.items():
    rows=(len(items)+C-1)//C; sh=Image.new('RGB',(C*W,rows*(H+38)),'white'); d=ImageDraw.Draw(sh)
    for j,(lab,f) in enumerate(items):
        im=Image.open(f); im.thumbnail((W-8,H)); x=(j%C)*W; y=(j//C)*(H+38)
        sh.paste(im,(x+4,y+38)); d.text((x+8,y+6),lab,fill='red',font=font)
    out=os.path.join(OUT,f'{per}.jpg'); sh.save(out,quality=82); print(out,len(items))
