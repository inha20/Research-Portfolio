/* Research hub behaviour. Inlined into index.html by build.py. */
(function () {
  'use strict';
  var root = document.documentElement;
  var KEY = 'sr_theme';

  /* ---- theme: light/dark, remembered per browser ---- */
  var toggle = document.getElementById('theme-toggle');
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: light)') : null;

  function current() {
    var t = root.getAttribute('data-theme');
    if (t === 'dark' || t === 'light') return t;
    return mq && mq.matches ? 'light' : 'dark';
  }
  function label() {
    if (!toggle) return;
    var text = current() === 'dark' ? 'Switch to light theme' : 'Switch to dark theme';
    toggle.setAttribute('aria-label', text);
    toggle.setAttribute('title', text);
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) { /* storage can be blocked */ }
      label();
    });
    label();
  }
  if (mq && mq.addEventListener) {
    mq.addEventListener('change', function () {
      var stored = null;
      try { stored = localStorage.getItem(KEY); } catch (e) { /* ignore */ }
      if (stored !== 'dark' && stored !== 'light') {
        root.setAttribute('data-theme', mq.matches ? 'light' : 'dark');
        label();
      }
    });
  }

  /* The two <meta name="theme-color"> tags are matched by the browser against the operating-system setting, so a saved or
     toggled theme that differs from it left the toolbar in the wrong colour. Both tags get the colour of the theme that is
     showing, and follow every change. */
  var CHROME = { dark: '#0d0f17', light: '#fbfbf9' };
  function chrome() {
    var color = CHROME[current()];
    var tags = document.querySelectorAll('meta[name="theme-color"]');
    for (var j = 0; j < tags.length; j++) {
      if (tags[j].getAttribute('content') !== color) tags[j].setAttribute('content', color);
    }
  }
  chrome();
  if (window.MutationObserver) {
    new MutationObserver(chrome).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
  }

  /* ---- mobile menu ---- */
  var header = document.getElementById('site-header');
  var menuBtn = document.getElementById('menu-btn');
  function setMenu(open) {
    if (!header || !menuBtn) return;
    header.classList.toggle('nav-open', open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (header && menuBtn) {
    menuBtn.addEventListener('click', function () {
      setMenu(!header.classList.contains('nav-open'));
    });
    var links = header.querySelectorAll('.nav-links a');
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener('click', function () { setMenu(false); });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('nav-open')) {
        setMenu(false);
        menuBtn.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (!header.contains(e.target)) setMenu(false);
    });
  }

  /* ---- archive: open it when the address points at something inside ---- */
  var archive = document.getElementById('archive-list');
  function openForHash() {
    if (!archive || !location.hash || location.hash.length < 2) return;
    var el = null;
    try { el = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { return; }
    if (el && archive.contains(el)) {
      archive.open = true;
      el.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', openForHash);
  openForHash();

  /* ---- old addresses: earlier versions of the hub used other section names ---- */
  var ALIASES = {
    overview: 'top', architecture: 'map', repositories: 'current', author: 'about',
    program: 'map', 'hub-docs': 'documents', keywords: 'about'
  };
  function followAlias() {
    var id = location.hash.slice(1);
    if (!id || document.getElementById(id)) return;
    if (!Object.prototype.hasOwnProperty.call(ALIASES, id)) return;
    var to = ALIASES[id];
    if (window.history && history.replaceState) history.replaceState(null, '', '#' + to);
    var el = document.getElementById(to);
    if (el) el.scrollIntoView(); else window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', followAlias);
  followAlias();
})();
