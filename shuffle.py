def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import numpy as np
import scipy

a = get_number()
bpGraph= np.ones([a, a], dtype = int) 
for i in range(a):
    b = input().split(' ')
    bpGraph[i][i]=0
    for j in b:
        bpGraph[i][int(j)]=0
        

  
class GFG: 
    def __init__(self,graph): 
        
        self.graph = graph  
        self.ppl = len(graph) 
        self.jobs = len(graph[0]) 
  
    def bpm(self, u, matchR, seen): 
  
        for v in range(self.jobs): 
  
            if self.graph[u][v] and seen[v] == False: 
                  
                seen[v] = True 
  
                if matchR[v] == -1 or self.bpm(matchR[v],  
                                               matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
  
    def maxBPM(self): 
        matchR = [-1] * self.jobs 
          
        result = 0 
        for i in range(self.ppl): 
              
            seen = [False] * self.jobs 
              
            if self.bpm(i, matchR, seen): 
                result += 1
        return result 
  
  

  
g = GFG(bpGraph) 
  
print (a- g.maxBPM()) 
  