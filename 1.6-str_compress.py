def str_compress(string):
	if len(string) < 3:
		return string
	comp, char, count = [], string[0], 1
	for i in range(1, len(string)):
		if string[i] is not char:
			comp.append((char, count))
			char, count = string[i], 1
		else:
			count += 1
	comp.append((char, count)) # add the last (single or repeated) char
	if len(comp)*2 < len(string):
		return ''.join([c + str(i) for c, i in comp])
	else:
		return string

# Let's test it!
print('aabcccccaaa', str_compress('aabcccccaaa'))
print(repr(''), str_compress(''))
print('a', str_compress('a'))	
print('aa', str_compress('aa'))
print('ab', str_compress('ab'))
print('aaa', str_compress('aaa'))
print('aabb', str_compress('aabb'))
print('aaab', str_compress('aaab'))
print('aaabb', str_compress('aaabb'))
print('Ooooooh!!', str_compress('Ooooooh!!'))
print('oooOoOOO', str_compress('oooOoOOO'))
print('oooOOoOOO', str_compress('oooOOoOOO'))
