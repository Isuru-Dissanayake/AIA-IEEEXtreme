import numpy as np

n=int(input().strip())
tree= {}
for i in range(n+1):
    tree[i]=[[],[]]
for j in range(n-1):
    a,b,c= list(map(int,input().strip().split(' ')))
    tree[a][0].append(b)
    tree[b][0].append(a)
    tree[a][1].append(c)
    tree[b][1].append(c)
    #tree[a][b]= c
    #tree[b][a]=c

val=0
for i in range(1,n):
    stack=[]
    #for j in range(1,n+1):
    #    if tree[i][j]>0:
    for j in range(len(tree[i][0])):
        stack.append([tree[i][0][j],tree[i][1][j],i])
    #print(stack)
    while len(stack)!=0:
        #print(stack)
        current= stack.pop(-1)
        now= current[0]
        run=0
        #for j in range(1,n+1):
        for j in range(len(tree[now][0])):
            if tree[now][0][j]!= current[2]:
                run=1
                if tree[now][1][j]>current[1]:
                    stack.append([tree[now][0][j],tree[now][1][j],current[0]])
                else:
                    stack.append([tree[now][0][j],current[1],current[0]])

        if i<current[0]:
            val+= current[1]
            #print(current[1])

    #print('NEXT')
    
print(val)