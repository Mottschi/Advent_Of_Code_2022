import time
import re

DEBUG = True

if DEBUG:
	FILE = 'day16_debug.txt'
else:
	FILE = 'day16.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr


def parse(data):
	valve_controls = []
	valves = []
	result = {}
	result['valves'] = valves
	result['controls'] = valve_controls
	for line in data:
		line = re.search('^Valve ([A-Z]{2}) has flow rate=(\d+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ((?:[A-Z]{2}(?:,\s)?)+)$', line)
		valve = line.group(1)
		flow_rate = int(line.group(2))
		tunnels = line.group(3).split(', ')
		valve_controls.append((valve, flow_rate, tunnels))
		valves.append(valve)	
	return result


def part_one(data):
	current_room = 'aa'
	current_flow = 0
	status = {valve: False for valve in data['valves']}
	queue = [(current_room, current_flow, status)]
	valves = data['valves']
		


def part_two(data):
	pass


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
