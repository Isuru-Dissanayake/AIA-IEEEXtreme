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

t = get_number()
arr=[]
for i in range(t):
    data= list(map(int,input().strip().split()))
    arr.append(data)
    
arr= np.array(arr)
arr= arr[arr[:,1].argsort()]
#print(arr)

dynamic=[]
dynamic.append([arr[0][2],arr[0][2]])
#print(dynamic)
maxi= arr[0][2]
for i in range(1,t):
    run=0
    #print(dynamic)
    for j in range(i):
        if arr[i-j-1][1]<arr[i][0]:
            #print(i,j)
            run=1
            dynamic.append([arr[i][2]+dynamic[i-j-1][1]])
            #print(dynamic)
            break
    if run==0:
        dynamic.append([arr[i][2]])
    if maxi< dynamic[i][0]:
        maxi= dynamic[i][0]
    dynamic[i].append(maxi)

#print(dynamic)
print(dynamic[-1][1])

