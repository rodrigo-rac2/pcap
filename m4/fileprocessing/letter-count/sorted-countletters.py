from os import strerror

filename = input('Enter file name: ')
lettercount = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}
try:
	for line in open(filename, 'rt'):
		for ch in line:
			if ch.isalpha():
				lettercount[ch.lower()] += 1
	ordered_lettercount = sorted(lettercount.items(), key=lambda x: x[1], reverse=True)
	with open(f'{filename}.hist', 'wt') as file:
		for letter in ordered_lettercount:
			if letter[1] != 0:
				file.write(f"{letter[0]} -> {letter[1]}\n")
				print(f"{letter[0]} -> {letter[1]}")
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
