# import pour la gestion de tableaux
from numpy import zeros, array

# import pour la librairie graphique
import matplotlib.pyplot as plt

# import pour la gestion des types
from typing import Iterable

# des imports utiles pour la suite
from math import cos, sin, pi

Couleur = (float, float, float)


class Point:
    x: float = 0
    y: float = 0


# type tableau de points
TabPoints = Iterable[Point]

# type tableau de points
TabReels = Iterable[float]


def creer_point(x: float, y: float) -> Point:
    p: Point = Point()
    p.x = x
    p.y = y
    return p

