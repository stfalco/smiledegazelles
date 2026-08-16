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

  /* ----- Carrousel (frise historique) -----
     Un seul jalon visible à la fois, navigation par flèches et points.
     Sans JavaScript, les jalons s'empilent (repli CSS via .is-enhanced). */
  document.querySelectorAll('[data-carousel]').forEach((carousel) => {
    const track = carousel.querySelector('.tl-carousel__track');
    const slides = Array.from(carousel.querySelectorAll('.tl-carousel__slide'));
    const prev = carousel.querySelector('[data-carousel-prev]');
    const next = carousel.querySelector('[data-carousel-next]');
    const dotsHost = carousel.querySelector('[data-carousel-dots]');
    if (!track || slides.length < 2) return;

    carousel.classList.add('is-enhanced');
    let index = 0;

    const dots = slides.map((_, i) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'tl-carousel__dot';
      dot.setAttribute('role', 'tab');
      dot.setAttribute('aria-label', 'Jalon ' + (i + 1) + ' sur ' + slides.length);
      dot.addEventListener('click', () => go(i));
      dotsHost && dotsHost.appendChild(dot);
      return dot;
    });

    function go(i) {
      index = (i + slides.length) % slides.length;
      track.style.transform = 'translateX(' + -index * 100 + '%)';
      slides.forEach((s, n) => s.setAttribute('aria-hidden', n === index ? 'false' : 'true'));
      dots.forEach((d, n) => {
        d.classList.toggle('is-active', n === index);
        d.setAttribute('aria-selected', n === index ? 'true' : 'false');
      });
    }

    prev && prev.addEventListener('click', () => go(index - 1));
    next && next.addEventListener('click', () => go(index + 1));
    carousel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') { go(index - 1); }
      else if (e.key === 'ArrowRight') { go(index + 1); }
    });

    go(0);
  });

  /* ----- Formules : présélection dans le formulaire de contact -----
     Chaque carte porte un [data-formule] dont la valeur correspond à l'option
     du <select name="formule">. Le lien reste un simple ancrage vers #contact
     si le script n'est pas exécuté. */
  const formuleSelect = document.querySelector('select[name="formule"]');
  const formuleLinks = document.querySelectorAll('[data-formule]');
  if (formuleSelect && formuleLinks.length) {
    const objetSelect = document.querySelector('select[name="objet"]');
    let flashTimer;
    formuleLinks.forEach((link) => {
      link.addEventListener('click', function () {
        formuleSelect.value = link.dataset.formule;
        if (objetSelect) objetSelect.value = 'sponsor';
        formuleSelect.classList.add('is-prefilled');
        clearTimeout(flashTimer);
        flashTimer = setTimeout(() => formuleSelect.classList.remove('is-prefilled'), 2600);
      });
    });
  }

  /* ----- Objet présélectionné dans le formulaire de contact -----
     Les liens [data-objet] (espace presse notamment) pointent vers #ecrire et
     positionnent la liste « Objet » sur la bonne valeur. Sans script, l'ancre
     fonctionne toujours : la liste reste simplement sur son option par défaut. */
  const objetSelectContact = document.querySelector('select[name="objet"]');
  const objetLinks = document.querySelectorAll('[data-objet]');
  if (objetSelectContact && objetLinks.length) {
    let objetTimer;
    objetLinks.forEach((link) => {
      link.addEventListener('click', function () {
        objetSelectContact.value = link.dataset.objet;
        objetSelectContact.classList.add('is-prefilled');
        clearTimeout(objetTimer);
        objetTimer = setTimeout(() => objetSelectContact.classList.remove('is-prefilled'), 2600);
      });
    });
  }

  /* ----- Formulaire de contact (Netlify Forms) -----
     Le formulaire est un POST classique : sans JavaScript, Netlify enregistre
     le message et affiche sa propre page de confirmation. Le script ci-dessous
     ne fait qu'envoyer les mêmes données en arrière-plan pour afficher la
     confirmation sans quitter la page. En cas d'échec, on affiche l'adresse
     email plutôt que de perdre le message en silence. */
  const contactForm = document.querySelector('[data-contact-form]');
  if (contactForm && window.fetch) {
    const successBox = document.querySelector('[data-form-success]');
    const errorBox = contactForm.querySelector('[data-form-error]');
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const submitLabel = submitBtn ? submitBtn.textContent : '';
      if (errorBox) errorBox.hidden = true;
      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Envoi en cours…'; }
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(contactForm)).toString(),
      })
        .then(function (res) {
          if (!res.ok) throw new Error('Réponse ' + res.status);
          // .form est en display:flex : l'attribut hidden ne suffirait pas à le masquer.
          contactForm.style.display = 'none';
          if (successBox) {
            successBox.hidden = false;
            successBox.focus();
          }
        })
        .catch(function () {
          if (errorBox) errorBox.hidden = false;
        })
        .finally(function () {
          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = submitLabel; }
        });
    });
  }

  /* ----- Ancres internes : scroll précis sous header sticky ----- */
  const scrollToHashTarget = (hash, smooth) => {
    if (!hash || hash === '#') return;
    const target = document.querySelector(hash);
    if (!target) return;

    const headerEl = document.querySelector('.header');
    const headerHeight = headerEl ? headerEl.getBoundingClientRect().height : 0;
    const top = window.scrollY + target.getBoundingClientRect().top - headerHeight - 12;
    window.scrollTo({ top: Math.max(0, top), behavior: smooth ? 'smooth' : 'auto' });
  };

  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach((link) => {
    link.addEventListener('click', (e) => {
      const hash = link.getAttribute('href');
      if (!hash) return;
      e.preventDefault();
      if (window.location.hash !== hash) history.pushState(null, '', hash);
      scrollToHashTarget(hash, true);
    });
  });

  window.addEventListener('hashchange', () => {
    scrollToHashTarget(window.location.hash, false);
  });

  if (window.location.hash && window.location.hash !== '#') {
    requestAnimationFrame(() => scrollToHashTarget(window.location.hash, false));
  }

  /* ----- Année dynamique footer ----- */
  const yr = document.querySelector('[data-year]');
  if (yr) yr.textContent = new Date().getFullYear();
})();
