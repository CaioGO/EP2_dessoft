import random

#Cores
Vermelho   = "\033[1;31m"  
Azul  = "\033[1;34m"
Verde = "\033[0;32m"
MC = "\033[0;0m"

# Extrai o valor 
def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

# Extrai o naipe
def extrai_naipe(x):
    j = x[-1]
    return j

# Coloração
def cor(car):
    if extrai_naipe(car) == '♠':
        car = Azul + car + MC
    elif extrai_naipe(car) == '♥':
        car = Vermelho + car + MC
    elif extrai_naipe(car) == '♣':
        car = Azul + car + MC
    elif extrai_naipe(car) == '♦':
        car = Vermelho + car + MC

    return car

#Criando Deck
def cria_baralho():
    cart = []
    let = ['J', 'Q', 'K', 'A']
    naipes = ['♠', '♥', '♦', '♣']
    baralho = []

    for i in range(2, 11):
        cart.append(str(i))
    
    for j in range(4):
        cart.append(let[j])

    for w in range (4):
        for k in range(13):
            carta = (cart[k] + naipes[w])
            baralho.append(carta)

    random.shuffle(baralho)
    
    for n in range(52):
        print(cor(baralho[n]))

    return baralho

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