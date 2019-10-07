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
for j in range(n):
    a= get_number()
    b= get_number()

    #alis= [int(x) for x in bin(a)[2:]]
    #blis= [int(x) for x in bin(b)[2:]]
    alis= [int(i) for i in list('{0:0b}'.format(a))]
    blis= [int(i) for i in list('{0:0b}'.format(b))]
    path=0
    al=len(alis)
    bl=len(blis)
    if al!= bl:
        path+= abs(al-bl)
        if al>bl:
            alis= alis[:bl]
            q= bl-1
        else:
            blis= blis[:al]
            q= al-1
    else:
        q=al-1
        
    alis=alis[1:]
    blis=blis[1:]
    for i in range(q):
        if alis[i]!= blis[i]:
            path+=(2*(q-i))
            break
    #print(alis, blis,path)
    print(path)