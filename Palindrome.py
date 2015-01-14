def f(string):
	if len(string) < 2:
		return True

	elif string[0] == string[len(string) - 1]:
		 string = string[1:len(string) - 1]
		 return f(string)

	else:
		return False

#string = 'abcddcba'
print f('ab')
