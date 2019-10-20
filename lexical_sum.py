n,a,b= list(map(int,input().strip().split()))
if n<a:
    print("NO")
elif n<=b and n>=a:
    print('YES')
    print(n)
else:
    maxes=0
    distribute= n%a
    remain= (b-a)*(n//a)
    incomp=0
    print(distribute,remain)
    while distribute<= remain:
        if incomp!=0:
            distribute-= b-incomp
            maxes+=1
            print('a',maxes)
            maxes+= distribute// (b-a)
            incomp= ((distribute) % (b-a))
            #remain= remain-distribute
            remain-= distribute
            remain-= b-a
            distribute= a
            print(maxes,incomp,remain,distribute)
        else:
            maxes+= distribute// (b-a)
            incomp= ((distribute) % (b-a))
            #remain= remain-distribute
            remain-= distribute
            remain-= b-a
            distribute= a
            print(maxes,incomp,remain,distribute)

    ass= (n-maxes*b-incomp)//a
    print(ass, maxes, incomp)
    print('YES')
    ar=[a]*ass
    if incomp!=0:
        ar.append(incomp)
    ar+=[b]*maxes
    print(ar)