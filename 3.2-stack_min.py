from collections import namedtuple

Node = namedtuple('Node', 'val min')

class Stack:
	def __init__(self):
		self.data = []

	def push(self, val):
		if not self.data or self.data[-1].min > val:
			self.data.append(Node(val, val))
		else:
			self.data.append(Node(val, self.data[-1].min))

	def pop(self):
		if self.data:
			return self.data.pop().val
		else:
			return None
	
	def min(self):
		if self.data:
			return self.data[-1].min
		else:
			return None

# Let's test it!
s = Stack()
s.push(3)
s.push(7)
print('[3, 7]')
print('min:', s.min())
s.push(11)
s.push(2)
print('[3, 7, 11, 2]')
print('min:', s.min())
print('s.pop():', s.pop())
print('min:', s.min())
s.push(6)
s.push(-1)
print('[3, 7, 11, 6, -1]')
print('min:', s.min())
for i in range(len(s.data)):
	s.pop()
print('[]')
print('min:', repr(s.min()))
s.push(2)
print('[2]')
print('min:', s.min())
