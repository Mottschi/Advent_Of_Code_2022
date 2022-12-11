import time, copy

DEBUG = False

if DEBUG:
	FILE = 'day11_debug.txt'
else:
	FILE = 'day11.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n\n')
	return arr


class Monkey:
	def __init__(self, starting_items, operation, test, handle_true, handle_false, worry_reduction=None):
		self.items = starting_items
		self.test = test
		self.handle_true = handle_true
		self.handle_false = handle_false
		self.operation_a, self.operation_operator, self.operation_b = operation
		self.reduce_worry_naturally = True if worry_reduction is None else False
		self.worry_reduction = worry_reduction

		self.inspect_count = 0
		self.monkey_friends = None

	def do_operation(self, old):
		a = old if self.operation_a == 'old' else int(self.operation_a)
		b = old if self.operation_b == 'old' else int(self.operation_b)

		if self.operation_operator == '+':
			result = a + b
		elif self.operation_operator == '*':
			result = a * b

		return result

	def __repr__(self):
		result = f'"Monkey holding {len(self.items)} item{"s" if len(self.items) > 1 else ""}: '
		for item in self.items:
			result += f'{item}'
			if item != self.items[-1]:
				result += ', '
		return result + '"'

	def turn(self, monkeys):
		self.monkey_friends = monkeys
		while len(self.items) > 0:
			self.inspect_next_item()

	def inspect_next_item(self):
		item = self.items.pop(0)
		worry = self.do_operation(item)
		if self.reduce_worry_naturally:
			worry //= 3
		else:
			worry = worry % self.worry_reduction
		test_result = worry % self.test == 0
		if test_result:
			target = self.handle_true
		else:
			target = self.handle_false
		self.monkey_friends[target].catch(worry)

		self.inspect_count += 1

	def catch(self, item):
		self.items.append(item)


def parse(data):
	monkeys = []
	for line in data:
		starting_items, operation, test, handle_true, handle_false = [action.lstrip() for action in line.split('\n')[1:]]
		starting_items = [int(item) for item in starting_items.split(': ')[1].split(', ')]
		operation = operation.split(' = ')[1].split()
		operation = 'old' if operation[0] == 'old' else int(operation[0]), operation[1], 'old' if operation[2] == 'old' else int(operation[2])
		test = int(test.split('by ')[1])
		handle_true = int(handle_true.split('monkey ')[1])
		handle_false = int(handle_false.split('monkey ')[1])
		monkeys.append((starting_items, operation, test, handle_true, handle_false))
	return monkeys


def part_one(data):
	monkeys = []
	for monkey in data:
		monkeys.append(Monkey(*monkey))
	for r in range(20):
		for monkey in monkeys:
			monkey.turn(monkeys)

	counts = []
	for monkey in monkeys:
		counts.append(monkey.inspect_count)
	counts.sort()
	return counts[-1] * counts[-2]


def part_two(data):
	monkeys = []
	test_divisor_multiplier = 1
	for monkey in data:
		test_divisor_multiplier *= monkey[2]
	for monkey in data:
		monkeys.append(Monkey(*monkey, test_divisor_multiplier))

	for r in range(10000):
		for monkey in monkeys:
			monkey.turn(monkeys)

	counts = []
	for monkey in monkeys:
		counts.append(monkey.inspect_count)
	counts.sort()
	return counts[-1] * counts[-2]


if __name__ == '__main__':
	data = load()
	data = parse(data)
	data2 = copy.deepcopy(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')

	start_time = time.time()
	print('Part Two:', part_two(data2))
	print(f'--- {time.time() - start_time} seconds ---')
