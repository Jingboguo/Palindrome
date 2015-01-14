def f(string, lh, rh):
	if lh == rh:
		return True

	elif lh == rh - 1:
		 return True 

	elif string[lh] == string[rh]:
		 #lh = lh + 1
		 #rh = rh - 1
		 return f(string, ++lh, --rh)

	else:
		return False

string = 'a'
print f(string, 0, len(string) - 1)
