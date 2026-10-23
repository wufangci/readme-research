import os, re, sys
P=os.path.dirname(os.path.abspath(sys.argv[0])); OUT=os.path.join(os.path.dirname(P),'04_screenshots')
items=sorted([l.rstrip('\n').split('\t') for l in open(f'{P}/items.tsv') if l.strip()],key=lambda r:int(r[0]))
cap={}
if os.path.exists(f'{P}/captions.tsv'):
    for l in open(f'{P}/captions.tsv'):
        if l.strip(): k,v=l.rstrip('\n').split('\t',1); cap[k]=v
dirs={d.split('_',1)[0]:d for d in os.listdir(OUT) if os.path.isdir(f'{OUT}/{d}')}
L=['# 截圖索引','','> 由腳本產生。「原書圖說」只抄錄書上印的文字；空白表示沒有圖說或待補。圖檔不進 git。','']
total=0
for num,title,ident,rights in items:
    if num not in dirs: continue
    d=dirs[num]; files=sorted(os.listdir(f'{OUT}/{d}'),key=lambda f:[int(x) for x in re.findall(r'\d+',f.rsplit('_',1)[-1])] or [0])
    files=[f for f in files if f.endswith('.jpg')]; total+=len(files)
    L+= [f'## {num}　{title}','',f'- archive.org：[`{ident}`](https://archive.org/details/{ident})',f'- 權利欄位：{rights}',f'- 截圖：{len(files)} 張，資料夾 `{d}/`','','| 檔案 | 原頁 | 原書圖說 |','|---|---|---|']
    for f in files:
        m=re.search(r'_n(\d+)\.jpg$',f); m2=re.search(r'_(\d{6})\.jpg$',f); m3=re.search(r'_f(\d+)\.jpg$',f)
        if m: link=f'[n{m.group(1)}](https://archive.org/details/{ident}/page/n{m.group(1)})'
        elif m2: link=f'影格 {int(m2.group(1))} 秒（[影片](https://archive.org/details/{ident})）'
        else: link=f'[檔案 {m3.group(1)}](https://archive.org/details/{ident})'
        L.append(f'| `{f}` | {link} | {cap.get(f,"")} |')
    L.append('')
L.insert(3,f'共 {total} 張。'); L.insert(4,'')
open(f'{OUT}/INDEX.md','w').write('\n'.join(L)); print('INDEX', total)
