"""  6. Klasa MyPolynomial powinna mieć zaimplementowaną metodę degree, która zwraca stopień wielomianu.

Przykłady:

    MyPolynomial(5, 4).degree() == 1  # powinna zwrócić True
    MyPolynomial().degree() == 0  # powinna zwrócić True """


class MyPolynomial:
    def __init__(self, *coefficients):
        self.__coefficients = list(coefficients)

    @classmethod
    def from_iterable(cls, new_coeff):
        return cls(*new_coeff)

    def degree(self):
        res = 0
        for i, x in enumerate(self.__coefficients):
            if x != 0:
                res = i
        return res


assert MyPolynomial(5, 4).degree() == 1
assert MyPolynomial().degree() == 0
