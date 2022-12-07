import time

DEBUG = 0

if DEBUG:
	FILE = 'day07_debug.txt'
else:
	FILE = 'day07.txt'


def load():
	with open(FILE) as file:
		arr = file.read().rstrip().split('\n')
	return arr

class Folder:
	def __init__(self, parent, name):
		self.parent = parent
		self.name = name
		self.files = {}
		self.folders = {}
		self.depth = 0 if self.parent is None else parent.depth + 1

	def add_folder(self, folder):
		self.folders[folder.name] = folder

	def add_file(self, file):
		self.files[file.name]= file
		file.folder = self

	def __repr__(self):
		result = f'{" " * self.depth * 2}- {self.name} (dir)\n'
		for folder in self.folders.values():
			result += f'{folder}'

		for file in self.files.values():

			result += f'{file}\n'
		return result

	def calculate_size(self):
		size = 0
		for file in self.files.values():
			size += file.size
		for folder in self.folders.values():
			size += folder.calculate_size()
		return size
class File:
	def __init__(self, name, size):
		self.size = size
		self.name = name

	def __repr__(self):
		return f'{" "*(2 + 2*self.folder.depth)}- {self.name} (file, size={self.size})'

def parse(data):
	i = 0
	length = len(data)
	root = Folder(None, '/')
	current = None
	while i < length:
		line = data[i]
		i += 1
		if line.startswith('$'):
			_, command, *parameter = line.split()
			if command == 'cd':
				folder_name = parameter[0]
				if folder_name == '/':
					current = root
				elif folder_name == '..':
					if current.parent is None:
						raise ValueError('Already at root, unable to go up')
					current = current.parent
				else:
					if folder_name in current.folders:
						current = current.folders[folder_name]
					else:
						new_folder = Folder(current, folder_name)
						current.add_folder(new_folder)
						current = new_folder
			elif command == 'ls':
				while i < length and not data[i].startswith('$'):
					if data[i].startswith('dir'):
						_, folder_name = data[i].split()
						if folder_name not in current.folders:
							new_folder = Folder(current, folder_name)
							current.add_folder(new_folder)
							# print(current)
					else:
						size, file_name = data[i].split()
						size = int(size)
						if file_name not in current.files:
							file = File(file_name, size)
							current.add_file(file)
							# print(file)
					i += 1

	return root


def part_one(root):
	result = 0
	for folder in root.folders.values():
		result += part_one(folder)

	size = root.calculate_size()
	if size <= 100000:
		result += size

	return result



def part_two(root, needed_space=None):
	total_space = 70000000
	required_space = 30000000
	if needed_space is None:
		current_space = total_space - root.calculate_size()
		needed_space = required_space - current_space

	minimum = root.calculate_size()
	for folder in root.folders.values():
		local_min = part_two(folder, needed_space)
		if local_min > needed_space:
			if local_min < minimum:
				minimum = local_min
	print('best min found so far:', minimum)
	return minimum


if __name__ == '__main__':
	data = load()
	data = parse(data)
	# print(data)

	start_time = time.time()
	print('Part One:', part_one(data))
	print(f'--- {time.time() - start_time} seconds ---')
	
	start_time = time.time()
	print('Part Two:', part_two(data))
	print(f'--- {time.time() - start_time} seconds ---')
