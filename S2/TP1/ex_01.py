from numpy import zeros, array
from typing import Iterable, TypeVar

TabReels = TypeVar(Iterable[float])
MatReels = TypeVar(Iterable[TabReels])

MAXPRODUITS = 100
askValue = "Saisissez {value} du produit n°{noproduct}"
infoProduct = "Voici les détails du produit n°{noproduct} :\nPrix : {price}\nNote : {mark}"


# Saisir le prix et la note d'un produit no et les stocke dans la colonne no de tabPrixNotes
def saisir_produit(no: int, tabPrixNotes: MatReels):
    prix: int = int(input(askValue.format(value="le prix", noproduct=no)))
    note: int = int(input(askValue.format(value="la note", noproduct=no)))
    tabPrixNotes[0][no] = prix
    tabPrixNotes[1][no] = note


# Appelle la procédure saisir_produit nb fois pour saisir nb produits
def saisir_produits(nb: int, tabPrixNotes: MatReels):
    for i in range(nb):
        saisir_produit(i, tabPrixNotes)


# Affiche le no, le prix et la note du produit no
def afficher_detail_produit(no: int, tabPrixNotes: MatReels):
    print(infoProduct.format(noproduct=no, price=tabPrixNotes[0][no], mark=tabPrixNotes[1][no]))


# Appelle la procédure afficher_detail_produit nb fois
def afficher_produits(nb: int, tabPrixNotes: MatReels):
    for i in range(nb):
        afficher_detail_produit(i, tabPrixNotes)
