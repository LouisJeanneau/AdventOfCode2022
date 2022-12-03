sum = 0

'''
input_str = input()
while input_str != "":
    first, second = input_str[:len(input_str) // 2], input_str[len(input_str) // 2:]
    #print(first, second)
    for c in first:
        #print(c, end=' ')
        if (second.find(c) != -1):
            #print(" FOUND ")
            if "a" <= c <= "z":
                sum += (ord(c) - 96)
            else:
                sum += (ord(c) - 38)
            break
    #print()
    input_str = input()
print(sum)
'''

# Part 2
bags = [input() for i in range(3)]
while bags != ["","",""]:
    for c in bags[0]:
        if (bags[1].find(c) != -1 and bags[2].find(c) != -1):
            if "a" <= c <= "z":
                sum += (ord(c) - 96)
            else:
                sum += (ord(c) - 38)
            break
    bags = [input() for i in range(3)]
print(sum)
