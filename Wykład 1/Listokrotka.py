""" Wykład 1 - Zadanie 2
Napisać kod tworzący listę krotek kolejnych elementów parzystych < 100 według schematu: [(0, ), (2, ), ... , (98, )].

Wynikową listę przypisz do zmiennej result. """

result = []

for x in range(100):
    if x % 2 == 0:
        result.append((x,))

assert result[1] == (2, )
