import numpy as np

nb_int = int(input("Entrer un nombre d'entiers à saisir :\n"))

while nb_int < 1:
    print("Valeur saisie incorrecte.")
    nb_int = int(input("Entrer un nombre d'entiers à saisir :\n"))

array_int = np.empty(nb_int, dtype=int)
array_int[0] = int(input("Entrer l'entier n°{num} :\n".format(num=1)))
smallest = array_int[0]

for i in range(nb_int-1):
    array_int[i+1] = int(input("Entrer l'entier n°{num} :\n".format(num=i+2)))
    if array_int[i+1] < smallest:
        smallest = array_int[i+1]

print(array_int)
print("L'entier le plus petit est", smallest)
