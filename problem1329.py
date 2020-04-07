ncases = 1

while ncases != 0:

    ncases = int(input())
    if ncases == 0:
        break

    results = input().split(" ")
    j = [int(j) for j in results if int(j) == 1]
    m = [int(m) for m in results if int(m) == 0]
    
    print("Mary won {0} times and John won {1} times".format(len(m), len(j)))
