import re as _re, html as _html
def R(a,b):
    global body
    assert a in body, a[:70]
    body=body.replace(a,b,1)
# ---- remove fade CSS ----
a=body.index('  /* ---- page-level fade transition'); b=body.index('  .card-grid,.post-list,.detail-view{transition:opacity .2s ease;}\n')+len('  .card-grid,.post-list,.detail-view{transition:opacity .2s ease;}\n')
body=body[:a]+body[b:]
R('margin-bottom:28px;transition:opacity .2s ease;}','margin-bottom:28px;}')
R('text-align:right;opacity:1;transition:opacity .2s ease;}','text-align:right;}')
R('  main.fade-out:not(.detail-nav) .joker-teaser{opacity:0;}\n','')
# ---- remove fade JS ----
a=body.index('  // fades <main> out, runs the DOM mutation'); b=body.index('  function renderPost(detail){')
body=body[:a]+'''  // page changes are instant (no fade); kept as a thin wrapper so the
  // navigation functions below stay unchanged
  function fadeNavigate(mutateFn, fadeMode, onFadeIn){ mutateFn(); if(onFadeIn) onFadeIn(); }

'''+body[b:]
# ---- hash routing (#/tag) ----
R('  function scrollToTop(){','''  var routing=false, curHash=(location.hash||'');
  function setHash(h){
    if(routing) return;
    var full=h?'#'+h:'';
    if(curHash===full) return;
    curHash=full;
    try{ history.pushState(null,'',full||(location.pathname+location.search)); }
    catch(e){ try{ location.hash=h; }catch(e2){} }
  }
  function syncTab(tab){
    if(tab==='home'){ setHash(''); return; }
    var p=document.getElementById('panel-'+tab), sp=p&&p.querySelector('.subpanel.is-active');
    setHash('/'+tab+(sp?'/'+sp.getAttribute('data-sub'):''));
  }
  function scrollToTop(){''')
R('  function showTab(tab, sub){','  function showTab(tab, sub){ showTab0(tab, sub); syncTab(tab); }\n  function showTab0(tab, sub){')
R('  function showSub(tab, sub){','  function showSub(tab, sub){ showSub0(tab, sub); setHash(\'/\'+tab+\'/\'+sub); }\n  function showSub0(tab, sub){')
R('  function openPost(id){','  function openPost(id){ openPost0(id); setHash(\'/\'+id); }\n  function openPost0(id){')
R('  function openParty(id){','  function openParty(id){ openParty0(id); setHash(\'/\'+id); }\n  function openParty0(id){')
R("detail.setAttribute('data-current', order[idx-1]); renderPost(detail);","detail.setAttribute('data-current', order[idx-1]); renderPost(detail); setHash('/'+order[idx-1]);")
R("detail.setAttribute('data-current', order[idx+1]); renderPost(detail);","detail.setAttribute('data-current', order[idx+1]); renderPost(detail); setHash('/'+order[idx+1]);")
R("sp.classList.remove('show-detail'); scrollToTop(); }, 'detail'); }","sp.classList.remove('show-detail'); scrollToTop(); setHash('/'+sp.closest('.panel').id.replace('panel-','')+'/'+sp.getAttribute('data-sub')); }, 'detail'); }")
body=body.replace("card.classList.toggle('is-expanded');","card.classList.toggle('is-expanded'); albumHash(card);")
R('  function scrollToTop(){','''  function albumHash(card){
    var id=card.getAttribute('data-id'), sp=card.closest('.subpanel');
    if(card.classList.contains('is-expanded') && id) setHash('/'+id);
    else if(sp) setHash('/'+sp.closest('.panel').id.replace('panel-','')+'/'+sp.getAttribute('data-sub'));
  }
  function scrollToTop(){''')
# router: placed right before applyLang(); at end of first script
R("\n  applyLang();\n})();\n</script>",'''
  function route(force){
    var h=(location.hash||'').replace(/^#\\/?/,'').replace(/\\/+$/,'');
    var full=h?'#/'+h:'';
    if(!force && full===curHash) return;
    curHash=full;
    routing=true;
    try{
      var p=h?h.split('/').map(function(s){ try{return decodeURIComponent(s);}catch(e){return s;} }):[];
      if(!p.length){ showTab0('home'); }
      else if(p.length>=2 && document.getElementById('panel-'+p[0]) && document.querySelector('#panel-'+p[0]+' .subpanel[data-sub="'+p[1]+'"]')){ showTab0(p[0],p[1]); }
      else if(p.length===1 && document.getElementById('panel-'+p[0])){ showTab0(p[0]); }
      else { go(p[p.length-1]); }
    } finally { routing=false; }
  }
  function go(id){
    if(partiesData[id]){ showTab0('dj',partiesData[id].group); openParty0(id); return; }
    if(postsData[id]){ showTab0('behind',postsData[id].group); openPost0(id); return; }
    var el=null;
    document.querySelectorAll('[data-id]').forEach(function(n){ if(!el && n.getAttribute('data-id')===id) el=n; });
    if(!el){ showTab0('home'); return; }
    var sp=el.closest('.subpanel'), pn=el.closest('.panel');
    showTab0(pn.id.replace('panel-',''), sp.getAttribute('data-sub'));
    if(window.__hxReveal) window.__hxReveal(el);
    if(el.classList.contains('album-card')) el.classList.add('is-expanded');
    el.scrollIntoView({block:'center'});
    el.classList.remove('hx-flash'); void el.offsetWidth; el.classList.add('hx-flash');
  }
  window.addEventListener('popstate',function(){ route(); });
  window.addEventListener('hashchange',function(){ route(); });
  window.__hxRoute=route;

  applyLang();
})();
</script>''')
body=body.replace("  .card-grid{position:relative;}","  .card-grid{position:relative;}\n  @keyframes hxflash{0%,60%{box-shadow:0 0 0 3px var(--accent),0 10px 24px -8px rgba(14,143,132,.5);}100%{box-shadow:0 0 0 0 transparent;}}\n  .hx-flash{animation:hxflash 2s ease;}",1)
# reveal + initial route in 2nd script
R("  document.querySelectorAll('.card-grid').forEach(function(g){\n    g._old=false;","""  function refresh(g){
    g.querySelectorAll('.release-card').forEach(function(c){ if(vis(c,g)) c.removeAttribute('data-off'); else c.setAttribute('data-off',''); });
  }
  window.__hxReveal=function(el){
    var g=el.closest('.card-grid');
    if(!g||!el.hasAttribute('data-off')) return;
    g._old=true; g._flt=null;
    var bar=g.previousElementSibling;
    if(bar&&bar.classList.contains('flt-bar')) bar.querySelectorAll('input').forEach(function(i){ i.checked=true; });
    refresh(g);
  };
  function initFlt(g){
    var bar=g.previousElementSibling;
    if(bar&&bar.classList.contains('flt-bar')){
      var f={}; bar.querySelectorAll('input').forEach(function(i){ f[i.value]=i.hasAttribute('data-def'); });
      g._flt=f;
    } else g._flt=null;
  }
  function resetGrid(g){
    if(g._done) g._done();
    g._old=false;
    var bar=g.previousElementSibling;
    if(bar&&bar.classList.contains('flt-bar')) bar.querySelectorAll('input').forEach(function(i){ i.checked=i.hasAttribute('data-def'); });
    initFlt(g); refresh(g);
  }
  window.__hxReset=function(){
    document.querySelectorAll('.card-grid').forEach(function(g){ if(g.querySelector('.release-card')) resetGrid(g); });
  };
  document.querySelectorAll('.card-grid').forEach(function(g){
    g._old=false; initFlt(g); if(g.querySelector('.release-card')) refresh(g);""")
R("      g._flt=f; run(g);\n    });\n  });\n})();\n</script>","      g._flt=f; run(g);\n    });\n  });\n  if(window.__hxRoute) window.__hxRoute(true);\n})();\n</script>")
# ---- ids on album cards / sample packs ----
AID={'chaos in joy':'chaos-in-joy','subculture adventure!':'subculture-adventure','forever sunshine':'forever-sunshine','skyline simulator':'skyline-simulator','headphone headache':'headphone-headache','satellite oversky':'satellite-oversky','photosynthesis':'photosynthesis','airy vibe':'airy-vibe',"let's go, hardcore!":'lets-go-hardcore'}
def _alb(m):
    t=_html.unescape(m[3]).strip().lower()
    i=AID.get(t)
    assert i,t
    return '<div class="%s" data-id="%s"%s>%s'%(m[1],i,m[2] or '',m[4]) if False else m[0].replace('<div class="%s"'%m[1],'<div class="%s" data-id="%s"'%(m[1],i),1)
body=_re.sub(r'<div class="(album-card[^"]*)"([^>]*)>\s*<div class="album-card-main">.*?<h3 class="album-title">(.*?)</h3>',lambda m:(lambda t:(m[0].replace('<div class="%s"'%m[1],'<div class="%s" data-id="%s"'%(m[1],AID[t]),1) if t in AID else m[0]))(_html.unescape(m[3]).strip().lower()),body,flags=_re.S)
def _sp(m):
    t=_html.unescape(m[1])
    i='energyhard' if t.lower().startswith('energyhard') else ('doujin-hardcore-vocal-best' if 'VOCAL BEST' in t else None)
    return m[0].replace('<article class="post-card sample-card">','<article class="post-card sample-card"'+(' data-id="%s"'%i if i else '')+'>',1)
body=_re.sub(r'<article class="post-card sample-card">.*?<h3>(.*?)</h3>',_sp,body,flags=_re.S)
R('          <p class="altego-headline">','          <img class="altego-logo" src="assets/joker-mark.jpg" alt="COPYRiGHT JOKER logo">\n          <p class="altego-headline">')
R('  .altego-headline{','  .altego-logo{display:block;width:clamp(180px,34vw,320px);height:auto;margin:6px auto 18px;mix-blend-mode:multiply;}\n  .altego-headline{')
R('height:clamp(110px,20vw,190px);width:auto;margin:0 auto 22px;}','height:clamp(165px,30vw,290px);width:auto;margin:0 auto 22px;}')
R('width:clamp(180px,34vw,320px);height:auto;margin:6px auto 18px;','width:clamp(140px,22vw,225px);height:auto;margin:6px auto 18px;')

R('  function showTab0(tab, sub){','  function showTab0(tab, sub){\n    if(window.__hxReset) window.__hxReset();')
R('  function showSub0(tab, sub){','  function showSub0(tab, sub){\n    if(window.__hxReset) window.__hxReset();')

R('''                <a class="album-action-btn" href="https://hexacube.bandcamp.com/track/lets-go-hardcore" target="_blank" rel="noopener noreferrer">Download</a>
              </div>
            </div>''','''                <a class="album-action-btn" href="https://hexacube.bandcamp.com/track/lets-go-hardcore" target="_blank" rel="noopener noreferrer">Download</a>
              </div>
            </div>

            <div class="album-card no-expand" data-id="xnockmeout">
              <div class="album-card-main">
                <div class="album-cover"><img src="assets/xnockmeout-cover.jpg" alt="XNOCKMEOUT cover"></div>
                <div class="album-info">
                  <h3 class="album-title">XNOCKMEOUT</h3>
                  <p class="album-subtitle">Rooftop Release</p>
                  <div class="album-meta">
                    <span class="meta-line">Tearout Hardcore</span>
                    <span class="meta-line">2024.05.20</span>
                  </div>
                </div>
              </div>
              <div class="album-actions">
                <button class="album-action-btn album-goto" data-goto-sub="doujin">Doujin</button>
                <a class="album-action-btn" href="https://youtu.be/kqPG5xhXFeM?si=_DuyADdv6aZNBGYB" target="_blank" rel="noopener noreferrer">Video</a>
                <a class="album-action-btn" href="https://rooftop-official.bandcamp.com/album/xnockmeout-rooftop-release" target="_blank" rel="noopener noreferrer">Download</a>
              </div>
            </div>''')

exec(open('stories.py',encoding='utf8').read())

exec(open('langdd.py',encoding='utf8').read())

import re as _re, os as _os
body=_re.sub(r'((?:assets|covers)/[A-Za-z0-9_.-]+?)\.(?:jpg|jpeg|png)(?![A-Za-z0-9])',lambda m: m.group(1)+'.webp' if _os.path.exists('wp/'+m.group(1)+'.webp') else m.group(0),body)
