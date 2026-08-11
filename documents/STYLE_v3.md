# Style — Smile de Gazelles

**Ce document n'est plus une specification a appliquer. C'est un journal.** Il decrit `style.css` tel qu'il existe reellement, et liste les ecarts encore a corriger — chacun comme un correctif d'une ligne sur un selecteur precis, jamais comme une reecriture.

> **Ce qui a casse la version precedente** : une demande formulee comme « voici le nouveau style, applique-le » a conduit a une reconstruction complete du fichier, qui a fait perdre des comportements qui n'etaient ecrits nulle part — ils vivaient dans le fichier existant, pas dans les instructions. Ne plus jamais reproduire cette formulation.

---

## Methode de travail avec Claude Code

**Un changement, un commit, un controle visuel.** Jamais un paquet de plusieurs ajustements dans la meme demande. Apres chaque correctif : recharger la page, regarder, puis commiter avant de passer au suivant. Si quelque chose casse, on sait immediatement lequel des deux commits est en cause.

**Toute demande cible un selecteur qui existe deja**, jamais une reecriture de fichier. La formulation « remplace X par Y dans tel selecteur, ne touche a rien d'autre » borne strictement l'intervention. La formulation « applique ce nouveau style » ne la borne pas — c'est elle qui a casse la v0.

**Toujours demander le diff avant l'ecriture.** Claude Code doit montrer ce qu'il va changer avant de l'enregistrer, jamais l'inverse.

### Le prompt-cadre a reutiliser pour chaque correctif

```
Corrige uniquement le point suivant dans css/style.css, sans reconstruire 
ni reorganiser le fichier :

Selecteur : [nom exact du selecteur, par exemple .split__media img]
Propriete actuelle : [ce qui est ecrit aujourd'hui]
Nouvelle valeur : [ce qu'il faut mettre a la place]

Ne touche a aucun autre selecteur, aucune autre propriete, aucune autre 
regle du fichier. Montre-moi le diff avant de l'enregistrer. Si le 
selecteur indique n'existe pas exactement sous ce nom, dis-le-moi au 
lieu d'en creer un nouveau ou d'en deviner un proche.
```

**Pourquoi cette derniere phrase compte** : si le selecteur qu'on cible n'existe pas tel qu'on l'a nomme, Claude Code doit s'arreter et demander plutot que d'improviser une classe voisine — c'est exactement ce genre d'improvisation silencieuse qui introduit une incoherence de plus.

Pour un ajout de contenu nouveau (une mosaique de photos, par exemple, qui n'a pas encore de classe), le prompt change de nature : il ne corrige plus une valeur, il definit un nouveau motif. Ce cas releve de `PATTERNS.md`, pas de ce document.

---

## Ce qui existe deja dans `style.css` — inventaire, a ne pas retoucher sans raison

### Couleurs, mode clair

| Role | Variable | Valeur |
|---|---|---|
| Accent principal | `--color-primary` | orange, la teinte deja en place |
| Or / ambre | `--color-gold` | `#D99A2B`, survol `#BD8018`, fond `#F6E7C8` |
| Fond sombre de marque | `--color-brand-dark` | `#2E2620` |
| Fond sombre de marque, alterne | `--color-brand-dark-2` | `#3A2F27` |

### Couleurs, mode sombre

Bloc `[data-theme="dark"]` distinct et complet. L'or y devient `#E6B552`, plus clair pour rester lisible sur fond sombre. Le fond de marque descend a `#14100C` / `#1C1611`. Le mode sombre est fonctionnel et fait partie du site — ne pas le simplifier sans le dire explicitement.

### Typographie

`--font-display` : Clash Display, replis General Sans puis Helvetica Neue. `--font-body` : General Sans. Titres `h1` a `h4` en graisse 600.

### Rayons

`--radius-sm` (6 px) a `--radius-2xl` (24 px), plus `--radius-full` pour les pilules. **`.split__media img` utilise aujourd'hui `--radius-2xl`** — c'est le point exact du premier correctif ci-dessous.

### Composants deja reussis, a ne pas toucher

Le bandeau RSE en fond `--color-brand-dark`, deja neutre et non chocolat. La banniere de degrade en fin de page, orange vers or. La frise horizontale des dates, les trois cartes du defi sportif. Les logos qui basculent automatiquement entre version claire et sombre via `[data-theme="dark"] .logo__img--light / --dark`.

---

## Correctifs valides, un par selecteur

Chacun de ces points est pret a etre donne a Claude Code sous la forme du prompt-cadre ci-dessus, un par un.

### 1. Angles des photos en split, plus nets

**Selecteur :** `.split__media img`
**Aujourd'hui :** `border-radius: var(--radius-2xl)` (24 px)
**Cible :** `border-radius: var(--radius-sm)` (6 px)

*Ne pas toucher a `.split__media--portrait img.portrait` ni a `.media-inset img`, qui ont leur propre logique (le portrait et les petits logos inseres).*

### 2. Bandeau du compteur, fond sombre plutot qu'orange

**Selecteur :** `.countdown-bar`
**Aujourd'hui :** `background: var(--color-primary)` (orange plein cadre)
**Cible :** `background: var(--color-brand-dark)`, et dans `.countdown__num`, `color: var(--color-gold)` pour que les chiffres restent la seule touche de couleur sur ce fond.

*Le hero se termine deja en orange (bouton, badge) — un bandeau orange juste en dessous ne cree aucune respiration. Le fond sombre en cree une, et fait ressortir les chiffres en ambre comme sur la maquette validee.*

### 3. Ambre en pied de page — usage decoratif seulement, jamais en texte courant

**Ne pas** appliquer `--color-gold` au texte des liens ou des mentions legales du pied de page : sur le fond clair du footer, ce contraste tombe autour de 2,2:1, largement sous le seuil de lisibilite.

**A la place**, un seul usage decoratif ponctuel est valide : la signature *« Deux femmes, un defi, mille sourires a partager »* peut passer en `--color-gold` si elle est en graisse suffisante (600 ou plus) et a une taille d'au moins 14px — dans ce cas precis le contraste reduit reste acceptable parce que c'est un element de signature, pas une information a lire absolument.

---

## Ce qui reste a observer avant tout autre correctif

Les mosaiques de photos ne sont pas dans cette liste : elles introduisent une classe qui n'existe pas encore, ce n'est pas un correctif de valeur mais un motif nouveau. Elles seront decrites dans `PATTERNS.md`, avec la regle de nombre d'images et d'espacement, avant d'etre donnees a Claude Code.

La taille du titre du hero n'a pas encore de correctif valide — a trancher apres avoir vu les trois correctifs ci-dessus en place, pas avant.
