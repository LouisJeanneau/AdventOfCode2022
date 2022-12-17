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

def parse_input(file):
    input_str = open("input.txt").read()
    lines = input_str.strip().split("\n")
    all_directory = Directory("root")
    current_dir = "/"
    for line in lines:
        if line.startswith("$ cd"):
            # Split the line into parts and extract the argument
            parts = line.split()
            if len(parts) > 1:
                arg = parts[2]
                if arg == "/":
                    # If the argument is /, switch to the outermost directory
                    current_dir = "/"
                elif arg == "..":
                    # If the argument is .., move out one level
                    current_dir = current_dir[:current_dir[:-1].rfind("/")+1]
                else:
                    # Otherwise, move into the specified directory
                    current_dir += arg + "/"
        elif not line.startswith("$ ls"):
            # Split the line into parts and extract the list of items
            parts = line.split()
            if parts[0] == "dir":
                # If the item is a directory, add it to the current directory
                name = parts[1]
                directory = Directory(current_dir + name + "/")
                all_directory.contents[current_dir] = directory
                all_directory.add_directory(directory)
            else:
                # If the item is a file, extract the name and size and add it to the current directory
                name, size = parts[1], parts[0]
                file = File(name, int(size))
                all_directory.contents[current_dir].add_file(file)
    return all_directory

filesystem = parse_input("input.txt")
print(filesystem)