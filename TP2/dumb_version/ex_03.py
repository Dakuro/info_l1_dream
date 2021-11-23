from numpy import *
from typing import Iterable

Tableau = Iterable

TAB = Tableau[str]

array_char: TAB = zeros(100, str)
char: str
index = int(0)
end_flag = '.'
input_end = False

while not input_end:
    char = input("Entrer un caractère à la fois (. pour terminer) :\n")
    if char == end_flag:
        input_end = True
    else:
        array_char[index] = char
        index += 1

print(array_char)
