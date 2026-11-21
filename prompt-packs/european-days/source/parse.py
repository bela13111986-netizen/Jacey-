import subprocess,re,json,sys
P=sys.argv[1]
def raw(i,layout=False):
    a=['pdftotext','-f',str(i),'-l',str(i)]+(['-layout'] if layout else [])+[P,'-']
    return subprocess.run(a,capture_output=True,text=True).stdout
LABELS=['Identity','Subject','Location and scene','Wardrobe','Accessories and props','Pose and action','Camera and composition','Lighting','Makeup','Color grading','Negative prompt']
prompts=[]
for i in range(17,77):
    t=raw(i)
    m=re.match(r'\s*No\. (\d+)\s+(.+?)\n\s*\n(.+?)\nCOPY THE FULL PROMPT\s*\n(.+?)\s*\nEUROPEAN DAYS',t,re.S)
    if not m: continue
    num,cat,ts,body=m.groups()
    tl=ts.strip().split('\n'); sub=tl[-1]; title=' '.join(tl[:-1])
    body=' '.join(l.strip() for l in body.split('\n'))
    sub=sub.strip()
    # split into fields
    parts=[]
    pat='('+'|'.join(re.escape(l)+':' for l in LABELS)+')'
    segs=re.split(pat,body)
    head=segs[0].strip()
    fields=[]
    for k in range(1,len(segs),2):
        fields.append([segs[k][:-1],segs[k+1].strip()])
    prompts.append(dict(num=int(num),cat=cat.strip(),title=title.strip(),sub=sub,head=head,fields=fields))
print(len(prompts),file=sys.stderr)
# subtitle may wrap: check
stories=[]
for i in range(10,14):
    L=raw(i,True).split('\n')
    title=None;desc=[];nums=[];vars_=[]
    for l in L:
        s=l.strip()
        if not s: continue
        if 'PHOTO STORY' in s or 'EUROPEAN DAYS' in s: continue
        if re.search(r'No\. \d+',s):
            nums+= [int(x) for x in re.findall(r'No\. (\d+)',s)]; continue
        if re.search(r'as written|variation',s):
            vars_+= re.findall(r'as written|\+ \w+ variation',s); continue
        if title is None: title=s; continue
        if not nums and '·' not in s and 'T H E' not in s and not re.match(r'0\s?\d',s): desc.append(s)
    stories.append(dict(title=title,desc=' '.join(desc),nums=nums,vars=vars_))
json.dump(dict(prompts=prompts,stories=stories),open('data.json','w'),ensure_ascii=False,indent=1)
for s in stories: print(s['title'],len(s['nums']),len(s['vars']),s['desc'][:80],file=sys.stderr)
