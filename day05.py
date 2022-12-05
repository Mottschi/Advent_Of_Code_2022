import time, copy

DEBUG = 0

if DEBUG:
	FILE = 'day05_debug.txt'
else:
	FILE = 'day05.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n\n')
	return arr


def parse(data):
	setup, instructions = data
	*setup, stacknames = setup.split('\n')
	stack_count = int(stacknames[-1])
	stacks = [[] for _ in range(stack_count)]

	setup.reverse()
	for blocks in setup:
		for j in range(stack_count):
			block = ' ' if len(blocks) < j * 4 + 1 else blocks[j * 4 + 1]
			if block != ' ':
				stacks[j].append(block)
	moves = []
	for instruction in instructions.split('\n'):
		_, count, _, origin, _, target = instruction.split()
		moves.append((int(count), int(origin) - 1, int(target) - 1))
	print(stacks)
	print(moves)
	return stacks, moves


def part_one(data):
	stacks, moves = data
	for count, origin, target in moves:
		for i in range(count):
			stacks[target].append(stacks[origin].pop())

	result = ''
	for i in range(len(stacks)):
		result += stacks[i][-1]
	return result


def part_two(data):
	stacks, moves = data
	for count, origin, target in moves:
		crates = stacks[origin][-count:]
		for i in range(count):
			stacks[origin].pop()
		stacks[target] += crates

	result = ''
	for i in range(len(stacks)):
		result += stacks[i][-1]
	return result


if __name__ == '__main__':
	data = load()
	data = parse(data)

	data_p2 = copy.deepcopy(data)
	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')

	start_time = time.time()
	print('Part Two:', part_two(data_p2))
	print(f'--- {time.time() - start_time} seconds ---')
