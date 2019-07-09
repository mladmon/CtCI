def quicksort(arr, p, r):
	if p < r:
		q = partition(arr, p, r)
		quicksort(arr, p, q - 1)
		quicksort(arr, q + 1, r)

def partition(arr, p, r):
	pivot = arr[r]
	lt_index = p - 1
	for i in range(p, r):
		if arr[i] < pivot:
			lt_index += 1
			arr[lt_index], arr[i] = arr[i], arr[lt_index] # Python! :D
	arr[lt_index + 1], arr[r] = arr[r], arr[lt_index + 1]
	return lt_index + 1


# Let's test it!
foo = [3, 7, 2, 16, 19, 18, 1, 12]
print(foo)
quicksort(foo, 0, len(foo) - 1)
print(foo)

bar = [6, 2, 3, 4, 7, 1, 8, 5]
print(bar)
quicksort(bar, 0, len(bar) - 1)
print(bar)
