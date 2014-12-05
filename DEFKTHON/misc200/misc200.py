import Image
w,h = 126,488
img = Image.new('RGB', (w, h))
pixels = img.load()

f = open("flag.txt", "r")
index=0
while True:
	line = f.readline()
	if line=='':
		break
	line = [int(i) for i in line.split(',')]
	pixels[index/h, index%h] = (line[0], line[1], line[2])
	index += 1
	#print index
img.show()

