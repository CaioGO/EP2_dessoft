def possui_movimentos_possiveis(bar):

    for e in range(len(bar)):     
        mp = lista_movimentos_possiveis(bar, e)
        if mp != []:
            return True

    return False