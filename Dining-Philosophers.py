#p, q, r = list(map(int,input("").split()))
#arr = list(map(int,input("").split()))
#rArr = arr + arr + arr
#sortArr = sorted(arr)
#for i in range(r-1,p):
#    num = sortArr[i]
#    lArr = sortArr[:i]
#   ind = p + arr.index(num)
#    check = rArr[ind-q+1:ind+q]
#    mx = max(check)
#    mn = 0
#    for j in range(r):
#        mn = min(check)
#        check[check.index(min(check))] = mx
    #print (mn)
#    if mn == num:
#        print (num)

# Python3 program to find the number  
# of subsequences with gcd 1  
  
MAX = 1000
  
def gcd(a, b):  
    if (a == 0): 
        return b  
    return gcd(b % a, a) 
  
# Recursive function to calculate the  
# number of subsequences with gcd 1  
# starting with particular index  
def func(ind, g, dp, n, a): 
  
    # Base case  
    if (ind == n):  
        if (g == 1):  
            return 1
        else: 
            return 0
  
    # If already visited  
    if (dp[ind][g] != -1):  
        return dp[ind][g]  
  
    # Either we take or we do not  
    ans = (func(ind + 1, g, dp, n, a) + 
           func(ind + 1, gcd(a[ind], g),  
                             dp, n, a))  
  
    # Return the answer  
    dp[ind][g] = ans 
    return dp[ind][g] 
  
# Function to return the number  
# of subsequences  
def countSubsequences(a, n):  
  
    # Hash table to memoize  
    dp = [[-1 for i in range(MAX)]  
              for i in range(n)]  
  
    # Count the number of subsequences  
    count = 0
  
    # Count for every subsequence  
    for i in range(n):  
        count += func(i + 1, a[i], dp, n, a)  
  
    return count  
  
# Driver Code  
a = list(map(int,input().split())) 
n = len(a) 
print(countSubsequences(a, n))  


    
