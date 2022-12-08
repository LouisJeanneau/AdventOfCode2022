input_str = input()

'''
# Part 1
current = input_str[:4]
input_str = input_str[1:]
pos = 4

while len(set(current)) != 4:
    pos += 1
    current = input_str[:4]
    input_str = input_str[1:]
    '''

current = input_str[:14]
input_str = input_str[1:]
pos = 14

while len(set(current)) != 14:
    pos += 1
    current = input_str[:14]
    input_str = input_str[1:]

print(pos)