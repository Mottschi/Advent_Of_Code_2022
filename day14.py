import time

DEBUG = 1

if DEBUG:
	FILE = 'day14_debug.txt'
else:
	FILE = 'day14.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	grid = {'max_y': 0}
	for line in data:
		line = line.split(' -> ')
		line = [(int(pair[0]), int(pair[1])) for pair in [pair.split(',') for pair in line]]
		for i in range(len(line) - 1):
			current_x, current_y = line[i]
			target_x, target_y = line[i+1]
			step_x = 1 if target_x >= current_x else -1
			step_y = 1 if target_y >= current_y else -1
			for x in range(current_x, target_x+step_x, step_x):
				for y in range(current_y, target_y+step_y, step_y):
					grid[(x, y)] = '#'
					if y > grid['max_y']:
						grid['max_y'] = y
	return grid


def part_one(grid):
	x, y = 500, 0
	while y <= grid['max_y']:
		if (x, y+1) not in grid:
			y += 1
		elif (x-1, y+1) not in grid:
			x -= 1
			y += 1
		elif (x+1, y+1) not in grid:
			x += 1
			y += 1
		else:
			grid[(x, y)] = 'o'
			x, y = 500, 0

	return len(list(filter(lambda e: e == 'o', grid.values())))

def part_two(grid):
	x, y = 500, 0
	while True:
		if (x, y+1) not in grid and y <= grid['max_y']:
			y += 1
		elif (x-1, y+1) not in grid and y <= grid['max_y']:
			x -= 1
			y += 1
		elif (x+1, y+1) not in grid and y <= grid['max_y']:
			x += 1
			y += 1
		else:
			grid[(x, y)] = 'o'
			if (x, y) == (500, 0):
				return len(list(filter(lambda e: e == 'o', grid.values())))
			x, y = 500, 0




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
