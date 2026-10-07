# ---- language selector: dropdown with dim backdrop ----
R('''    <div class="lang-toggle" role="group" aria-label="language">
      <button class="lang-seg is-active" data-lang="kr">KOR</button>
      <button class="lang-seg" data-lang="jp">JPN</button>
      <button class="lang-seg" data-lang="en">ENG</button>
    </div>''','''    <div class="lang-wrap" id="lang-wrap">
      <button class="lang-btn" id="lang-btn" type="button" aria-haspopup="listbox" aria-expanded="false" aria-label="language"><span id="lang-cur">KOR</span><span class="caret">&#9662;</span></button>
      <div class="lang-menu" id="lang-menu" role="listbox" aria-label="language">
        <button class="lang-seg is-active" data-lang="kr" role="option" type="button"><b>KOR</b><span>한국어</span></button>
        <button class="lang-seg" data-lang="jp" role="option" type="button"><b>JPN</b><span>日本語</span></button>
        <button class="lang-seg" data-lang="en" role="option" type="button"><b>ENG</b><span>English</span></button>
      </div>
    </div>''')
a=body.index('  .lang-toggle{'); b=body.index('  /* ---- persistent nav ---- */')
body=body[:a]+'''  .lang-wrap{position:relative;flex:0 0 auto;}
  .lang-btn{
    display:inline-flex;align-items:center;gap:6px;border:none;background:var(--wash);border-radius:999px;
    padding:7px 13px;font-family:var(--font-en);font-size:12.5px;font-weight:700;letter-spacing:.03em;
    color:var(--ink);cursor:pointer;transition:background-color .15s ease;
  }
  .lang-btn:hover,.lang-btn[aria-expanded="true"]{background:#e6ecec;}
  .lang-btn .caret{transition:transform .15s ease;}
  .lang-btn[aria-expanded="true"] .caret{transform:rotate(180deg);}
  .lang-menu{
    position:absolute;top:calc(100% + 8px);right:0;z-index:30;min-width:158px;
    background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:6px;
    box-shadow:0 16px 34px -14px rgba(10,20,20,.28);
    opacity:0;pointer-events:none;transform:translateY(-4px);transition:opacity .15s ease,transform .15s ease;
  }
  .lang-wrap.is-open .lang-menu{opacity:1;pointer-events:auto;transform:translateY(0);}
  .lang-seg{
    display:flex;align-items:center;justify-content:space-between;gap:14px;width:100%;
    border:none;background:none;padding:9px 12px;border-radius:9px;font-family:var(--font-kr);font-size:14px;
    color:var(--ink);cursor:pointer;text-align:left;
  }
  .lang-seg b{font-family:var(--font-en);font-size:12.5px;letter-spacing:.03em;}
  .lang-seg span{font-size:13px;color:var(--ink-soft);}
  .lang-seg:hover{background:#eef3f3;}
  /* always a fixed near-black pill, independent of the active color theme */
  .lang-seg.is-active{background:#10171c;color:#fff;}
  .lang-seg.is-active span{color:rgba(255,255,255,.75);}
  /* while the language menu is open the rest of the nav can't be used either */
  #app.lang-open .brand-mark,#app.lang-open .nav-tabs,#app.lang-open .hamburger{pointer-events:none;}
  html.lang-lock{overflow:hidden;}

'''+body[b:]
R('''    document.querySelectorAll('.lang-seg').forEach(function(b){
      b.classList.toggle('is-active', b.getAttribute('data-lang') === state.lang);
    });''','''    document.querySelectorAll('.lang-seg').forEach(function(b){
      b.classList.toggle('is-active', b.getAttribute('data-lang') === state.lang);
    });
    var langCur = document.getElementById('lang-cur');
    if(langCur) langCur.textContent = {kr:'KOR',jp:'JPN',en:'ENG'}[state.lang] || 'KOR';''')
R('''  document.getElementById('logo-home-btn').addEventListener('click',''','''  // ---- language dropdown (dims + locks the page behind it, like the hamburger menu) ----
  function openLang(){
    closeMobileMenu(true);
    var w=document.getElementById('lang-wrap'), bd=document.getElementById('mobile-backdrop');
    if(mobileCloseTimer){ clearTimeout(mobileCloseTimer); mobileCloseTimer=null; }
    w.classList.add('is-open'); document.getElementById('lang-btn').setAttribute('aria-expanded','true');
    bd.classList.add('is-open'); bd.style.pointerEvents='auto';
    document.getElementById('app').classList.add('lang-open'); document.documentElement.classList.add('lang-lock');
  }
  function closeLang(){
    var w=document.getElementById('lang-wrap');
    if(!w.classList.contains('is-open')) return;
    var bd=document.getElementById('mobile-backdrop');
    w.classList.remove('is-open'); document.getElementById('lang-btn').setAttribute('aria-expanded','false');
    bd.classList.remove('is-open');
    mobileCloseTimer=setTimeout(function(){ bd.style.pointerEvents='none'; },320);
    document.getElementById('app').classList.remove('lang-open'); document.documentElement.classList.remove('lang-lock');
  }
  document.getElementById('lang-btn').addEventListener('click', function(e){
    e.stopPropagation();
    if(document.getElementById('lang-wrap').classList.contains('is-open')) closeLang(); else openLang();
  });
  document.querySelectorAll('.lang-seg').forEach(function(b){ b.addEventListener('click', function(){ closeLang(); }); });
  document.getElementById('mobile-backdrop').addEventListener('click', closeLang);
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') closeLang(); });
  document.addEventListener('click', function(e){ if(!e.target.closest('#lang-wrap')) closeLang(); });

  document.getElementById('logo-home-btn').addEventListener('click',''')
