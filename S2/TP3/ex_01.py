import numpy
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


def copier_tab(src: numpy.ndarray, dest: numpy.ndarray, nb: int):
    numpy.copyto(dest, src)
