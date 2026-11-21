import json,sys,html
from texts import *
lang=sys.argv[1]; t=T[lang]
d=json.load(open('data_fixed.json')); P={p['num']:p for p in d['prompts']}
PH={2:'im-002.jpg',4:'im-003.jpg',5:'im-004.jpg',6:'im-005-clean.jpg',8:'im-006.jpg',12:'im-007.jpg',16:'im-008.jpg',17:'im-009.jpg',22:'im-010.jpg',26:'im-011.jpg'}
e=html.escape
def cat(c): return CAT_RU[c] if lang=='ru' else c
pages=[]; pn=[0]
def page(body,cls='',foot=True,pid=None):
    pn[0]+=1
    f=f'<div class="foot"><span>EUROPEAN DAYS</span><a href="#contents">{t["back"]}</a><span>{pn[0]:02d}</span></div>' if foot else ''
    pages.append(f'<section class="page {cls}"{f" id={chr(34)}{pid}{chr(34)}" if pid else ""}>{body}{f}</section>')
def h(k,a,b): return f'<div class="kicker">{k}</div><h1>{a}<br><i>{b}</i></h1>'
# cover
page(f'''<img class="bleed" src="im-000.jpg"><div class="cv-shade"></div>
<div class="cv-top">JACEY MORETTI &nbsp;·&nbsp; PROMPT STUDIO</div>
<div class="cv-bot"><div class="cv-ed">COLLECTOR’S EDITION &nbsp;·&nbsp; VOL. I</div><div class="cv-t1">European</div><div class="cv-t2">Days</div><div class="cv-rule"></div>
<div class="cv-sub">{e(t["cover_sub"]).upper()}</div><div class="cv-pl">Paris · London · Grand Hotels · Cafés · Evenings</div><div class="cv-tag">{e(t["cover_tag"])}</div></div>''','cover',foot=False)
# lookbook
def cell(n): return f'<a href="#p{n}" class="lbc"><img src="{PH[n]}"><span>No. {n:02d}</span></a>'
page(f'<div class="kicker">THE LOOKBOOK</div><h1>{t["lb_title"][0]}<br><i>{t["lb_title"][1]}</i></h1><div class="lb g3">{"".join(cell(n) for n in [4,8,6,5,12,2])}</div><p class="cap">{e(t["lb_cap"])}</p>')
page(f'<div class="kicker">THE LOOKBOOK</div><div class="lb g2">{"".join(cell(n) for n in [16,17,26,22])}</div>')
# welcome
ins=''.join(f'<div class="ins"><b>{a}</b><span>{e(b)}</span></div>' for a,b in t['inside'])
page(h(t['w_kicker'],*t['w_title'])+f'<p class="lead">{e(t["w_lead"])}</p><p class="body">{e(t["w_body"])}</p><div class="kicker sm">{t["w_inside"]}</div>{ins}<p class="note">{e(t["w_note"])}</p>')
# where to generate
gens=''.join(f'<div class="gen"><div class="gh"><b>{e(a)}</b><span>{e(b)}</span></div><p>{e(c)}</p></div>' for a,b,c in t['gens'])
page(h(t['g_kicker'],*t['g_title'])+f'<p class="body">{e(t["g_lead"])}</p>{gens}<p class="note">{e(t["g_tip"])}</p>')
# steps + photo
st=''.join(f'<div class="step"><em>{i+1:02d}</em><div><b>{e(a)}</b><p>{e(b)}</p></div></div>' for i,(a,b) in enumerate(t['steps']))
ca=f'<div class="ca"><div class="cbox"><div class="kicker sm">{t["choose_t"]}</div>{"".join(f"<p>{e(x)}</p>" for x in t["choose"])}</div><div class="cbox av"><div class="kicker sm">{t["avoid_t"]}</div>{"".join(f"<p>{e(x)}</p>" for x in t["avoid"])}</div></div>'
page(h(t['s_kicker'],*t['s_title'])+st+ca)
# 9-frame method + rules
dark={2,6,8}; mid={1,3,5}
grid=''.join(f'<div class="nf {"dk" if i in dark else ("md" if i in mid else "")}"><em>{i+1:02d}</em><b>{e(a).upper()}</b><span>{e(b)}</span></div>' for i,(a,b) in enumerate(ROLES[lang]))
rules=''.join(f'<div class="rule"><b>{e(a)}</b><span>{e(b)}</span></div>' for a,b in t['rules'])
page(h(t['m_kicker'],*t['m_title'])+f'<p class="body">{e(t["m_lead"])}</p><div class="nine">{grid}</div><div class="rules">{rules}</div>')
# shot variations
vv=''.join(f'<div class="var"><div class="vh"><b>{k}</b><span>{e(v[0] if lang=="ru" else v[1])}</span></div><div class="vt">{e(v[2])}</div></div>' for k,v in VARS.items())
page(h(t['v_kicker'],*t['v_title'])+f'<p class="body">{e(t["v_lead"])}</p>{vv}','vars')
# stories 2 per page
def story(s):
    title=STORY_RU[s['title']][0] if lang=='ru' else s['title']
    desc=STORY_RU[s['title']][1] if lang=='ru' else STORY_EN[s['title']]
    cells=''.join(f'<a class="sc" href="#p{n}"><em>{i+1:02d} · {e(ROLES[lang][i][0]).upper()}</em><b>No. {n:02d}</b><span>{e(P[n]["title"])}</span><i>{VAR_LABEL[lang][v]}</i></a>' for i,(n,v) in enumerate(zip(s['nums'],s['vars'])))
    return f'<div class="story"><div class="kicker sm">{t["st_kicker"]}</div><h2>{e(title)}</h2><p class="sd">{e(desc)} {e(t["st_common"])}</p><div class="sg">{cells}</div></div>'
S=d['stories']
page(story(S[0])+story(S[1]),'stories'); page(story(S[2])+story(S[3]),'stories')
# contents
items=''.join(f'<a class="ci" href="#p{p["num"]}"><em>{p["num"]:02d}</em><span>{e(p["title"])}</span></a>' for p in d['prompts'])
page(h(t['c_kicker'],*t['c_title'])+f'<p class="note">{e(t["c_hint"])}</p><div class="cols">{items}</div>','contents',pid='contents')
# prompts
for p in d['prompts']:
    n=p['num']
    th=f'<figure><img src="{PH[n]}"><figcaption>{e(t["made"])}</figcaption></figure>' if n in PH else ''
    body=f'<p>{e(p["head"])}</p>'+''.join(f'<p><b>{e(k)}:</b> {e(v)}</p>' for k,v in p['fields'])
    page(f'<div class="ph {"wt" if th else ""}">{th}<div class="pnum">No. {n:02d}<span>{e(cat(p["cat"]))}</span></div><h2 class="pt">{e(p["title"])}</h2><p class="ps">{e(p["sub"])}</p></div><div class="kicker sm">{t["copy"]}</div><div class="pbox">{body}</div>','prompt',pid=f'p{n}')
# checklist
cks=''.join(f'<div class="ck"><span>☐</span>{e(x)}</div>' for x in t['checks'])
fx=''.join(f'<div class="fx"><b>{e(a)}</b><span>{e(b)}</span></div>' for a,b in t['fixes'])
page(h(t['ck_kicker'],*t['ck_title'])+cks+f'<div class="kicker sm" style="margin-top:16pt">{t["fix_t"]}</div><div class="fxg">{fx}</div>')
# merci
page(f'<div class="merci"><div class="kicker">MERCI</div><h1>{t["thanks"][0]}<br><i>{t["thanks"][1]}</i></h1><div class="cv-rule dk"></div><p class="share">{t["share"]}</p><p class="soon">{e(t["soon"])}</p><p class="lic">{e(t["license"])}</p><p class="lic">{e(t["disclaimer"])}</p><div class="sig">JACEY MORETTI &nbsp;·&nbsp; PROMPT STUDIO</div></div>',foot=False)
css=open('style.css').read()
open(f'build/{lang}.html','w').write(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=block" rel="stylesheet"><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print(lang,'pages',pn[0])
