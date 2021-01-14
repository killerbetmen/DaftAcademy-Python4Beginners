""" Wykład 1 - Zadanie 3
Napisz kod, który na podstawie podanego słownika:

{
    1: 'Mateusz',
    2: 'Marcin',
    3: 'Wojciech',
    4: 'Marcin',
    5: 'Michał',
    6: 'Antoni',
    7: 'Katarzyna',
    8: 'Agata',
}

stworzy nowy słownik o postaci (zamiana klucza z wartością):

{
    'Mateusz': 1,
    'Marcin': 2,
    ...
    'Agata': 8
}

Wynik przypisz do zmiennej result.

Uwaga, nie zmieniaj nic w słowniku names! """

names = {
    1: 'Mateusz',
    2: 'Marcin',
    3: 'Wojciech',
    4: 'Marcin',
    5: 'Michał',
    6: 'Antoni',
    7: 'Katarzyna',
    8: 'Agata',
}

result = {}

for num in names:
    result[names[num]] = num

assert 'Mateusz' in result
