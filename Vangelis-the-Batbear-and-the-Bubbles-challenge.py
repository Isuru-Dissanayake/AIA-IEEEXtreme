#https://csacademy.com/ieeextreme-practice/task/979a09a0cd8c4e98dd0a690f39a55bd2/

testCases = int(input(""))

for cases in range(testCases):
    nm = list(map(int,(input("")).split()))
    e = list(map(int,(input("")).split()))
    edges = [[] for i in range(nm[0])]
    for i in range(len(e)):
        if i%2 == 0:
            edges[e[i]].append(e[i+1])
        elif i%2 == 1:
            edges[e[i]].append(e[i-1])
print (edges)
