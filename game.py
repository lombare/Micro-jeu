import sys

from Joueurs import Joueur

print("C'est au tour du premier joueur")
j1 = Joueur()
print("C'est au tour du deuxieme joueur")
j2 = Joueur()

j1.Presentation()
j2.Presentation()

# Tant que j1 n'est pas KO et j2 n'est pas KO
while not j1.EstKO() and not j2.EstKO():
    j1.Attaquer(j2)
    j1.FinTour()

    tmp = j1
    j1 = j2
    j2 = tmp

# On affiche d'abord le message de victoire
if not j1.EstKO():
    j1.Victoire()
elif not j2.EstKO():
    j2.Victoire()

# Ensuite celui de la défaite
if j1.EstKO():
    j1.Defaite()
elif j2.EstKO():
    j2.Defaite()
