import time

DEBUG = 0

if DEBUG:
	FILE = 'day10_debug2.txt'
else:
	FILE = 'day10.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	return [(element[0],) if len(element) == 1 else (element[0], int(element[1])) for element in [line.split() for line in data]]


def part_one(instructions):
	x = 1
	cycle = 0
	signal_sum = 0
	for line in instructions:
		instruction = line[0]
		cycles = len(line)
		for c in range(cycles):
			cycle += 1
			if cycle % 40 == 20:
				signal_strength = cycle * x
				signal_sum += signal_strength

		if instruction == 'addx':
			x += line[1]
	print('cycles total: ', cycle)
	return signal_sum


def part_two(instructions):
	x = 1
	cycle = 0
	signal_sum = 0
	for line in instructions:
		instruction = line[0]
		cycles = len(line)
		for c in range(cycles):
			if abs(x - cycle % 40) > 1:
				char = '.'
			else:
				char = '#'
			print(char, end='')
			cycle += 1
			if cycle % 40 == 0:
				print()
		if instruction == 'addx':
			x += line[1]
	return signal_sum


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
