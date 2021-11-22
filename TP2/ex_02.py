import numpy as np

nb_notes = int(input("Entrer un nombre de notes à saisir :\n"))
occ = int(-1)
ask = """Voulez-vous afficher le nombre d'étudiants ayant eu 10 au DS ?
0 - Quitter le programme
1 - Afficher le nombre d'étudiants\n"""

while nb_notes < 1:
    print("Valeur saisie incorrecte.")
    nb_notes = int(input("Entrer un nombre de notes à saisir :\n"))

array_notes = np.empty(nb_notes, dtype=int)

for i in range(nb_notes):
    array_notes[i] = int(input("Entrer la note n°{num} :\n".format(num=i + 1)))

print("Les notes saisies sont :\n", array_notes)
print("La moyenne du groupe est :", np.mean(array_notes))

while occ != 0:
    occ = int(input(ask))
    if occ == 1:
        print("Il y a {nb_occ} étudiant(s) ayant eu 10 au DS.".format(nb_occ=(array_notes == 10).sum()))
    else:
        print("Valeur saisie incorrecte.")
