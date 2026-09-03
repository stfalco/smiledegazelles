# Style — Smile de Gazelles

**Ce document n'est pas une spécification à appliquer. C'est un journal.** Il décrit `css/style.css` tel qu'il existe réellement sur la branche `site_v32_optimisé`, et liste les écarts encore ouverts — chacun comme un correctif d'une ligne sur un sélecteur précis, jamais comme une réécriture.

*Dernière relecture du fichier réel : 2 septembre 2026 — `css/style.css`, 1 146 lignes, dernier commit touchant le CSS : `5266f25`.*

> **Ce qui a cassé la version précédente** : une demande formulée comme « voici le nouveau style, applique-le » a conduit à une reconstruction complète du fichier, qui a fait perdre des comportements qui n'étaient écrits nulle part — ils vivaient dans le fichier existant, pas dans les instructions. Ne plus jamais reproduire cette formulation.

---

## Où vit quoi

| Ce qu'on veut changer | Le fichier à ouvrir |
|---|---|
| Une valeur de style (couleur, rayon, espacement, grille) | `css/style.css` |
| Une structure de page, un texte, une classe posée sur un élément | `build_pages.py` |
| Un comportement (thème, menu, compteur, carrousel, présélection) | `js/main.js` |

**Les huit pages HTML sont générées.** `build_pages.py` est la source unique : `index.html` et les sept fichiers de `pages/` en sortent. Ne jamais retoucher un `.html` à la main — la prochaine génération l'écraserait. Une classe n'existe dans le site que si `build_pages.py` la pose.

Conséquence pour le CSS : avant d'écrire une nouvelle règle, vérifier que la classe visée est bien émise par `build_pages.py`. Si elle ne l'est pas, le travail commence là, pas dans la feuille de style.

---

## Méthode de travail avec Claude Code

**Un changement, un commit, un contrôle visuel.** Jamais un paquet de plusieurs ajustements dans la même demande. Après chaque correctif : régénérer les pages, recharger, regarder, puis commiter avant de passer au suivant. Si quelque chose casse, on sait immédiatement lequel des deux commits est en cause.

**Toute demande cible un sélecteur qui existe déjà**, jamais une réécriture de fichier. La formulation « remplace X par Y dans tel sélecteur, ne touche à rien d'autre » borne strictement l'intervention. La formulation « applique ce nouveau style » ne la borne pas — c'est elle qui a cassé la v0.

**Toujours demander le diff avant l'écriture.** Claude Code doit montrer ce qu'il va changer avant de l'enregistrer, jamais l'inverse.

### Le prompt-cadre à réutiliser pour chaque correctif

```
Corrige uniquement le point suivant dans css/style.css, sans reconstruire
ni réorganiser le fichier :

Sélecteur : [nom exact du sélecteur, par exemple .split__media img]
Propriété actuelle : [ce qui est écrit aujourd'hui]
Nouvelle valeur : [ce qu'il faut mettre à la place]

Ne touche à aucun autre sélecteur, aucune autre propriété, aucune autre
règle du fichier. Montre-moi le diff avant de l'enregistrer. Si le
sélecteur indiqué n'existe pas exactement sous ce nom, dis-le-moi au
lieu d'en créer un nouveau ou d'en deviner un proche.
```

**Pourquoi cette dernière phrase compte** : si le sélecteur qu'on cible n'existe pas tel qu'on l'a nommé, Claude Code doit s'arrêter et demander plutôt que d'improviser une classe voisine — c'est exactement ce genre d'improvisation silencieuse qui introduit une incohérence de plus.

Pour un ajout de contenu nouveau (une mosaïque de photos, par exemple, qui n'a pas encore de classe), le prompt change de nature : il ne corrige plus une valeur, il définit un nouveau motif. Le motif se décrit d'abord, se pose ensuite dans `build_pages.py`, et se style en dernier.

---

## Comment le fichier est organisé

L'ordre des blocs de `style.css` s'est stabilisé ainsi — le respecter en cas d'ajout :

1. **Tokens** (`:root`) — échelle typographique, espacement, rayons, largeurs de contenu, polices
2. **Palette claire** (`:root, [data-theme="light"]`) puis **palette sombre** (`[data-theme="dark"]`)
3. **Base** — reset, `html`/`body`, titres, focus, `prefers-reduced-motion`, `.sr-only`
4. **Utilitaires de layout** — `.container`, `section`, `.eyebrow`, `.section-title`, `.section-lead`
5. **Composants partagés** — boutons, header, hero, compteur, split, cartes, sponsors, footer…
6. **Sections par page**, ajoutées au fil de l'eau et explicitement marquées *« Ajouts uniquement — aucun sélecteur existant n'est modifié ici »* : Équipage, Sponsors, Le rallye, Solidarité et RSE, Nous soutenir

Cette convention d'ajout en fin de fichier est ce qui a permis d'ajouter cinq pages sans casser les précédentes. **Un nouveau composant propre à une page va dans sa section de page, pas dans le bloc des composants partagés.**

---

## Les tokens tels qu'ils sont

### Échelle typographique — entièrement fluide (`clamp`)

`--text-xs` · `--text-sm` · `--text-base` · `--text-lg` · `--text-xl` · `--text-2xl` · `--text-3xl` · `--text-hero`

Aucune taille n'est fixe : chacune interpole entre une borne mobile et une borne desktop. Ne pas introduire de `font-size` en pixels — cela sortirait l'élément de l'échelle et il cesserait de suivre au redimensionnement.

### Espacement, rayons, divers

- Espacement sur base 4 px : `--space-1` (0.25rem) → `--space-32` (8rem)
- Rayons : `--radius-sm` 6px · `--radius-md` 8px · `--radius-lg` 12px · `--radius-xl` 16px · `--radius-2xl` 24px · `--radius-full` (pilules)
- `--transition-interactive: 200ms cubic-bezier(0.16, 1, 0.3, 1)` — la courbe unique de toutes les interactions
- Largeurs : `--content-narrow` 680px · `--content-default` 1040px · `--content-wide` 1280px

### Typographie

`--font-display` : Clash Display, replis General Sans puis Helvetica Neue — titres `h1`–`h4`, graisse 600, `line-height: 1.1`, `text-wrap: balance`.
`--font-body` : General Sans — corps de texte, `line-height: 1.65`, `text-wrap: pretty`.
`--font-eyebrow` : General Sans — surtitres, libellés de tableaux, étapes. Toujours en 700, `letter-spacing` 0.10 à 0.14em, capitales.

Les trois polices sont auto-hébergées (`assets/Fonts/`, déclarées dans `css/clash-display.css` et `css/general-sans.css`). Aucune dépendance à un CDN de polices.

### Tokens définis mais jamais utilisés

`--text-hero`, `--color-primary-active`, `--color-text-inverse`, `--color-surface-2`. Ils ne gênent pas ; les connaître évite de croire qu'un composant s'en sert. `--text-hero` en particulier n'est **pas** la taille du titre du hero (voir plus bas).

---

## Les couleurs telles qu'elles sont

### Mode clair

| Rôle | Variable | Valeur |
|---|---|---|
| Fond de page (crème) | `--color-bg` | `#faf6f0` |
| Surface de carte | `--color-surface` | `#fffdf9` |
| Encadré beige | `--color-surface-offset` | `#f3ebe0` |
| Encadré beige, alterné | `--color-surface-offset-2` | `#ebe0d2` |
| Filets | `--color-divider` / `--color-border` | `#e4d8c8` / `#d8c8b4` |
| Texte | `--color-text` | `#2e2620` (brun chocolat) |
| Texte secondaire | `--color-text-muted` | `#6a5c4f` |
| Texte discret | `--color-text-faint` | `#a2917f` |
| Fond sombre de marque | `--color-brand-dark` | `#2e2620` |
| Fond sombre de marque, alterné | `--color-brand-dark-2` | `#3a2f27` |
| Accent principal (orange) | `--color-primary` | `#e8641e`, survol `#cf5312`, fond `#fbe1d0` |
| Accent secondaire (or) | `--color-gold` | `#d99a2b`, survol `#bd8018`, fond `#f6e7c8` |
| Accent tertiaire (rose) | `--color-rose` | `#d4699a`, fond `#f7dfec` |

Le rose est la couleur de la cause (Cœur de Gazelles). Il est **réservé** aux blocs qui parlent du volet solidaire : `.cause-box` et `.keyfact`. Ne pas l'étendre à des éléments décoratifs — sa rareté est ce qui lui donne son sens.

### Mode sombre

Bloc `[data-theme="dark"]` distinct et complet, piloté par `js/main.js` et mémorisé. Chaque variable de la palette claire y a sa contrepartie — c'est ce qui permet aux composants de ne jamais écrire une couleur en dur.

L'orange s'éclaircit (`#f27a3a`), l'or aussi (`#e6b552`), le rose aussi (`#e585b3`) : sur fond sombre les teintes de la palette claire deviennent illisibles. Le fond de marque descend à `#14100c` / `#1c1611`. Les ombres passent en noir pur, et `--hero-overlay` s'assombrit.

**Le mode sombre est fonctionnel et fait partie du site — ne pas le simplifier sans le dire explicitement.** Toute nouvelle couleur écrite en dur dans un composant y crée un trou.

---

## Les composants qui existent — inventaire, à ne pas retoucher sans raison

### Structure commune à toutes les pages

- **`.header`** — collant, fond translucide (`color-mix` + `backdrop-filter`), ombre qui n'apparaît qu'au scroll (`.header--scrolled`, posée par JS)
- **`.logo`** — wordmark + `.logo__team-text` en or à droite ; bascule automatique clair/sombre par `.logo__img--light` / `--dark`. Même mécanisme pour `.logo__emblem` au footer
- **`.nav`** — horizontale au-dessus de 760px, panneau plein écran en dessous
- **`.footer`** — fond `--color-surface-offset`, grille 2fr/1fr/1fr, `.footer__bottom` en filet
- **`.page-hero`** — bandeau brun des pages intérieures, avec triangle orange en angle haut-droit (`clip-path`). Variantes : `--photo` (photo en fond via `--page-hero-img`, passée en style inline par `build_pages.py`), `--sponsors` (plus compact)
- **`.reveal` / `.is-visible`** — apparition au scroll, pilotée par `IntersectionObserver`

### Blocs de contenu partagés

`.split` (texte/image, variantes `--reverse`, `--portrait`, `--duo`) · `.card` / `.cards-grid` · `.card--photo` · `.stat` / `.stats-grid` · `.steps-grid` · `.timeline` · `.quote` · `.note` et `.note-pair` · `.pledge` · `.id-card` · `.accordion` (`<details>` stylé, `+`/`–`) · `.chips` · `.gallery` (`--quad`) · `.figure` / `.figure-grid` / `.figure-stack` · `.band` · `.spec-table` dans `.table-wrap` · `.source-note` · `.cta-banner` (dégradé orange → or) · `.form`.

### Composants propres à une page

| Page | Composants |
|---|---|
| Accueil | `.hero`, `.countdown-bar` |
| Équipage | `.crew-card` (+ `__quote`, `__strengths`), `.roadmap` (frise « du rêve au départ », états `--done` / `--current` / `--todo` / `--goal`), `.budget-bars`, `.budget-box` |
| Le rallye | `.tl-carousel` (frise historique), `.timeline--history` (dépliable), `.acte__title`, `.agenda__date` |
| Solidarité et RSE | `.eco-panel` (chiffres or sur fond brun), `.keyfact` (rose), `.volets`, `.axis__title` |
| Sponsors | `.sponsor-tiers` en escalier (`.tier--step1` → `--step4`), `.tier-hero` (« La Totale », panneau brun bordé d'or), `.vehicle-layout`, `.spec-pair` |
| Nous soutenir | `.donation-intro-grid`, `.donation-embed` |
| Contact | `.contact-grid`, `.contact-item`, `.form__row`, `.form__consent`, `select.is-prefilled` |

### Réussites à ne pas toucher

Le bandeau RSE en `--color-brand-dark`, neutre et non chocolat. La bannière de dégradé orange → or en fin de page. La frise horizontale des dates et les trois cartes du défi sportif. La bascule automatique des logos entre thèmes. L'escalier des quatre formules de sponsoring, dont les hauteurs minimales croissantes ne s'appliquent qu'au-dessus de 900px. Le panneau « La Totale », seul bloc du site à porter une bordure or.

---

## Les décisions déjà arbitrées, écrites en commentaire dans le CSS

Elles sont documentées **dans le fichier lui-même**, au-dessus des règles concernées. Ce sont des corrections de bugs réels : les défaire les ferait revenir.

- **`.nav` fermé (≤760px)** — `visibility` et `pointer-events` en plus du `transform`, et le panneau garde toujours ses liens. Sans cela, sa hauteur dépendait de son état, `translateY(-100%)` ne le sortait pas de l'écran, et il interceptait les clics sur le logo, le burger et le sélecteur de thème.
- **`.btn` (≤760px)** — `white-space: normal`. Le `nowrap` par défaut faisait déborder du viewport le bouton « Télécharger le rapport RSE CAP 2024-2025 (PDF) » sur un écran de 375px.
- **`.tl-carousel__dot`** — 28px de zone tactile pour 9px visibles, via `background-clip: content-box` et un `gap: 0`. Corollaire écrit en commentaire : ses survols utilisent `background-color` et **jamais** le raccourci `background`, qui réinitialiserait `background-clip` et peindrait la puce sur ses 28px.
- **`.tl-carousel:not(.is-enhanced)`** — repli sans JavaScript : les jalons s'empilent, flèches et points masqués.
- **`.vehicle-layout__schema` et `.spec-pair .figure--schema`** — le schéma est en position absolue dans son cadre pour que la hauteur de la ligne soit donnée par le tableau seul.
- **`.donation-embed iframe`** — hauteur et largeur pilotées par HelloAsso (`postMessage`). `min-height` ne sert qu'à réserver la place. Ne rien imposer ici qui contredise le widget.

---

## Correctifs toujours ouverts

Les trois points ci-dessous étaient déjà listés dans la version précédente de ce journal. **Vérification faite le 2 septembre 2026 : aucun n'a été appliqué**, les valeurs d'origine sont toujours en place. Chacun reste prêt à être donné à Claude Code sous la forme du prompt-cadre, un par un.

### 1. Angles des photos en split, plus nets

**Sélecteur :** `.split__media img` (ligne 316)
**Aujourd'hui :** `border-radius: var(--radius-2xl)` (24 px)
**Cible :** `border-radius: var(--radius-sm)` (6 px)

*Ne pas toucher à `.split__media--portrait img.portrait` ni à `.media-inset img`, qui ont leur propre logique (le portrait et les petits logos insérés).*

*À noter avant d'agir* : `--radius-2xl` est aujourd'hui partagé par `.crew-card`, `.band--rounded`, `.cta-banner`, `.tier-hero`, `.eco-panel`, `.budget-box` et `.tl-carousel__viewport`. Le correctif ne vise **que** `.split__media img` — c'est un changement local, pas un changement de convention. Si l'on veut des angles nets partout, c'est une autre décision, à prendre séparément et à écrire ici avant d'être exécutée.

### 2. Bandeau du compteur, fond sombre plutôt qu'orange

**Sélecteur :** `.countdown-bar` (ligne 296)
**Aujourd'hui :** `background: var(--color-primary)` (orange plein cadre)
**Cible :** `background: var(--color-brand-dark)`, et dans `.countdown__num`, `color: var(--color-gold)` pour que les chiffres restent la seule touche de couleur sur ce fond.

*Le hero se termine déjà en orange (bouton, badge) — un bandeau orange juste en dessous ne crée aucune respiration. Le fond sombre en crée une, et fait ressortir les chiffres en ambre comme sur la maquette validée.*

*Le bandeau n'existe que sur l'accueil, et l'accueil est généré par `build_pages.py` : le contrôle visuel se fait sur `index.html` après régénération.*

### 3. Ambre en pied de page — usage décoratif seulement, jamais en texte courant

**Ne pas** appliquer `--color-gold` au texte des liens ou des mentions légales du pied de page : sur le fond clair du footer, ce contraste tombe autour de 2,2:1, largement sous le seuil de lisibilité.

**À la place**, un seul usage décoratif ponctuel est validé : la signature *« Deux femmes, un défi, mille sourires à partager »* peut passer en `--color-gold` si elle est en graisse suffisante (600 ou plus) et à une taille d'au moins 14px — dans ce cas précis le contraste réduit reste acceptable parce que c'est un élément de signature, pas une information à lire absolument.

*État actuel* : la phrase est dans `.footer__brand p` (`build_pages.py`, fonction `footer()`), en `--color-text-muted` et `--text-sm`. Elle n'est donc **ni** en or **ni** assez grande pour y passer telle quelle : le correctif suppose d'ajouter une classe dédiée dans `build_pages.py` avant de la styler. Ce n'est pas un correctif d'une ligne, contrairement aux deux précédents.

*La règle du « jamais en texte courant », elle, est déjà respectée partout : l'or n'apparaît en texte que sur fond brun — `.eco-panel`, `.tier-hero`, `.page-hero__aside`, `.logo__team-text` — où le contraste est bon.*

---

## Points d'hygiène repérés, sans urgence

Aucun n'a d'effet visible. Ils sont notés pour ne pas être redécouverts trois fois.

- **`.logo__emblem--dark` et ses deux règles de bascule sont dupliquées à l'identique** (lignes 243-249). Supprimer le second bloc de trois lignes ne change rien au rendu.
- **`.sponsor-tiers` est déclaré deux fois** : grille `auto-fit` dans les composants partagés (ligne 367), puis redéfini en `repeat(2, 1fr)` dans la section Sponsors (ligne 759). C'est la seconde déclaration qui gagne. Voulu, mais à savoir avant de modifier la première en croyant agir sur la page.
- **Deux points de rupture voisins coexistent** : `760px` partout, et `767px` pour la seule `.donation-intro-grid`. Aligner sur 760 si l'occasion se présente.
- **Les tokens inutilisés** listés plus haut.

### Points de rupture en usage

`1100px` (roadmap, galerie quad) · `900px` (bascule majeure : split, crew, contact, steps, eco-stats, timeline, footer, vehicle-layout, spec-pair — et le `min-width: 900px` qui active l'escalier des formules) · `760px` (header/menu mobile, boutons, figure-grid, form__row, media-inset) · `620px` (dernier repli en colonne unique).

---

## Ce qui reste à observer avant tout autre correctif

Les mosaïques de photos ne sont toujours pas dans cette liste : elles introduisent une classe qui n'existe pas encore, ce n'est pas un correctif de valeur mais un motif nouveau. À décrire, puis à poser dans `build_pages.py`, avant tout style. Noter cependant que `.gallery`, `.gallery--quad`, `.figure-grid` et `.split__media--duo` couvrent déjà plusieurs cas de plusieurs images côte à côte — vérifier qu'aucun ne suffit avant d'en créer un de plus.

La taille du titre du hero n'a toujours pas de correctif validé. Pour mémoire, `.hero h1` porte son propre `clamp(3rem, 0.5rem + 5vw, 5rem)` écrit en dur, et n'utilise **pas** le token `--text-hero`, qui monte jusqu'à 7rem et n'est utilisé nulle part. Un ajustement passera donc par la règle `.hero h1` elle-même. À trancher après avoir vu les correctifs 1 et 2 en place, pas avant.
