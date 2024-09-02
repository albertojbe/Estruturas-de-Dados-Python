def swap(word, i, j):
    listWord = list(word)
    listWord[i], listWord[j] = listWord[j], listWord[i]
    return "".join(listWord)
    

def invert(word, start, end):
    if not (start > end):
        word = swap(word, start, end)
        return invert(word, start + 1, end - 1)
    return word

name = "Python"
print(invert(name, 0, len(name)- 1))