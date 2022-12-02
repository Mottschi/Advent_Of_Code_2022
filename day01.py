import time

DEBUG = False

if DEBUG:
	FILE = 'day01_debug.txt'
else:
	FILE = 'day01.txt'

def load():
	data = []
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n\n')
		for line in arr:
			line = line.split('\n')
			line = [int(num) for num in line]
			data.append(line)
	return data


def part_one(data):
	maximum = 0
	for elf in data:
		summe = sum(elf)
		maximum = max(maximum, summe)
	return maximum


def part_two(data):
	summen = []
	for elf in data:
		summe = sum(elf)
		summen.append(summe)
	summen = sorted(summen, reverse=True)
	summe = sum(summen[0:3])
	return summe


if __name__ == '__main__':
	data = load()

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
