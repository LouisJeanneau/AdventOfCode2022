# define a dictionary to store the total Calories for each Elf
elf_calories = {}

# define a variable to store the current Elf ID
current_elf = 1

input_str = "0"

# read input until there is nothing left
while input_str != "-0":
  # read a line of input
  input_str = input()
  if input_str == "-0":
      break
  # check if the line is a blank line
  if input_str == "":
    # if it is a blank line, increment the Elf ID
    current_elf += 1
  else:
    # if it is not a blank line, add the Calories to the total for the current Elf
    if current_elf not in elf_calories:
      # create a new entry in the dictionary for the current Elf
      elf_calories[current_elf] = 0
    # add the Calories from the current line to the total for the current Elf
    elf_calories[current_elf] += int(input_str)

# find the Elf carrying the most Calories
# sort the entries in the dictionary by the total Calories in descending order
sorted_elf_calories = sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)

# take the first three elements from the sorted list
top_three = sorted_elf_calories[:3]

# sum the total Calories for the top three Elves
total_calories = 0
for elf, calories in top_three:
  total_calories += calories

# print the total Calories for the top three Elves
print(total_calories)
