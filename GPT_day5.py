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

# define the regular expression pattern
pattern = 'move \d+ from \d+ to \d+'

# iterate over the steps
input()
input_str = input()

while input_str != "":
    # Split the line on the 'from' keyword to get the first and second numbers
    a, b = input_str.split('from')
    # Remove the "move" keyword and the space after it from the first number
    a = a[5:]
    # Split the second number on the 'to' keyword to get the last number
    b, c = b.split('to')
    # Remove the space before the 'to' keyword from the second number
    b = b.strip()
    # Convert the numbers to integers
    a, b, c = map(int, (a, b, c))

    # move the crates one at a time
    for i in range(a):
        # remove the top crate from the source stack
        crate = stacks[b-1].pop()

        # append the crate to the destination stack
        stacks[c-1].append(crate)
    input_str = input()

    # No Part 2 cause i'm lazy and ChatGPT had a hard time understanding today's graphical input format

print("".join(stacks[i][-1] for i in range(num_stacks)))
