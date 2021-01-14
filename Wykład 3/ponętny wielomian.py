""" 2. Instancje klasy MyPolynomial powinno dać się rzutować na string, zaimplementuj odpowiednie metody,
w taki sposób, żeby polecenie str na obiekcie MyPolynomial(1,2,3) zwracało '1 + 2x + 3x^2'. Metoda reprezentacyjna(repr) dla MyPolynomial, powina zwracać strig w takiej postaci, żeby przeklejony do konsoli interpretera (bez '') mógł stworzyć obiekt o identycznej strukturze.

Przyklady:

    '1 + 2x^1' == str(MyPolynomial(1, 2))
    '1 + 1x^1 + 2x^2' == str(MyPolynomial(1, 1, 2))
    'MyPolynomial(1, 2)' == repr(MyPolynomial(1, 2)) """


class MyPolynomial:

    def __init__(self, *coeficients):
        self.__coefficients = list(coeficients)

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


assert '1 + 2x^1' == str(MyPolynomial(1, 2))
assert '1 + 1x^1 + 2x^2' == str(MyPolynomial(1, 1, 2))
assert '1 + 2x^2' == str(MyPolynomial(1, 0, 2))
assert 'MyPolynomial(1, 2)' == repr(MyPolynomial(1, 2))
