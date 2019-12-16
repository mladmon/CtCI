# O(n) runtime, O(n) space solution
def is_palindrome_perm(string):
	char_freq = {}
	# assumes case-insensitive and removes whitespace
	for char in string.lower().replace(' ', ''):
		char_freq[char] = char_freq.get(char, 0) + 1

	num_odd = 0
	for freq in char_freq.values():
		if freq % 2 == 1:
			num_odd += 1

	return num_odd < 2

# O(n) runtime, O(1) space solution (could argue above is constant too)
def is_palindrome_perm2(string):
    char_freq = [0] * 128
    for char in string.lower().replace(' ', ''):
        char_freq[ord(char)] += 1

    num_odd = 0 
    for freq in char_freq:
        if freq % 2 == 1:
            num_odd += 1

    return num_odd < 2 

# Let's test it!
print('Tact Coa', is_palindrome_perm('Tact Coa'))
print('mario is the thorns man', is_palindrome_perm('mario is the thorns man'))
print(repr(''), is_palindrome_perm(''))
print('tttaaaabbdddddd', is_palindrome_perm('tttaaaabbdddddd'))
print('tttaaaabbddddd', is_palindrome_perm('tttaaaabbddddd'))

print('Tact Coa', is_palindrome_perm2('Tact Coa'))
print('mario is the thorns man', is_palindrome_perm2('mario is the thorns man'))
print(repr(''), is_palindrome_perm2(''))
print('tttaaaabbdddddd', is_palindrome_perm2('tttaaaabbdddddd'))
print('tttaaaabbddddd', is_palindrome_perm2('tttaaaabbddddd'))
