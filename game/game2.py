  
# Extrai o valor 
def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

# Extrai o naipe
def extrai_naipe(x):
    j = x[-1]
    return j

# Movimentos possíveis
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

# Empilha cartas
def empilha(b, x, y):
    b[y] = b[x]
    del b[x]

    return b


# Possui movimentos possíveis
def possui_movimentos_possiveis(bar):

    for e in range(len(bar)):     
        mp = lista_movimentos_possiveis(bar, e)
        if mp != []:
            return True

    return False

def g1(bar):
    
    z = 1
    
    print("Situação: ")

    print("------------")
    
    for b in bar:
        print("{}. {}".format(z,b))
        z += 1

def g2(bar):
    while possui_movimentos_possiveis(bar):
        
        c = int(input("Escolha uma carta (digite um número entre 1 e {}): ".format(len(bar))))
        while c < 1 and c > len(bar) and c != " ":
            c = int(input("Por favor, digite um número entre 1 e {}".format(len(bar))))
        
        i = c - 1
        mov = lista_movimentos_possiveis(bar, i)
        print(mov)
        
        if len(mov) == 2:

            print("Sobre qual carta você quer empilhar {}? ".format(bar[i]))

            print("1. {}".format(bar[i - 3]))

            print("2. {}".format(bar[i - 1]))

            a = int(input("Digite 1 ou 2: "))            
            if a == 1:
                bar[i - 3] = bar[i]
                del(bar[i])
                
            elif a == 2:
                bar[i - 1] = bar[i]
                del(bar[i])
        
        else:
            for z in mov:
                if z == 1:
                    bar = empilha(bar, i, i-1)
                    print(len(bar))
                elif i == 3:
                    bar = empilha(bar, i, i-3)
                    print(len(bar))
        
                else:
                    print("A carta {} não pode ser movida. Escolha outra carta(digite um número entre 1 e {}): ".format(bar[i], len(bar)))
    
    return bar