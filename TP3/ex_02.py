from random import *
from numpy import *
from typing import Iterable
Tableau = Iterable

Tab = Tableau[int]


def afficher(t: Tab):
    print(t)


def remplir_rndm(t: Tab, rndm_min: int, rndm_max: int):
    for n in t:
        t[n] = randint(rndm_min, rndm_max)


test_tab1: Tab = zeros(20, int)
test_tab2: Tab = zeros(20, int)
remplir_rndm(test_tab1, 0, 100)
remplir_rndm(test_tab2, 0, 100)
afficher(test_tab1)
afficher(test_tab2)
