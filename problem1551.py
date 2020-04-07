cases = int(input())

for x in range(0, cases):
    phrase = input()
    letters = set()
    for char in phrase:
        if char.isalpha(): letters.add(char)

    if len(letters) == 26:
        print("frase completa")
    elif len(letters) >= 13 and len(letters) < 26:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
