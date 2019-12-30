class EmptyStackError(Exception):
	pass


# creative way to implement pop_at() - add arg and default value of
# -1 to pop(self, index=-1), and call self.pop(index) from pop_at()
class SetOfStacks:
	def __init__(self, threshold=4):
		self.threshold = threshold
		self.stacks = []

	def push(self, elem):
		if not self.stacks or len(self.stacks[-1]) == self.threshold:
			self.stacks.append([elem])
		else:
			self.stacks[-1].append(elem)

	def pop(self, index=-1):
		if not self.stacks:
			raise EmptyStackError('pop() from an empty stack')

		elem = self.stacks[index].pop()
		if not self.stacks[index]:
			del self.stacks[index]

		return elem

	def pop_at(self, index):
		if index < 0 or index >= len(self.stacks):
			raise IndexError('index out of bounds')

		return self.pop(index)


# Let's test it!
foo = SetOfStacks()
for i in range(10):
	foo.push(i)
print('foo:', foo.stacks)
print('foo.pop():', foo.pop())
print('foo.pop():', foo.pop())
print('foo.pop():', foo.pop())
print('foo:', foo.stacks)
print('foo.pop_at(0):', foo.pop_at(0))
print('foo.pop():', foo.pop())
print('foo:', foo.stacks)
print()

bar = SetOfStacks(2)
print('bar:', bar.stacks)
try:
	print('bar.pop():', end=' ')
	print(bar.pop())
except EmptyStackError as err:
	print(err)
bar.push('a')
bar.push('b')
bar.push('c')
bar.push('d')
bar.push('e')
print('bar:', bar.stacks)
print('bar.pop:', bar.pop())
print('bar.pop:', bar.pop())
print('bar.push: 6\nbar.push: 7')
bar.push(6)
bar.push(7)
print(bar.stacks)
print('bar.pop_at(1):', bar.pop_at(1))
print('bar.pop_at(0):', bar.pop_at(0))
print('bar.pop:', bar.pop())
print(bar.stacks)
print('bar.pop_at(1):', bar.pop_at(1))
print(bar.stacks)
try:
	print('bar.pop_at(1):', end=' ')
	print(bar.pop_at(1)) # raises IndexError exception
except IndexError as err:
	print(err)
