
def isSubSequence(string1, string2, m, n):
    if m == 0:    return 0
    if n == 0:    return m
  
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1) 
  
    return isSubSequence(string1, string2, m, n-1)


print(4-isSubSequence('ntac','naramatac',4,9))