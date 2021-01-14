""" 5. Tworzenie obiektu MyPolynomial metodą from_iterable(iterable)

Przykłady:

    MyPolynomial.from_iterable([0, 1, 2]) == MyPolynomial(0, 1, 2)
    MyPolynomial.from_iterable((0, 1, 2)) == MyPolynomial(0, 1, 2) """


class MyPolynomial:
    def __init__(self, *coefficients):
        self.__coefficients = list(coefficients)

    @classmethod
    def from_iterable(cls, new_coeff):
        return cls(*new_coeff)

    def __eq__(self, other):
        return self.to_string() == other.to_string()

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


assert MyPolynomial.from_iterable([0, 1, 2]) == MyPolynomial(0, 1, 2)
assert MyPolynomial.from_iterable((0, 1, 2)) == MyPolynomial(0, 1, 2)

