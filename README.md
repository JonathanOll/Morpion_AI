# Morpion_AI
Une intelligence artificielle de morpion, jouable dans la console

## Fonctionnement
L'IA teste toutes les actions possibles dans les n tours suivants, si la partie est gagnante, elle est notée 2^(nombre d'espaces restants), si elle est perdante 2^(nombre d'espaces restants), et en cas d'égalité, 0. Toutes les meilleurs actions sont stockées dans une liste, et l'une d'entre elle est selectionnée au hasard pour être jouée.
