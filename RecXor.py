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

t = get_number()
for i in range(t):
    l = get_number()
    h = get_number()
    n = get_number()
    d1 = get_number()
    d2 = get_number()
    
    
    if ((d1-n)%l+1 > (d2-n)%l+1):
        L= ((d1-n)%l+1) - ((d2-n)%l+1)
        X= d1-L
        Y= d2+L
    else:
        L= ((d2-n)%l+1) - ((d1-n)%l+1)
        X= d1
        Y= d2
    
    
    x1= (X-n)%l
    y1= int((X-n)/l)
    x2=  (Y-n)%l
    y2=  int((Y-n)/l)
    
    
    a= np.arange(n, n+l*h).reshape(h,l)
    c= a[:y1,:].flatten()
    d= a[y2+1:,:].flatten()
    e= a[y1:y2+1,:x1].flatten()
    f= a[y1:y2+1,x2+1:].flatten()
    
    a= np.concatenate((c, d,e,f), axis=None)
    
    if len(a)==0:
        xor=0
    else:
        xor= a[0]
        for j in range(1,len(a)):
            xor= xor^a[j]
    print(xor)
    