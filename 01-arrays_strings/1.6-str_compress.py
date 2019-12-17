# O(n) runtime, O(n) space 
def compress_str(string):
	if len(string) < 3:
		return string

	compressed_str = []
	i = 0
	while i < len(string):
		compressed_str.append(string[i])
		j = i + 1
		while j < len(string) and string[i] == string[j]:
			j += 1

		seq_length = j - i
		compressed_str.append(str(seq_length))
		i = j

	if len(compressed_str) < len(string):
		return ''.join(compressed_str)
	else:
		return string


print()
print('aabcccccaaa', compress_str('aabcccccaaa'))
print(repr(''), compress_str(''))
print('a', compress_str('a'))	
print('aa', compress_str('aa'))
print('ab', compress_str('ab'))
print('aaa', compress_str('aaa'))
print('aabb', compress_str('aabb'))
print('aaab', compress_str('aaab'))
print('aaabb', compress_str('aaabb'))
print('Ooooooh!!', compress_str('Ooooooh!!'))
print('oooOoOOO', compress_str('oooOoOOO'))
print('oooOOoOOO', compress_str('oooOOoOOO'))
