import time

DEBUG = False

if DEBUG:
	FILE = 'day02_debug.txt'
else:
	FILE = 'day02.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	return [line.split() for line in data]

player_one = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
player_two = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

game_score = {('rock', 'paper'): 6,
		 ('rock', 'scissors'): 0,
		 ('rock', 'rock'): 3,
		 ('paper', 'paper'): 3,
		 ('paper', 'scissors'): 6,
		 ('paper', 'rock'): 0,
		 ('scissors', 'paper'): 0,
		 ('scissors', 'scissors'): 3,
		 ('scissors', 'rock'): 6,
		 }

figure_score = {'rock': 1, 'paper': 2, 'scissors': 3}

game_score_part2 = {
	'X': 0,
	'Y': 3,
	'Z': 6,
}

def part_one(games):

	score = 0
	for elfs, mine in games:
		elf = player_one[elfs]
		me = player_two[mine]
		score += figure_score[me] + game_score[(elf, me)]
	return score

def part_two(games):
	player_two = {

		('rock', 'X'): 'scissors',
		('rock', 'Y'): 'rock',
		('rock', 'Z'): 'paper',
		('paper', 'X'): 'rock',
		('paper', 'Y'): 'paper',
		('paper', 'Z'): 'scissors',
		('scissors', 'X'): 'paper',
		('scissors', 'Y'): 'scissors',
		('scissors', 'Z'): 'rock',
	}
	score = 0
	for elfs, mine in games:
		elf = player_one[elfs]
		me = player_two[(elf, mine)]
		score += figure_score[me] + game_score_part2[mine]
	return score


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
