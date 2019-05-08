from collections import deque

def bfs(graph, s):
	discovered = {s}				# or set([s]), which is not as nice
	queue = deque([s])
	while queue:
		u = queue.popleft()
		print(u, end=' ')
		for v in graph[u]:
			if v not in discovered:
				discovered.add(v)
				queue.append(v)
	print()

# let's test it!
graph = {
	'a': ['b', 'f', 'h'],
	'b': ['a', 'd', 'c'],
	'c': ['b', 'f', 'e'],
	'd': ['b'],
	'e': ['c', 'g'],
	'f': ['a', 'c'],
	'g': ['h', 'e'],
	'h': ['a', 'g']
}

bfs(graph, 'a')
