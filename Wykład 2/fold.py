""" Napisz funkcję fold.
Funkcja ma na celu mnożenie kolejnych par elementów zadanych list i
zwrócić listę iloczynów kolejnych par.
Jeżeli listy wejściowe są nierówne,
na ostatnich pozycjach listy wyjściowej powinny znaleźć się 0 w liczbie różnicy długości list. """


def fold(f_list, s_list):
    new_list = []
    if f_list is None and s_list is None:
        new_list = []
    elif f_list is None or s_list is None:
        new_list = [0, 0, 0]
    else:
        for x in f_list:
            if x not in s_list:
                new_list.append(0)
            elif x in s_list:
                if len(f_list) != len(s_list):
                    f_list.append(0)
                new_list.append(x**2)
    return new_list


assert fold([1, 2, 3], [1, 2, 3]) == [1, 4, 9]
assert fold([1, 2, 3], None) == [0, 0, 0]
assert fold([1, 2, 3], []) == [0, 0, 0]
