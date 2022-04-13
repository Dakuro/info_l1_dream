from random import *

nb_myst = randint(0, 100)
nb_guess = int(-1)
nb_test = int(0)
ask_guess = "Essai n° {nb} : Entrer un nombre entre 0 et 100 :\n"
nb_bigger = "Trop grand."
nb_smaller = "Trop petit."
nb_good = "Gagné en {nb} essais."

while nb_myst != nb_guess:
    nb_test += 1
    nb_guess = int(input(ask_guess.format(nb=nb_test)))
    if nb_guess > nb_myst:
        print(nb_bigger.format(nb=nb_test))
    elif nb_guess < nb_myst:
        print(nb_smaller.format(nb=nb_test))
    else:
        print(nb_good.format(nb=nb_test))
