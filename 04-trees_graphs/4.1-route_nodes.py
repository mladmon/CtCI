from data_structs import *
from collections import deque

# O(V+E) runtime, O(V) space - use BFS to see if dest is reachable
def route_bet_nodes(graph, source, dest):
	init(graph)
	return bfs(source, dest)


def bfs(source, dest):
	source.discovered = True
	queue = deque([source])
	while queue:
		u = queue.popleft()
		if u is dest:
			return True

		for edge in u.adj:
			if not edge.v.discovered:
				edge.v.discovered = True
				queue.append(edge.v)

	return False


def init(graph):
	for v in graph.vertices.values():
		v.discovered = False


# Let's test it
print('(0, 1):', route_bet_nodes(graph, graph.vertices[0], graph.vertices[1]))
print('(1, 0):', route_bet_nodes(graph, graph.vertices[1], graph.vertices[0]))
print('(3, 1):', route_bet_nodes(graph, graph.vertices[3], graph.vertices[1]))
print('(1, 4):', route_bet_nodes(graph, graph.vertices[1], graph.vertices[4]))
print('(3, 2):', route_bet_nodes(graph, graph.vertices[3], graph.vertices[2]))
print('(6, 3):', route_bet_nodes(graph, graph.vertices[6], graph.vertices[3]))
