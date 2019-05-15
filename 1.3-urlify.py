# python str methods make this problem very easy... yay python!
# this version modifies the input string
def urlify(string):
	string = string.rstrip().replace(' ', '%20')

# this version returns a URLified copy
def urlify2(string):
	return string.rstrip().replace(' ', '%20')

# Let's test it!
s1 = "mario admon"
s2 = "mario admon   "
s3 = "mario  admon  "
s4 = "This sentence has several spaces   "
print(repr(s1), urlify2(s1))
print(repr(s2), urlify2(s2))
print(repr(s3), urlify2(s3))
print(repr(s4), urlify2(s4))
