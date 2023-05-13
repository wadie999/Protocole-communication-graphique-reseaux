# Protocole-communication-graphique-reseaux

Dans le cadre de ce projet, nous sommes amenés à concevoir un protocole de communication
graphique. L’objectif est de proposer une méthode de transmission d’informations visuelles
qui puisse être imprimée et lue par une machine. Un exemple de protocole graphique connu
est le QR code, qui permet de stocker une grande quantité d’informations dans un petit
espace.
Notre tâche consiste à concevoir un nouveau protocole de A à Z en proposant des solutions
originales aux problèmes posés. Nous devrons dessiner les informations dans une matrice
constituée de cellules, où chaque cellule représente une unité d’information de base. Nous
devrons également inclure des informations permettant de détecter et de corriger des erreurs,
ainsi que des informations spécifiques à notre protocole.




Pour notre QR code, nous avons décidé d’utiliser des triangles équilatéraux comme unité de
base. Nous avons dessiné un grand triangle équilatéral qui est divisé en quatre sous-triangles
équilatéraux. Le triangle du haut contient des informations supplémentaires au message, et
il est lui-même divisé en quatre sous-triangles. Le triangle du haut est totalement colorié
en noir, tandis que les trois autres contiennent respectivement le nombre de caractères, le
nombre de mots et un petit triangle noir qui désigne notre cellule d’informations.
Les trois autres triangles en bas contiennent notre message codé. L’idée générale est d’effectuer un pavage de triangles en petits triangles pour représenter les informations de manière
compacte et efficace.
Nous pensons que cette méthode permettra de stocker une grande quantité d’informations
dans un petit espace tout en facilitant la lecture et la détection d’erreurs. Nous expliquerons
plus en détail notre idée dans la suite.
