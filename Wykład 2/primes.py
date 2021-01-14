""" Napisz funkcję która zwraca listę liczb pierwszych aż do zadanej wlącznie.
Funkcja ma nazywać się primes i przyjmować jeden argument: to_number. """


def primes(number):
    lst = []
    k = 0
    for i in range(2, number+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst


assert primes(5) == [2, 3, 5]
