import math

do_loop = int(-1)
primes = []
choice = """Que voulez-vous faire ?
0 - Quitter le programme
1 - Entrer un nombre pour savoir s'il est premier
2 - Afficher tout les nombres premiers < 100\n"""


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if (num % a) < 1:
            return False
        a += 1
    return num > 1


print(isprime(11))  # Test 1
print(isprime(21))  # Test 2

while do_loop != 0:
    do_loop = int(input(choice))
    if do_loop == 1:
        nb = int(input("Entrer un nombre pour savoir s'il est premier :\n"))
        print(isprime(nb))
    elif do_loop == 2:
        primes.clear()
        for i in range(2, 100):
            if isprime(i):
                primes.append(i)
        print(primes)
    elif do_loop != 0:
        print("Saisie incorrecte.")
