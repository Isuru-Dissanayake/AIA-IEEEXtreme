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
import numpy
import scipy
import math
t = get_number()
for i in range(t):
    b,x= list(map(int,input().strip().split(' ')))
    x+=1
    powe=1
    sumi=0
    while sumi<x:
        sumi+= (b**powe)*powe
        powe+=1
       
    sumi-= (b**(powe-1))*(powe-1)
    powe=powe-1
    print(sumi,powe)
    now= x-sumi
    objct= (now//powe)+1
    letter= now%powe 
    if letter==0:
        objct-=1
        letter=powe

    print(objct,letter,powe)

    for j in range(letter):
        ans=math.ceil(objct/b**(powe-1))
        objct= objct%(b**(powe-1))
        powe-=1
    print(ans)