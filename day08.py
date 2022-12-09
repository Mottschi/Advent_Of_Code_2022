import time

DEBUG = 0

if DEBUG:
	FILE = 'day08_debug.txt'
else:
	FILE = 'day08.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	result = []
	for line in data:
		result.append(list(line))
	return result


def part_one(grid):
	visible_trees = set()
	invisible_trees = set()
	for row in range (0, len(grid)):
		for col in range(0, len(grid[row])):
			tree_pos = row, col
			# all trees on the border are visible
			if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[row]) - 1:
				visible_trees.add(tree_pos)
				continue

			# for all other trees, we need to check whether they are visible from any of the four directions
			# is there any tree that is bigger to the left?
			# the moment we find that a tree that is bigger, we know the current tree is hidden, until then we assume
			# it is visible
			current_tree_height = grid[row][col]
			visible = True
			# print(f'\nchecking on tree {tree_pos} of size {current_tree_height}')
			for i in range(0, col):
				# print('checking ')
				if grid[row][i] >= current_tree_height:
					visible = False
					# print(f'found a tree bigger then size {current_tree_height} to the left, at {row},{i}, size: {grid[row][i]}')
					break

			# if, after checking all trees to one side, the tree is visible (we havent found any bigger tree), we add it
			# to the list of visible trees and skip checking the other directions
			if visible:
				visible_trees.add(tree_pos)
				continue

			# is there any tree that is bigger to the right?
			visible = True
			for i in range(col+1, len(grid[row])):
				if grid[row][i] >= current_tree_height:
					visible = False
					# print(f'found a tree bigger then size {current_tree_height} to the right, at {row},{i}, size: {grid[row][i]}')
					break
			if visible:
				visible_trees.add(tree_pos)
				continue
			# is there any tree that is bigger to the top?
			visible = True
			for i in range(0, row):
				if grid[i][col] >= current_tree_height:
					visible = False
					# print(f'found a tree bigger then size {current_tree_height} to the top, at {i},{col}, size: {grid[i][col]}')
					break
			if visible:
				visible_trees.add(tree_pos)
				continue

			# is there any tree that is bigger to the bottom?
			visible = True
			for i in range(row+1, len(grid)):
				if grid[i][col] >= current_tree_height:
					visible = False
					# print(f'found a tree bigger then size {current_tree_height} to the bottom, at {i},{col}, size: {grid[i][col]}')
					break
			if visible:
				visible_trees.add(tree_pos)
				# print('tree is visible, adding to list')
				continue
			# print('tree is invisible')
			invisible_trees.add(tree_pos)
	return len(visible_trees)





def part_two(grid):
	height = len(grid)
	width = len(grid[0])
	max_score = 0
	for row in range(1, height-1):
		for col in range(1, width-1):
			tree = {'row': row, 'col': col, 'height': grid[row][col]}

			score_left = 0
			score_right = 0
			score_up = 0
			score_down = 0

			for i in range(col-1, -1, -1):
				c_row, c_col = row, i
				score_left += 1
				if grid[c_row][c_col] >= tree['height']:
					break

			for i in range(col+1, width):
				c_row, c_col = row, i
				score_right += 1
				if grid[c_row][c_col] >= tree['height']:
					break

			for i in range(row-1, -1, -1):
				c_row, c_col = i, col
				score_up += 1
				if grid[c_row][c_col] >= tree['height']:
					break

			for i in range(row+1, height):
				c_row, c_col = i, col
				score_down += 1
				if grid[c_row][c_col] >= tree['height']:
					break

			tree_score = score_up * score_down * score_right * score_left
			if tree_score > max_score:
				max_score = tree_score
	return max_score

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
