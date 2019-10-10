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
import math
import sys
np.set_printoptions(threshold=sys.maxsize)

array= np.zeros((30,30),dtype=int)
n=30

def putmask():
    y,x = np.ogrid[-a:n-a, -b:n-b]
    
    yd= y*math.cos(angle)-x*math.sin(angle)
    xd= x*math.cos(angle)+y*math.sin(angle)
    
    mask = (xd*xd)/a2 + (yd*yd)/b2 <= 1
    array[mask] = 1



t = get_number()
for i in range(t):
    u= get_number()
    for j in range(u):
        x1,y1,x2,y2,r= list(map(int,input().strip().split(' ')))
        if x1==x2:
            angle= math.pi/2
        else:
            angle= math.atan(abs(y1-y2)/abs(x1-x2))
        if y2>y1:
            angle= angle*-1
        a2= r*r/4
        c= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)/2
        c2=c*c
        b2= a2-c2
        a= (y1+y2)/2
        b= (x1+x2)/2
        putmask()
        print(array)
    sumu= sum(sum(x) for x in array)
    print(sumu)
    print((sumu/(n*n))*100)