
graph = {
	
	"A": ["B","C"],
	"B": ["A","C","D"],
	"C": ["A","B","D","E"],
	"D": ["B","E","C","F"],
	"E": ["C","D"],
	"F": ["D"]
}

# Breath_first_search

def BFS(graph, start):
	queue = []
	queue.append(start)
	saw = set()
	saw.add(start)

	while len(queue)>0 :  
		now_node = queue.pop(0)
		next_nodes = graph[now_node]
		for i in next_nodes:
			if i not in saw:
				queue.append(i)
				saw.add(i)
		print now_node,

#Depth_first_search
def DFS(graph, start):
	queue = []
	queue.append(start)
	saw = set()
	saw.add(start)

	while len(queue)>0 :  
		now_node = queue.pop()
		next_nodes = graph[now_node]
		for i in next_nodes:
			if i not in saw:
				queue.append(i)
				saw.add(i)
		print now_node,


BFS(graph,"A"), DFS(graph,"A")
print
BFS(graph,"B")
print
BFS(graph,"C")
print
BFS(graph,"D")
print
BFS(graph,"E")
print
BFS(graph,"F")
