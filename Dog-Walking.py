t = int(input(""))
for testCases in range(t):
    nk = list(map(int,input("").split()))
    n = nk[0]
    k = nk[1]
    dogs = []
    for i in range(n):
        dogs.append(int(input("")))
    dogs.sort()
    