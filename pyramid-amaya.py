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

dynamic=[0,1,2,3,5]
sumi=[0,2,6,12,22]
a = get_number()
if a<len(dynamic):
    print(dynamic[a])
else:
    for i in range(5,a+1):
        #print(i)
        n=i//2
        if i%2==1:
            cost=sumi[n]+1
            dynamic.append(cost)
        else:
            cost=sumi[n-1]+dynamic[n]+1
            dynamic.append(cost)

        sumi.append(sumi[-1]+2*cost)
    print((dynamic[-1])%((10**9)+7))
                
