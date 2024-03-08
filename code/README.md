# Bescherelle

Fichiers python `.py`

----
## Fichier `main.py`

**Base du programme**. *À ouvrir pour lancer l'exécution du logiciel*.

Fichier contenant les scripts du logiciel.

----
## Fichier `scripts.py`

**Définitions de scripts**.

Fichier contenant les scripts du bescherelle. Fonctionne comme un module python.

----
## Fichier `tabs.py`

**Données du bescherelle**.

Fichier contenant les donénes nécessaire au fonctionnement du bescherelle.

----

# Documentation

## Docstrings

### Typage Entrées, sorties

```
- [:type]               -> fait appel à un type en particulier
- []                    -> fait appel à n'importe quelle entrée
- [!type]               -> fait appel à tous les types sauf celui indiqué
- [:type :type2 !type3] -> fait appel à type, type2 mais pas à type3
```
- None sera retourné en cas d'erreur.

### Fil d'Ariane

Les docstrings commencent toujours par un **fil d'Ariane** qui indique en partie l'effet de la fonction.

----

## Définitions

```
- terminaison           -> terminaison de la forme '-er', '2-ir'
- terminaison brute     -> terminaison de la forme 'er', 'ir'
- radical               -> verbe sans terminaison de l'infinitif présent
- famille, mode         -> groupe de temps
```

----
