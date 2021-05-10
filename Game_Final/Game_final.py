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

def g1(bar):
    
    z = 1
    print(Verde + ('------------') + MC)
    print(Verde + ("Situação: ") + MC)
    print(Verde + ('------------') + MC)
    
    for b in bar:
        print("{}. {}".format(z,cor(b)))
        z += 1

def g2(bar):
    
    print(g1(bar))
    while possui_movimentos_possiveis(bar):
        v = False

        try:
            c = int(input("Escolha uma {} (digite um número entre 1 e {}): ".format(Verde + ('carta') + MC ,len(bar))))
            if c < 0 or c > len(bar):
                v = True
            else:
                c = c
                print(g1(bar))
        except ValueError:
            c = 0
            print(g1(bar))
            v = True
            
            
    
        while v == True:
                try:
                    c = int(input("{} Por favor, digite um {} entre 1 e {}. ".format((Vermelho + ('Inválido!')+ MC), (Vermelho + ('NÚMERO')+ MC),len(bar))))
                except ValueError:
                        c = 0
                if c > 0 and c <= len(bar):
                    v = False
                
                else:
                    print(g1(bar))
                    v = True
 
        i = c - 1
        mov = lista_movimentos_possiveis(bar, i)
        
        if len(mov) == 2:

            print("Você deseja empilhar a carta {} sobre qual carta? ".format(cor(bar[i])))

            print("1. {}".format(cor(bar[i - 3])))

            print("2. {}".format(cor(bar[i - 1])))

            a = int(input("Escolha (1/2): "))            
            if a == 1:
                bar[i - 3] = bar[i]
                del(bar[i])
                print(g1(bar))
                
            elif a == 2:
                bar[i - 1] = bar[i]
                del(bar[i])
                print(g1(bar))
        
        else:
            for z in mov:
                if z == 1:
                    bar = empilha(bar, i, i-1)
                    print(len(bar))
                    print(g1(bar))
                elif i == 3:
                    bar = empilha(bar, i, i-3)
                    print(len(bar))
                    print(g1(bar))
        
                else:
                    print(g1(bar))
                    print("A carta {} não pode ser movida. Escolha outra carta (digite um número entre 1 e {}): ".format(bar[i], len(bar)))
    return bar