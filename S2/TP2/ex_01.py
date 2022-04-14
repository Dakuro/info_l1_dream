# Import pour la gestion de tableaux
from numpy import zeros, array

# Import pour la librairie graphique
import matplotlib.pyplot as plt

# Import pour la gestion des types
from typing import Iterable

# Imports utiles pour la suite
from math import cos, sin, pi

Couleur = (float, float, float)


class Point:
    x: float = 0
    y: float = 0


# Type tableau de points
TabPoints = Iterable[Point]

# Type tableau de réels
TabReels = Iterable[float]


# Crée et retourne un point à partir des coordonnées d'entrée
def creer_point(x: float, y: float) -> Point:
    p: Point = Point()
    p.x = x
    p.y = y
    return p


# Tarifs du m^3 d'eau en 2018
tab_prix: TabReels = array([
    5.25,  # 00 - Bellaing
    5.59,  # 01 - Beuvrages
    4.71,  # 02 - Coudekerque-Branche
    3.90,  # 03 - Faches-Thumesnil
    5.25,  # 04 - Ghissignies
    5.08,  # 05 - Gravelines
    3.91,  # 06 - Lys-lez-Lannoy
    4.55,  # 07 - Maubeuge
    5.25,  # 08 - Méteren
    4.55,  # 09 - Pont-sur-Sambre
    3.91,  # 10 - Quesnoy-sur-Deule
    4.71,  # 11 - Saint-Pol-sur-Mer
    4.63,  # 12 - Sin-le-Noble
    5.25,  # 13 - Steene
    5.89,  # 14 - Valenciennes
    3.87,  # 15 - Wattignies
    3.92,  # 16 - Wattrelos
    4.71  # 17 - Zuydcoote
])


# Crée une courbe à partir du tableau donné en entrée
def creer_courbes_couts(tab_prix):
    # Récupération du nb de villes
    nb_villes: int = len(tab_prix)

    # Création d'un tableau d'entiers contenant nb_villes 0
    tab_x: TabReels = zeros(nb_villes, int)

    # Remplissage du tableau
    for i in range(0, nb_villes):
        tab_x[i] = i

    # Création de la courbe
    plt.plot(tab_x, tab_prix)
    plt.show()


# Test
creer_courbes_couts(tab_prix)


def creer_courbes_couts_seuils(tab_prix):
    # Récupération du nb de villes
    nb_villes: int = len(tab_prix)

    # Création d'un tableau de réels contenant nb_villes 0
    tab_x: TabReels = zeros(nb_villes, float)

    for i in range(nb_villes):
        tab_x[i] = i
    plt.plot(tab_x, tab_prix, color=(0, 0, 0))

    # Recherche du MIN, du MAX, et de la moyenne des valeurs du tableau tab_prix
    cout_min: float = tab_prix[0]
    cout_max: float = tab_prix[0]
    cout_moyen: float = 0.

    # Somme des coûts pour le calcul du coût moyen
    cout_sum: float = tab_prix[0]

    # TO-DO: CALCULER LE MAX, LE MIN ET LA MOYENNE
    for i in range(1, nb_villes):
        if tab_prix[i] > cout_max:
            cout_max = tab_prix[i]
        elif tab_prix[i] < cout_min:
            cout_min = tab_prix[i]
        cout_sum += tab_prix[i]
    cout_moyen = cout_sum / nb_villes

    # Courbe de la ligne du coût max
    tab_max = zeros(nb_villes, float)

    # Courbe de la ligne du coût min
    tab_min = zeros(nb_villes, float)

    # Courbe de la ligne du coût moyen
    tab_moy = zeros(nb_villes, float)

    for i in range(nb_villes):
        tab_max[i] = cout_max
        tab_min[i] = cout_min
        tab_moy[i] = cout_moyen

    # Création de la courbe
    plt.plot(tab_x, tab_max, color=(1, 0, 0))
    plt.plot(tab_x, tab_min, color=(0, 0, 1))
    plt.plot(tab_x, tab_moy, '--', color=(0, 1, 0))

    plt.show()


# Test
creer_courbes_couts_seuils(tab_prix)


def remplir_tab(tab: TabPoints):
    n: int = len(tab)
    a: float = 2. * pi / n
    for i in range(n):
        tab[i] = creer_point(cos(a * i), sin(a * i))


def dessiner_cercle(tab: TabPoints):
    n: int = len(tab)
    tab_x: TabReels = zeros(n, float)
    tab_y: TabReels = zeros(n, float)
    for i in range(n):
        tab_x[i] = tab[i].x
        tab_y[i] = tab[i].y
    plt.plot(tab_x, tab_y)
    plt.show()


# Test
nb_points: int = 36
le_tab: TabPoints = zeros(nb_points, dtype=Point)
remplir_tab(le_tab)
dessiner_cercle(le_tab)


def dessiner_droites(tab: TabPoints, coef: int):
    plt.figure(figsize=(20, 20))
    n: int = len(tab)

    # Tableaux pour stocker les coordonnées des points Pi et Pi*coef
    tab_x: TabReels = zeros(2, float)
    tab_y: TabReels = zeros(2, float)

    # Le couple de point change à chaque indentation de la boucle
    for i in range(n):
        # Pour chaque point, on vérifie si on dépasse des bornes du tableau
        if i * coef >= n:
            tab_x[0] = tab[i].x
            tab_y[0] = tab[i].y
            # Si on dépasse des bornes, le point Pi*coef devient Pi*coef%n
            tab_x[1] = tab[i * coef % n].x
            tab_y[1] = tab[i * coef % n].y
        else:
            tab_x[0] = tab[i].x
            tab_y[0] = tab[i].y
            tab_x[1] = tab[i * coef].x
            tab_y[1] = tab[i * coef].y
        # On trace une droite reliant les deux points du couple
        plt.plot(tab_x, tab_y, color=(0, 0, 0))

    plt.show()


# Test
nb_points: int = 1256
le_tab: TabPoints = zeros(nb_points, dtype=Point)
remplir_tab(le_tab)
dessiner_droites(le_tab, 2)


def dessiner_droites_colorees(tab: TabPoints, coef: int):
    plt.figure(figsize=(20, 20))
    n: int = len(tab)

    # Tableaux pour stocker les coordonnées des points Pi et Pi*coef
    tab_x: TabReels = zeros(2, float)
    tab_y: TabReels = zeros(2, float)

    # Le couple de point change à chaque indentation de la boucle
    for i in range(n):
        # Pour chaque point, on vérifie si on dépasse des bornes du tableau
        if i * coef >= n:
            tab_x[0] = tab[i].x
            tab_y[0] = tab[i].y
            # Si on dépasse des bornes, le point Pi*coef devient Pi*coef%n
            tab_x[1] = tab[i * coef % n].x
            tab_y[1] = tab[i * coef % n].y
        else:
            tab_x[0] = tab[i].x
            tab_y[0] = tab[i].y
            tab_x[1] = tab[i * coef].x
            tab_y[1] = tab[i * coef].y
        # On trace une droite reliant les deux points du couple
        plt.plot(tab_x, tab_y, color=(0, 0, 0))

    plt.show()


# Test
nb_points: int = 3000
le_tab: TabPoints = zeros(nb_points, dtype=Point)
remplir_tab(le_tab)
dessiner_droites_colorees(le_tab, 30)
