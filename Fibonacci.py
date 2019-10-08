fib1 = 0
fib2 = 1 

def fib(num):
    global fib1
    global fib2
    limit = max(num)
    counter = 0
    fibn = fib2
    fib_list = {}
    while counter < limit:
        fibn = fib1 + fib2
        fib1 = fib2
        fib2 = fibn
        if counter+1 in num:
            fib_list[counter+1] = fibn
        counter+=1
    for i in range(len(num)):
        print (fib_list[num[i]]%10)

t = int(input())
num = []
for testCases in range(t):
    n = int(input())
    num.append(n)
fib(num)


