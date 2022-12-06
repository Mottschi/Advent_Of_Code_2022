import time

DEBUG = 0

if DEBUG:
	FILE = 'day06_debug.txt'
else:
	FILE = 'day06.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	return data[0]


def part_one(signals):
	for i in range(4, len(signals)):
		if len(set(signals[i - 4:i])) == 4:
			return i


def part_two(signals):
	for i in range(14, len(signals)):
		if len(set(signals[i - 14:i])) == 14:
			return i


if __name__ == '__main__':
	data = load()
	data = parse(data)
	print(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
