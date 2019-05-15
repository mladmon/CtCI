# python str methods make this problem very easy
def urlify(string):
	return string.rstrip().replace(' ', '%20')

# the way the problem intended us to do it...
def urlify_not_the_python_way(string, n):
	result = list(string)
	num_spaces = 0
	for i in range(n):
		if result[i] is ' ':
			num_spaces += 1
	last_space = n
	for i in reversed(range(n)):
		if num_spaces is 0:
			break
		if result[i] is ' ':
			for j in reversed(range(i+1, last_space)):
				result[j + num_spaces*2] = result[j]
			result[i + num_spaces*2] = '0'
			result[i + num_spaces*2 - 1] = '2'
			result[i + num_spaces*2 - 2] = '%'
			last_space = i
			num_spaces -= 1
	return ''.join(result)

# Let's test it!
s1 = "mario admon"
s2 = "mario admon   "
s3 = "mario  admon  "
s4 = "This sentence has several spaces   "
print(repr(s1), urlify(s1))
print(repr(s2), urlify(s2))
print(repr(s3), urlify(s3))
print(repr(s4), urlify(s4))

s1 = "mario admon  "
s2 = "mario admon      "
s3 = "mario  admon    "
s4 = "This sentence has several spaces        "
print(repr(s1), urlify_not_the_python_way(s1, 11))
print(repr(s2), urlify_not_the_python_way(s2, 11))
print(repr(s3), urlify_not_the_python_way(s3, 12))
print(repr(s4), urlify_not_the_python_way(s4, 32))
