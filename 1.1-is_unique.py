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
