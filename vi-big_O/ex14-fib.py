# returns the nth fibonacci number
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)

# prints the first n terms of the fibonacci sequence
def print_fib(n):
	for i in range(0, n+1):
		print(fib(i), end=' ')
	print()

num = input('Enter a positive integer: ')
print_fib(int(num))

fn = input("Enter a fibonacci number you'd like to know: ")
print('F{0} is'.format(fn), fib(int(fn)))
