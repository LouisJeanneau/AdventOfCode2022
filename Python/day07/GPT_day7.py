class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_file(self, file):
        self.contents[file.name] = file

    def add_directory(self, directory):
        self.contents[directory.name] = directory

    def get_size(self):
        size = 0
        for item in self.contents.values():
            if isinstance(item, File):
                size += item.size
            elif isinstance(item, Directory):
                size += item.get_size()
        return size

def parse_input(input_str):
    lines = input_str.strip().split("\n")
    root = Directory("/")
    current_directory = root
    for line in lines:
        if line.startswith("$ cd"):
            # Split the line into parts and extract the argument
            parts = line.split()
            if len(parts) > 1:
                arg = parts[2]
                if arg == "/":
                    # If the argument is /, switch to the outermost directory
                    current_directory = root
                elif arg == "..":
                    # If the argument is .., move out one level
                    # TODO
                else:
                    # Otherwise, move into the specified directory
                    current_directory = current_directory.contents[arg]
        elif not line.startswith("$ ls"):
            # Split the line into parts and extract the list of items
            item = line.split()
            if item[0] == "dir":
                # If the item is a directory, add it to the current directory
                name = item[1]
                directory = Directory(name)
                current_directory.add_directory(directory)
            else:
                # If the item is a file, extract the name and size and add it to the current directory
                size, name = item
                file = File(name, int(size))
                current_directory.add_file(file)
    return current_directory

def find_small_directories(root, max_size):
    small_directories = []
    for item in root.contents.values():
        if isinstance(item, Directory):
            if item.get_size() <= max_size:
                small_directories.append(item)
            else:
                small_directories += find_small_directories(item, max_size)
    return small_directories

def sum_small_directories(root, max_size):
    small_directories = find_small_directories(root, max_size)
    total_size = 0
    for directory in small_directories:
        total_size += directory.get_size()
    return total_size

with open("input.txt") as f:
    input_str = f.read()

# Non-working
filesystem = parse_input(input_str)
total_size = sum_small_directories(filesystem, 100000)
print(total_size)

