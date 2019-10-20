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
for i in range(a):
    word= str(input())
    letters=['A','B','C','D']
    arr=[0,0,0,0]
    for j in range(len(word)):
        if word[j]=='A': arr[0]+=1
        elif word[j]=='B': arr[1]+=1
        elif word[j]=='C': arr[2]+=1
        elif word[j]=='D': arr[3]+=1
    #print(arr)
    num=[]
    for j in range(4):
        if arr[j]!=0:
            num.append(j)
    word2=''
    #print(num)
    for j in range(len(num)):
        word2+= letters[num[j]]*arr[num[j]]
    #print (word2)

    newword=''
    newword+=word
    newword+=word

    val=len(word)
    for k in range(1,2*len(word)-4):
        
        wordy= newword[k:k+len(word)]
        if len(wordy)!=len(word):
            break
        count=0
        #print(wordy)
        for l in range(len(word)):
            if word2[l]!= wordy[l]:
                count+=1
        #print(count)
        if count<val:
            val=count

    print(val)