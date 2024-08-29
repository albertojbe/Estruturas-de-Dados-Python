def exec5(n):
    if n == 1:
        return 
    if n % 2 == 0:
        n = n / 2
        print (n)
        exec5(n)
    else:
        n = (3 * n + 1)
        print(n)
        exec5(n)

exec5(13)

    