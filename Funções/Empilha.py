def empilha(b, x, y):
    b[y] = b[x]
    del b[x]

    return b