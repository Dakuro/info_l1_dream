import math


def parfait(nombre):
    primes = []
    perfect = []
    sq_nb = math.sqrt(nombre)

    for n in range(2, int(sq_nb) + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                primes.append(n)

    for i in primes:
        x = math.pow(2, i - 1) * (math.pow(2, i) - 1)
        if x < nombre:
            perfect.append(int(x))
        else:
            break

    return perfect


print("Les nombres parfaits entre 1 et 1000 sont :\n", parfait(1000))
