import json,re,html
F='/root/.claude/projects/-home-claude/80617713-5569-5cdc-abac-3155ffea4d3e/tool-results/artifact-34c03932-1790570913-4bbd.html'
src=open(F,encoding='utf8').read()
i=src.index('<title>Hexacube</title>'); j=src.rindex('</body></html>')
body=src[i:j]
d=json.load(open('mwc/data.json'))
d=[x for x in d if x['row']!=223]   # exact duplicate of row 224
COVER_OVR={'overcome':'dancing-machine-hexacube-remix.jpg'}   # site-only: Overcome uses the Accelerator compilation cover
for x in d:
    if x['id'] in COVER_OVR: x['img']=COVER_OVR[x['id']]
e=html.escape
def ndate(s):
    s=s.rstrip('.')
    m=re.match(r'(\d{4})\.(\d{1,2})\.(\d{1,2})$',s)
    return '%s.%02d.%02d'%tuple(map(lambda t:int(t) if False else t,(m[1],int(m[2]),int(m[3])))) if m else s
IC={
'date':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 3v3M16 3v3"/></svg>',
'disc':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.4"/></svg>',
'tag':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.6 12.6L12 21.2a2 2 0 01-2.8 0l-6.4-6.4a2 2 0 010-2.8L11.4 3.4A2 2 0 0112.8 3H19a2 2 0 012 2v6.2a2 2 0 01-.4 1.4z"/><circle cx="16" cy="8" r="1.4"/></svg>',
'c':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><text x="12" y="16" font-size="11" text-anchor="middle" fill="currentColor" stroke="none" font-family="Arial, sans-serif" font-weight="700">C</text></svg>',
'src':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4v8a3 3 0 003 3h11"/><path d="M15 11l4 4-4 4"/></svg>',
}
PH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.5"/></svg>'
def tabkey(x):
    t=x['tab']
    return {'Doujin / Compilation':'doujin','Rhythm Game':'rhythm','Remix / Arrange':'remix','Sampling Music':'sampling','HYPERFLIP':'hyperflip','Etc.':'etc','':'etc'}[t]
ETC={'missense':'Submission','make-your-own-kind-of-music':'Submission','oceanous-access':'Submission','funny-bunny-party':'Submission','happy-experience':'Game BGM','kkumeul-chajaseo':'At University','flyin':'At University'}
RG={'enceladus':'Official Track','zutto':'Official Track','no-matter-i-can-fly-higher':'Unofficial Contest','hit':'Unofficial Contest','real-rave-angelz':'Unofficial Contest'}
def pill(x,k):
    if k=='rhythm': return RG[x['id']]
    if k=='etc': return ETC.get(x['id'],'Lost Media?')
    if k!='remix': return ''
    if 'Tell Your World' in x['title']: return 'Bootleg'
    if 'Subculture Adventure' in x['p1']: return 'Bootleg'
    if 'Blue Archive' in x['src'] or '東方' in x['src']: return 'Arrange'
    t=x['title']+' '+x['sub']
    for kw,lab in (('Bootleg','Bootleg'),('Mash-up','Mash-up'),('Flip','Flip'),('Edit','Edit'),('Remix','Remix')):
        if kw in t: return lab
    return 'Arrange'
def collab(sub):
    parts=[p.strip() for p in re.split(r'\s+(?:&|vs\.?|feat\.|x)\s+',sub)]
    others=[p for p in parts if p.lower()!='hexacube']
    return ' (w/ %s)'%', '.join(others) if len(parts)>1 and others else ''
def isold(x,k):
    if k=='etc': return False
    if k=='sampling': return x['sub'].strip()=='Hexacube'
    yr=x['date'][:4]
    return yr.isdigit() and int(yr)<2023
def dkey(x):
    m=re.match(r'(\d{4})\.(\d{1,2})\.(\d{1,2})',x['date'])
    return (int(m[1]),int(m[2]),int(m[3])) if m else (0,0,0)
SELF_ALB={'FOREVER SUNSHINE','HEADPHONE HEADACHE','PHOTOSYNTHESIS','SATELLITE OVERSKY','SKYLINE SIMULATOR','CHAOS iN JOY'}
def isself(x,k):
    # hidden tag 'Self-Released' (Doujin / Sampling / Hyperflip): tracks marked as included on one of my own albums, or single releases
    if k not in ('doujin','sampling','hyperflip'): return False
    m=re.match(r'\s*\[(.*?)\]',x['p1'])
    if m and m[1] in SELF_ALB: return True
    if x['p1'] in ('Free Download','YT1KSubSpecial','YT2KSubSpecial'): return True
    return x['p1']=='Single' or bool(re.search(r'Kube \d+(st|nd|rd|th) Anniversary Song',x['p1']))
def card(x,k):
    lines=[]
    if x['date']: lines.append(('m-date',IC['date']+e(ndate(x['date']))))
    if x['p1']: lines.append(('m-p1',IC['disc']+e(x['p1'])))
    if x['p2']: lines.append(('m-p2',(IC['c'] if k=='remix' else IC['tag'])+e(x['p2'])))
    if x['src']: lines.append(('m-src',IC['src']+e(x['src'])))
    p=pill(x,k)
    old=isold(x,k)
    at=' data-id="%s"'%e(x['id'],quote=True)
    if old: at+=' data-old="1" data-off'
    if k=='remix': at+=' data-f="%s"'%({'Remix':'remix','Arrange':'arrange'}.get(p,'other'))
    if isself(x,k): at+=' data-f="self"'
    if k=='rhythm': at+=' data-f="%s"'%('official' if pill(x,k)=='Official Track' else 'unofficial')
    if k=='etc': at+=' data-f="%s"'%({'Submission':'submission','Game BGM':'game','At University':'univ'}.get(p,'lost'))
    cov=''
    if p: cov+='<span class="tag-pill">%s</span>'%e(p)
    cov+=('<img src="covers/%s" alt="" loading="lazy" decoding="async">'%x['img']) if x['img'] else PH
    h='<div class="cover">%s</div>\n              <div class="card-body">\n                <h3>%s</h3>\n'%(cov,e(x['title']))
    if x['sub']: h+='                <div class="work-sub">%s</div>\n'%e(x['sub'])
    if lines:
        h+='                <div class="party-meta">\n'+''.join('                  <span class="meta-line %s">%s</span>\n'%(c,l) for c,l in lines)+'                </div>\n'
    h+='              </div>\n'
    if x['url']:
        return '            <a class="release-card"%s href="%s" target="_blank" rel="noopener noreferrer">\n              %s            </a>\n'%(at,e(x['url'],quote=True),h)
    return '            <div class="release-card no-link"%s>\n              %s            </div>\n'%(at,h)
PLUS='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
def more(n,k):
    if k=='sampling':
        return '''            <button type="button" class="release-card more-card" data-more>
              <div class="cover">%s</div>
              <div class="card-body">
                <h3 class="i18n" data-kr="Hexacube 명의 작업 보기" data-en="View works under Hexacube" data-jp="Hexacube名義の作品を見る"></h3>
              </div>
            </button>
'''%PLUS
    return '''            <button type="button" class="release-card more-card" data-more>
              <div class="cover">%s</div>
              <div class="card-body">
                <h3 class="i18n" data-kr="작업물 더보기" data-en="Show more works" data-jp="過去の作品をもっと見る"></h3>
              </div>
            </button>
'''%PLUS
CK='<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
def mkflt(opts):
    return '<div class="flt-bar" role="group" aria-label="filter">'+''.join('<label class="flt%s"><input type="checkbox" value="%s"%s><span class="flt-box">%s</span><span class="flt-text">%s</span></label>'%(' blue' if (o[3:] and o[3]) else '',o[0],' checked data-def' if o[2] else '',CK,o[1]) for o in opts)+'</div>\n          '
FLT=mkflt((('remix','Remix',1),('arrange','Arrange',1),('other','Bootleg / Flip / Mash-up',0,1)))
FLT_SELF=mkflt((('self','Self-Released',0,1),))
FLT_RG=mkflt((('official','Official Track',1),('unofficial','Unofficial Contest',1)))
FLT_ETC=mkflt((('submission','Submission',1),('game','Game BGM',1),('univ','At University',0),('lost','Lost Media?',0)))
groups={}
for x in d: groups.setdefault(tabkey(x),[]).append(x)
# rhythm prose
games=['KALPA','Dynamix Universe','ChainBeeT','COXETA','vivid/stasis','Orbit Or Beat Extended Edition','rote²']
gs={g:[] for g in games}
for x in d:
    m=re.search(r'(.*?)\s*(?:에\s*)?수록',x['memo'].split('ㅁ')[0])
    if not m: continue
    for g in re.split(r'\s*,\s*',m[1].strip()):
        assert g in gs,(g,x['row'])
        gs[g].append(x['title']+collab(x['sub']))
prose='          <div class="game-list">\n'
for g in games:
    prose+='            <div class="game-sec">\n              <h3 class="game-name">%s</h3>\n              <p class="game-songs">%s</p>\n            </div>\n'%(e(g),'<br>'.join(e(t) for t in gs[g]))
prose+='          </div>\n'
print({g:len(v) for g,v in gs.items()},{k:len(v) for k,v in groups.items()})
ps=body.index('<section id="panel-music"'); pe=body.index('</section>',ps)
panel=body[ps:pe]
for k,items in groups.items():
    s=panel.index('<div class="subpanel%s" data-sub="%s">'%(' is-active' if k=='doujin' else '',k))
    a=panel.index('<div class="card-grid">',s)
    b=panel.index('\n          </div>\n        </div>',a)
    items.sort(key=dkey,reverse=True)
    nold=sum(1 for x in items if isold(x,k) and not isself(x,k)); nold_any=sum(1 for x in items if isold(x,k))
    grid='<div class="card-grid">\n'+''.join(card(x,k) for x in items)+(more(nold,k) if nold_any else '')
    if k=='remix': grid=FLT+grid
    if k=='etc': grid=FLT_ETC+grid
    if k=='rhythm': grid=FLT_RG+grid
    if k in ('doujin','sampling','hyperflip'): grid=FLT_SELF+grid
    new=grid+'          </div>'
    if k=='rhythm': new+='\n'+prose.rstrip('\n')
    panel=panel[:a]+new+panel[b+len('\n          </div>'):]
body=body[:ps]+panel+body[pe:]
css='''  .cover img{width:100%;height:100%;object-fit:cover;display:block;}
  .cover .tag-pill{z-index:1;}
  .release-card .party-meta .meta-line.m-date{color:var(--meta-date);font-weight:600;}
  .release-card .party-meta .meta-line.m-p1{color:var(--meta-venue);font-weight:600;}
  .release-card .party-meta .meta-line.m-p2{color:var(--meta-genre);font-weight:600;}
  .release-card .party-meta .meta-line.m-src{color:var(--ink-soft);font-weight:500;}
  #app.joker-theme .release-card{--accent:#44d6ca;--accent-deep:#0e8f84;--accent-ink:#053c37;--meta-date:#0e8f84;--meta-venue:#3366cc;--meta-genre:#b45309;}
  .release-card.no-link{cursor:default;}
  .release-card.no-link:hover{transform:none;box-shadow:none;}
  .game-list{margin-top:40px;padding-top:26px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:22px;max-width:900px;}
  .game-name{font-size:17px;margin:0 0 6px;color:var(--accent-deep);}
  .game-songs{margin:0;font-size:14px;line-height:1.85;color:var(--ink);}
'''
css+='''  .card-grid{position:relative;align-content:start;}
  .release-card[data-off]{display:none;}
  .release-card.is-leaving{position:absolute;margin:0;pointer-events:none;z-index:0;}
  .more-card{font:inherit;text-align:left;padding:0;width:100%;border:1px dashed var(--accent);}
  .more-card .cover svg{width:44px;height:44px;opacity:.55;transition:transform .25s,opacity .25s;}
  .more-card:hover .cover svg{transform:rotate(90deg) scale(1.1);opacity:.9;}
  .more-card .card-body h3{color:var(--accent-deep);}
  .more-card .work-sub{color:var(--ink-soft);font-size:13px;}
  .flt-bar{display:flex;flex-wrap:wrap;gap:10px;margin:-8px 0 20px;}
  .flt{position:relative;display:inline-flex;align-items:center;gap:9px;padding:7px 15px 7px 9px;border:1px solid var(--line);border-radius:999px;background:var(--paper);cursor:pointer;user-select:none;font-size:13.5px;font-weight:600;color:var(--ink-soft);transition:border-color .2s,color .2s,background .2s,box-shadow .2s;}
  .flt:hover{border-color:var(--accent);}
  .flt input{position:absolute;opacity:0;width:0;height:0;}
  .flt-box{width:20px;height:20px;border-radius:6px;border:1.8px solid #c3cbcd;background:var(--paper);display:inline-flex;align-items:center;justify-content:center;transition:background .2s,border-color .2s,transform .2s;}
  .flt-box svg{width:14px;height:14px;fill:none;stroke:var(--accent-ink);stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:24;stroke-dashoffset:24;transition:stroke-dashoffset .25s ease;}
  .flt input:checked + .flt-box{background:var(--accent);border-color:var(--accent);}
  .flt input:checked + .flt-box svg{stroke-dashoffset:0;}
  .flt:has(input:checked){border-color:var(--accent);color:var(--ink);box-shadow:0 2px 8px -4px rgba(14,143,132,.45);}
  .flt.blue:hover{border-color:#3366cc;}
  .flt.blue input:checked + .flt-box{background:#3366cc;border-color:#3366cc;}
  .flt.blue .flt-box svg{stroke:#fff;}
  .flt.blue:has(input:checked){border-color:#3366cc;box-shadow:0 2px 8px -4px rgba(51,102,204,.5);}
  .flt.blue input:focus-visible + .flt-box{outline-color:#3366cc;}
  .flt:active .flt-box{transform:scale(.88);}
  .flt input:focus-visible + .flt-box{outline:2px solid var(--accent-deep);outline-offset:2px;}
'''+css
anchor='  .work-sub{'
assert anchor in body
body=body.replace(anchor,css+anchor,1)

JS=r"""<script>
(function(){
  var DUR=500;
  function vis(c,g){
    if(c.hasAttribute('data-more')) return !g._old;
    if(c.hasAttribute('data-old') && !g._old) return false;
    if(c.hasAttribute('data-f') && g._flt && !g._flt[c.getAttribute('data-f')]) return false;
    return true;
  }
  function run(g){
    if(g._done) g._done();
    var cards=[].slice.call(g.querySelectorAll('.release-card'));
    var gb=g.getBoundingClientRect();
    var first=new Map();
    cards.forEach(function(c){ if(!c.hasAttribute('data-off')) first.set(c,c.getBoundingClientRect()); });
    var h0=g.offsetHeight;
    var leave=[],enter=[],stay=[];
    cards.forEach(function(c){
      var was=first.has(c), now=vis(c,g);
      if(was&&!now) leave.push(c); else if(!was&&now) enter.push(c); else if(was&&now) stay.push(c);
    });
    // apply final state
    enter.forEach(function(c){ c.removeAttribute('data-off'); });
    leave.forEach(function(c){
      var r=first.get(c);
      c.classList.add('is-leaving');
      c.style.left=(r.left-gb.left)+'px'; c.style.top=(r.top-gb.top)+'px';
      c.style.width=r.width+'px'; c.style.height=r.height+'px';
    });
    var h1=g.offsetHeight;
    var last=new Map(); stay.forEach(function(c){ last.set(c,c.getBoundingClientRect()); });
    var T='transform '+DUR+'ms cubic-bezier(.4,0,.2,1), opacity '+DUR+'ms ease';
    stay.forEach(function(c){
      var a=first.get(c), b=last.get(c);
      c.style.transition='none';
      c.style.transform='translate('+(a.left-b.left)+'px,'+(a.top-b.top)+'px)';
    });
    enter.forEach(function(c){ c.style.transition='none'; c.style.opacity='0'; c.style.transform='translateY(26px) scale(.92)'; });
    g.style.minHeight=h0+'px'; g.style.overflow='visible';
    void g.offsetHeight;
    g.style.transition='min-height '+DUR+'ms cubic-bezier(.4,0,.2,1)'; g.style.minHeight=h1+'px';
    stay.concat(enter).forEach(function(c){ c.style.transition=T; c.style.transform=''; c.style.opacity=''; });
    leave.forEach(function(c){ c.style.transition=T; c.style.opacity='0'; c.style.transform='scale(.9)'; });
    var tm=setTimeout(done,DUR+60);
    function done(){
      clearTimeout(tm); g._done=null;
      leave.forEach(function(c){
        c.classList.remove('is-leaving'); c.setAttribute('data-off','');
        ['left','top','width','height'].forEach(function(p){ c.style[p]=''; });
      });
      cards.forEach(function(c){ c.style.transition=''; c.style.transform=''; c.style.opacity=''; });
      g.style.minHeight=''; g.style.transition=''; g.style.overflow='';
    }
    g._done=done;
  }
  document.querySelectorAll('.card-grid').forEach(function(g){
    g._old=false; g._flt=null;
    var more=g.querySelector('[data-more]');
    if(more) more.addEventListener('click',function(){ g._old=true; run(g); });
  });
  document.querySelectorAll('.flt-bar').forEach(function(bar){
    var g=bar.nextElementSibling;
    bar.addEventListener('change',function(){
      var f={};
      bar.querySelectorAll('input').forEach(function(i){ f[i.value]=i.checked; });
      g._flt=f; run(g);
    });
  });
})();
</script>
"""
body=body.rstrip('\n')+'\n'+JS
exec(open('post.py',encoding='utf8').read())
json.dump({k:[x['id'] for x in items if isself(x,k)] for k,items in groups.items() if k in ('doujin','sampling','hyperflip')},open('self_released.json','w'),ensure_ascii=False,indent=1)
open('site.html','w',encoding='utf8').write(body)
print(len(body))
