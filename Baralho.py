def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

def extrai_naipe(x):
    j = x[-1]
    return j


def lista_movimentos_possiveis(x):
    dev = []
    z = 0
    for i in range(len(x)):
        if x[i - 1] == x[i]:
            dev.append(z)
            z += 1
        elif x[i - 1] != x[i]:
            if extrai_valor(x[i - 1]) == extrai_valor(x[i]):
                dev.append(z)
                z += 1