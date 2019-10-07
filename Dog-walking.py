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

a = get_number()
for i in range(a):
    ndogs= get_number()
    nwalkers= get_number()
    lis=[]
    for j in range(ndogs):
        lis.append(get_number())
        
    lis.sort()
    cost= lis[-1]-lis[0]
    
    liss=[]
    current= lis[0]
    for j in range(1,ndogs):
        if lis[j]==current:
            liss.append([0,j-1])
            current=lis[j]
            pass
        else:
            liss.append([lis[j]-current,j-1])
            current=lis[j]
            
    liss.sort()
    liss=liss[nwalkers*-1+1:]
    sum=0
    for j in range(len(liss)):
        sum+= liss[j][0]
    print(cost-sum)
