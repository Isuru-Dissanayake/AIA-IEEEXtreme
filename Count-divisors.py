#https://www.hackerrank.com/contests/moraxtreme3-0/challenges/count-divisors-1-1

t = int(input(""))
for testCases in range(t):
    n = str(input(""))
    num = [int(i) for i in n]
    n = int(n)
    ans = 0
    for i in range(len(num)):
        if num[i] != 0:
            if n%num[i] ==0:
                ans +=1
    print (ans)