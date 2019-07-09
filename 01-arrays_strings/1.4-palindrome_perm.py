def palindrome_perm(string):
	d = {}
	for c in string.lower().replace(' ', ''):
		d[c] = d.get(c, 0) + 1
	num_odd = 0
	for v in d.values():
		if v % 2 is 1:
			num_odd += 1
	return num_odd < 2

def palindrome_perm2(string):
    freq = [0] * 256 
    for c in string.lower().replace(' ', ''):
        freq[ord(c)] += 1
    num_odd = 0 
    for f in freq:
        if f % 2 is 1:
            num_odd += 1
    return num_odd < 2 

# Let's test it!
print('Tact Coa', palindrome_perm('Tact Coa'))
print('mario is the thorns man', palindrome_perm('mario is the thorns man'))
print(repr(''), palindrome_perm(''))
print('tttaaaabbdddddd', palindrome_perm('tttaaaabbdddddd'))
print('tttaaaabbddddd', palindrome_perm('tttaaaabbddddd'))

print('Tact Coa', palindrome_perm2('Tact Coa'))
print('mario is the thorns man', palindrome_perm2('mario is the thorns man'))
print(repr(''), palindrome_perm2(''))
print('tttaaaabbdddddd', palindrome_perm2('tttaaaabbdddddd'))
print('tttaaaabbddddd', palindrome_perm2('tttaaaabbddddd'))
