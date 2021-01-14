""" 8. Wielomiany powinno dać się pomnożyć(*, *=), zarówno przez wielomian, jak i przez liczbę.
    MyPolynomial(6, 14, 8) == MyPolynomial(2, 2) * MyPolynomial(3, 4)
    MyPolynomial(6, 14, 8) == MyPolynomial(3, 7, 4) * 2
    MyPolynomial(6, 14, 8) == 2 * MyPolynomial(3, 7, 4) """

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

    def __mul__(self, other):
        if isinstance(other, MyPolynomial):
            _s = self.__coefficients
            _v = other.__coefficients
            res = [0] * (len(_s) + len(_v) - 1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow + valpow] += selfco * valco
        else:
            res = [co * other for co in self.__coefficients]
        return self.__class__.from_iterable(res)

    def __imul__(self, other):
        if isinstance(other, MyPolynomial):
            _s = self.__coefficients
            _v = other.__coefficients
            res = [0] * (len(_s) + len(_v) - 1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow + valpow] += selfco * valco
        else:
            res = [co * other for co in self.__coefficients]
        self.__coefficients = res
        return self

    def __rmul__(self, other):
        return self * other


assert MyPolynomial(6, 14, 8) == MyPolynomial(2, 2) * MyPolynomial(3, 4)
assert MyPolynomial(6, 14, 8) == MyPolynomial(3, 7, 4) * 2
assert MyPolynomial(6, 14, 8) == 2 * MyPolynomial(3, 7, 4)
