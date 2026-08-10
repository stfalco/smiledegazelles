#!/usr/bin/env python3
"""Génère les pages intérieures du site Smile de Gazelles (préfixe ../ pour les assets)."""
import os

PAGES_DIR = os.path.join(os.path.dirname(__file__), "pages")
os.makedirs(PAGES_DIR, exist_ok=True)

# Logo officiel — bascule clair/sombre, préfixe ../ pour les pages intérieures
LOGO_IMG = '''<img class="logo__img logo__img--light" src="../assets/logo.png" alt="Smile de Gazelles" width="62" height="62" />
        <img class="logo__img logo__img--dark" src="../assets/logo-dark.png" alt="Smile de Gazelles" width="62" height="62" />'''

# Emblème officiel pour le footer — bascule clair/sombre
LOGO_EMBLEM = '''<img class="logo__emblem logo__emblem--light" src="../assets/logo.png" alt="Smile de Gazelles" width="130" height="130" />
            <img class="logo__emblem logo__emblem--dark" src="../assets/logo-dark.png" alt="Smile de Gazelles" width="130" height="130" />'''

NAV_ITEMS = [
    ("index.html", "Accueil", "accueil"),
    ("equipage.html", "L'équipage", "equipage"),
    ("le-rallye.html", "Le rallye", "le-rallye"),
    ("solidarite.html", "Solidarité", "solidarite"),
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
            <a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
            <a href="#" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
            <a href="#" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
          </div>
        </div>
        <div class="footer__col"><h4>Navigation</h4><ul>
          <li><a href="equipage.html">L'équipage</a></li>
          <li><a href="le-rallye.html">Le rallye</a></li>
          <li><a href="solidarite.html">Solidarité</a></li>
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
        <span>Site réalisé avec ❤️ pour l'aventure.</span>
      </div>
    </div>
  </footer>'''

def page(current, title, desc, page_hero, body):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Smile de Gazelles</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{title} — Smile de Gazelles" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="../assets/hero-desert.png" />
  <link rel="icon" href="../assets/favicon.png" type="image/png" />
  <link rel="preconnect" href="https://api.fontshare.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&f[]=clash-display@500,600,700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>
{header(current)}
  <main>
    <section class="page-hero">
      <div class="container container-default">
        <p class="breadcrumb"><a href="../index.html">Accueil</a> / {title}</p>
        <h1>{page_hero[0]}</h1>
        <p>{page_hero[1]}</p>
      </div>
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
    "Rencontrez Sandra Aversenq et Stéphanie Falco, l'équipage Smile de Gazelles.",
    ("L'alliance de la maîtrise et de l'instinct",
     "Deux femmes, un défi, mille sourires à partager. L'idée est née il y a un an, entre deux discussions sur les voyages de Sandra."),
    '''    <section>
      <div class="container">
        <div class="crew-grid reveal">
          <article class="crew-card">
            <div class="crew-card__photo">
              <span class="crew-card__initials">SA</span>
              <span class="crew-card__placeholder-note">[Photo à ajouter]</span>
            </div>
            <div class="crew-card__body">
              <h2 class="crew-card__name">Sandra Aversenq</h2>
              <span class="crew-card__role">« Wonder Sandra »</span>
              <div class="crew-card__meta"><span>53 ans</span><span>Chef d'Entreprise</span></div>
              <p class="crew-card__bio">Entrepreneuse ambitieuse et structurée, elle est, lors de ses nombreux voyages, toujours en quête d'échanges et de rencontres humaines authentiques. Elle apporte sa vision pragmatique des affaires, son leadership naturel et sa réactivité face aux crises terrain.</p>
            </div>
          </article>
          <article class="crew-card">
            <div class="crew-card__photo">
              <span class="crew-card__initials">SF</span>
              <span class="crew-card__placeholder-note">[Photo à ajouter]</span>
            </div>
            <div class="crew-card__body">
              <h2 class="crew-card__name">Stéphanie Falco</h2>
              <span class="crew-card__role">Collectif « Les Biches »</span>
              <div class="crew-card__meta"><span>49 ans</span><span>Data Analyst</span></div>
              <p class="crew-card__bio">Co-fondatrice du collectif « Les Biches » mettant en avant les femmes artistes, elle est profondément animée par la force du collectif. Bercée dès son plus jeune âge par le ronflement des 4x4 de son papa, habitué des rallyes de franchissement, elle allie sérénité et sens de la mécanique. Face à l'imprévu, elle apporte le calme et l'énergie.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container container-default">
        <div class="reveal">
          <span class="eyebrow">Notre histoire</span>
          <h2 class="section-title">Comment tout a commencé</h2>
          <p style="color:var(--color-text-muted);margin-bottom:var(--space-4)">L'idée est née il y a un an, entre deux discussions sur les voyages de Sandra. Ce qui n'était qu'un rêve s'est transformé en une inscription pour 2027. Notre déclic&nbsp;? Ne plus attendre pour vivre les aventures dont on a toujours rêvé.</p>
          <p style="color:var(--color-text-muted)">Deux âmes réunies autour d'un projet associatif ambitieux et unique. Une aventure qui s'annonce déjà inoubliable, jalonnée d'obstacles et d'imprévus, mais surtout riche de sens et d'émotions.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="text-center reveal">
          <span class="eyebrow">Notre devise</span>
          <h2 class="section-title">Deux femmes – un défi – mille sourires à partager</h2>
          <p class="section-lead mx-auto">Animées par des valeurs communes de solidarité, d'engagement, de respect, de dépassement de soi et de partage, nous inscrivons chacune de nos actions dans une démarche porteuse de sens.</p>
        </div>
      </div>
    </section>''')

# ---- LE RALLYE ----
PAGES["le-rallye.html"] = page(
    "le-rallye", "Le rallye",
    "Tout savoir sur le Rallye Aïcha des Gazelles 2027 : concept, dates, navigation.",
    ("Le Rallye Aïcha des Gazelles",
     "Le seul rallye-raid hors-piste 100 % féminin au monde, au cœur du Sahara marocain."),
    '''    <section>
      <div class="container">
        <div class="split reveal">
          <div class="split__body">
            <span class="eyebrow">Le concept</span>
            <h2>Le moins de kilomètres, le plus de balises</h2>
            <p>Le Rallye des Gazelles est un rallye-raid mythique, 100&nbsp;% féminin, qui se déroule au cœur du désert marocain. L'épreuve est une course uniquement en hors-piste, sans GPS, avec pour seuls moyens de s'orienter&nbsp;: une carte, une boussole, une règle de navigation.</p>
            <p>Soutenant des valeurs responsables et solidaires, l'équipage gagnant sera celui qui aura parcouru le moins de kilomètres en pointant un maximum de balises&nbsp;: c'est l'éco-concept.</p>
            <ul class="feature-list">
              <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Pas de critère de vitesse</li>
              <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Navigation authentique&nbsp;: carte, boussole, règle et roadbook</li>
              <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg> Seul événement de sport mécanique au monde certifié ISO 14001</li>
            </ul>
          </div>
          <div class="split__media"><img src="../assets/navigation.png" alt="Outils de navigation du rallye" /></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="text-center reveal" style="margin-bottom:var(--space-12)">
          <span class="eyebrow">Édition 2027</span>
          <h2 class="section-title">Les dates clés</h2>
          <p class="section-lead mx-auto">Du 20 mars au 3 avril 2027 — du sud de la France jusqu'à la plage d'Essaouira.</p>
        </div>
        <div class="cards-grid reveal">
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></div><h3>20–21 mars</h3><p>Accueil des participantes, vérifications techniques et départ officiel sous l'arche, dans le sud de la France.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div><h3>26 mars – 1er avril</h3><p>La compétition&nbsp;: plusieurs étapes en plein désert, réparties sur trois bivouacs différents.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 21h8M12 17v4M17 5a5 5 0 0 1-10 0V3h10zM7 5H4a2 2 0 0 0 2 3M17 5h3a2 2 0 0 1-2 3"/></svg></div><h3>3 avril</h3><p>Arrivée officielle sur la plage d'Essaouira, remise des prix et soirée de clôture.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="container">
        <div class="stats-grid reveal">
          <div class="stat"><div class="stat__num">160+</div><div class="stat__label">Équipages internationaux</div></div>
          <div class="stat"><div class="stat__num">100 %</div><div class="stat__label">Féminin</div></div>
          <div class="stat"><div class="stat__num">ISO 14001</div><div class="stat__label">Seul rallye certifié</div></div>
          <div class="stat"><div class="stat__num">0</div><div class="stat__label">Déchet abandonné</div></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="text-center reveal" style="margin-bottom:var(--space-12)">
          <span class="eyebrow">Responsable par engagement</span>
          <h2 class="section-title">Le seul rallye au monde certifié ISO 14001</h2>
          <p class="section-lead mx-auto">Depuis sa création, le rallye relève un défi automobile tout en structurant une démarche environnementale exigeante et concrète.</p>
        </div>
        <div class="cards-grid reveal">
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg></div><h3>Certification & exigence</h3><p>Système de management environnemental en place depuis 2010, avec audit annuel par SGS ICS.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg></div><h3>Des mesures concrètes</h3><p>0 déchet abandonné, 100&nbsp;% des déchets triés, 10&nbsp;000 bouteilles plastiques recyclées, produits sans solvant.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div><h3>Une démarche ambitieuse</h3><p>Comité RSE, présence à la COP21 et la COP22, catégorie E-Gazelle pour les véhicules 100&nbsp;% électriques depuis 2017.</p></div>
        </div>
      </div>
    </section>''')

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
PAGES["sponsors.html"] = page(
    "sponsors", "Sponsors",
    "Devenez partenaire de l'équipage Smile de Gazelles : offres de sponsoring et visibilité.",
    ("Devenez partenaire",
     "Associez votre image à une aventure humaine, sportive et solidaire porteuse de valeurs fortes."),
    '''    <section>
      <div class="container">
        <div class="text-center reveal" style="margin-bottom:var(--space-8)">
          <span class="eyebrow">Pourquoi nous soutenir</span>
          <h2 class="section-title">Une vitrine porteuse de sens</h2>
          <p class="section-lead mx-auto">Le rallye bénéficie chaque année d'une forte médiatisation (TV, presse, radio, web) à l'échelle nationale et internationale.</p>
        </div>
        <div class="cards-grid reveal">
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg></div><h3>Visibilité médiatique</h3><p>Un événement fortement relayé dans les médias, à toutes les échelles.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></svg></div><h3>Valeurs positives</h3><p>Sport féminin, dépassement, solidarité, écoresponsabilité&nbsp;: une image valorisante.</p></div>
          <div class="card"><div class="card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div><h3>Avantage fiscal</h3><p>Le mécénat peut ouvrir droit à une réduction d'impôt <em>[à préciser selon le statut de l'association]</em>.</p></div>
        </div>
      </div>
    </section>

    <section class="section-alt">
      <div class="container">
        <div class="text-center reveal" style="margin-bottom:var(--space-4)">
          <span class="eyebrow">Nos formules</span>
          <h2 class="section-title">Choisissez votre niveau de partenariat</h2>
          <p class="section-lead mx-auto"><em>Montants et contreparties provisoires — à ajuster selon votre dossier de sponsoring.</em></p>
        </div>
        <div class="sponsor-tiers reveal">
          <div class="tier">
            <div class="tier__name">Bronze</div>
            <div class="tier__price">[€]</div>
            <ul class="tier__list">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Logo sur le site web</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Remerciements sur les réseaux</li>
            </ul>
          </div>
          <div class="tier tier--featured">
            <div class="tier__name">Argent</div>
            <div class="tier__price">[€]</div>
            <ul class="tier__list">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Tout le niveau Bronze</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Logo sur le véhicule</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Publications dédiées</li>
            </ul>
          </div>
          <div class="tier">
            <div class="tier__name">Or</div>
            <div class="tier__price">[€]</div>
            <ul class="tier__list">
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Tout le niveau Argent</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Emplacement premium (capot, casques)</li>
              <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Journée de communication en entreprise</li>
            </ul>
          </div>
        </div>
        <div class="text-center" style="margin-top:var(--space-12)">
          <a href="contact.html" class="btn btn-primary btn-lg">Recevoir le dossier de sponsoring</a>
        </div>
      </div>
    </section>

    <section>
      <div class="container text-center">
        <div class="reveal">
          <span class="eyebrow">Ils nous font confiance</span>
          <h2 class="section-title">Nos partenaires</h2>
        </div>
        <div class="logo-wall reveal">
          <div class="logo-slot">Votre logo</div><div class="logo-slot">Votre logo</div>
          <div class="logo-slot">Votre logo</div><div class="logo-slot">Votre logo</div>
          <div class="logo-slot">Votre logo</div><div class="logo-slot">Votre logo</div>
        </div>
      </div>
    </section>''')

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
