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

def swap(a,b): 
  
    temp=a 
    a=b 
    b=temp 
  
# log(n) solution 
def xnor(a, b): 
      
    # Make sure a is larger 
    if (a < b): 
        swap(a, b) 
  
    if (a == 0 and b == 0) : 
        return 1; 
      
    # for last bit of a 
    a_rem = 0 
      
    # for last bit of b 
    b_rem = 0 
  
    # counter for count bit and  
    #  set bit in xnor num 
    count = 0
      
    # for make new xnor number 
    xnornum = 0 
  
    # for set bits in new xnor 
    # number 
    while (a!=0) : 
      
        # get last bit of a 
        a_rem = a & 1 
          
        # get last bit of b 
        b_rem = b & 1 
  
        # Check if current two  
        # bits are same 
        if (a_rem == b_rem):      
            xnornum |= (1 << count) 
          
        # counter for count bit 
        count=count+1
          
        a = a >> 1
        b = b >> 1
      
    return xnornum; 


def xno(a,b):
    r= [int(k) for k in bin(a^b)[2:]]
    for i in range(len(r)):
        if r[i]==1: r[i]=0
        else: r[i]=1
    print(r)
    return r

n = get_number()
bets=[]
wins=[0]*n
for i in range(n):
    a=input().strip()
    bets.append(int(a,2))
    l= len(a)
    
for i in range(2**l):
    lis=[]
    for j in bets:
        val= sum([int(k) for k in bin(xnor(i,j))[2:]])
        lis.append(val)
    #print(lis)
    if len(list(set(lis)))!=1:
        maxi=max(lis)
        for i in range(len(lis)):
            if lis[i]==maxi:
                wins[i]+=1
#print(bets,wins)
print(min(wins))
    
