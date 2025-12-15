from queue import Queue
graph={
'a':['b','d'],
'b':['c','e'],
'c':['d','f'],
'd':[],
'e':['a'],
'f':[]
}
visited={}
parent={}
queue=Queue()
for node in graph.keys():
	visited[node]=False
	parent[node]=None
s=input("enter source node")
visited[s]=True
queue.put(s)
while not queue.empty():
	u=queue.get();
	for v in graph[u]:
		if not visited[v]:
			visited[v]=True
			parent[v]=u
			queue.put(v)
v=input("enter destination ")
path=[]
while v is not None:
	path.append(v)
	v=parent[v]
path.reverse()
print(path)