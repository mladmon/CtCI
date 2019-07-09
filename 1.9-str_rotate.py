def is_rotation(s1, s2):
	if len(s1) != len(s2):
		return False
	longest_sub = 0
	for i in reversed(range(len(s1))):
		if s1[i] == s2[0]:
			for j in range(1, len(s1) - i):
				if s1[i + j] != s2[j]:
					break
			else:
				longest_sub = len(s1) - i
	# our one call to 'isSubstring', the 'in' operator :)
	if s1[:len(s1) - longest_sub] in s2[longest_sub:]:
		return True
	else:
		return False

# Optimal sln - O(n) to create s1s1, check if s2 is substr; O(n) space for s1s1
def is_rotation2(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		return s2 in s1 + s1

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

print(s1, s2, is_rotation2(s1, s2))
print(s2, s1, is_rotation2(s2, s1))
print(s1, s3, is_rotation2(s1, s3))
print(s2, s3, is_rotation2(s2, s3))
print(s1, s4, is_rotation2(s1, s4))
print(s1, s1, is_rotation2(s1, s1))
print(s1, s5, is_rotation2(s1, s5))
print(repr(s6), repr(s6), is_rotation2(s6, s6))
