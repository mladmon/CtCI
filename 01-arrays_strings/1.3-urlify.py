# Python str methods make this problem very easy
def urlify(string):
	return string.rstrip().replace(' ', '%20')

# The problem intends for us to implement str.replace() in-place
def non_pythonic_urlify(string, true_length):
	char_list = list(string)
	num_spaces = 0
	for i in range(true_length):
		if char_list[i] == ' ':
			num_spaces += 1

	copy_to_index = true_length + num_spaces*2 - 1
	for i in reversed(range(true_length)):
		if char_list[i] == ' ':
			char_list[copy_to_index] = '0'
			char_list[copy_to_index - 1] = '2'
			char_list[copy_to_index - 2] = '%'
			copy_to_index -= 3
		else:
			char_list[copy_to_index] = char_list[i]
			copy_to_index -= 1

	return ''.join(char_list)

# Let's test it!
s1 = "Mr John Smith    "
s2 = "mario admon  "
s3 = "mario  admon    "
s4 = "This sentence has several spaces        "
print(repr(s1), repr(urlify(s1)))
print(repr(s2), repr(urlify(s2)))
print(repr(s3), repr(urlify(s3)))

print(repr(s1), repr(non_pythonic_urlify(s1, 13)))
print(repr(s2), repr(non_pythonic_urlify(s2, 11)))
print(repr(s3), repr(non_pythonic_urlify(s3, 12)))
print(repr(s4), repr(non_pythonic_urlify(s4, 32)))
