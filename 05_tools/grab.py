import sys, json, os, re, urllib.request, urllib.parse, concurrent.futures as cf
P=os.path.dirname(os.path.abspath(sys.argv[0]))
OUT=os.path.join(os.path.dirname(P),'04_screenshots')
rows=[l.rstrip('\n').split('\t') for l in open(f'{P}/sel.tsv') if l.strip()]
only=set(sys.argv[1:])
def fetch(url, fp):
    if os.path.exists(fp) and os.path.getsize(fp)>1000: return True
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    for _ in range(3):
        try:
            data=urllib.request.urlopen(req,timeout=180).read(); open(fp,'wb').write(data); return True
        except Exception as e: err=e
    print('  FAIL',url,err); return False
for num,slug,ident,spec in rows:
    if only and num not in only: continue
    d=f'{OUT}/{num}_{slug}'; os.makedirs(d,exist_ok=True)
    jobs=[]
    if spec.startswith('FILES:') or spec.startswith('FRAMES:'):
        m=json.load(urllib.request.urlopen(f'https://archive.org/metadata/{ident}',timeout=60))
        names=[f['name'] for f in m['files']]
        want=[int(x) for x in spec.split(':',1)[1].split(',')]
        for w in want:
            if spec.startswith('FILES:'):
                def key(n):
                    m2=re.findall(r'\d+',n); return int(m2[-1]) if m2 else 0
                cand=[n for n in names if n.endswith('.jpg') and not n.endswith('_thumb.jpg') and key(n)==w]
            else:
                cand=[n for n in names if '.thumbs/' in n and re.search(rf'_0*{w}\.jpg$',n)]
            if cand:
                jobs.append((f'https://archive.org/download/{ident}/'+urllib.parse.quote(cand[0]), f'{d}/{num}_{slug}_{w:06d}.jpg' if spec.startswith('FRAMES') else f'{d}/{num}_{slug}_f{w}.jpg'))
    else:
        for i in [int(x) for x in spec.split(',')]:
            jobs.append((f'https://archive.org/download/{ident}/page/n{i}_w1600.jpg', f'{d}/{num}_{slug}_n{i}.jpg'))
    with cf.ThreadPoolExecutor(4) as ex: ok=list(ex.map(lambda j: fetch(*j), jobs))
    print(num, slug, f'{sum(ok)}/{len(jobs)}')
