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
    max_value: float = float(tab[0])
    for i in range(nb):
        if tab[i + 1] > max_value:
            max_value = tab[i + 1]
    return max_value


# Retourne la valeur maximum avec pour type float parmi les nb valeurs de tab
def min_tab(nb: int, tab: TabReels) -> float:
    min_value: float = float(tab[0])
    for i in range(nb):
        if tab[i + 1] < min_value:
            min_value = tab[i + 1]
    return min_value


# Détermine le prix minimum parmi nb produits puis affiche les produits correspondants
def afficher_moins_chers(nb: int, tab_prix_notes: MatReels):
    prix_min: float = min_tab(nb, tab_prix_notes[0])
    print("Voici les produits les moins chers :")
    for i in range(nb):
        if tab_prix_notes[0][i] == prix_min:
            afficher_detail_produit(i, tab_prix_notes)


# Détermine la note maximum parmi nb produits puis affiche les produits correspondants
def afficher_mieux_notes(nb: int, tab_prix_notes: MatReels):
    note_max: float = max_tab(nb, tab_prix_notes[1])
    print("Voici les produits les mieux notés :")
    for i in range(nb):
        if tab_prix_notes[1][i] == note_max:
            afficher_detail_produit(i, tab_prix_notes)


def remplir_tab_norme(nb: int, tab: TabReels, tab_norm: TabReels):
    max_value: float = max_tab(nb, tab)
    for i in range(nb):
        tab_norm[i] = tab[i] / max_value
