import time

DEBUG = 0

if DEBUG:
	FILE = 'day12_debug.txt'
else:
	FILE = 'day12.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	grid = {}
	grid['width'] = len(data[0])
	grid['height'] = len(data)
	grid['possible_start'] = set()
	for row in range(grid['height']):
		for col in range(grid['width']):
			grid[(row, col)] = data[row][col]
			if grid[(row, col)] == 'S':
				grid['start'] = row, col
				grid[(row, col)] = 'a'
			elif grid[row, col] == 'E':
				grid[(row, col)] = 'z'
				grid['finish'] = row, col

			if grid[(row, col)] == 'a':
				grid['possible_start'].add((row, col))
	return grid


def part_one(grid, max_steps=None):
	start = grid['start']
	finish = grid['finish']

	visited = set()
	queue = set()
	temp_queue = set()
	queue.add(start)
	visited.add(start)
	# as long as we have locations in the queue, keep going
	# if we hit the finish line during the loop, we will break out
	steps = 1
	while queue:
		# get a location from the queue
		row, col = queue.pop()

		current = grid[(row, col)]
		current_height = ord(current)

		# find all neighbors we can move to
		possible_moves = set()
		left = (row, col-1) if col > 0 else None
		right = (row, col+1) if col < grid['width'] - 1 else None
		up = (row-1, col) if row > 0 else None
		down = (row+1, col) if row < grid['height'] - 1 else None

		if left and ord(grid[left]) <= current_height + 1:
			possible_moves.add(left)
		if right and ord(grid[right]) <= current_height + 1:
			possible_moves.add(right)
		if up and ord(grid[up]) <= current_height + 1:
			possible_moves.add(up)
		if down and ord(grid[down]) <= current_height + 1:
			possible_moves.add(down)

		# check all of those whether we already were there (if so, we already have a path to them that was shorter
		possible_moves = possible_moves - visited

		# after doing so, check whether that location is the finish line
		if finish in possible_moves:
			return steps

		# mark all the moves as visited
		visited = visited | possible_moves

		# add all possible moves to a temporary queue we will use for our next step
		temp_queue = temp_queue | possible_moves

		# if main queue is empty, we have exhausted all options for our current step
		# now we add the current temporary queue to the main queue, and empty the temporary queue, so that we can move
		# to check our next steps
		# increase step counter while doing that
		if len(queue) == 0:
			queue = temp_queue
			temp_queue = set()
			steps += 1
			if max_steps is not None and steps > max_steps:
				return None
	return None



def part_two(grid):
	start_options = grid['possible_start']
	best_length = None
	for start in start_options:
		grid['start'] = start
		path_length = part_one(grid, best_length)
		if best_length is None:
			best_length = path_length
		elif path_length is not None and path_length < best_length:
			best_length = path_length
	return best_length




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
