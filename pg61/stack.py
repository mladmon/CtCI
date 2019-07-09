class Stack:
	def __init__(self, data=[]):
		self.data = data

	def push(self, obj):
		self.data.append(obj)

	def pop(self):
		return self.data.pop()

# oops! the above is incorrect

class Stack2:
	def __init__(self, data=None):
		if data is None:
			self.data = []
		else:
			self.data = list(data)

	def push(self, obj):
		self.data.append(obj)
	
	def pop(self):
		return self.data.pop()

