def contKey(word: str, key: str, start = 0, cont = 0):
    if start > len(word) -1:
        return cont
    elif key == word[start]:
        cont += 1
        
    return contKey(word, key, start + 1, cont)

word = input("Digite uma palavra: ").lower()
key = input("Digite uma letra: ").lower()
print(f"A quantidade de vezes que essa letra aparece na palavra é: {contKey(word, key)}")