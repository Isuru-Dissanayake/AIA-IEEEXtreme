#https://csacademy.com/ieeextreme-practice/task/96c8b1313edd72abf600facb0a14dbab/

T = int(input())
for t in range(T):
    val1 = 1
    val2 = 1
    N = int(input())
    for i in range(N - 1):
        val = val1 + val2
        val1 = val2
        val2 = val
    print (val2)