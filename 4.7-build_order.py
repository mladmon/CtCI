from enum import Enum
from collections import deque

class Color(Enum):
	WHITE = 1
	GRAY = 2
	BLACK = 3

class Node:
	def __init__(self, key):
		self.key = key
		self.color = Color.WHITE
		self.adj = []

class CycleDetectedError(Exception):
	pass

def build_order(projects, dependencies):
	init(projects, dependencies)
	return topological_sort(projects)

def init(vertices, edges):
	for v in vertices.values():
		v.color = Color.WHITE
	for e in edges:
		vertices[e[1]].adj.append(vertices[e[0]])

def topological_sort(vertices):
	order = deque()
	for v in vertices.values():
		print(v.key, v.color)
		if v.color == Color.WHITE:
			v.color = Color.GRAY
			dfs_visit(v, order)
	return order

def dfs_visit(v, order):
	print(v.key, v.color)
	for other in v.adj:
		print('  ', other.key, other.color)
		if other.color == Color.GRAY:
			raise CycleDetectedError('not a dag')
		if other.color == Color.WHITE:
			other.color = Color.GRAY
			dfs_visit(other, order)
	v.color = Color.BLACK
	order.append(v.key) # topo sort: appendleft(); prob. wants opp. order

# Let's test it!
projects = {chr(i) : Node(chr(i)) for i in range(ord('a'), ord('f') + 1)}
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
order = build_order(projects, dependencies)
for project in order:
	print(project, end=' ')
print() 
