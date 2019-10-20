n= int(input().strip())

word=''

dist=1
while(len(word)<n):
    word+='Y'
    for i in range(dist):
        word+='y'
        dist+=1
        if len(word)==n:
            break
    
print(word)