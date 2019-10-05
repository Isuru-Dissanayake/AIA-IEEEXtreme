stack = []
lastPos = 0
def dfs_recursive(v,ngbrs)
def dfs(v,ngbrs):
    if visited[v] == False:
        visited[v] == True
        nei = ngbrs[v]
        for k in range(len(nei)):
            if nei[k] != lastPos:
                stack.append(nei[k])
                visited[nei[k]] = True



testCases = int(input(""))
for cases in range(testCases):
    loop = 0
    nm = list(map(int,(input("")).split()))
    v_num = nm[0]
    e_num = nm[1] 
    e = list(map(int,(input("")).split()))
    visited = [False for i in range(v_num)]
    ngbrs = [[] for i in range(nm[0])]
    for i in range(len(e)):
        if i%2 == 0:
            ngbrs[e[i]].append(e[i+1])
        elif i%2 == 1:
            ngbrs[e[i]].append(e[i-1])
    for i in range(v_num):
        loop = dfs(i,ngbrs)
    