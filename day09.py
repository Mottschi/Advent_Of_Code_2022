import time

DEBUG = 0

if DEBUG:
	FILE = 'day09_debug2.txt'
else:
	FILE = 'day09.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	movement = [(direction, int(step)) for direction, step in  [line.split() for line in data]]
	return movement

def distance(head, tail):
	x1, y1 = head
	x2, y2 = tail
	return abs(x1-x2) + abs(y1-y2)

def touching(head, tail):
	d = distance(head, tail)
	if d < 2:
		return True
	if d > 2:
		return False
	return head[0] != tail[0] and head[1] != tail[1]

def part_one(h_movement):
	tail = [0, 0]
	head = [0, 0]

	visited = set()
	visited.add((tail[0], tail[1]))

	# Head movement
	for direction, steps in h_movement:
		for _ in range(steps):
			match direction:
				case 'R':
					head[0] += 1
				case 'L':
					head[0] -= 1
				case 'U':
					head[1] += 1
				case 'D':
					head[1] -= 1

			# Tail movement
			if touching(head, tail):
				# still touching, tail not moving
				continue
			if tail[0] == head[0]:
				if head[1] > tail[1]:
					tail[1] += 1
				else:
					tail[1] -= 1
			elif tail[1] == head[1]:
				if head[0] > tail[0]:
					tail[0] += 1
				else:
					tail[0] -= 1
			else:
				if head[0] > tail[0]:
					tail[0] += 1
				else:
					tail[0] -= 1
				if head[1] > tail[1]:
					tail[1] += 1
				else:
					tail[1] -= 1

			visited.add((tail[0], tail[1]))
	return len(visited)



def part_two(h_movement):
	print('part 2 start')
	tails = [[0, 0] for _ in range(10)]

	visited = set()
	visited.add((0, 0))

	# Head movement
	head = tails[0]
	for direction, steps in h_movement:
		for _ in range(steps):
			head = tails[0]
			match direction:
				case 'R':
					head[0] += 1
				case 'L':
					head[0] -= 1
				case 'U':
					head[1] += 1
				case 'D':
					head[1] -= 1

			for i in range(1, len(tails)):
				head = tails[i-1]
				tail = tails[i]
				# Tail movement
				if touching(head, tail):
					# still touching, tail not moving
					continue
				if tail[0] == head[0]:
					if head[1] > tail[1]:
						tail[1] += 1
					else:
						tail[1] -= 1
				elif tail[1] == head[1]:
					if head[0] > tail[0]:
						tail[0] += 1
					else:
						tail[0] -= 1
				else:
					if head[0] > tail[0]:
						tail[0] += 1
					else:
						tail[0] -= 1
					if head[1] > tail[1]:
						tail[1] += 1
					else:
						tail[1] -= 1
			visited.add((tails[-1][0], tails[-1][1]))
	return len(visited)


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
