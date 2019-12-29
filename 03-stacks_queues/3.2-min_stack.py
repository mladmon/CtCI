from collections import namedtuple

Pair = namedtuple('Pair', 'elem min')


# methods pop() and min() return None when called on an empty MinStack
class MinStack:
	def __init__(self):
		self.data = []

	def push(self, elem):
		if not self.data or elem < self.data[-1].min:
			self.data.append(Pair(elem, elem))
		else:
			self.data.append(Pair(elem, self.data[-1].min))

	def pop(self):
		if not self.data:
			return None

		return self.data.pop().elem
	
	def min(self):
		if not self.data:
			return None

		return self.data[-1].min


def print_stack(stack):
	print('[', end=' ')
	for pair in stack.data:
		print(pair, end=' ')
	print(']')


# Let's test it!
foo = MinStack()
foo.push(5)
foo.push(13)
foo.push(3)

print('foo:', end=' ')
print_stack(foo)
print('foo.min():', foo.min())
print('foo.pop():', foo.pop())
print('foo.min():', foo.min())
print('foo.pop():', foo.pop())
print('foo.min():', foo.min())
print('foo.pop():', foo.pop())
print('foo.min():', foo.min()) # None
print()

print('bar:', end=' ')
bar = MinStack()
bar.push('r')
bar.push('l')
bar.push('z')
bar.push('x')
bar.push('a')
bar.push('r')
print_stack(bar)
