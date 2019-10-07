import math

def solve():
    C, G = [int(i) for i in input().split()]
    gadgets = [[int(i) for i in input().split()] for _ in range(G)]
    sol = [[0] * (C+1) for _ in range(G+1)]
    for i in range(1, G+1):
        for j in range(1, C+1):
            new_j = j - gadgets[i-1][0]
            if new_j < 0:
                sol[i][j] = sol[i-1][j]
                continue
            sol[i][j] = max(sol[i-1][j], gadgets[i-1][1]+sol[i-1][new_j])
    print (sol[-1][-1])



N = int(input())
for _ in range(N):
    solve()
