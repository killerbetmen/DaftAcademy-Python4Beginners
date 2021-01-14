"""
Napisz generator który zwraca kolejne liczby całkowite nieujemne oraz
funkcję, która sprawdza czy liczba n, jest palidromiczna - jeśli jest, to funkcja zwraca True.
Jeśli podana liczba nie nie może być palindomiczna,
bo na przykład jest liczbą ujemną to powinien być rzucony wyjątek ValueError.


Rozbuduj podane funkcje.
"""


def infinite_sequence(n):
    while n >= 0:
        yield n
        n += 1


def is_palindrome(n):

    if str(n) == str(n)[::-1]:
        return True

    if float(n).is_integer():
        return False
    else:
        raise ValueError
