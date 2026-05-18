# Python - 1 - Array

## Exercise 0

- on peux cree des **liste avec deux types** ex :

`list[int | float] `

qui peux prendre soit un **int** soit un **float**

## Exercise 1

- fonction **isinstance** --> verife si une variable est d'un des types que on mets en parametre ex :

`isinstance(variable , (int , float)) ` -> retuen **True** si la variable est soit un int soit un float

- pour **decouper**(slice) une liste on utilies la syntaxe suivante :

`list[start : end] ` -> decoupe la liste de l'index **start** a l'index **end** (exclus)
`list[::2]` -> decoupe la liste en prenant un element sur deux

## Exercise 2

- **numpy** est une librairie qui permet de **gere des tableaux multidimensionnels** (utile pour les images , les videos , les sons ...)

pour l'importer on utilise la syntaxe suivante :
    `import numpy as np ` -> importe numpy et donne lui le nom de **np** pour pouvoir   l'utiliser plus facilement

nunpy vas etre utilie a combiner avec **Pillow** pour faire du traitement d'image

- **Pillow** est une librairie qui permet de **gere des images** par exemple.
pour l'importer on utilise la syntax suivante : 
    `from PIL import Image` -> importe la classe **Image** de la librairie **PIL** (Pillow) pour pouvoir l'utiliser pour manipuler des images

pour ouvrir une image on utilise la syntaxe suivante :
    `img = Image.open(path)`

pour convertir une image en tableau numpy on uitilise la syntaxe suivante :
    `img_array = np.array(img)`

## Exercise 3




