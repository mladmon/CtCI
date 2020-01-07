from enum import Enum
from collections import deque

class CycleDetectedError(Exception):
	pass


class Color(Enum):
	WHITE = 1
	GRAY = 2
	BLACK = 3


class Node:
	def __init__(self, key):
		self.key = key
		self.color = Color.WHITE
		self.adj = []


def create_graph(vertices, edges):
	for vertex in vertices.values():
		vertex.color = Color.WHITE

	for edge in edges:
		vertices[edge[0]].adj.append(vertices[edge[1]])


def dfs(u, build_order):
	#print(u.key, u.color)
	u.color = Color.GRAY
	for v in u.adj:
		#print('  ', v.key, v.color)
		if v.color == Color.GRAY:
			raise CycleDetectedError('not a dag')
		elif v.color == Color.WHITE:
			dfs(v, build_order)

	u.color = Color.BLACK
	build_order.appendleft(u.key)


def topological_sort(vertices):
	build_order = deque()
	for vertex in vertices.values():
		#print(vertex.key, vertex.color)
		if vertex.color == Color.WHITE:
			dfs(vertex, build_order)

	return build_order


# O(V + E) runtime, O(V) space - recursion depth of DFS is O(V)
def find_build_order(projects, dependencies):
	create_graph(projects, dependencies)
	return topological_sort(projects)


# Let's test it!
projects = {chr(i) : Node(chr(i)) for i in range(ord('a'), ord('f') + 1)}
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
build_order = find_build_order(projects, dependencies)

print('projects: a b c d e f')
print('build order:', end=' ')
for project in build_order:
	print(project, end=' ')
print()

