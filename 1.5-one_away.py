def one_away(str1, str2):
	size_diff = abs(len(str1)-len(str2))
	if size_diff > 1:
		return False
	elif size_diff is 1:
		return diff_by_one(str1, str2)
	else:
		return same_size(str1, str2)

def diff_by_one(str1, str2):
	s1, s2 = set(str1), set(str2)
	if s1.issubset(s2):
		return compare(str1, str2)
	elif s2.issubset(s1):
		return compare(str2, str1)
	else:
		return False

def compare(subs, string):
	j = 0
	for i in range(len(subs)):
		if subs[i] is string[j]:
			j += 1
		elif subs[i] is string[j + 1]:
			j += 2
		else:
			return False
	return True

def same_size(str1, str2):
	one_diff = False
	for i in range(len(str1)):
		if str1[i] is not str2[i]:
			if one_diff:
				return False
			else:
				one_diff = True
	return True

# Let's test it!
print('pale', 'ple', one_away('pale', 'ple'))
print('pales', 'pale', one_away('pales', 'pale'))
print('pale', 'bale', one_away('pale', 'bale'))
print('pale', 'bake', one_away('pale', 'bake'))

