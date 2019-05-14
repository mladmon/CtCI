# using a hash table of char:freq pairs
def is_permutation(str1, str2):
	if len(str1) is not len(str2):
		return False
	d1 = {}
	for c in str1:
		d1[c] = d1.get(c, 0) + 1
	for c in str2:
		if c not in d1:
			return False
		elif d1[c] is 1:
			del d1[c]
		else:
			d1[c] -= 1
	return True # bec init. check if strings same length, d1 always empty here

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
