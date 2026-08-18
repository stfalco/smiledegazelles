# Plan d'actions correctives — Smile de Gazelles

Basé sur l'audit du site (contrôle responsive smartphone + revue des 8 pages). Découpé en lots par priorité ; chaque lot est livrable indépendamment.

---

## Lot 1 — Corrections critiques (bloquantes)

### 1.1 Menu mobile inutilisable (toutes les pages, ≤760px)
- **Fichier :** `css/style.css`, bloc `@media (max-width: 760px)` (règles `.nav`, `.nav.is-open`)
- **Problème :** `.nav` fermé n'a pour hauteur que son padding (`.nav__links` est `display:none`), donc `transform: translateY(-120%)` ne le sort pas assez de l'écran : il reste positionné sous le header (`inset: 72px 0 auto 0`) et, du fait de l'ordre d'empilement CSS, intercepte les clics sur le logo, le bouton de thème et le burger lui-même.
- **Action :** revoir la stratégie de masquage du panneau fermé (ex. `visibility`/`pointer-events` en plus du `transform`, ou ne plus dépendre de la hauteur du contenu pour la distance de translation) et vérifier que le panneau fermé ne capte plus aucun événement pointeur.
- **Recette :** sur un viewport ≤760px, taper le burger doit l'ouvrir ; le logo et le toggle de thème doivent rester cliquables en permanence, panneau ouvert ou fermé.

### 1.2 Formulaire de sponsoring non connecté (page Sponsors)
- **Fichier :** `pages/sponsors.html`, ligne ~373 (`<form class="form reveal" onsubmit="return false">`) et bouton ligne ~401
- **Problème :** le formulaire ne peut rien envoyer (`onsubmit="return false"`, aucun `method`/`data-netlify`/`name`) ; le bouton affiche le texte de repli « Envoyer *[formulaire à connecter]* ».
- **Action :** câbler ce formulaire sur le même modèle que celui de `pages/contact.html` (Netlify Forms + gestion AJAX `data-contact-form` déjà implémentée dans `js/main.js`), retirer le texte de repli du bouton.
- **Recette :** une soumission de test doit arriver dans les notifications Netlify Forms, avec confirmation affichée sans rechargement de page.

---

## Lot 2 — Contenu & cohérence

### 2.1 Lien LinkedIn mort
- **Fichiers :** pied de page de `build_pages.py` (template partagé) + `index.html` (maintenu à part)
- **Problème :** le lien LinkedIn du footer pointe vers `#` sur les 7 pages générées ; seule `index.html` a la vraie URL.
- **Action :** reporter l'URL correcte (celle utilisée sur `index.html`) dans le template du footer de `build_pages.py`, régénérer les 7 pages.

### 2.2 Widget de don HelloAsso affiché en anglais
- **Fichier :** `pages/soutenir.html`, bloc `.donation-embed` (iframe HelloAsso)
- **Problème :** le formulaire embarqué s'affiche en anglais par défaut (« Select a donation », « Donate »…), alors que le site est entièrement en français.
- **Action :** forcer la locale française sur l'URL/les paramètres d'intégration du widget HelloAsso (vérifier la documentation HelloAsso pour le paramètre de langue), tester sur un navigateur configuré en anglais pour confirmer que le FR est bien forcé.

---

## Lot 3 — Responsive / mobile

### 3.1 Débordement du bouton PDF (page Solidarité/RSE)
- **Fichier :** `css/style.css` (classe `.btn`, `white-space: nowrap`) ; `pages/solidarite.html`, bouton « Télécharger le rapport RSE CAP 2024-2025 (PDF) »
- **Problème :** le texte du bouton est trop long pour tenir sur une largeur de 375px ; `white-space: nowrap` force le bouton à dépasser le viewport et son bord droit est visuellement tronqué.
- **Action :** autoriser le retour à la ligne du libellé sur mobile (ou raccourcir le texte du bouton), vérifier qu'aucun autre bouton à libellé long ne présente le même problème sur les autres pages.

### 3.2 Puces de pagination du carrousel trop petites (page Le rallye)
- **Fichier :** `css/style.css`, classe `.tl-carousel__dot`
- **Problème :** puces de ~12px, huit d'entre elles serrées côte à côte — cible tactile inconfortable (contre 44px pour les flèches prev/next).
- **Action :** agrandir la zone tactile de chaque puce (par exemple en gardant un point visuel petit mais une zone cliquable ≥ 24-32px via padding), sans changer l'esthétique.

---

## Lot 4 — Hygiène technique & performance

### 4.1 Script tiers résiduel dans `index.html`
- **Fichier :** `index.html`, fin de fichier, bloc `<script data-pplx-inline-edit>`
- **Problème :** artefact d'un outil d'édition (bridge de capture d'écran via `postMessage` vers des domaines perplexity.ai), présent uniquement sur cette page.
- **Action :** supprimer ce bloc de script avant toute mise en production.

### 4.2 Avertissements de préchargement des polices
- **Fichier :** `index.html` et template `build_pages.py` (balises `<link rel="preload">` des polices), `netlify.toml` (en-têtes CORS des polices)
- **Problème :** l'attribut `crossorigin` sur les preloads de polices auto-hébergées déclenche des avertissements navigateur (police non utilisée / mode credentials incompatible).
- **Action :** retirer `crossorigin` des preloads (les polices sont servies en same-origin, l'attribut n'est pas nécessaire) ou aligner le mode credentials avec les en-têtes CORS définis dans `netlify.toml`.

### 4.3 `README.md` vide/corrompu
- **Action :** réécrire un `README.md` minimal (objet du dépôt, commande de génération des pages via `build_pages.py`).

### 4.4 Fichiers superflus versionnés
- **Fichiers :** `assets/old_hero-desert.png`, `assets/hero-desert1.png`, `assets/hero-desert2.png`, dossier `ajouts/`, `__pycache__/build_pages.cpython-311.pyc`
- **Action :** supprimer les images de test/doublons et le bytecode compilé du dépôt ; ajouter `__pycache__/` au `.gitignore` s'il n'y est pas déjà.

---

## Suggestion d'ordonnancement

| Lot | Effort estimé | Dépendances |
|---|---|---|
| Lot 1 | Moyen (CSS + branchement formulaire) | Aucune — à traiter en premier, impact direct sur les conversions |
| Lot 2 | Faible | Aucune |
| Lot 3 | Faible | Aucune |
| Lot 4 | Faible | Peut être fait en parallèle, sans urgence |
