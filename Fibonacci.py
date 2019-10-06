def fibonacci(n):
    gold = 1.618033988
    fib = int(((gold**(n+1))/(5**0.5)) + 0.5)
    #print (fib)
    return(fib)

t = int(input())
for testCases in range(t):
    n = int(input())
    print (fibonacci(n)%10)
