#!/usr/bin/env python3
"""Génère les pages intérieures du site Smile de Gazelles (préfixe ../ pour les assets).

Note : index.html n'est PAS généré par ce script. La page d'accueil est maintenue
à la main ; l'en-tête, le pied de page et les liens sociaux ci-dessous sont alignés
sur elle et doivent le rester si elle évolue.
"""
import os

PAGES_DIR = os.path.join(os.path.dirname(__file__), "pages")
os.makedirs(PAGES_DIR, exist_ok=True)

# Logo officiel — bascule clair/sombre, préfixe ../ pour les pages intérieures
LOGO_IMG = '''<img class="logo__img logo__img--light" src="../assets/logo.png" alt="Smile de Gazelles" width="62" height="62" />
        <img class="logo__img logo__img--dark" src="../assets/logo-dark.png" alt="Smile de Gazelles" width="62" height="62" />
        <span class="logo__team-text" aria-hidden="true">
          <span>Equipage 134</span>
          <span>Rallye Aïcha Des Gazelles</span>
        </span>'''

# Emblème officiel pour le footer — bascule clair/sombre
LOGO_EMBLEM = '''<img class="logo__emblem logo__emblem--light" src="../assets/logo.png" alt="Smile de Gazelles" width="130" height="130" />
            <img class="logo__emblem logo__emblem--dark" src="../assets/logo-dark.png" alt="Smile de Gazelles" width="130" height="130" />'''

# Réseaux sociaux officiels de l'équipage
URL_FACEBOOK = "https://www.facebook.com/smiledegazelles"
URL_INSTAGRAM = "https://www.instagram.com/smiledegazelles2027"

NAV_ITEMS = [
    ("index.html", "Accueil", "accueil"),
    ("equipage.html", "L'équipage", "equipage"),
    ("le-rallye.html", "Le rallye", "le-rallye"),
    ("solidarite.html", "Solidarité et RSE", "solidarite"),
    ("sponsors.html", "Sponsors", "sponsors"),
    ("soutenir.html", "Nous soutenir", "soutenir"),
    ("contact.html", "Contact", "contact"),
]

def nav_links(current):
    out = []
    for href, label, key in NAV_ITEMS:
        target = "../index.html" if href == "index.html" else href
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'          <li><a href="{target}"{cur}>{label}</a></li>')
    return "\n".join(out)

def header(current):
    return f'''  <header class="header">
    <div class="container header__inner">
      <a href="../index.html" class="logo" aria-label="Smile de Gazelles, accueil">
        {LOGO_IMG}
      </a>
      <nav class="nav" aria-label="Navigation principale">
        <ul class="nav__links">
{nav_links(current)}
        </ul>
      </nav>
      <div class="header__actions">
        <button class="theme-toggle" data-theme-toggle aria-label="Basculer le thème"></button>
        <a href="soutenir.html" class="btn btn-primary">Contribuer</a>
        <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>'''

FOOTER = f'''  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a href="../index.html" class="logo logo--footer">
            {LOGO_EMBLEM}
          </a>
          <p>Deux femmes, un défi, mille sourires à partager. Équipage engagé au Rallye Aïcha des Gazelles 2027 — l'énergie du défi au service d'une aventure solidaire.</p>
          <div class="socials">
            <a href="{URL_INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
            <a href="{URL_FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
          </div>
        </div>
        <div class="footer__col"><h4>Navigation</h4><ul>
          <li><a href="equipage.html">L'équipage</a></li>
          <li><a href="le-rallye.html">Le rallye</a></li>
          <li><a href="solidarite.html">Solidarité et RSE</a></li>
          <li><a href="sponsors.html">Sponsors</a></li>
        </ul></div>
        <div class="footer__col"><h4>Soutenir</h4><ul>
          <li><a href="soutenir.html">Faire un don</a></li>
          <li><a href="sponsors.html">Devenir sponsor</a></li>
          <li><a href="contact.html">Nous contacter</a></li>
        </ul></div>
      </div>
      <div class="footer__bottom">
        <span>© <span data-year>2027</span> Smile de Gazelles — Tous droits réservés.</span>
        <span>Crédits photos du rallye&nbsp;: © Maïenga.</span>
        <span>Site réalisé avec ❤️ pour l'aventure.</span>
      </div>
    </div>
  </footer>'''

def page(current, title, desc, page_hero, body, og_desc=None, og_image="../assets/hero-desert.png",
         hero_photo=None, hero_eyebrow=None, hero_stamp=None, hero_actions=None):
    """Assemble une page intérieure.

    page_hero   : (titre H1, chapô)
    og_desc     : description Open Graph si elle diffère de la meta description
    og_image    : visuel de partage
    hero_photo  : chemin d'une photo affichée en bandeau derrière l'en-tête
    hero_eyebrow: étiquette affichée au-dessus du H1
    hero_stamp  : logo posé en aplat transparent sur le bandeau (ex. logo team RAG)
    hero_actions: bloc HTML (boutons, mention) inséré sous le chapô du bandeau
    """
    hero_class = "page-hero page-hero--photo" if hero_photo else "page-hero"
    hero_style = f''' style="--page-hero-img:url('{hero_photo}')"''' if hero_photo else ""
    eyebrow = f'\n        <span class="page-hero__eyebrow">{hero_eyebrow}</span>' if hero_eyebrow else ""
    stamp = (f'\n      <img class="page-hero__stamp" src="{hero_stamp}" alt="" aria-hidden="true" />'
             if hero_stamp else "")
    actions = f'\n{hero_actions}' if hero_actions else ""
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Smile de Gazelles</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{title} — Smile de Gazelles" />
  <meta property="og:description" content="{og_desc or desc}" />
  <meta property="og:image" content="{og_image}" />
  <link rel="icon" href="../assets/favicon.png" type="image/png" />
  <link rel="preconnect" href="https://api.fontshare.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&f[]=clash-display@500,600,700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>
{header(current)}
  <main>
    <section class="{hero_class}"{hero_style}>
      <div class="container container-default">
        <p class="breadcrumb"><a href="../index.html">Accueil</a> / {title}</p>{eyebrow}
        <h1>{page_hero[0]}</h1>
        <p>{page_hero[1]}</p>{actions}
      </div>{stamp}
    </section>
{body}
  </main>
{FOOTER}
  <script src="../js/main.js"></script>
</body>
</html>
'''

# ============ CONTENUS DES PAGES ============
PAGES = {}

# ---- ÉQUIPAGE ----
PAGES["equipage.html"] = page(
    "equipage", "L'équipage",
    "Sandra Aversenq et Stéphanie Falco, équipage 134 du Rallye Aïcha des Gazelles 2027 : "
    "leurs portraits, leur préparation, le budget détaillé et l'association Smile de Gazelles.",
    ("L'alliance de la maîtrise et de l'instinct",
     "Tout est parti d'une conversation et d'un rêve un peu fou : prendre le départ du Rallye "
     "Aïcha des Gazelles. Un an plus tard, le rêve est devenu un projet, puis une inscription "
     "pour 2027. Notre déclic ? Arrêter d'attendre, oser l'inconnu et passer à l'action."),
    '''
    <!-- ============ LES PORTRAITS ============ -->
    <section id="portraits">
      <div class="container">
        <div class="crew-grid reveal">
          <article class="crew-card">
            <div class="crew-card__photo">
              <img src="../assets/portrait-sandra.jpg" alt="Portrait de Sandra Aversenq" loading="lazy" />
            </div>
            <div class="crew-card__body">
              <h2 class="crew-card__name">Sandra Aversenq</h2>
              <span class="crew-card__role">« Wonder Sandra »</span>
              <div class="crew-card__meta"><span>53 ans</span><span>Chef d'entreprise</span></div>
              <p class="crew-card__bio">Entrepreneuse instinctive, fonceuse et structurée — un mélange rare. Ses nombreux voyages l'ont façonnée : elle y cherche moins les paysages que les échanges et les rencontres humaines authentiques.</p>
              <p class="crew-card__bio">Elle apporte à l'équipage sa vision pragmatique des affaires, son leadership naturel et sa réactivité face aux crises de terrain. Là où d'autres hésitent, elle décide.</p>
              <!-- Citation personnelle à recueillir auprès de Sandra : une phrase sur ce que ce rallye représente pour elle. -->
              <div class="crew-card__strengths">
                <span class="crew-card__strengths-title">Ce qu'elle apporte</span>
                <ul class="chips">
                  <li class="chip">Leadership</li>
                  <li class="chip">Décision rapide</li>
                  <li class="chip">Sens du contact</li>
                </ul>
              </div>
            </div>
          </article>
          <article class="crew-card">
            <div class="crew-card__photo">
              <img src="../assets/portrait-stephanie.jpg" alt="Portrait de Stéphanie Falco" loading="lazy" />
            </div>
            <div class="crew-card__body">
              <h2 class="crew-card__name">Stéphanie Falco</h2>
              <span class="crew-card__role">Cadre supérieur RH</span>
              <div class="crew-card__meta"><span>49 ans</span><span>Collectif « Les Biches »</span></div>
              <p class="crew-card__bio">Co-fondatrice du collectif « Les Biches », qui met en avant les femmes artistes, elle est profondément animée par la force du collectif. Bercée dès son plus jeune âge par le ronflement des 4x4 de son père, habitué des rallyes de franchissement, elle allie sérénité et sens de la mécanique.</p>
              <p class="crew-card__bio">Face à l'imprévu, elle apporte le calme et l'énergie, avec une capacité d'analyse qui, dans une épreuve où tout se joue sur la précision du pilotage, n'a rien d'un détail.</p>
              <blockquote class="crew-card__quote">« Ils ne savaient pas que c'était impossible, alors ils l'ont fait. »</blockquote>
              <div class="crew-card__strengths">
                <span class="crew-card__strengths-title">Ce qu'elle apporte</span>
                <ul class="chips">
                  <li class="chip">Rigueur d'analyse</li>
                  <li class="chip">Mécanique</li>
                  <li class="chip">Sang-froid</li>
                </ul>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- ============ NOTRE BINÔME ============ -->
    <section class="section-alt">
      <div class="container">
        <div class="split reveal">
          <div class="split__media">
            <img src="../assets/duo-signature.jpg" alt="Sandra Aversenq et Stéphanie Falco, l'équipage Smile de Gazelles" loading="lazy" />
          </div>
          <div class="split__body">
            <span class="eyebrow">Notre binôme</span>
            <h2>Deux tempéraments, une même trajectoire</h2>
            <p>Dans le désert, l'équipage compte autant que le véhicule. Pendant sept jours de course, il faut décider vite et bien, se relayer au volant et à la carte, gérer la fatigue, les erreurs et les imprévus — sans jamais se retourner l'une contre l'autre. C'est l'entraide qui fait la différence, bien plus que la performance individuelle.</p>
            <blockquote class="quote">« Deux âmes réunies autour d'un projet associatif ambitieux et unique. Une aventure qui s'annonce déjà inoubliable, jalonnée d'obstacles et d'imprévus, mais surtout riche de sens, de rencontres et d'émotions. »</blockquote>
            <p><strong>Deux femmes — un défi — mille sourires à partager.</strong></p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ DU RÊVE AU DÉPART ============ -->
    <section id="parcours">
      <div class="container">
        <div class="reveal">
          <span class="eyebrow">Notre parcours</span>
          <h2 class="section-title">Du rêve au départ</h2>
          <p class="section-lead">Chaque étape nous rapproche du désert.</p>
        </div>
        <div class="roadmap reveal">
          <div class="roadmap__item roadmap__item--done">
            <div class="roadmap__step">✓ Réalisé</div>
            <div class="roadmap__title">Le déclic</div>
            <div class="roadmap__label">Été 2024 — et si on se lançait&nbsp;?</div>
          </div>
          <div class="roadmap__item roadmap__item--done">
            <div class="roadmap__step">✓ Réalisé</div>
            <div class="roadmap__title">L'association</div>
            <div class="roadmap__label">Smile de Gazelles est créée en juillet 2026.</div>
          </div>
          <div class="roadmap__item roadmap__item--done">
            <div class="roadmap__step">✓ Réalisé</div>
            <div class="roadmap__title">L'inscription</div>
            <div class="roadmap__label">Team 134 : le départ est confirmé.</div>
          </div>
          <div class="roadmap__item roadmap__item--current">
            <div class="roadmap__step">◉ En cours</div>
            <div class="roadmap__title">La préparation</div>
            <div class="roadmap__label">Physique, mentale et logistique.</div>
            <span class="roadmap__here">Vous êtes ici</span>
          </div>
          <div class="roadmap__item roadmap__item--todo">
            <div class="roadmap__step">○ À venir</div>
            <div class="roadmap__title">La préparation technique</div>
            <div class="roadmap__label">Navigation, 4x4 et pilotage.</div>
          </div>
          <div class="roadmap__item roadmap__item--todo roadmap__item--goal">
            <div class="roadmap__step">⚑ Objectif</div>
            <div class="roadmap__title">Le départ</div>
            <div class="roadmap__label">20 mars 2027.</div>
          </div>
        </div>
        <ul class="roadmap-legend reveal">
          <li><span class="dot dot--done"></span> Réalisé</li>
          <li><span class="dot dot--current"></span> En cours</li>
          <li><span class="dot dot--todo"></span> À venir</li>
        </ul>
        <div class="actions reveal">
          <a href="sponsors.html" class="btn btn-primary">Aidez-nous à franchir ces étapes</a>
        </div>
        <div class="band band--rounded reveal" style="margin-top:var(--space-12)">
          <img src="../assets/equipage_parcours.jpg" alt="L'équipage Smile de Gazelles en préparation" loading="lazy" />
        </div>
      </div>
    </section>

    <!-- ============ NOTRE PRÉPARATION ============ -->
    <section class="section-alt" id="preparation">
      <div class="container">
        <div class="reveal" style="margin-bottom:var(--space-12)">
          <span class="eyebrow">Se préparer</span>
          <h2 class="section-title">Rien n'est laissé au hasard</h2>
          <p class="section-lead">Primo-participantes, nous abordons ce rallye avec méthode : quatre chantiers menés de front jusqu'à la ligne de départ.</p>
        </div>
        <div class="cards-grid reveal">
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
            <h3>Physique</h3>
            <p>Endurance et résistance à la chaleur, gainage, préparation au manque de sommeil. Sept jours d'effort continu, sous quarante degrés, avec des nuits courtes au bivouac.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16.24 7.76l-2.12 6.36-6.36 2.12 2.12-6.36 6.36-2.12z"/></svg></div>
            <h3>Navigation</h3>
            <p>Stage dédié à la lecture de carte, à l'utilisation du compas et au calcul de cap. C'est la compétence décisive : le classement récompense la précision, pas la vitesse.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 17h18"/><path d="M5 17l1.5-5.5A2 2 0 0 1 8.4 10h7.2a2 2 0 0 1 1.9 1.5L19 17"/><circle cx="7" cy="19" r="2"/><circle cx="17" cy="19" r="2"/></svg></div>
            <h3>Pilotage</h3>
            <p>Stage au Maroc, sur le terrain réel : franchissement, passage de dunes, désensablement, lecture du sable.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0 5 5l-8.4 8.4a2.8 2.8 0 0 1-4-4L15.7 7.3z"/><path d="M9.3 17.7l-4 4"/></svg></div>
            <h3>Mécanique et matériel</h3>
            <p>Préparation du véhicule, pièces de rechange, équipement de bivouac, balise satellite IRITRACK, odomètre, boussole, casques.</p>
          </div>
        </div>
        <div class="gallery reveal">
          <img src="../assets/accueil-teaser-rallye-1.jpg" alt="Franchissement de dunes en 4x4 lors du rallye" loading="lazy" />
          <img src="../assets/navigation.png" alt="Navigation à la carte et à la boussole, sans GPS" loading="lazy" />
          <img src="../assets/equipage_prepa.jpg" alt="L'équipage pendant sa préparation" loading="lazy" />
        </div>
        <div class="actions reveal">
          <a href="#budget" class="btn btn-outline">Le détail de notre budget</a>
          <a href="sponsors.html" class="btn btn-primary">Financer notre préparation</a>
        </div>
      </div>
    </section>

    <!-- ============ LE BUDGET ============ -->
    <section id="budget">
      <div class="container container-default">
        <div class="reveal">
          <span class="eyebrow">Un projet construit avec vous</span>
          <h2 class="section-title">Chaque contribution donne vie à l'aventure</h2>
          <p class="section-lead">Participer au Rallye Aïcha des Gazelles représente un budget global de <strong>42 000 €</strong>. Cette somme couvre l'ensemble de notre participation : le véhicule, les frais d'inscription, la préparation, la sécurité, la logistique et la communication. Chaque dépense répond à un besoin concret pour nous permettre de prendre le départ dans les meilleures conditions.</p>
        </div>
        <div class="budget-bars reveal">
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Frais d'inscription</span>
              <span class="budget-line__amount">14 500 €<span>34,5 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:34.5%"></div></div>
          </div>
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Location du 4x4, préparation, pièces, assurances</span>
              <span class="budget-line__amount">11 000 €<span>26,2 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:26.2%"></div></div>
          </div>
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Stages de pilotage et de navigation, équipement</span>
              <span class="budget-line__amount">5 000 €<span>11,9 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:11.9%"></div></div>
          </div>
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Aller et retour jusqu'au désert marocain</span>
              <span class="budget-line__amount">4 300 €<span>10,2 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:10.2%"></div></div>
          </div>
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Sécurité : balise IRITRACK, odomètre, casques, boussole</span>
              <span class="budget-line__amount">3 800 €<span>9,0 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:9%"></div></div>
          </div>
          <div class="budget-line">
            <div class="budget-line__head">
              <span class="budget-line__label">Communication, animations, covering</span>
              <span class="budget-line__amount">3 400 €<span>8,1 %</span></span>
            </div>
            <div class="budget-line__track"><div class="budget-line__fill" style="width:8.1%"></div></div>
          </div>
        </div>
        <div class="budget-total reveal">
          <span class="budget-total__label">Budget total de participation</span>
          <span class="budget-total__value">42 000 €</span>
        </div>
        <details class="accordion reveal">
          <summary>Que couvrent les frais d'inscription&nbsp;?</summary>
          <div class="accordion__body">
            <ul>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Encadrement</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Assistance médicale</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Assistance mécanique</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Vie au bivouac</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Sécurité et assurances</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg> Communication et médias</li>
            </ul>
          </div>
        </details>
        <div class="pledge reveal">
          <h3>Notre engagement</h3>
          <p>L'association Smile de Gazelles est l'unique organisme collecteur des sommes versées pour couvrir le budget de participation au rallye. Le reliquat sera versé en intégralité à l'association Cœur de Gazelles.</p>
        </div>
      </div>
    </section>

    <!-- ============ L'ASSOCIATION ============ -->
    <section class="section-alt" id="association">
      <div class="container">
        <div class="split split--reverse reveal">
          <div class="split__media split__media--portrait" style="display:flex;align-items:center;justify-content:center">
            <img src="../assets/logo.png" alt="Logo de l'association Smile de Gazelles" style="aspect-ratio:auto;box-shadow:none;border-radius:0;max-width:320px" loading="lazy" />
          </div>
          <div class="split__body">
            <span class="eyebrow">Notre association</span>
            <h2>Défendre des valeurs qui nous animent</h2>
            <p>L'association Smile de Gazelles est née de la volonté de deux amies de faire d'une aventure sportive un véritable projet humain. Animées par des valeurs communes de solidarité, d'engagement, de respect, de dépassement de soi et de partage, nous inscrivons chacune de nos actions dans une démarche porteuse de sens.</p>
            <p>Participer au Rallye Aïcha des Gazelles s'est imposé comme une évidence. Bien plus qu'une compétition, ce rallye incarne l'entraide, l'autonomie et l'engagement solidaire, notamment à travers les actions de Cœur de Gazelles auprès des populations locales.</p>
            <p>Notre objectif : sortir de notre zone de confort, repousser les limites, et prouver qu'avec de la détermination, de l'audace, de la persévérance, de l'entraide et de la bonne humeur, il est possible de déplacer des montagnes — même au cœur du désert.</p>
            <ul class="chips" style="margin-top:var(--space-6)">
              <li class="chip chip--gold">Solidarité</li>
              <li class="chip chip--gold">Engagement</li>
              <li class="chip chip--gold">Respect</li>
              <li class="chip chip--gold">Dépassement de soi</li>
              <li class="chip chip--gold">Partage</li>
            </ul>
            <blockquote class="quote">« Un gagnant est un rêveur qui n'abandonne jamais. »</blockquote>
          </div>
        </div>
        <div class="id-card reveal" style="margin-top:clamp(var(--space-12), 6vw, var(--space-20))">
          <h3>Fiche d'identité</h3>
          <dl>
            <dt>Nom</dt><dd>Association Smile de Gazelles — association loi 1901 à but non lucratif</dd>
            <dt>Déclaration</dt><dd>Préfecture n° W343034911 · SIREN 108 320 961</dd>
            <dt>Siège social</dt><dd>453 Enclos des Palourdes, 34130 Carnon</dd>
            <dt>Objet</dt><dd>Participation au Rallye Aïcha des Gazelles et actions solidaires associées</dd>
            <dt>Collecte</dt><dd>Unique organisme collecteur des sommes versées pour la participation au rallye</dd>
          </dl>
        </div>
      </div>
    </section>

    <!-- ============ SUIVEZ L'AVENTURE ============ -->
    <section class="section--compact">
      <div class="container container-default text-center">
        <div class="reveal">
          <span class="eyebrow" style="justify-content:center">Suivez l'aventure</span>
          <h2 class="section-title" style="font-size:var(--text-xl)">Photos, coulisses et avancées du projet</h2>
          <p class="section-lead mx-auto">Photos de préparation, coulisses, avancées du projet : nous partageons tout sur nos réseaux.</p>
          <div class="social-links">
            <a class="social-link" href="https://www.facebook.com/smiledegazelles" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
              facebook.com/smiledegazelles
            </a>
            <a class="social-link" href="https://www.instagram.com/smiledegazelles2027" target="_blank" rel="noopener">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
              instagram.com/smiledegazelles2027
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ APPEL FINAL ============ -->
    <section>
      <div class="container">
        <div class="cta-banner reveal">
          <h2>Rejoignez l'aventure et donnez du sens à votre engagement</h2>
          <p>Devenez sponsor ou faites un don : chaque contribution nous rapproche de la ligne de départ et du reliquat reversé à Cœur de Gazelles.</p>
          <div class="hero__cta">
            <a href="sponsors.html" class="btn btn-light btn-lg">Devenir sponsor</a>
            <a href="soutenir.html" class="btn btn-outline btn-lg" style="color:#fff;border-color:rgba(255,255,255,0.6)">Faire un don</a>
          </div>
        </div>
      </div>
    </section>''',
    og_desc="Deux tempéraments, une même trajectoire. Découvrez l'équipage 134, "
            "sa préparation, son budget et son association.",
    og_image="../assets/equipage_hero.JPG",
    hero_photo="../assets/equipage_hero.JPG",
    hero_eyebrow="Équipage 134 · Smile de Gazelles",
    hero_stamp="../assets/logo-team-rag.png")

# ---- LE RALLYE ----
PAGES["le-rallye.html"] = page(
    "le-rallye", "Le rallye",
    "Le Rallye Aïcha des Gazelles : navigation sans GPS, calendrier de l'édition 2027, "
    "histoire depuis 1990, certification ISO 14001 et reconnaissance de l'épreuve.",
    ("Le Rallye Aïcha des Gazelles",
     "Le seul rallye-raid hors-piste certifié ISO 14001 au monde, 100&nbsp;% féminin, "
     "au cœur du Sahara marocain."),
    '''    <!-- ============ LE CONCEPT ============ -->
    <section id="concept">
      <div class="container">
        <div class="reveal" style="margin-bottom:var(--space-12)">
          <span class="eyebrow">Le concept</span>
          <h2 class="section-title">Ici, la stratégie prime sur la rapidité</h2>
          <p class="section-lead">Le principe est rare, presque anachronique&nbsp;: naviguer à l'ancienne. Munies d'une carte des années 1950, d'une boussole et d'une règle de navigation, les équipages traversent les regs, les oueds, les dunes et les montagnes du sud marocain. Chaque itinéraire est un choix, chaque décision est assumée.</p>
          <p style="color:var(--color-text-muted);max-width:68ch">Le classement récompense la sobriété kilométrique&nbsp;: celle qui rallie le plus de balises en parcourant le moins de kilomètres l'emporte. Un principe qui aligne performance sportive et respect de l'environnement — et qui n'a pas d'équivalent dans le sport automobile.</p>
        </div>
        <div class="cards-grid reveal">
          <div class="card card--photo">
            <img src="../assets/rallye_02.JPG" alt="Navigation à la carte et à la boussole, sans GPS" loading="lazy" />
            <div class="card__body">
              <h3>Navigation à l'ancienne</h3>
              <p>Carte, boussole, règle. Aucun GPS, aucune assistance électronique. Un week-end de formation permet d'acquérir les bases avant le départ.</p>
            </div>
          </div>
          <div class="card card--photo">
            <img src="../assets/rallye_04.JPG" alt="Regs, oueds, dunes et montagnes du sud marocain" loading="lazy" />
            <div class="card__body">
              <h3>Terrain imprévisible</h3>
              <p>Regs, oueds, dunes, montagnes. Chaque jour est une immersion dans l'inconnu, où l'orientation reste la clé.</p>
            </div>
          </div>
          <div class="card card--photo">
            <img src="../assets/rallye_feminin.JPG" alt="Des équipages 100 % féminins, débutantes comme expérimentées" loading="lazy" />
            <div class="card__body">
              <h3>Accessible à toutes</h3>
              <p>Débutantes comme expérimentées. Il ne s'agit pas d'être sportive de haut niveau, mais d'avoir l'envie, l'audace et l'esprit d'équipe.</p>
            </div>
          </div>
        </div>
        <div class="note reveal">
          <p>Nous concourons en <strong>4x4</strong>, la catégorie historique du rallye — franchissements techniques et terrain mixte.</p>
        </div>
        <div class="actions reveal">
          <a href="sponsors.html" class="btn btn-primary">Nous aider à prendre le départ</a>
        </div>
      </div>
    </section>

    <!-- ============ L'ÉDITION 2027 ============ -->
    <section class="section-alt" id="edition-2027">
      <div class="container container-default">
        <div class="reveal" style="margin-bottom:var(--space-10)">
          <span class="eyebrow">L'agenda</span>
          <h2 class="section-title">Quinze jours d'aventure, du sud de la France à Essaouira</h2>
          <p class="section-lead">Le calendrier se lit en trois temps&nbsp;: le départ, la course, l'arrivée. Chaque acte se déplie pour en révéler les dates.</p>
        </div>
        <details class="accordion reveal" open>
          <summary><span class="acte__title">Acte I — Le départ <em>Du sud de la France au Maroc</em></span></summary>
          <div class="accordion__body">
            <ul class="agenda">
              <li><span class="agenda__date">Samedi 20 mars</span> Accueil des équipages, briefing dans le sud de la France, remise des gilets Gazelles.</li>
              <li><span class="agenda__date">Dimanche 21 mars</span> Vérifications techniques et administratives, départ officiel, embarquement pour le Maroc.</li>
              <li><span class="agenda__date">Lundi 22 mars</span> Arrivée au Maroc, rencontre des équipages internationaux.</li>
            </ul>
          </div>
        </details>
        <details class="accordion reveal">
          <summary><span class="acte__title">Acte II — La course <em>Sept jours dans le désert</em></span></summary>
          <div class="accordion__body">
            <ul class="agenda">
              <li><span class="agenda__date">Jeudi 25 mars</span> Accompagnement de la caravane Cœur de Gazelles et remise des dons. <span class="agenda__aside">Le détail de cette action solidaire est sur la <a href="solidarite.html">page Solidarité</a>.</span></li>
              <li><span class="agenda__date">Du 26 mars au 1<sup>er</sup> avril</span> Un prologue puis cinq étapes sans GPS, avec cinq à huit balises à retrouver chaque jour, dont deux étapes marathon&nbsp;: deux nuits en autonomie complète, à la belle étoile, sans retour au bivouac.</li>
              <li><span class="agenda__date">Jeudi 1<sup>er</sup> avril</span> Fête de fin au bivouac.</li>
            </ul>
          </div>
        </details>
        <details class="accordion reveal">
          <summary><span class="acte__title">Acte III — L'arrivée <em>Essaouira</em></span></summary>
          <div class="accordion__body">
            <ul class="agenda">
              <li><span class="agenda__date">Vendredi 2 avril</span> Direction Essaouira, traversée des villages.</li>
              <li><span class="agenda__date">Samedi 3 avril</span> Arrivée officielle sur la plage, accueil des familles, rencontres presse, remise des prix et soirée de gala.</li>
            </ul>
          </div>
        </details>
        <p class="source-note" style="margin-top:var(--space-6)">Les partenaires de la formule La Totale sont conviés à la soirée de gala. <a href="sponsors.html#formules">Voir les formules de sponsoring →</a></p>
      </div>
    </section>

    <!-- ============ L'HISTOIRE ============ -->
    <section id="histoire">
      <div class="container">
        <div class="reveal">
          <span class="eyebrow">Depuis 1990</span>
          <h2 class="section-title">Un pari audacieux devenu une référence</h2>
          <p class="section-lead">En 1990, Dominique Serra imagine un rallye à contre-courant&nbsp;: le premier rallye inter-entreprises sans critère de vitesse, où il faut parcourir le moins de kilomètres possible pour gagner. Le 11 octobre 1990, vingt-sept pionnières démarrent les moteurs de leurs Lada Niva pour huit cents kilomètres.</p>
        </div>
        <div class="timeline timeline--history reveal">
          <details class="timeline__item">
            <summary><div class="timeline__date">1990</div><div class="timeline__label"><span>La première édition</span></div></summary>
            <p class="timeline__detail">Vingt-sept pionnières au départ, en Lada Niva.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2001</div><div class="timeline__label"><span>La caravane médicale</span></div></summary>
            <p class="timeline__detail">Création de Cœur de Gazelles · suivi satellite IRITRACK.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2009</div><div class="timeline__label"><span>Les Armoiries du Royaume</span></div></summary>
            <p class="timeline__detail">Accordées par Sa Majesté le Roi Mohammed VI.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2010</div><div class="timeline__label"><span>La certification ISO 14001</span></div></summary>
            <p class="timeline__detail">Maintenue sans interruption depuis 2010.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2017</div><div class="timeline__label"><span>La catégorie E-Gazelle</span></div></summary>
            <p class="timeline__detail">Une première mondiale en rallye-raid pour les véhicules électriques.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2021</div><div class="timeline__label"><span>Le Prix Gazelles Solidaires</span></div></summary>
            <p class="timeline__detail">10&nbsp;000&nbsp;€ versés chaque année à une association portée par un équipage.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2023</div><div class="timeline__label"><span>La COP 28</span></div></summary>
            <p class="timeline__detail">Participation de l'organisation aux travaux sur le climat.</p>
          </details>
          <details class="timeline__item">
            <summary><div class="timeline__date">2026</div><div class="timeline__label"><span>La 35<sup>e</sup> édition</span></div></summary>
            <p class="timeline__detail">Anniversaire — 12 400 participantes depuis les débuts.</p>
          </details>
        </div>
        <div class="pledge reveal">
          <h3>2027, notre édition</h3>
          <p>Trente-sept ans après la première édition, Smile de Gazelles prend le départ sous le numéro 134. Sandra et Stéphanie rejoignent les douze mille femmes qui ont fait cette route avant elles.</p>
        </div>
        <div class="actions reveal">
          <a href="sponsors.html" class="btn btn-primary">Faire partie de l'aventure</a>
        </div>
      </div>
    </section>

    <!-- ============ L'ENGAGEMENT ENVIRONNEMENTAL ============ -->
    <section class="section-alt" id="environnement">
      <div class="container">
        <div class="eco-panel reveal">
          <span class="eyebrow">Responsable par engagement</span>
          <h2>La plus belle trace est celle que l'on ne laisse pas</h2>
          <p>Maïenga est la première agence au monde, et la seule à ce jour, à proposer des événements dont le système de management environnemental est certifié conforme à la norme ISO 14001 — une démarche engagée en 2007, obtenue en 2010, maintenue sans interruption depuis.</p>
          <p style="margin-top:var(--space-4)">Le principe même du classement — rallier un maximum de balises en parcourant le moins de kilomètres — aligne performance sportive et sobriété&nbsp;: ce n'est pas un engagement ajouté après coup, c'est le cœur de la compétition.</p>
          <blockquote class="quote">« Être responsable, ce n'est pas viser la perfection, mais agir, évoluer et montrer l'exemple. »</blockquote>
          <div class="actions">
            <a href="solidarite.html#rse-entreprises" class="btn btn-light">Voir notre engagement RSE en détail</a>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ UN ÉVÉNEMENT RECONNU ============ -->
    <section id="reconnaissance">
      <div class="container">
        <div class="reveal" style="margin-bottom:var(--space-10)">
          <span class="eyebrow">Reconnaissance</span>
          <h2 class="section-title">Trente-cinq ans de crédibilité</h2>
        </div>
        <div class="stats-grid reveal">
          <div class="stat"><div class="stat__num">12 400+</div><div class="stat__label">Participantes depuis 1990</div></div>
          <div class="stat"><div class="stat__num">75</div><div class="stat__label">Nationalités représentées</div></div>
          <div class="stat"><div class="stat__num">2 500</div><div class="stat__label">Entreprises mobilisées chaque année</div></div>
          <div class="stat"><div class="stat__num">622</div><div class="stat__label">Équipages engagés par des entreprises depuis 1990</div></div>
        </div>
        <div class="note reveal">
          <h3>Soutiens institutionnels</h3>
          <p>Le rallye est placé sous le Haut Patronage de Sa Majesté le Roi Mohammed VI et bénéficie du soutien de S.A.S. le Prince Albert II de Monaco.</p>
          <p class="source-note">Le détail de sa gouvernance RSE (Comité indépendant, membres honorifiques) est sur la page Solidarité.</p>
          <div class="actions" style="margin-top:var(--space-6)">
            <a href="solidarite.html#rse-entreprises" class="btn btn-outline">En savoir plus sur cette gouvernance</a>
          </div>
        </div>
        <div class="note-pair reveal" style="margin-top:var(--space-8)">
          <div class="note">
            <h3>Une aventure ouverte à tous les profils</h3>
            <p>Des équipages en situation de handicap participent depuis 2002&nbsp;: championne paralympique, participante hémiplégique, roadbooks retranscrits en version audio pour un participant malvoyant, médaillés porteurs de trisomie 21.</p>
          </div>
          <div class="note">
            <h3>Un engagement d'entreprise qui se reconduit</h3>
            <p>La Poste a engagé six équipages par an pendant seize ans. Total, quinze équipages par an pendant quinze ans. Renault, cinq équipages par an pendant dix ans. Soutenir un équipage n'est pas une démarche exotique&nbsp;: c'est une pratique établie que des milliers d'entreprises reconduisent.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ APPEL FINAL ============ -->
    <section>
      <div class="container">
        <div class="cta-banner reveal">
          <h2>Rejoignez l'aventure et donnez du sens à votre engagement</h2>
          <p>Devenez sponsor ou faites un don&nbsp;: chaque contribution nous rapproche de la ligne de départ.</p>
          <div class="hero__cta">
            <a href="sponsors.html" class="btn btn-light btn-lg">Devenir sponsor</a>
            <a href="soutenir.html" class="btn btn-outline btn-lg" style="color:#fff;border-color:rgba(255,255,255,0.6)">Faire un don</a>
          </div>
        </div>
      </div>
    </section>''',
    og_desc="Navigation sans GPS, sobriété kilométrique, certification ISO 14001 : "
            "découvrez l'épreuve que rejoint l'équipage 134 en 2027.",
    og_image="../assets/Rallye_01.JPG",
    hero_photo="../assets/Rallye_01.JPG",
    hero_eyebrow="L'épreuve")

# ---- SOLIDARITÉ ----
PAGES["solidarite.html"] = page(
    "solidarite", "Solidarité",
    "La dimension solidaire du rallye : Cœur de Gazelles et la cause que nous soutenons.",
    ("Un rallye qui a du cœur",
     "Au-delà du sport, une aventure profondément humaine et solidaire."),
    '''    <section>
      <div class="container">
        <div class="split reveal">
          <div class="split__media"><img src="../assets/solidarite.png" alt="Caravane médicale Cœur de Gazelles" /></div>
          <div class="split__body">
            <span class="eyebrow">Cœur de Gazelles</span>
            <h2>La caravane médicale du désert</h2>
            <p>Au-delà du défi sportif, le Rallye Aïcha des Gazelles s'appuie sur l'association Cœur de Gazelles, reconnue d'intérêt général depuis 2001. Elle organise la plus importante caravane médicale itinérante du sud du Maroc afin de donner accès aux soins aux populations les plus reculées.</p>
            <p>Ses domaines d'action répondent aux besoins des populations locales&nbsp;: accès aux soins médicaux gratuits, accès universel à l'éducation, développement durable et aide matérielle.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="text-center reveal" style="margin-bottom:var(--space-12)">
          <span class="eyebrow">Des actions concrètes sur le terrain</span>
          <h2 class="section-title">L'impact de Cœur de Gazelles</h2>
        </div>
        <div class="stats-grid reveal">
          <div class="stat"><div class="stat__num">99 370</div><div class="stat__label">Personnes soignées</div></div>
          <div class="stat"><div class="stat__num">930</div><div class="stat__label">Enfants accompagnés contre le décrochage scolaire</div></div>
          <div class="stat"><div class="stat__num">41 821</div><div class="stat__label">Personnes sensibilisées à la pollution plastique</div></div>
          <div class="stat"><div class="stat__num">26</div><div class="stat__label">Puits construits pour 4 300 familles nomades</div></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container container-default">
        <div class="reveal">
          <span class="eyebrow">Notre engagement</span>
          <h2 class="section-title">La cause que nous portons</h2>
          <p style="color:var(--color-text-muted)">Depuis 2021, chaque équipage peut mettre en lumière une association reconnue d'intérêt général. À l'issue de l'événement, un jury vote pour l'un des projets présentés et un prix de 10&nbsp;000&nbsp;€ est versé à l'association lauréate. Soutenir Smile de Gazelles, c'est associer votre engagement à une aventure utile, humaine et concrète.</p>
          <div class="cause-box">
            <h3>Association soutenue : <em>Cœur de Gazelles</em></h3>
            <p>Nous avons choisi de mettre en lumière <strong>Cœur de Gazelles</strong>, association reconnue d'intérêt général depuis 2001, qui organise la plus importante caravane médicale itinérante du sud du Maroc&nbsp;: soins gratuits, éducation, développement durable et aide matérielle aux populations les plus isolées. Soutenir Smile de Gazelles, c'est associer votre engagement à cette cause utile, humaine et concrète.</p>
            <p><a class="cause-box__link" href="https://www.coeurdegazelles.org" target="_blank" rel="noopener">Découvrir Cœur de Gazelles →</a></p>
          </div>
        </div>
      </div>
    </section>''')

# ---- SPONSORS ----
# Coche verte réutilisée dans les listes de contreparties
CHECK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>')

PAGES["sponsors.html"] = page(
    "sponsors", "Sponsors",
    "Devenez partenaire de l'équipage Smile de Gazelles : retombées médias du rallye, "
    "cinq formules de sponsoring, visibilité sur le véhicule et les équipements, modalités et contact.",
    ("Devenez partenaire",
     "Associez votre image à une aventure humaine, sportive et solidaire porteuse de valeurs fortes."),
    '''    <!-- ============ POURQUOI NOUS SOUTENIR ============ -->
    <section id="pourquoi">
      <div class="container">
        <div class="reveal" style="margin-bottom:var(--space-10)">
          <span class="eyebrow">Pourquoi nous soutenir</span>
          <h2 class="section-title">Quatre raisons de nous accompagner</h2>
        </div>
        <div class="cards-grid reveal">
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
            <h3>Associez votre marque</h3>
            <p>Un rallye international porteur de sens&nbsp;: audace, engagement, partage, responsabilité. Vous ne serez pas seulement sponsor, mais acteur d'un projet humain qui fédère, inspire et crée de l'émotion.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
            <h3>Optimisez votre fiscalité</h3>
            <p>Les sommes versées au titre du sponsoring sont considérées comme des dépenses de communication et peuvent être déduites du résultat imposable de votre entreprise, au titre de l'article 39.1.7 du Code général des impôts.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11v2a1 1 0 0 0 1 1h3l5 4V6L7 10H4a1 1 0 0 0-1 1z"/><path d="M17 8a5 5 0 0 1 0 8"/><path d="M20 5a9 9 0 0 1 0 14"/></svg></div>
            <h3>Bénéficiez de notre couverture</h3>
            <p>Réseaux sociaux, site internet, newsletters, visuels sur notre véhicule et nos équipements, presse locale.</p>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 0 20 15.3 15.3 0 0 1 0-20z"/></svg></div>
            <h3>Profitez d'une exposition d'envergure</h3>
            <p>Le rallye dépasse largement les frontières&nbsp;: presse, télévision, radio et réseaux sociaux, en France comme à l'international.</p>
          </div>
        </div>

        <div class="eco-panel reveal" style="margin-top:clamp(var(--space-12), 6vw, var(--space-20))">
          <span class="eyebrow">Bilan officiel</span>
          <h2>Les retombées médias de la 35<sup>e</sup> édition</h2>
          <p>Une audience mesurée, chiffrée et vérifiable — dont <strong>4,63 M€ de valeur média générée</strong>, le seul indicateur qui traduit la visibilité en euros, comparable à un budget de communication.</p>
          <div class="eco-stats">
            <div class="eco-stat"><div class="eco-stat__num">1 676</div><div class="eco-stat__label">Retombées médias</div></div>
            <div class="eco-stat"><div class="eco-stat__num">435,6 M</div><div class="eco-stat__label">Personnes atteintes</div></div>
            <div class="eco-stat"><div class="eco-stat__num">4,63 M€</div><div class="eco-stat__label">De valeur média générée</div></div>
            <div class="eco-stat"><div class="eco-stat__num">+ de 10 M</div><div class="eco-stat__label">De vues sur les réseaux sociaux</div></div>
          </div>
          <p class="source-note">Source&nbsp;: 35<sup>e</sup> édition, retombées mesurées du 1<sup>er</sup> mai 2025 au 30 avril 2026, source Onclusive. Données réseaux sociaux du 27 mars au 11 avril 2026.</p>
        </div>

        <details class="accordion reveal">
          <summary>Presse — 1 052 retombées</summary>
          <div class="accordion__body">
            <p>1 052 retombées, dont 469 en presse écrite et 583 en presse en ligne, pour 389 millions de personnes atteintes et 3,36 M€ de valeur média. La presse représente 77&nbsp;% des retombées totales.</p>
          </div>
        </details>
        <details class="accordion reveal">
          <summary>Télévision et radio — 348 retombées</summary>
          <div class="accordion__body">
            <p>261 retombées télévisées&nbsp;: 161 diffusions sur les chaînes du groupe M6, 11 sur L'Équipe TV et 10 sur 2M, pour 16,8 M de personnes atteintes. Côté radio, 87 retombées dont 42 diffusions nationales sur Chérie FM, pour 4,9 M de personnes atteintes.</p>
          </div>
        </details>
        <details class="accordion reveal">
          <summary>Réseaux sociaux et site live — 1 216 contenus</summary>
          <div class="accordion__body">
            <p>1 216 contenus publiés, plus de 10 M de vues et plus de 2 M de personnes atteintes, pour une communauté de plus de 170 000 abonnés.</p>
          </div>
        </details>

        <div class="note reveal">
          <h3>L'effet communauté</h3>
          <p>Au-delà des retombées médias, le rallye mobilise un écosystème entier&nbsp;: 320 Gazelles ambassadrices cumulant plus de 200 000 abonnés, environ 20 000 contenus générés sur une année de préparation, et plus de 6 000 acteurs économiques engagés autour des équipages. <strong>Une mobilisation continue sur douze mois</strong>, pas seulement pendant la course.</p>
          <p class="source-note">Ces chiffres illustrent la capacité d'amplification des Gazelles et des partenaires du rallye, et ne sont pas intégrés aux audiences médias mesurées par Onclusive.</p>
        </div>

        <div class="gallery gallery--quad reveal">
          <img src="../assets/sponsor_01.jpg" alt="Couverture médiatique du Rallye Aïcha des Gazelles" loading="lazy" />
          <img src="../assets/sponsors-02.jpg" alt="Équipages et véhicules relayés par les médias" loading="lazy" />
          <img src="../assets/sponsors-03.JPG" alt="Reportage sur le Rallye Aïcha des Gazelles" loading="lazy" />
          <img src="../assets/sponsors-04.JPG" alt="Visibilité des partenaires sur le rallye" loading="lazy" />
        </div>
      </div>
    </section>

    <!-- ============ UN PARTENARIAT GAGNANT-GAGNANT ============ -->
    <section class="section-alt">
      <div class="container">
        <div class="split reveal">
          <div class="split__media">
            <img src="../assets/sponsors_rallye.jpg" alt="Un 4x4 du Rallye Aïcha des Gazelles dans le désert marocain" loading="lazy" />
          </div>
          <div class="split__body">
            <span class="eyebrow">Un partenariat gagnant-gagnant</span>
            <h2>Nous recherchons un partenaire, pas un simple sponsor</h2>
            <ul class="feature-list">
              <li>''' + CHECK + ''' Une mise en avant de votre entreprise sur nos réseaux sociaux avant, pendant et après le rallye.</li>
              <li>''' + CHECK + ''' Votre logo sur notre véhicule, nos tenues et nos équipements, avec une exposition auprès des médias et du grand public.</li>
              <li>''' + CHECK + ''' La possibilité d'organiser une rencontre dans vos locaux, pour partager cette aventure avec vos collaborateurs et vos clients.</li>
            </ul>
            <blockquote class="quote">« Un partenaire que nous mettrons en lumière tout au long de cette formidable aventure. »</blockquote>
          </div>
        </div>
        <div class="band band--rounded reveal" style="margin-top:clamp(var(--space-12), 6vw, var(--space-20))">
          <img src="../assets/sponsors_rallye-02.jpg" alt="Le Rallye Aïcha des Gazelles au cœur des dunes" loading="lazy" />
        </div>
      </div>
    </section>

    <!-- ============ LES FORMULES ============ -->
    <section id="formules">
      <div class="container">
        <div class="reveal">
          <span class="eyebrow">Comment nous soutenir</span>
          <h2 class="section-title">Cinq formules, une progression d'engagement</h2>
          <p class="section-lead">Du logo sur le véhicule au partenariat titre&nbsp;: chaque formule ouvre droit aux contreparties de la précédente.</p>
        </div>
        <div class="sponsor-tiers reveal">
          <div class="tier tier--step tier--step1">
            <div class="tier__level">Formule 01</div>
            <div class="tier__name">Pack Solidaire</div>
            <div class="tier__range">500 € à 2 000 €</div>
            <ul class="tier__list">
              <li>''' + CHECK + ''' Logo 10 × 20 cm sur le véhicule</li>
              <li>''' + CHECK + ''' Mention sur nos réseaux sociaux</li>
            </ul>
            <a href="#contact" class="btn btn-outline tier__cta" data-formule="solidaire">Choisir cette formule</a>
          </div>
          <div class="tier tier--step tier--step2">
            <div class="tier__level">Formule 02</div>
            <div class="tier__name">Pack Cool</div>
            <div class="tier__range">2 001 € à 5 000 €</div>
            <ul class="tier__list">
              <li>''' + CHECK + ''' Logo 20 × 35 cm sur zone à forte visibilité</li>
              <li>''' + CHECK + ''' Relais régulier de votre marque sur nos réseaux</li>
            </ul>
            <a href="#contact" class="btn btn-outline tier__cta" data-formule="cool">Choisir cette formule</a>
          </div>
          <div class="tier tier--step tier--step3">
            <div class="tier__level">Formule 03</div>
            <div class="tier__name">Pack Audacieux</div>
            <div class="tier__range">5 001 € à 10 000 €</div>
            <ul class="tier__list">
              <li>''' + CHECK + ''' Logo 30 × 50 cm sur zone à forte visibilité</li>
              <li>''' + CHECK + ''' Relais régulier sur nos réseaux</li>
              <li>''' + CHECK + ''' Une journée conférence ou retour d'expérience dans vos locaux</li>
            </ul>
            <a href="#contact" class="btn btn-outline tier__cta" data-formule="audacieux">Choisir cette formule</a>
          </div>
          <div class="tier tier--step tier--step4">
            <div class="tier__level">Formule 04</div>
            <div class="tier__name">Pack Dépassement de soi</div>
            <div class="tier__range">10 001 € à 30 000 €</div>
            <ul class="tier__list">
              <li>''' + CHECK + ''' Logo grand format 40 × 70 cm sur capot, ailes latérales ou toit</li>
              <li>''' + CHECK + ''' Communiqué de presse conjoint</li>
              <li>''' + CHECK + ''' Relais régulier sur nos réseaux</li>
              <li>''' + CHECK + ''' Une journée conférence ou retour d'expérience dans vos locaux</li>
            </ul>
            <a href="#contact" class="btn btn-primary tier__cta" data-formule="depassement">Choisir cette formule</a>
          </div>
        </div>

        <div class="tier-hero reveal">
          <span class="tier-hero__badge">Formule 05 · Partenaire titre majeur</span>
          <h3 class="tier-hero__name">La Totale</h3>
          <div class="tier-hero__range">Au-delà de 30 000 €</div>
          <p class="tier-hero__note">Jusqu'à la couverture intégrale du budget de participation, soit 42 000 € — le véhicule, l'équipage et l'aventure portent vos couleurs, du départ à l'arrivée.</p>
          <ul class="tier-hero__list">
            <li>''' + CHECK + ''' Covering intégral du 4x4</li>
            <li>''' + CHECK + ''' Marquage exclusif des gilets et des casques</li>
            <li>''' + CHECK + ''' Invitation VIP à l'arrivée à Essaouira, soirée de gala</li>
            <li>''' + CHECK + ''' L'ensemble des contreparties des formules précédentes</li>
          </ul>
          <div class="actions">
            <a href="#contact" class="btn btn-light" data-formule="totale">Choisir cette formule</a>
            <a href="../assets/dossier-sponsoring.pdf" class="btn btn-outline" download>Télécharger le dossier</a>
          </div>
        </div>
        <div class="note reveal">
          <h3>Partenariats en nature</h3>
          <p>Casques, covering, location du 4x4, équipement, prestations&nbsp;: les partenariats en nature sont les bienvenus et donnent droit aux mêmes contreparties, à valeur équivalente.</p>
        </div>
      </div>
    </section>

    <!-- ============ VOTRE VISIBILITÉ ============ -->
    <section class="section-alt" id="visibilite">
      <div class="container">
        <div class="reveal">
          <span class="eyebrow">Où vous serez visible</span>
          <h2 class="section-title">Sur le véhicule, sur nous, sur nos réseaux</h2>
        </div>

        <h3 class="subhead reveal">Le véhicule</h3>
        <p class="section-lead reveal">Emplacements publicitaires officiels, avec leurs zones et leurs dimensions maximales.</p>
        <div class="table-wrap reveal">
          <table class="spec-table">
            <thead><tr><th scope="col">Zone</th><th scope="col">Dimensions maximales</th></tr></thead>
            <tbody>
              <tr><th scope="row">Capot avant et toit</th><td>80 × 100 cm</td></tr>
              <tr><th scope="row">Portières arrière, ailes, vitres latérales</th><td>40 × 60 cm</td></tr>
              <tr><th scope="row">Arrière du 4x4</th><td>30 × 40 cm</td></tr>
              <tr><th scope="row">Vitre arrière</th><td>20 × 30 cm</td></tr>
            </tbody>
          </table>
        </div>
        <div class="note reveal">
          <h3>Emplacements réservés</h3>
          <p>Conformément au règlement du rallye, les trois plaques «&nbsp;Rallye Aïcha des Gazelles&nbsp;», les numéros d'équipage (12 × 7 cm) et la plaque d'identification de toit (42 × 27 cm) sont strictement réservés à l'organisation. Toutes les autres surfaces sont à votre disposition.</p>
        </div>

        <h3 class="subhead reveal" style="margin-top:clamp(var(--space-12), 6vw, var(--space-16))">Les équipements</h3>
        <div class="table-wrap reveal">
          <table class="spec-table">
            <thead><tr><th scope="col">Support</th><th scope="col">Emplacement</th></tr></thead>
            <tbody>
              <tr><th scope="row">T-shirts</th><td>Manches, dos et poitrine</td></tr>
              <tr><th scope="row">Gilets officiels</th><td>Zone dorsale, portée pendant toute la compétition</td></tr>
              <tr><th scope="row">Casques</th><td>Jusqu'à 10 × 20 cm</td></tr>
            </tbody>
          </table>
        </div>
        <div class="figure-grid reveal">
          <figure class="figure">
            <img src="../assets/sponsors_covering02.jpg" alt="Gilet officiel, casque et t-shirt d'un équipage du rallye" loading="lazy" />
            <figcaption>Exemple&nbsp;: gilet officiel, casque et t-shirt d'un équipage — édition précédente.</figcaption>
          </figure>
          <figure class="figure">
            <img src="../assets/sponsors_covering.jpg" alt="Covering publicitaire d'un 4x4 engagé sur le rallye" loading="lazy" />
            <figcaption>Exemple de covering — édition précédente.</figcaption>
          </figure>
        </div>
        <div class="note reveal">
          <h3>Une remarque sur les formats</h3>
          <p>Nos formats sont volontairement calibrés en dessous du maximum autorisé, afin de pouvoir accueillir plusieurs partenaires sur une même zone. Un emplacement plus grand reste possible pour les formules supérieures.</p>
        </div>
      </div>
    </section>

    <!-- ============ MODALITÉS ============ -->
    <section id="modalites">
      <div class="container container-default">
        <div class="reveal">
          <span class="eyebrow">Modalités</span>
          <h2 class="section-title">Comment procéder</h2>
        </div>
        <div class="table-wrap reveal">
          <table class="spec-table">
            <thead><tr><th scope="col">Moyen</th><th scope="col">Détail</th></tr></thead>
            <tbody>
              <tr><th scope="row">Virement bancaire</th><td>Coordonnées communiquées sur demande — <a href="contact.html">nous écrire</a></td></tr>
              <tr><th scope="row">Paiement en ligne</th><td>Formulaire sécurisé HelloAsso</td></tr>
              <tr><th scope="row">Partenariat en nature</th><td>Casques, covering, location du 4x4, prestations — à définir ensemble</td></tr>
            </tbody>
          </table>
        </div>
        <div class="id-card reveal" style="margin-top:var(--space-10)">
          <h3>Facturation et cadre juridique</h3>
          <p style="color:var(--color-text-muted);margin-bottom:var(--space-6)">Une facture est émise pour tout versement, vous permettant de comptabiliser votre soutien en dépense de communication. Une convention de sponsoring est signée entre l'association et l'entreprise partenaire, précisant les engagements réciproques, les contreparties et leur valorisation. Les sommes versées relèvent du régime du parrainage, article 39.1.7 du Code général des impôts.</p>
          <dl>
            <dt>Nom</dt><dd>Association Smile de Gazelles — loi 1901, à but non lucratif</dd>
            <dt>Déclaration</dt><dd>Préfecture n° W343034911 · SIREN 108 320 961</dd>
            <dt>Siège social</dt><dd>453 Enclos des Palourdes, 34130 Carnon</dd>
            <dt>Contact</dt><dd><a href="mailto:smiledegazelles@gmail.com">smiledegazelles@gmail.com</a></dd>
          </dl>
        </div>
      </div>
    </section>

    <!-- ============ PARLONS-EN ============ -->
    <section class="section-alt" id="contact">
      <div class="container">
        <div class="reveal" style="margin-bottom:var(--space-10)">
          <span class="eyebrow">Parlons-en</span>
          <h2 class="section-title">Prenons rendez-vous</h2>
          <p class="section-lead">En présentiel à Montpellier et alentours, ou en visioconférence. Nous vous présentons le projet, écoutons vos attentes et construisons ensemble un partenariat sur mesure.</p>
        </div>
        <div class="contact-grid">
          <div class="contact-info reveal">
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4zM22 6l-10 7L2 6"/></svg></div>
              <div><h4>Email</h4><p><a href="mailto:smiledegazelles@gmail.com">smiledegazelles@gmail.com</a></p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div>
              <div><h4>Rendez-vous</h4><p>En présentiel à Montpellier et alentours, ou en visioconférence.</p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg></div>
              <div><h4>Le dossier de sponsoring</h4><p><a href="../assets/dossier-sponsoring.pdf" download>Télécharger le dossier (PDF)</a></p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
              <div><h4>Vous êtes un particulier&nbsp;?</h4><p><a href="soutenir.html">Découvrez les autres façons de nous soutenir</a></p></div>
            </div>
          </div>
          <form class="form reveal" onsubmit="return false">
            <div class="form__row">
              <label>Nom<input type="text" name="nom" placeholder="Votre nom" required /></label>
              <label>Entreprise<input type="text" name="entreprise" placeholder="Votre entreprise" required /></label>
            </div>
            <label>Email<input type="email" name="email" placeholder="vous@entreprise.fr" required /></label>
            <div class="form__row">
              <label>Objet
                <select name="objet">
                  <option value="sponsor">Devenir sponsor</option>
                  <option value="rib">Demander les coordonnées bancaires</option>
                  <option value="nature">Partenariat en nature</option>
                  <option value="autre">Autre</option>
                </select>
              </label>
              <label>Formule envisagée
                <select name="formule">
                  <option value="indecis">Je ne sais pas encore</option>
                  <option value="solidaire">Pack Solidaire — 500 € à 2 000 €</option>
                  <option value="cool">Pack Cool — 2 001 € à 5 000 €</option>
                  <option value="audacieux">Pack Audacieux — 5 001 € à 10 000 €</option>
                  <option value="depassement">Pack Dépassement de soi — 10 001 € à 30 000 €</option>
                  <option value="totale">La Totale — au-delà de 30 000 €</option>
                </select>
              </label>
            </div>
            <label>Message<textarea name="message" rows="5" placeholder="Votre projet, vos attentes, vos questions…"></textarea></label>
            <label class="form__consent"><input type="checkbox" name="consentement" required /> J'accepte que ces informations soient utilisées par l'association Smile de Gazelles pour répondre à ma demande.</label>
            <button type="submit" class="btn btn-primary btn-lg">Envoyer <em style="font-style:normal;opacity:.7">[formulaire à connecter]</em></button>
          </form>
        </div>
      </div>
    </section>

    <!-- ============ ILS NOUS FONT CONFIANCE ============
         Grille de logos volontairement masquée tant qu'aucun partenaire n'est signé :
         une grille vide est un signal négatif. À réactiver dès le premier partenaire.
    <section>
      <div class="container text-center">
        <div class="reveal">
          <span class="eyebrow">Ils nous font confiance</span>
          <h2 class="section-title">Nos partenaires</h2>
        </div>
        <div class="logo-wall reveal">
          <div class="logo-slot">Votre logo</div>
        </div>
      </div>
    </section>
    ============================================================ -->

    <!-- ============ APPEL FINAL ============ -->
    <section>
      <div class="container">
        <div class="cta-banner reveal">
          <h2>Traçons le chemin ensemble</h2>
          <p>Face à l'imprévu, on improvise. Face aux obstacles, on sourit. Ensemble, on transforme chaque défi en terrain de jeu.</p>
          <div class="hero__cta">
            <a href="#contact" class="btn btn-light btn-lg">Nous contacter</a>
            <a href="../assets/dossier-sponsoring.pdf" class="btn btn-outline btn-lg" style="color:#fff;border-color:rgba(255,255,255,0.6)" download>Télécharger le dossier</a>
          </div>
        </div>
      </div>
    </section>''',
    og_desc="4,63 M€ de valeur média générée, 435,6 M de personnes atteintes : associez votre entreprise "
            "à l'équipage 134 du Rallye Aïcha des Gazelles 2027.",
    og_image="../assets/sponsoring-272-recalibr%C3%A9e.png",
    hero_photo="../assets/sponsoring-272-recalibr%C3%A9e.png",
    hero_eyebrow="Entreprises · Sponsoring 2027",
    hero_actions='''        <div class="actions">
          <a href="#formules" class="btn btn-primary">Voir les formules</a>
          <a href="../assets/dossier-sponsoring.pdf" class="btn btn-outline" download>Télécharger le dossier</a>
        </div>
        <p class="page-hero__aside">Vous êtes un particulier&nbsp;? <a href="soutenir.html">Découvrez comment nous soutenir</a>.</p>''')

# ---- SOUTENIR ----
PAGES["soutenir.html"] = page(
    "soutenir", "Nous soutenir",
    "Faites un don, participez à nos événements ou devenez partenaire de Smile de Gazelles.",
    ("Rejoignez l'aventure",
     "Chaque contribution, petite ou grande, nous rapproche de la ligne de départ."),
    '''    <section>
      <div class="container">
        <div class="cards-grid reveal">
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div>
            <h3>Faire un don</h3>
            <p>Soutenez-nous directement via notre cagnotte en ligne. Chaque euro compte&nbsp;!</p>
            <a href="#" class="btn btn-primary" style="margin-top:var(--space-4)">Accéder à la cagnotte <em>[lien à venir]</em></a>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
            <h3>Devenir sponsor</h3>
            <p>Votre entreprise peut nous accompagner et gagner en visibilité. Découvrez nos formules.</p>
            <a href="sponsors.html" class="btn btn-outline" style="margin-top:var(--space-4)">Voir les formules</a>
          </div>
          <div class="card">
            <div class="card__icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
            <h3>Participer à nos événements</h3>
            <p>Tombola, loto, soirées&nbsp;: rejoignez-nous lors de nos actions de récolte de fonds.</p>
            <a href="contact.html" class="btn btn-outline" style="margin-top:var(--space-4)">Être informé</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="cta-banner reveal">
          <h2>Ensemble, on va plus loin</h2>
          <p>Votre soutien finance l'inscription, le véhicule, l'équipement et notre engagement solidaire. Merci&nbsp;!</p>
          <div class="hero__cta">
            <a href="#" class="btn btn-light btn-lg">Faire un don</a>
            <a href="contact.html" class="btn btn-outline btn-lg" style="color:#fff;border-color:rgba(255,255,255,0.6)">Nous contacter</a>
          </div>
        </div>
      </div>
    </section>''')

# ---- CONTACT ----
PAGES["contact.html"] = page(
    "contact", "Contact",
    "Contactez l'équipage Smile de Gazelles pour toute question, partenariat ou soutien.",
    ("Contactez-nous",
     "Une question, une envie de nous soutenir ou de nous rejoindre ? Écrivez-nous."),
    '''    <section>
      <div class="container">
        <div class="contact-grid">
          <div class="contact-info reveal">
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4zM22 6l-10 7L2 6"/></svg></div>
              <div><h4>Email</h4><p><a href="mailto:smiledegazelles@gmail.com">smiledegazelles@gmail.com</a></p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
              <div><h4>L'équipage</h4><p>Sandra Aversenq &amp; Stéphanie Falco</p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
              <div><h4>Association Smile de Gazelles</h4><p>453, Enclos des Palourdes, Carnon, 34130 Mauguio</p></div>
            </div>
            <div class="contact-item">
              <div class="contact-item__icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div>
              <div><h4>Prenons rendez-vous</h4><p>En présentiel (Montpellier) ou en visioconférence, à votre convenance.</p></div>
            </div>
          </div>
          <form class="form reveal" onsubmit="return false">
            <label>Nom<input type="text" name="nom" placeholder="Votre nom" required /></label>
            <label>Email<input type="email" name="email" placeholder="vous@exemple.fr" required /></label>
            <label>Sujet<input type="text" name="sujet" placeholder="Sponsoring, don, question…" /></label>
            <label>Message<textarea name="message" rows="5" placeholder="Votre message"></textarea></label>
            <button type="submit" class="btn btn-primary btn-lg">Envoyer <em style="font-style:normal;opacity:.7">[formulaire à connecter]</em></button>
          </form>
        </div>
      </div>
    </section>''')

for name, html in PAGES.items():
    with open(os.path.join(PAGES_DIR, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit :", name)
print("Terminé —", len(PAGES), "pages.")
