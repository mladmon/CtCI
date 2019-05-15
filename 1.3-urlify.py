# python str methods make this problem very easy
def urlify(string):
	return string.rstrip().replace(' ', '%20')

# Let's test it!
s1 = "mario admon"
s2 = "mario admon   "
s3 = "mario  admon  "
s4 = "This sentence has several spaces   "
print(repr(s1), urlify(s1))
print(repr(s2), urlify(s2))
print(repr(s3), urlify(s3))
print(repr(s4), urlify(s4))
