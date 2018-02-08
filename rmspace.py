def rspace(string):
	new = string.split()
	char = ''
	i = 0
	while i < len(new):
		char = char + new[i]
		i = i + 1
	return(char)
