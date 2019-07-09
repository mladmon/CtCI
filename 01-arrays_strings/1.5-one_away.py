def one_away(str1, str2):
	size_diff = abs(len(str1)-len(str2))
	if size_diff > 1:
		return False
	elif size_diff is 1:
		if len(str1) < len(str2):
			return diff_by_one(str1, str2)
		else:
			return diff_by_one(str2, str1)
	else:
		return same_size(str1, str2)

def diff_by_one(subs, string):
	j = 0
	for i in range(len(subs)):
		if j is len(string): # more than one char was different
			return False
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
print('apxpl', 'pple', one_away('apxpl', 'pple')) #out of bounds
