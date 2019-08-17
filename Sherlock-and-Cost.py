def getCost(b):
    cost = []
    for i in range(len(b)):
        cost.append([0,0])
    for i in range(1,len(b)):
        cost[i][0] = cost[i-1][1] + abs(b[i-1] - 1)
        u = cost[i-1][0] + abs(b[i] - 1)
        v = cost[i-1][1] + abs(b[i] - b[i-1])
        cost[i][1] = max(u,v)
    print (max(cost[len(b) - 1][0],cost[len(b)-1][1]))

t = int(input(""))
for q in range(t):
    n = int(input(""))
    array = list(map(int,(input("")).split()))
    getCost(array)
