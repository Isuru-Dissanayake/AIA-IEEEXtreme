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

a = get_number()
lis=[]
for i in range(a):
    word= str(input().strip())
    lis.append(word)

    '''
for i in range(a):
    word= lis[i]
    run=1
    for j in range(1,len(word)):
        a=word[:j]
        b=word[j:]
        #print(a,b)
        if a>b:
            run=0
            break

    if run==0:
        print(0,end='')
    else:
        print(1,end='')
'''
def isvalid(wordy):
    
    if len(wordy)==1:
        return True
    else:
        now= wordy[0]
        for i in range(1,len(wordy)):
            if now> wordy[i]:
                run=1
                if not (wordy[i:] >= wordy[:i] and isvalid(wordy[i:]) and isvalid(wordy[:i])):
                    return False
            now= wordy[i]
        return True

for i in lis:
    if isvalid(i):
        print(1,end='')
    else:
        print(0,end='')
#print(isvalid('BABAAB'))