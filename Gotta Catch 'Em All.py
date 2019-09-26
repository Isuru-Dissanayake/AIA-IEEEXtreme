def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import numpy as np
import scipy

a = get_number()
b = get_number()

def left(i,j):
    if ((j-1)<0):
        return False
    return True
    
def top(i,j):
    if ((i-1)<0):
        return False
    return True
    
forest= np.zeros((a,b),dtype=int)
dynamic =np.zeros((a,b),dtype=int)
direction =np.zeros((a,b),dtype=int)

for i in range(a):
    for j in range(b):
        forest[i][j]= get_number()
        
dynamic[0][0]= forest[0][0]

for i in range(a):
    for j in range(b):
        if left(i,j):
            if top(i,j):
                dynamic[i][j]= forest[i][j]+max(dynamic[i-1][j],dynamic[i][j-1])
                if (dynamic[i-1][j]>dynamic[i][j-1]):
                    direction[i][j]= 1
                else:
                    direction[i][j]= 2
            else:
                dynamic[i][j]= forest[i][j]+ dynamic[i][j-1]
                direction[i][j]= 2
        else:
            if top(i,j):
                dynamic[i][j]= forest[i][j]+ dynamic[i-1][j]
                direction[i][j]= 1
            else:
                dynamic[i][j]= forest[i][j]
                
                
if dynamic[a-1][b-1]<0:
    health= (dynamic[a-1][b-1]*-1)+1
else:
    health=1
    
minimum=1
for i in range(a):
    for j in range(b):
        if left(i,j):
            if top(i,j):
                dynamic[i][j]= forest[i][j]+max(dynamic[i-1][j],dynamic[i][j-1])
            else:
                dynamic[i][j]= forest[i][j]+ dynamic[i][j-1]
        else:
            if top(i,j):
                dynamic[i][j]= forest[i][j]+ dynamic[i-1][j]
            else:
                dynamic[i][j]= forest[i][j]+health
    
i=a-1
j=b-1

while(i!=0 or j!=0):
    if(dynamic[i][j]<minimum):
        minimum= dynamic[i][j]
    if(direction[i][j]==2):
        j=j-1
    elif (direction[i][j]==1):
        i=i-1
        
if minimum!=1:
    health= health+ (minimum*-1)+1
    
print(health)