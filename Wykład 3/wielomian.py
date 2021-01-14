""" W tym zadaniu zawsze będą poprawne dane.
Nie ma potrzeby obsługiwania sytuacji wyjątkowych.
Napisz klasę MyPolynomial → https://pl.wikipedia.org/wiki/Wielomian
Ta klasa ma reprezentować wielomian.
Ta klasa ma być mutowalna.
Ta klasa ma mieć jedno pole `prywatne`(prywatne przez konwencję). Nazwa pola - dowolna


1. Instancję klasy MyPolynomial powinno dać się utworzyć na następujące sposoby
(Po znaku komentarza jest opis, jak należy interpretować wartości wewnątrz):
    MyPolynomial()  # 0
    MyPolynomial(1)  # 1
    MyPolynomial(1, 2)  # 1 + 2x
    MyPolynomial(1, 2, 3)  # 1 + 2x + 3x^2 """


class MyPolynomial:

    def __init__(self, *coeficients):
        self.__coefficients = list(coeficients)

    def __repr__(self):
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

        return "{}{}".format(num, "x" * power if power < 2 else "x^" + str(power))


assert MyPolynomial()  # 0
assert MyPolynomial(1)  # 1
assert MyPolynomial(1, 2)  # 1 + 2x
assert MyPolynomial(1, 2, 3)  # 1 + 2x + 3x^2
