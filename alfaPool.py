arr=[1,3,15,31,63,127,255,511,1023,2047,4095,8191,24575,57343]
from itertools import combinations 
import math
  
t= int(input())
for j in range(t):
    num= int(input())
    count=0
    count+=1
    for k in range(14):
        if arr[k]>num:
            break
    myarr=arr[:k]
    for k in range(1,len(myarr)+1):
        comb = list(combinations(myarr, k) )
        print(comb)
        for l in comb:
            if not l[0]==1:
                if sum(l)<=num:
                    for u in range(1,num//l[0]):
                        if l[0]*u<num:
                            count+= math.factorial(num-u*l[0]+1)/(math.factorial(u)*math.factorial(num-u*l[0]))

    print(count)