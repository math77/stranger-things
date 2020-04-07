cases = int(input())

for x in range(0, cases):
    string = input()
    words = list(string.split(" "))
    list_sort = sorted(words, key=len, reverse=True)

    print(' '.join(list_sort))
