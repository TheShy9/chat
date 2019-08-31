def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	Allen_word_count = 0
	Viki_word_count = 0
	Allen_sticker_count = 0
	Viki_sticker_count = 0
	Allen_picture_count = 0
	Viki_picture_count = 0
	for line in lines:
		l = line.split(' ')
		time = l[0]
		name = l[1]
		if name == 'Allen':
			if l[2] == '貼圖':
				Allen_sticker_count += 1
			elif l[2] == '圖片':
				Allen_picture_count += 1
			else:
				for msg in l[2:]:
					Allen_word_count += len(msg)
		if name == 'Viki':
			if l[2] == '貼圖':
				Viki_sticker_count += 1
			elif l[2] == '圖片':
				Viki_picture_count += 1
			else:
				for msg in l[2:]:
					Viki_word_count += len(msg)
	print('Allen say', Allen_word_count, Allen_sticker_count, Allen_picture_count)
	print('Viki say', Viki_word_count, Viki_sticker_count, Viki_picture_count)
	

def save_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('1.txt')
	lines = convert(lines)
	# save_file('output2.txt', lines)

main()