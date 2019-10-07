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



################### another solution





def find_anc(k):
    anc = []
    t = k
    anc.append(t)
    while t>1:
        t = int(t/2)
        anc.append(t)
    return (anc)
t = int(input())
for cases in range(t):
    n,m = list(map(int,input().split()))
    if n == m:
        print (0)
    else:
        n_anc = find_anc(n)
        m_anc = find_anc(m)
        n_len = len(n_anc)
        m_len = len(m_anc)
        if n_len < m_len:
            n_new_anc = n_anc
            m_new_anc = m_anc[-n_len:]
        else:
            m_new_anc = m_anc
            n_new_anc = n_anc[-m_len:]
        indx = len(n_new_anc)
        for i in range(len(n_new_anc)):
            if n_new_anc[i] == m_new_anc[i]:
                indx = i
                break
        dist = n_len + m_len - 2*(len(n_new_anc) - indx)
        print (dist)
        '''
        indx = len(n_anc)
        for i in range(len(n_anc)):
            if n_anc[i] in m_anc:
                indx = i
                break
        dist = len(n_anc) + len(m_anc) - 2*(len(n_anc) - indx)
        print (dist)
        '''
