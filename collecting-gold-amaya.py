# a simple parser for python. use get_number() and get_word() to read
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

# numpy and scipy are available for use
import numpy as np
import scipy

ncities = get_number()
npaths = get_number()
cities={}
current=0
for i in range(ncities):
    city=get_number()
    cities[city]=current
    current+=1
maxi=cities[max(cities)]
mini=cities[min(cities)]

paths= np.zeros((ncities,ncities),dtype=int)
for i in range(npaths):
    x= cities[get_number()]
    y= cities[get_number()]
    dist= get_number()
    paths[x][y]=dist
    paths[y][x]= dist
print(cities)
print(paths,mini,maxi)
dijkis=np.zeros((ncities))
queue=[]
queue.append(mini)
while queue:
    now=queue.pop(0)
    for j in range(ncities):
        if paths[now][j]>0 and j!=mini:
            if dijkis[j]==0 or dijkis[j]> dijkis[now]+paths[now][j]:
                dijkis[j]= dijkis[now]+paths[now][j]
                queue.append(j)
                
print(dijkis)