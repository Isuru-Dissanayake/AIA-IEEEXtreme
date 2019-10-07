def solve(ngbrs,v_num,e_num):
    visited = [False] * v_num
    path = []
    stack = []
    def dfs_recursive(ngbrs):
        #print (stack)
        if len(stack) == 0:
            return 
        else:
            current = stack.pop()
            visited[current] = True
            path.append(current)
            nei = ngbrs[current]
            for k in range(len(nei)):
                if not visited[nei[k]]:
                    stack.append(nei[k])
            dfs_recursive(ngbrs)   
    for i in range(v_num):
        if not visited[i]:
            stack.append(i)
            dfs_recursive(ngbrs)
    if len(path) > v_num:
        print (1)
    else:
        print (0)

t = int(input())
for cases in range(t):
    v_num,e_num = list(map(int,input().split()))
    edges = list(map(int,input().split()))
    ngbrs = [[] for i in range(v_num)]
    proc = 1
    for i in range(len(edges)):
        if i%2 == 0:
            check = ngbrs[edges[i]]
            if (edges[i] == edges[i+1]) or (edges[i] in check):
                proc = 0
            ngbrs[edges[i]].append(edges[i+1])
        else:
            ngbrs[edges[i]].append(edges[i-1])
    if proc == 0:
        print (1)
    else:
        solve(ngbrs,v_num,e_num)
		
