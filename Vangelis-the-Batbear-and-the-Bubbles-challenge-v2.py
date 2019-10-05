stack = []
lastPos = 0
current = 0
visited = []
check = []
proc = 1

def dfs_recursive(ngbrs):
    if len(stack) == 0:
        return (False)
    else:
        current = stack.pop()
        visited[current] = True
        nei = ngbrs[current]
        for k in range(len(nei)):
            if not visited[nei[k]]:
                if nei[k] in stack:
                    return (True)
                else:
                    stack.append(nei[k])
        return (dfs_recursive(ngbrs))


def dfs(v,ngbrs):
    if visited[v] == False:
        visited[v] = True
        nei = ngbrs[v]
        for k in range(len(nei)):
            stack.append(nei[k])
        return(dfs_recursive(ngbrs)) 
    if visited[v] == True:
        return (False)
        


testCases = int(input(""))
for cases in range(testCases):
    stack = []
    lastPos = 0
    current = 0
    loop = 0
    nm = list(map(int,(input("")).split()))
    v_num = nm[0]
    e_num = nm[1] 
    e = list(map(int,(input("")).split()))
    visited = [False for i in range(v_num)]
    ngbrs = [[] for i in range(nm[0])]
    for i in range(len(e)):
        if i%2 == 0:
            check = ngbrs[e[i]]
            if (e[i] == e[i+1]) or (e[i+1] in check):
                proc = 0
            ngbrs[e[i]].append(e[i+1])
        elif i%2 == 1:
            ngbrs[e[i]].append(e[i-1])
    if proc == 0:
        print (1)
    else:
        for i in range(v_num):
            loop = dfs(i,ngbrs)
            if loop:
                loop = 1
                break
            else:
                loop = 0
                pass
        print (loop)
    