# using a hash table of char:freq pairs
def is_permutation(str1, str2):
	if len(str1) != len(str2):
		return False
	freq = {}
	for char in str1:
		freq[char] = freq.get(char, 0) + 1
	for char in str2:
		if char not in freq:
			return False
		elif freq[char] == 1:
			del freq[char]
		else:
			freq[char] -= 1
	return True

# Let's test it!
str1, str2 = "mario", "oiram"
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = "Mario", "mario"
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = "marioo", "mario"
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = "mario", "marioo"
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = '', ''
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = ' ', ''
print(repr(str1), repr(str2), is_permutation(str1, str2))
str1, str2 = '#4Rm!=  _-foo', 'o f-m!# o_=R4'
print(repr(str1), repr(str2), is_permutation(str1, str2))
