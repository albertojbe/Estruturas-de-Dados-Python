def contNaturalNums(num, cont = -2):
    cont = num if cont == -2 else cont
    if cont >= 0:
        print(cont)
        contNaturalNums(num, cont - 1)
    
contNaturalNums(10)