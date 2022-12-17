import collections

input_str = input()
current = ""
folder = collections.OrderedDict()

while input_str != "":
    split = input_str.split()
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] == "..":
                current = current[:current[:-1].rfind('/') + 1]
            elif split[2] == "/":
                current = "/"
            else:
                current += split[2] + "/"
    else:
        l = folder.pop(current, [])
        if split[0] == "dir":
            l.append(split[1])
        else:
            l.append((split[0], split[1]))
        folder[current] = l

    input_str = input()

size = {}

for dir, content in reversed(folder.items()):
    for item in content:
        value = size.pop(dir, 0)
        if isinstance(item, tuple):
            value += int(item[0])
        else:
            value += size[dir + item + "/"]
        size[dir] = value

# Part 1
# print(sum([a for a in size.values() if a<=100000]))

# Part 2
print([v for v in sorted(size.values()) if size["/"] - 40000000 <= v][0])
