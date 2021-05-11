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

def g3(bar):

    if bar > 1:
        print(Vermelho + ("------------") + MC)

        print(Vermelho + ("YOU LOSE!") + MC)

        print(Vermelho + ("------------") + MC)

        novo_jogo = str(input("Quer jogar de novamente? {}: ".format(Azul + ('(s/n)') + MC)))

        return novo_jogo

    else:
        print(Vermelho + ("------------") + MC)

        print(Verde + ("YOU WIN!") + MC)

        print(Vermelho + ("------------") + MC)

        novo_jogo = str(input("Quer jogar de novamente? {}: ".format(Azul + ('(s/n)') + MC)))

        return novo_jogo



print(Azul + ("Paciência Acordeão") + MC)
print("---------------------")
print("{} ao jogo '{}', o objetivo é simples:".format((Verde + ('Bem-vindo(a)') + MC), (Azul + ("Paciência Acordeão") + MC)))
print('As {} cartas do um baralho são embaralhadas e distribuídas em sequência. O objetivo do jogo é {}.'.format((Azul + ('52') + MC), (Verde + ('colocar todas as cartas em uma mesma pilha') + MC)))
print("Há apenas {} movimentos possíveis, e são eles:".format(Vermelho + ('dois') + MC))
print("{}. Empilhar a carta sobre uma {} anterior;".format((Azul + ('1') + MC), (Verde + ('imediatamente') + MC)))
print("{}. Empilhar a carta sobre a {} anterior.".format((Azul + ('2') + MC), (Verde + ('terceira') + MC)))
print("Para que se possa executar um movimento, {} condição da lista deve ser atendida:".format(Vermelho + ('ao menos uma') + MC))
print("{}. Ambas as cartas possuem o {};".format((Azul + ('1') + MC), (Verde + ('mesmo valor') + MC)))
print("{}. Ambas cartas possuem o {}.".format((Azul + ('2') + MC), (Verde + ('mesmo naipe') + MC)))
print('---------------------')
print(Vermelho + ('PARA DIFICULTAR') + MC)
print('Os naipes {} e {} possuem a cor {}, e os naipes {} e {} possuem a cor {}'.format((Azul + ('♠') + MC), (Azul + ('♣') + MC), (Azul + ('AZUL') + MC), (Vermelho + ('♥') + MC), (Vermelho + ('♦') + MC), (Vermelho + ('VERMELHA') + MC)))
print('---------------------')
print('{}'.format(Verde + ('BOA SORTE') + MC))
print('---------------------')

try:
    com = int(input("Digite {} para iniciar o jogo  ".format(Azul + ('1') + MC)))
    if com != 1:
        v2 = True
    elif com == 1:
        com = com
        v2 = False
except ValueError:
    c = 0
    v2 = True

while v2 == True:
    try:
        com = int(input("Digite {} para iniciar o jogo  ".format(Azul + ('1') + MC)))
    except ValueError:
        com = 0
        v2 = True
        
    if com == 1:
        com = com
        v2 = False
            
                
    else:
        v2 = True


f = True
bar = cria_baralho()

while f:
    bar = g2(bar)
    f = g3(bar)
    
    if f == "s":
        f == True
        bar = cria_baralho()
        
    elif f == "n":
        f == False

print(Verde + ("Volte sempre!") + MC)