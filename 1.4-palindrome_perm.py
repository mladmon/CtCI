def palindrome_perm(string):
	d = {}
	for c in string.lower().replace(' ', ''):
		d[c] = d.get(c, 0) + 1
	num_odd = 0
	for v in d.values():
		if v % 2 is 1:
			num_odd += 1
	return num_odd < 2

# Let's test it!
print('Tact Coa', palindrome_perm('Tact Coa'))
print('mario is the thorns man', palindrome_perm('mario is the thorns man'))
print(repr(''), palindrome_perm(''))
print('tttaaaabbdddddd', palindrome_perm('tttaaaabbdddddd'))
print('tttaaaabbddddd', palindrome_perm('tttaaaabbddddd'))
