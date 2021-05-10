def g3(bar):

    if bar > 1:

        print("YOU LOSE!")

        print("------------")

        novo_jogo = str(input("Quer jogar de novo? (s/n): "))

        return novo_jogo

    else:

        print("YOU WIN!")

        print("------------")

        novo_jogo = str(input("Quer de jogar de novo? (s/n): "))

        return novo_jogo