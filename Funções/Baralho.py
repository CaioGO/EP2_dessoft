def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

def extrai_naipe(x):
    j = x[-1]
    return j


def lista_movimentos_possiveis(x, y):
    dev = []
    i = 1

    while i <= 4:
        if x[y - i] == x[y]:
            dev.append(i)
            i += 2
        elif y == 0:
            break

        elif x[y - i] != x[y]:
            if y - i < 0:
                break
            elif extrai_valor(x[y - i]) == extrai_valor(x[y]):
                dev.append(i)
                i += 2
            elif extrai_naipe(x[y - i]) == extrai_naipe(x[y]):
                dev.append(i)
                i += 2
            else:
                i += 2
        else:
            i += 2

    return dev