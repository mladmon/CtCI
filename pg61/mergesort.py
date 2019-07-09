def merge(arr, p, q, r):
	l_index = p
	r_index = q + 1
	result = []
	n = r-p + 1
	while n > 0:
		if l_index > q:
			result.append(arr[r_index])
			r_index += 1
		elif r_index > r:
			result.append(arr[l_index])
			l_index += 1
		else:
			if arr[l_index] < arr[r_index]:
				result.append(arr[l_index])
				l_index += 1
			else:
				result.append(arr[r_index])
				r_index += 1
		n -= 1
	arr[p:r+1] = result

def mergesort(arr, p, r):
	if r > p:
		mid = (p+r) // 2
		mergesort(arr, p, mid)
		mergesort(arr, mid+1, r)
		merge(arr, p, mid, r)

# let's test it!
a = [31, -4, 0, 7, 8, 4, 55, 13, 7, 21, 8]
b = a[:-1]

print(a)
mergesort(a, 0, len(a)-1)
print(a)

print(b)
mergesort(b, 0, len(b)-1)
print(b)
