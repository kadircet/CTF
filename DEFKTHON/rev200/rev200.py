indexes = [
	[1, 1],
	[4, 5],
	[8, 9],
	[12, 12],
	[18, 17],
	[10, 21],
	[9, 25]
]
key = "42447255344574653276838751"

flag = ""
for pair in indexes:
	flag += chr(ord(key[pair[0]]) + ord(key[pair[1]]))
print flag

