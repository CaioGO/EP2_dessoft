import random

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
        print(baralho[n])

    return baralho