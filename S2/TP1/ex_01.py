from numpy import zeros, array
from typing import Iterable, TypeVar

TabReels = TypeVar(Iterable[float])
MatReels = TypeVar(Iterable[TabReels])

MAXPRODUITS = 100


# Saisir le prix et la note d'un produit no et les stocke dans la colonne no de tab_prix_notes
def saisir_produit(no: int, tab_prix_notes: MatReels):
    ask_value = "Saisissez {value} du produit n°{noproduct}"
    prix: float = float(input(ask_value.format(value="le prix", noproduct=no)))
    note: float = float(input(ask_value.format(value="la note", noproduct=no)))
    tab_prix_notes[0][no] = prix
    tab_prix_notes[1][no] = note


# Appelle la procédure saisir_produit nb fois pour saisir nb produits
def saisir_produits(nb: int, tab_prix_notes: MatReels):
    for i in range(nb):
        saisir_produit(i, tab_prix_notes)


# Affiche le no, le prix et la note du produit no
def afficher_detail_produit(no: int, tab_prix_notes: MatReels):
    info_product = "Voici les détails du produit n°{noproduct} :\nPrix : {price}\nNote : {mark}"
    print(info_product.format(noproduct=no, price=tab_prix_notes[0][no], mark=tab_prix_notes[1][no]))


# Appelle la procédure afficher_detail_produit nb fois
def afficher_produits(nb: int, tab_prix_notes: MatReels):
    for i in range(nb):
        afficher_detail_produit(i, tab_prix_notes)


# Retourne la valeur maximum avec pour type float parmi les nb valeurs de tab
def max_tab(nb: int, tab: TabReels) -> float:
    max_value: float = tab[0]
    for i in range(1, nb):
        if tab[i] > max_value:
            max_value = tab[i]
    return max_value


# Retourne la valeur maximum avec pour type float parmi les nb valeurs de tab
def min_tab(nb: int, tab: TabReels) -> float:
    min_value: float = tab[0]
    for i in range(1, nb):
        if tab[i] < min_value:
            min_value = tab[i]
    return min_value


# Détermine le prix minimum parmi nb produits puis affiche les produits correspondants
def afficher_moins_chers(nb: int, tab_prix_notes: MatReels):
    prix_min: float = min_tab(nb, tab_prix_notes[0])
    print("Voici le(s) produit(s) le(s) moins cher(s) :")
    for i in range(nb):
        if tab_prix_notes[0][i] == prix_min:
            afficher_detail_produit(i, tab_prix_notes)


# Détermine la note maximum parmi nb produits puis affiche les produits correspondants
def afficher_mieux_notes(nb: int, tab_prix_notes: MatReels):
    note_max: float = max_tab(nb, tab_prix_notes[1])
    print("Voici le(s) produit(s) le(s) mieux noté(s) :")
    for i in range(nb):
        if tab_prix_notes[1][i] == note_max:
            afficher_detail_produit(i, tab_prix_notes)


# Remplace les nb cases de tab_norm par nb cases de tab divisées par la valeur max de tab
def remplir_tab_norme(nb: int, tab: TabReels, tab_norm: TabReels):
    max_value: float = max_tab(nb, tab)
    for i in range(nb):
        tab_norm[i] = tab[i] / max_value


# Erreur de sujet ? Le type de tab_prix_notes est noté "TabReels" sur le sujet.
# Or, tab_prix_notes est logiquement de type "MatReels" pour pouvoir accéder à ses deux lignes.
def trouver_compromis(nb: int, tab_prix_notes: MatReels):
    # Crée et remplie tab_norm_prix et tab_norm_notes à partir de nb valeurs de tab_prix_notes
    tab_norm_prix: TabReels = zeros(nb, float)
    tab_norm_notes: TabReels = zeros(nb, float)
    remplir_tab_norme(nb, tab_prix_notes[0], tab_norm_prix)
    remplir_tab_norme(nb, tab_prix_notes[1], tab_norm_notes)

    # Crée et remplie tab_mixe, contenant nb valeurs calculées à partir de tab_norm_prix et tab_norm_notes
    tab_mixe: TabReels = zeros(nb, float)
    for i in range(nb):
        # Erreur de sujet ? On multiplie par 0.9 dans la formule, mais pas dans les exemples
        tab_mixe[i] = tab_norm_notes[i] * (1 - tab_norm_prix[i])  # Selon les exemples donnés
        # Selon la formule donnée dans le sujet, il faudrait écrire ceci :
        # tab_mixe[i] = tab_norm_notes[i] * (1 - tab_norm_prix[i] * 0.9)
        # Dans cette formule, la multiplication par 0.9 est prioritaire dans la parenthèse.

    # Détermine la valeur maximale de tab_mixe et affiche le(s) produit(s) correspondant(s)
    max_mixe: float = max_tab(nb, tab_mixe)
    print("Voici le(s) produit(s) le(s) plus intéressant(s) :")
    for i in range(nb):
        if tab_mixe[i] == max_mixe:
            afficher_detail_produit(i, tab_prix_notes)


# Calcul et retourne la moyenne des nb premières valuers de tab
def moyenne(nb: int, tab: TabReels) -> float:
    avg: float = tab[0]
    for i in range(1, nb):
        avg += tab[i]
    avg /= nb
    return avg


def test_tp1():
    prix: TabReels = array([81, 72, 85, 71, 66, 104, 91, 87])
    notes: TabReels = array([2, 4, 5, 3, 2, 0, 2, 5])
    prix_notes: MatReels = array([prix, notes])
    nb: int = len(prix)
    afficher_moins_chers(nb, prix_notes)
    afficher_mieux_notes(nb, prix_notes)
    trouver_compromis(nb, prix_notes)
    print("Moyenne des prix : " + str(moyenne(nb, prix)))
    print("Moyenne des notes : " + str(moyenne(nb, notes)))


test_tp1()

# Le produit le moins cher est le produit n°4 pour 66€
# Les produits les mieux notés sont les produits n°2 et n°7 avec une note de 5
# Le produit le plus intéressant est le produit n°1
# La moyenne des prix est de 82.125€
# La moyenne des notes est de 2.875
