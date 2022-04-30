from numpy import array, zeros
from typing import Iterable
from random import randint

# Les Types
TabEntiers = Iterable[int]
Texte = (str, 15)
TabTexte = Iterable[str]


class Calcul:
    etapes: TabTexte = None
    valeur: int = 0


# Les Constantes
SIGNES: TabTexte = array(["+", "*", "-", "//"])


def copier_tab(src: TabEntiers, dest: TabEntiers, nb: int):
    for i in range(nb):
        dest[i] = src[i]


def extraire(tab: TabEntiers, i: int, pos_fin: int) -> int:
    i_value: int = tab[i]
    tab[i] = tab[pos_fin]
    tab[pos_fin] = 0
    return i_value


# Test
# tab: TabEntiers = [1, 2, 3, 4, 5, 6, 7]
# v: int = extraire(tab, 2, 6)
# print(v, tab)


def verifier(op: str, a: int, b: int) -> bool:
    if (op == SIGNES[3] and (b == 1 or a / b != a // b))\
            or (op == SIGNES[1] and (a == 1 or b == 1))\
            or (op == SIGNES[2] and a - b <= 0):
        return False
    else:
        return True


# Test
# a: int = 1
# b: int = 2
# print(verifier("+", a, b), verifier("-", a, b), verifier("*", a, b), verifier("//", a, b))
# a: int = 5
# b: int = 4
# print(verifier("+", a, b), verifier("-", a, b), verifier("*", a, b), verifier("//", a, b))


def calculer(op: str, a: int, b: int) -> int:
    if op == SIGNES[0]:
        return a + b
    elif verifier(op, a, b):
        if op == SIGNES[1]:
            return a * b
        elif op == SIGNES[2]:
            return a - b
        elif op == SIGNES[3]:
            return a // b


# Test
# print(calculer("+", 4, 5))
# print(calculer("//", 984, 24))


def choisir_operateur(a: int, b: int) -> str:
    rand_x: int = randint(0, 3)
    while not verifier(SIGNES[rand_x], a, b):
        rand_x = randint(0, 3)
    return SIGNES[rand_x]


# Test
# print(choisir_operateur(4, 4))
# print(choisir_operateur(4, 4))
# print(choisir_operateur(4, 4))


def essayer_calcul(tab_num: TabEntiers, but: int) -> Calcul:
    # Tente des opérations au hasard, sur les nombres pris au hasard, jusqu'à ce qu'il n'en reste qu'un.
    # S'il arrive au but, retourne la chaîne menant au calcul.
    calcul = Calcul()
    calcul.etapes = zeros(5, Texte)

    # Travailler sur une copie du tableau des nombres
    copie_num: TabEntiers = zeros(6, int)
    copier_tab(tab_num, copie_num, 6)
    j: int = 0
    for nb in range(5, 0, -1):
        # Prendre une valeur entre 0 et nb
        i = randint(0, nb)
        a: int = extraire(copie_num, i, nb)

        # Prendre une valeur entre 0 et nb - 1
        i: int = randint(0, nb - 1)
        b: int = extraire(copie_num, i, nb - 1)

        # Choisir une opération applicable sur a et b
        signe = choisir_operateur(a, b)

        # Lancer le calcul de l'opération
        resultat = calculer(signe, a, b)

        # Classer le résultat en fin de tableau
        copie_num[nb - 1] = resultat

        # Noter le détail de l'opération dans le tableau du calcul
        calcul.etapes[j] = str(a) + " " + signe + " " + str(b) + " = " + str(resultat)

        j += 1

        # Mettre à jour le résultat actuel dans le calcul
        calcul.valeur = resultat

        # Sortir si le but est trouvé
        if resultat == but:
            return calcul
    return calcul


# Test
# c: Calcul = essayer_calcul([12, 23, 34, 45, 56, 65], 77)
# print(c.valeur, " trouvé par ", c.etapes)

# c = essayer_calcul([12, 23, 34, 45, 56, 65], 77)
# print(c.valeur, " trouvé par ", c.etapes)


def lancer_essais(but: int, tab_num: TabEntiers):
    essais_max: int = 100000
    calc = Calcul()
    nb_essais: int = 0
    val_proche: int = 0
    print("À partir des opérations sur les nombres", tab_num, "\nLe but est d'obtenir", but)

    for i in range(essais_max):
        calc = essayer_calcul(tab_num, but)
        nb_essais = i + 1
        if abs(but - calc.valeur) < abs(but - val_proche):
            val_proche = calc.valeur
            if val_proche == but:
                break

    print("Fin de recherche, valeur la plus proche trouvée :", calc.valeur)
    print("Nb d'essais effectués :", nb_essais)
    print("Détail des opérations :")
    for e in calc.etapes:
        print(e)


lancer_essais(668, [1, 10, 4, 5, 3, 50])
lancer_essais(789, [1, 2, 4, 8, 10, 25])
