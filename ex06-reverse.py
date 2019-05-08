def reverse(arr):
	i = 0
	n = len(arr)
	while i < (n//2):
		arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
		i += 1

a = input('Enter a positive integer: ')
a = list(range(int(a)))

print(a)
reverse(a)
print(a)
