import time

DEBUG = 0

if DEBUG:
	FILE = 'day04_debug.txt'
else:
	FILE = 'day04.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	results=[]
	data =  [line.split(',') for line in data]
	for first, second in data:
		first = first.split('-')
		second = second.split('-')

		first = int(first[0]), int(first[1])
		second = int(second[0]), int(second[1])
		results.append((first, second))

	return results

def contains(pair):
	(first_start, first_end), (second_start, second_end) = pair
	return (first_start <= second_start and first_end >= second_end) or (first_start >= second_start and first_end <= second_end)

def overlaps(pair):
	(first_start, first_end), (second_start, second_end) = pair
	return first_start <= second_end and first_start >= second_start  or second_start <= first_end and second_start >= first_start


def part_one(elfs):
	count = 0
	for pair in elfs:
		if contains(pair):
			count += 1
	return count


def part_two(elfs):
	count = 0
	for pair in elfs:
		if overlaps(pair):
			count += 1
	return count


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
