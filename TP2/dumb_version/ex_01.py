from numpy import *
from typing import Iterable

Tableau = Iterable

TAB = Tableau[int]

nb_int = int(input("Entrer un nombre d'entiers à saisir :\n"))
occ = int(-1)
ask = """Que voulez-vous faire ?
0 - Quitter le programme
1 - Compter les occurences d'un entier\n"""
occ_int: int
occ_result: int

while nb_int < 1:
    print("Valeur saisie incorrecte.")
    nb_int = int(input("Entrer un nombre d'entiers à saisir :\n"))

array_int: TAB = zeros(nb_int, int)
array_int[0] = int(input("Entrer l'entier n°{num} :\n".format(num=1)))
smallest = array_int[0]

for i in range(nb_int-1):
    array_int[i+1] = int(input("Entrer l'entier n°{num} :\n".format(num=i+2)))
    if array_int[i+1] < smallest:
        smallest = array_int[i+1]

print(array_int)
print("L'entier le plus petit est", smallest)

while occ != 0:
    occ = int(input(ask))
    occ_result = 0
    if occ == 1:
        occ_int = int(input("Entrer l'entier voulu :\n"))
        for i in range(nb_int):
            if array_int[i] == occ_int:
                occ_result += 1
        print("Cette valeur apparaît {nb_occ} fois.".format(nb_occ=occ_result))
    else:
        print("Valeur saisie incorrecte.")
