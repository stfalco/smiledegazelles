/* SMILE DE GAZELLES — interactions */
(function () {
  'use strict';

  /* ----- Thème clair/sombre ----- */
  const toggle = document.querySelector('[data-theme-toggle]');
  const root = document.documentElement;
  let mode = 'light';
  root.setAttribute('data-theme', mode);
  function iconFor(m) {
    return m === 'dark'
      ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
      : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }
  if (toggle) {
    toggle.innerHTML = iconFor(mode);
    toggle.addEventListener('click', function () {
      mode = mode === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', mode);
      toggle.innerHTML = iconFor(mode);
      toggle.setAttribute('aria-label', 'Basculer en mode ' + (mode === 'dark' ? 'clair' : 'sombre'));
    });
  }

  /* ----- Header au scroll ----- */
  const header = document.querySelector('.header');
  if (header) {
    const onScroll = () => header.classList.toggle('header--scrolled', window.scrollY > 12);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ----- Menu mobile ----- */
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      const open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach((a) =>
      a.addEventListener('click', () => nav.classList.remove('is-open'))
    );
  }

  /* ----- Compte à rebours (départ 20 mars 2027) ----- */
  const cd = document.querySelector('[data-countdown]');
  if (cd) {
    const target = new Date('2027-03-20T08:00:00+01:00').getTime();
    const el = {
      d: cd.querySelector('[data-d]'), h: cd.querySelector('[data-h]'),
      m: cd.querySelector('[data-m]'), s: cd.querySelector('[data-s]'),
    };
    const pad = (n) => String(n).padStart(2, '0');
    function tick() {
      const diff = target - Date.now();
      if (diff <= 0) { Object.values(el).forEach((e) => e && (e.textContent = '00')); return; }
      const d = Math.floor(diff / 86400000);
      const h = Math.floor((diff % 86400000) / 3600000);
      const m = Math.floor((diff % 3600000) / 60000);
      const s = Math.floor((diff % 60000) / 1000);
      if (el.d) el.d.textContent = d;
      if (el.h) el.h.textContent = pad(h);
      if (el.m) el.m.textContent = pad(m);
      if (el.s) el.s.textContent = pad(s);
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ----- Animations au scroll ----- */
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      }),
      { threshold: 0.12 }
    );
    reveals.forEach((r) => io.observe(r));
  } else {
    reveals.forEach((r) => r.classList.add('is-visible'));
  }

  /* ----- Année dynamique footer ----- */
  const yr = document.querySelector('[data-year]');
  if (yr) yr.textContent = new Date().getFullYear();
})();
