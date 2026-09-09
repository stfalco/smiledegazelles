# Smile de Gazelles

Site vitrine de l'équipage 134 **Smile de Gazelles** (Sandra Aversenq & Stéphanie Falco),
engagé sur le Rallye Aïcha des Gazelles 2027.

Site statique : HTML, CSS et JavaScript sans dépendance ni étape de build côté client.
Hébergement Netlify (voir `netlify.toml` pour les en-têtes de cache et de polices).

## Structure

| Chemin | Rôle |
|---|---|
| `index.html` | Page d'accueil — **générée**, ne pas éditer directement |
| `pages/*.html` | Pages intérieures — **générées**, ne pas éditer directement |
| `build_pages.py` | Générateur de toutes les pages (en-tête, pied de page, contenus) |
| `css/` | `style.css` (feuille principale) + les deux familles de polices auto-hébergées |
| `js/main.js` | Menu mobile, bascule de thème, carrousel, envoi AJAX des formulaires |
| `assets/` | Images, polices `woff2`/`woff`, favicons |
| `documents/` | Documents de travail (audit, plan d'actions correctives) |

## Générer les pages

**Tous** les fichiers HTML du site — `index.html` comme les pages de `pages/` — sont
produits par `build_pages.py`. Toute modification de leur contenu, de l'en-tête ou du
pied de page se fait **dans le script**, jamais dans les fichiers HTML générés (ils
seraient écrasés à la génération suivante).

```bash
python build_pages.py
```

Le script réécrit les huit pages et affiche la liste de ce qu'il a produit.

En-tête, navigation, pied de page et métadonnées sont partagés par toutes les pages.
Seule la profondeur des chemins les distingue : `root=True` pour l'accueil, à la
racine, `root=False` pour les pages de `pages/`. Les fonctions `up()`, `inner()` et
`home()` s'en chargent — aucun chemin relatif n'est à écrire à la main.

## Prévisualiser en local

```bash
python -m http.server 8000
```

Puis ouvrir <http://localhost:8000>. Passer par un serveur plutôt que par `file://` :
les polices sont préchargées en mode CORS et les chemins relatifs entre `index.html`
et `pages/` supposent une racine de site.
