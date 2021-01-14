""" Wykład 1 - Zadanie 4
Napisz program tworzący ze zbioru U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'} zbiór zawierający wszystkie podzbiory U (włącznie z pustym i U).

UWAGA: w Pythonie zbiory nie mogą być elementami innych zbiorów, proszę użyć frozenset jako zbiorów wewnętrznych (było to wspomniane na wykładzie!)

Wynik przypisz do zmienej result. """

from itertools import combinations

U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'}

result = set()

for i in range(len(U) + 1):
    for c in combinations(U, i):
        result.add(frozenset(c))


assert frozenset(('👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌')) in result