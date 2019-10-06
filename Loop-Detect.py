# Python Program to detect cycle in an undirected graph 

from collections import defaultdict 

#This class represents a undirected graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 


	# function to add an edge to graph 
	def addEdge(self,v,w): 
		self.graph[v].append(w) #Add w to v_s list 
		self.graph[w].append(v) #Add v to w_s list 

	# A recursive function that uses visited[] and parent to detect 
	# cycle in subgraph reachable from vertex v. 
	def isCyclicUtil(self,v,visited,parent): 

		#Mark the current node as visited 
		visited[v]= True

		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			# If the node is not visited then recurse on it 
			if visited[i]==False : 
				if(self.isCyclicUtil(i,visited,v)): 
					return True
			# If an adjacent vertex is visited and not parent of current vertex, 
			# then there is a cycle 
			elif parent!=i: 
				return True
		
		return False
		

	#Returns true if the graph contains a cycle, else false. 
	def isCyclic(self): 
		# Mark all the vertices as not visited 
		visited =[False]*(self.V) 
		# Call the recursive helper function to detect cycle in different 
		#DFS trees 
		for i in range(self.V): 
			if visited[i] ==False: #Don't recur for u if it is already visited 
				if(self.isCyclicUtil(i,visited,-1))== True: 
					return True
		
		return False

t = int(input())
proc = 1
for testCases in range(t):
    v_num, e_num = list(map(int,(input("")).split()))
    edges = list(map(int,(input("")).split()))
    e = edges
    visited = [False for i in range(v_num)]
    ngbrs = [[] for i in range(v_num)]
    for i in range(len(e)):
        if i%2 == 0:
            check = ngbrs[e[i]]
            if (e[i] == e[i+1]) or (e[i+1] in check):
                proc = 0
            ngbrs[e[i]].append(e[i+1])
        elif i%2 == 1:
            ngbrs[e[i]].append(e[i-1])
    if proc == 0:
        print (1)
    else:
        g = Graph(v_num)
        i = 0
        while i<e_num:
            g.addEdge(edges[i],edges[i+1])
            i += 2
        if g.isCyclic(): 
            print (1)
        else : 
            print (0)