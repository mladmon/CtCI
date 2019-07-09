# this algorithm returns a list of the starting indices of all permutations
# of a string, s, in a text, t in O(t) time

def substr_perms(s, t):
	# calculate the sum of the Unicode values of s's characters
	s_unicode_val = 0
	for char in s:
		s_unicode_val += ord(char) # thank you python :D

	# initialize sliding_window to the sum of t's first len(s) characters
	sliding_window = 0
	for char in t[:len(s)]:
		sliding_window += ord(char)
	
	# search through t for all permutations of s!
	result = []
	if sliding_window == s_unicode_val:
		result.append(0)
	for i in range(len(s), len(t)):
		sliding_window -= ord(t[i-len(s)])
		sliding_window += ord(t[i])
		if sliding_window == s_unicode_val:
			result.append(i-len(s) + 1)
	return result

# let's test it!
print(substr_perms('abbc', 'cbabadcbbabbcbabaabccbabc'))
