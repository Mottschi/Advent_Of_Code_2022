import time

DEBUG = 0

if DEBUG:
	FILE = 'day03_debug.txt'
else:
	FILE = 'day03.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr

def part_one(data):
	rucksacks = []
	for line in data:
		half = len(line) // 2
		first_half = set(line[:half])
		second_half = set(line[half:])
		rucksacks.append((first_half, second_half))
	priority_sum = 0
	for c1, c2 in rucksacks:
		common_item = c1 & c2
		for char in common_item:
			priority_sum += priority(char)
	return priority_sum


def part_two(data):
	priority_sum = 0
	for i in range(0, len(data), 3):
		elf_one = set(data[i])
		elf_two = set(data[i+1])
		elf_three = set(data[i+2])
		badge = (elf_one & elf_two & elf_three).pop()
		priority_sum += priority(badge)
	return priority_sum

def priority(char):
	priority = ord(char)
	if priority >= 97:
		priority -= 96
	else:
		priority += 26 - 64
	return priority

if __name__ == '__main__':
	data = load()

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
