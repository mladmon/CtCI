# No restrictions: O(n) runitme, O(n) space (all from creating the set!)
def is_unique(string):
	return len(set(string)) == len(string)

# Let's test it!
print("hello, world!", is_unique("hello, world!"))
print('mario', is_unique("mario"))
print('Mm', is_unique("Mm"))
print('whatboudis?', is_unique('whatboudis?'))
print('whataboudis?', is_unique('whataboudis?'))
print('h', is_unique('h'))
print('', is_unique(''))
print()

# No data structures allowed: O(n^2), O(1)
def is_unique2(string):
	for i, char in enumerate(string):
		for j in range(i+1, len(string)):
			if char == string[j]:
				return False
	return True

# Let's test it!
print("hello, world!", is_unique2("hello, world!"))
print('mario', is_unique2("mario"))
print('Mm', is_unique2("Mm"))
print('whatboudis?', is_unique2('whatboudis?'))
print('whataboudis?', is_unique2('whataboudis?'))
print('h', is_unique2('h'))
print('', is_unique2(''))
print()

# No data structures allowed: O(n*log n), O(1)
def is_unique3(string):
	s = sorted(string) # s is a list!
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True

# Let's test it!
print("hello, world!", is_unique3("hello, world!"))
print('mario', is_unique3("mario"))
print('Mm', is_unique3("Mm"))
print('whatboudis?', is_unique3('whatboudis?'))
print('whataboudis?', is_unique3('whataboudis?'))
print('h', is_unique3('h'))
print('', is_unique3(''))

