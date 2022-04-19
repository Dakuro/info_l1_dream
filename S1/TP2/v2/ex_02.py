from numpy import *
from typing import Iterable

Tableau = Iterable

TAB = Tableau[int]

nb_notes = int(input("Entrer un nombre de notes à saisir :\n"))
sum_notes = float(0)
moy_notes: float
occ_result = int(0)

while nb_notes < 1:
    print("Valeur saisie incorrecte.")
    nb_notes = int(input("Entrer un nombre de notes à saisir :\n"))

array_notes: TAB = zeros(400, int)

for i in range(nb_notes):
    array_notes[i] = int(input("Entrer la note n°{num} :\n".format(num=i + 1)))

print("Les notes saisies sont :\n", array_notes)

for j in range(nb_notes):
    sum_notes += array_notes[j]
moy_notes = sum_notes / nb_notes

print("La moyenne du groupe est :", round(moy_notes, 2))

occ = int(0)
while occ < nb_notes:
    if array_notes[occ] == 10:
        occ_result += 1
    occ += 1

print("Il y a {nb_occ} étudiant(s) ayant eu 10 au DS.".format(nb_occ=occ_result))
