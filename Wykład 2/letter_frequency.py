""" Napisz funkcję letter_frequency, która przyjmuje jako argument string.
Dla podanego stringa funkcja musi zliczyć ile razy wystąpiła każda litera z alfabetu łacińskiego.
Zwróc wynik jako słownik wartości ile razy wystąpiła każda litera, gdzie klucz
to występująca litera a wartścią jest liczba jej wystąpień. """


def letter_frequency(text=None):
    result = {}
    if text is None:
        result = {}
    else:
        for letter in text:
            if letter.isalpha():
                count = text.count(letter)
                result[letter] = count
    return result


assert letter_frequency("Mateusz ;;;';'- mateusz") == {'M': 1, 'a': 2, 't': 2, 'e': 2, 'u': 2, 's': 2, 'z': 2, 'm': 1}
assert letter_frequency() == {}
