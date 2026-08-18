# Instantanés d'audit

Copies des pages du site **telles qu'elles étaient au moment de l'audit** (18 août 2026),
avant l'application des correctifs décrits dans [../plan.md](../plan.md).
Elles servent de référence « avant / après » — ce ne sont pas des pages du site.

| Fichier | Page d'origine |
|---|---|
| `index.html` | `/index.html` |
| `le-rallye.html` | `/pages/le-rallye.html` |
| `solidarite.html` | `/pages/solidarite.html` |
| `sponsors.html` | `/pages/sponsors.html` |
| `soutenir.html` | `/pages/soutenir.html` |
| `contact.html` | `/pages/contact.html` |

Les chemins vers `css/`, `js/` et `assets/` ont été réécrits lors du déplacement :
les instantanés s'ouvrent donc toujours correctement, mais **ils pointent vers les
feuilles de style et scripts actuels**, pas vers ceux d'origine. Seul le HTML reflète
l'état d'avant les correctifs. Les liens vers `equipage.html` et `mentions-legales.html`
(pages non capturées) renvoient vers le site en production.

`index.html` contient en fin de fichier le script de diagnostic utilisé pendant l'audit
pour mesurer l'accessibilité du logo, du burger et du sélecteur de thème (point 1.1 du plan).
