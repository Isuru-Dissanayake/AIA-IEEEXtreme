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

n = get_number()
k = get_number()
nums= list(map(int,input().strip().split()))

def find_gcd(x, y): 
      
    while(y): 
        x, y = y, x % y 
      
    return x 
          
lis=[]          
for i in range(1,k+1):
    #print(i)
    for j in range(n-i+1):
        #print(j)
        #print(i)
        l = nums[j:j+i] 
        
        #print(l)
        if len(l)>1:
            num1 = l[0] 
            num2 = l[1] 
            gcd = find_gcd(num1, num2) 
              
            for k in range(2, len(l)): 
                gcd = find_gcd(gcd, l[k]) 
                  
            lis.append(gcd)
        else:
            lis.append(l[0])

lis=list(set(lis))
print(len(lis))