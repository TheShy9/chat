lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		l = line.strip().split(' ')
		time = l[0][:5]
		name = l[0][5:]
		print(time)
		print(name)
		

