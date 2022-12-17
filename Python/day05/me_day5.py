'''
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

# If X is number of stacks, the len of each line is X*4-1
# len = X*4 - 1
# The number of stacks is thus X = (len + 1)//4
from queue import Queue

# We create initial stacks status
import re

input_stack = input()
num_stacks = (len(input_stack) + 1) // 4
stacks_reversed = [[] for _ in range(num_stacks)]

while input_stack != "" and input_stack.find("[") != -1:
    for i in range(num_stacks):
        if input_stack[i * 4 + 1] != " ":
            stacks_reversed[i].append(input_stack[i * 4 + 1])
    input_stack = input()

stacks = [stacks_reversed[i][::-1] for i in range(num_stacks)]

input()  # empty line
# we start modifying
input_stack = input()
while input_stack != "":
    how_many, origin, dest = re.split("move | from | to ", input_stack)[1:]
    h, o, d = int(how_many), int(origin), int(dest)
    '''
    # Part 1
    for i in range(j):
        stacks[d-1].append(stacks[o-1].pop())
    '''
    # Part 2
    stacks[d - 1].extend(stacks[o - 1][-h:])
    for i in range(h):
        stacks[o - 1].pop()
    # End part 2
    input_stack = input()

print("".join(stacks[i][-1] for i in range(num_stacks)))
