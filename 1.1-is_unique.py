def is_unique(string):
	#return len(set(string)) == len(string)
	return len(set(string)) is len(string)

# Let's test it!
print("hello, world!", is_unique("hello, world!"))
print('mario', is_unique("mario"))
print('Mm', is_unique("Mm"))
print('whatboudis?', is_unique('whatboudis?'))
print('whataboudis?', is_unique('whataboudis?'))
print('h', is_unique('h'))
print('', is_unique(''))


# restricted no data structures allowed - O(n^2), O(1)
def is_unique2(string):
	for i, char in enumerate(string):
		for other in range(i+1, len(string)):
			if char is string[other]:
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

