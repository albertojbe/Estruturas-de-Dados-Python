def contNaturalNums(num, cont = 0):
    if not cont > num:
        print(cont)
        contNaturalNums(num, cont + 1)
    
contNaturalNums(90)