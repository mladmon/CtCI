from enum import Enum
from collections import namedtuple

# algorithms may add to Vertex instances as needed
class Color(Enum):
	WHITE = 1
	GRAY = 2
	BLACK = 3
	RED = 4	


# algorithms may add to Edge instances as needed
class EdgeType(Enum):
	TREE = 1
	BACK = 2
	FORWARD = 3
	CROSS = 4


# Edges are stored in Vertex.adj attribute
# v is the adjacent vertex, w is the weight of the edge (default=1)
Edge = namedtuple('Edge', 'v w', defaults=[1])


# algorithms may add additional attributes as needed (e.g., color, discovered)
class Vertex:
	def __init__(self, key):
		self.key = key
		self.adj = []
		#self.color = Color.WHITE


# Graph is a dictionary of key: Vertex pairs
class Graph:
	def __init__(self, iterable=None):
		if iterable is None:
			self.vertices = {}
		else:
			self.vertices = dict(iterable)


# directed graph from CtCI pg. 106
graph = Graph([(i, Vertex(i)) for i in range(7)])
graph.vertices[0].adj.append(Edge(graph.vertices[1]))
graph.vertices[1].adj.append(Edge(graph.vertices[2]))
edges = [Edge(graph.vertices[0]), Edge(graph.vertices[3])]
graph.vertices[2].adj.extend(edges)
graph.vertices[3].adj.append(Edge(graph.vertices[2]))
graph.vertices[4].adj.append(Edge(graph.vertices[6]))
graph.vertices[5].adj.append(Edge(graph.vertices[4]))
graph.vertices[6].adj.append(Edge(graph.vertices[5]))
