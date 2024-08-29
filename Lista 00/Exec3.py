def fatorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n * fatorial(n-1)

print(fatorial(6))