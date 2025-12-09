# napari-3d-label-eraser

Petit plugin napari tout simple qui permet d'effacer **en 3D** un label entier
dans un layer de type `Labels`, en utilisant la valeur du `selected_label` du layer.

## Installation (mode développement)

Dans un environnement où napari est installé :

```bash
pip install -e .
```

Depuis le dossier racine du projet (`napari-3d-label-eraser`).

## Utilisation

1. Lance `napari`.
2. Charge une image et un layer de `Labels`.
3. Menu **Plugins → 3D Label Eraser → 3D Label Eraser**.
4. Dans le dock :
   - sélectionne ton layer de `Labels` comme layer actif,
   - choisis le label à effacer (via la palette de labels ou la pipette),
   - clique sur **"Effacer le label courant (3D)"**.

Tous les voxels de ce label seront mis à `0` dans tout le volume 3D.
