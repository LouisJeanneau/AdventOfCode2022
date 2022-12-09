def find_marker(input_string):
    # Initialize the buffer with the first four characters from the input string
    buffer = list(input_string[:4])

    # Iterate through the input string
    for i in range(len(input_string)):
        # Shift the buffer to the left by one position
        buffer[0] = buffer[1]
        buffer[1] = buffer[2]
        buffer[2] = buffer[3]
        buffer[3] = input_string[i]

        # Check if the buffer contains only unique characters
        if len(set(buffer)) == 4:
            # If it does, return the current position plus one
            return i + 1


    # If no marker was found, return -1
    return -1

def find_marker_2(input_string):
    # Initialize the buffer with the first 14 characters from the input string
    buffer = list(input_string[:14])

    # Iterate through the input string
    for i in range(len(input_string)):
        # Shift the buffer to the left by one position
        buffer[0] = buffer[1]
        buffer[1] = buffer[2]
        buffer[2] = buffer[3]
        buffer[3] = buffer[4]
        buffer[4] = buffer[5]
        buffer[5] = buffer[6]
        buffer[6] = buffer[7]
        buffer[7] = buffer[8]
        buffer[8] = buffer[9]
        buffer[9] = buffer[10]
        buffer[10] = buffer[11]
        buffer[11] = buffer[12]
        buffer[12] = buffer[13]
        buffer[13] = input_string[i]

        # Check if the buffer contains only unique characters
        if len(set(buffer)) == 14:
            # If it does, return the current position plus one
            return i + 1

    # If no marker was found, return -1
    return -1

from collections import deque

# Asked it to be less verbose
def find_marker_not_verbose(input_string):
    # Initialize the buffer with the first 14 characters from the input string
    buffer = deque(input_string[:14])

    # Iterate through the input string
    for i in range(len(input_string)):
        # Shift the buffer to the left by one position and add the current character
        buffer.popleft()
        buffer.append(input_string[i])

        # Check if the buffer contains only unique characters
        if len(set(buffer)) == 14:
            # If it does, return the current position plus one
            return i + 1

    # If no marker was found, return -1
    return -1



line = input()
print(find_marker(line))
print(find_marker_2(line))
print(find_marker_not_verbose(line))