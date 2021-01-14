""" Napisz funkcję doskonale,
ktora zwraca listę wszystich liczb doskonałych mniejszych bądź równych zadanemu n. """


def doskonale(number):
    list_doskonale = []
    for i in range(2, number + 1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        if s == i:
            list_doskonale.append(i)
    return list_doskonale


assert doskonale(6) == [6]