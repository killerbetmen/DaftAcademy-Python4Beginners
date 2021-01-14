""" 7. Wielomiany powinno dać się do siebie dodać.

Przykłady:

    MyPolynomial(5, 8) == MyPolynomial(2, 4) + MyPolynomial(3, 4)
    mp1 = MyPolynomial(2, 4)
    mp2 = MyPolynomial(3, 4)
    mp3 = MyPolynomial(5, 8)
    mp1 += mp2
    mp3 == mp1 """

import itertools


class MyPolynomial:

    def __init__(self, *coeficients):
        self.__coefficients = list(coeficients)

    @classmethod
    def from_iterable(cls, new_coeff):
        return cls(*new_coeff)

    def __eq__(self, other):
        return self.to_string() == other.to_string()

    def __call__(self, n):
        res = 0
        for i, c in enumerate(self.__coefficients):
            res += c * (n ** i)
        return res

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        if len(self.__coefficients) == 0 or set(self.__coefficients) == {0}:
            return 'MyPolynomial(0)'
        else:
            return 'MyPolynomial' + str(tuple(self.__coefficients))

    def to_string(self):
        if len(self.__coefficients) > 0 and set(self.__coefficients) != {0}:
            res = []
            for i, n in enumerate(self.__coefficients):
                res.append(self.__character_to_power(n, i))

            return " + ".join([i for i in res if i]).replace("+ -", "- ")
        else:
            return "0"

    @staticmethod
    def __character_to_power(num, power):
        if num == 0:
            return None

        return "{}{}".format(num, "x" * power if power < 1 else "x^" + str(power))

    def __add__(self, other):
        lists = [self.__coefficients, other.__coefficients]
        new_poly = [sum(x) for x in itertools.zip_longest(*lists, fillvalue=0)]

        return MyPolynomial.from_iterable(new_poly)

    def __iadd__(self, other):
        lists = [self.__coefficients, other.__coefficients]
        new_poly = [sum(x) for x in itertools.zip_longest(*lists, fillvalue=0)]

        self.__coefficients = new_poly

        return self


assert MyPolynomial(5, 8) == MyPolynomial(2, 4) + MyPolynomial(3, 4)

mp1 = MyPolynomial(2, 4)
mp2 = MyPolynomial(3, 4)
mp3 = MyPolynomial(5, 8)
mp1 += mp2
assert mp3 == mp1
