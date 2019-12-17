# O(n) runtime, O(n) space
def is_rotation(str1, str2):
	if len(str1) != len(str2):
		return False
	else:
		# Python's in operator implements isSubstring()
		return str2 in str1 + str1

# Let's test it!
s1 = 'waterbottle'
s2 = 'erbottlewat'
s3 = 'tlewaterbot'
s4 = 'aterbottleq'
s5 = 'water'
s6 = ''
print(s1, s2, is_rotation(s1, s2))
print(s2, s1, is_rotation(s2, s1))
print(s1, s3, is_rotation(s1, s3))
print(s2, s3, is_rotation(s2, s3))
print(s1, s4, is_rotation(s1, s4))
print(s1, s1, is_rotation(s1, s1))
print(s1, s5, is_rotation(s1, s5))
print(repr(s6), repr(s6), is_rotation(s6, s6))
