# O(n) runtime, O(1) space solution
def is_one_away(str1, str2):
	size_diff = abs(len(str1) - len(str2))
	if size_diff > 1:
		return False
	elif size_diff == 1:
		if len(str1) < len(str2):
			return check_one_insert_away(str1, str2)
		else:
			return check_one_insert_away(str2, str1)
	else:
		return check_one_replace_away(str1, str2)


def check_one_insert_away(smaller, larger):
	# i is smaller's index, j is larger's index
	j = 0
	made_edit = False
	for i in range(len(smaller)):
		if smaller[i] == larger[j]:
			j += 1
		elif smaller[i] == larger[j + 1]:
			if made_edit:
				return False
			else:
				made_edit = True
				j += 2
		else:
			return False

	return True


def check_one_replace_away(str1, str2):
	found_diff = False
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			if found_diff:
				return False
			else:
				found_diff = True
	return True


# Let's test it!
print('pale,', 'ple ->', is_one_away('pale', 'ple'))
print('pales,', 'pale ->', is_one_away('pales', 'pale'))
print('pale,', 'bale ->', is_one_away('pale', 'bale'))
print('pale,', 'bake ->', is_one_away('pale', 'bake'))
print('apxpl,', 'pple ->', is_one_away('apxpl', 'pple'))
