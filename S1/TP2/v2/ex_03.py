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

array_voy: TAB = zeros(6, str)
array_voy[0], array_voy[1], array_voy[2], array_voy[3], array_voy[4], array_voy[5]\
    = 'a', 'e', 'i', 'o', 'u', 'y'
count_voy = int(0)
count_con = int(0)

for i in array_char:
    for j in array_voy:
        if array_char[i] == array_voy[j]:

