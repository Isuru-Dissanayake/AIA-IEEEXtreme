#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    dp=[[0,0]]
    for i in range(1,len(B)):
        k=[abs(B[i-1]-1)+dp[i-1][1],max(abs(B[i]-1)+dp[i-1][0],abs(B[i]-B[i-1])+dp[i-1][1])]
        dp.append(k)

    return(max(dp[len(B)-1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')
        #print(str(result) + '\n')

    fptr.close()
