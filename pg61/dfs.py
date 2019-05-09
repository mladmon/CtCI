def dfs(graph, s):
	visited, stack = set(), [s]
	while stack:
		u = stack.pop()
		if u not in visited:
			visited.add(u)
			print(u, end=' ')
			for v in reversed(graph[u]): # for left-to-right traversal
				if v not in visited: # less duplicates pushed onto stack :D
					stack.append(v)
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

dfs(graph, 'a')

