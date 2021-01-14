""" 4. Nasze wielomiany powinno dać się porównywać, tak jak w przykładzie:

    MyPolynomial(5) == MyPolynomial(5, 1)  # powinno zwrócić False
    MyPolynomial() == MyPolynomial(0)  # powinno zwrócić True """


class MyPolynomial:

    def __init__(self, *coeficients):
        self.__coefficients = list(coeficients)

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


assert (MyPolynomial(5) == MyPolynomial(5, 1)) is False
assert MyPolynomial() == MyPolynomial(0)
