import numpy as np

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.val= None
        self.right = None
        self.left = None

n = int(input())
arr = list(map(int,input().strip().split()))

root= Node(0)
root.val= arr[0]
print(1)
for i in range(1,len(arr)):
    root= Node(0)
    root.val= arr[0]
    yes= True
    rec=1
    while yes==True:
        if root.val>arr[i]:
            if root.right==None:
                root.right= Node(i)
                root.right.val=arr[i]
                yes=False
                rec+=1
            else:
                root= root.right
                
        elif root.val <= arr[i]:
            if root.left==None:
                root.left= Node(i)
                root.left.val= arr[i]
                yes= False
                rec+=1
            else:
                root= root.left

    print(rec)      
            
for i in range(3):
    print(Node(i).val)
'''
for i in range(len(arr)):
    lis=[]
    lis.append(arr[i])
    lis.append(i)
    lis.append(1)
    listy.append(lis)
depths= np.zeros(n)   
while len(listy)>0:
    now= listy.pop(0)
    rn= now.pop(0)
    depths[rn[1]]=rn[2]
    
    if len(now)==0:
        pass
    else:
'''        
        