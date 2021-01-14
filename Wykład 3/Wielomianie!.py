""" 3. Instancję obiektu klasy MyPolynomial powinniśmy móc wywołać z argumentem x.
Podobnie jak w matematyce piszemy:
w(x) = 1 + 2x  + 2x^2, kiedy podstawimy za x 2 mamy w(2), chcielibyśmy otrzymać wynik:
w(2) = 1 + 2*2 + 2*2^2 = 13

Przykład:

w = MyPolynomial(1, 2, 2)
w(2) == 13  # powinno zwrócić True """


class MyPolynomial:

    def __init__(self, *coeficients):
        self.__coefficients = list(coeficients)

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


w = MyPolynomial(1, 2, 3)
assert w(2) == 17
