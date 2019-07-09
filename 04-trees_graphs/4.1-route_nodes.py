from data_structs import *
from collections import deque

def route_bet_nodes(graph, n1, n2):
	init(graph)
	if not bfs(n1, n2):
		init(graph)
		return bfs(n2, n1)
	return True

def bfs(n1, n2):
	n1.disc = True
	queue = deque([n1])
	while queue:
		u = queue.popleft()
		if u is n2:
			return True
		for edge in u.adj:
			if not edge.v.disc:
				edge.v.disc = True
				queue.append(edge.v)
	return False

def init(graph):
	for v in graph.vertices.values():
		v.disc = False

# Let's test it!
print('see CtCI pg. 106 for graph used')
print('(0, 1):', route_bet_nodes(graph, graph.vertices[0], graph.vertices[1]))
print('(1, 0):', route_bet_nodes(graph, graph.vertices[1], graph.vertices[0]))
print('(3, 1):', route_bet_nodes(graph, graph.vertices[3], graph.vertices[1]))
print('(1, 4):', route_bet_nodes(graph, graph.vertices[1], graph.vertices[4]))
print('(3, 2):', route_bet_nodes(graph, graph.vertices[3], graph.vertices[2]))
print('(6, 3):', route_bet_nodes(graph, graph.vertices[6], graph.vertices[3]))
