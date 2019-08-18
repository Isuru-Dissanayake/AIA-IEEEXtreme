#https://www.hackerrank.com/challenges/maxsubarray/problem

for q in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    max_sum = -99999999
    c_sum = 0
    sum1 = 0
    for i in range(n):
        sum1+=array[i]
        if array[i]>0:
            c_sum += array[i]
        if sum1>max_sum:
            max_sum = sum1
        if sum1<0:
            sum1 = 0
    if c_sum == 0:
        c_sum = max(array)
    print (max_sum,c_sum)