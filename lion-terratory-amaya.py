'''# a simple parser for python. use get_number() and get_word() to read
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
import numpy
import scipy

rown = get_number()
coln = get_number()
lionn= get_number()

arr=[]
ar= list(map(int,input().strip().split(' ')))+[0]
arr.append(ar)
for i in range(1,lionn):
    ar=list(map(int,input().strip().split(' ')))+[0]
    for j in range(len(arr)):
        if (abs(arr[j][0]-ar[0])+abs(arr[j][1]-ar[1])<= arr[j][2]+ar[2]):
            arr[j][3]+=1
            ar[3]+=1
        arr.append(ar)
        
maxi=[0,0]
for i in range(lionn):
    if arr[i][3]>maxi[1]:
        maxi[1]= arr[i][3]
        maxi[0]= i

print(maxi[0],maxi[1])
'''
import numpy as np

def fillSavanah(x,y,d):
    savanah[y][x]+=1
    xdev=1
    while xdev<d+1: #for xdev in range(1,d+1):
        if x+xdev<coln:
            savanah[y][x+xdev]+=1
        if x-xdev>=0:
            savanah[y][x-xdev]+=1
        if y+xdev<rown:
            savanah[y+xdev][x]+=1
        if y-xdev>=0:
            savanah[y-xdev][x]+=1
            
        ydev=1
        while ydev<d+1: #for ydev in range(1,d+1):
            if xdev+ydev<=d :
                if x+xdev<coln:
                    if y+ydev<rown:
                        savanah[y+ydev][x+xdev]+=1
                    if y-ydev>=0:
                        savanah[y-ydev][x+xdev]+=1
                if xdev!=0:
                    if x-xdev>=0:
                        if y+ydev<rown:
                            savanah[y+ydev][x-xdev]+=1
                        if y-ydev>=0:
                            savanah[y-ydev][x-xdev]+=1
            ydev+=1
        xdev+=1



rown=5
coln=4
savanah= np.zeros((5,4),dtype=int)
fillSavanah(0,1,3)
print(savanah)