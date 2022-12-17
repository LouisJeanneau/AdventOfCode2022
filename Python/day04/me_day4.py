input_str = input()
pairs = 0

while input_str != "":
    # print(input_str)
    elf1, elf2 = input_str.split(',')
    elf1low, elf1high = elf1.split("-")
    elf2low, elf2high = elf2.split('-')

    '''
    if (int(elf1low) <= int(elf2low) and int(elf1high) >= int(elf2high)) or (int(elf1low) >= int(elf2low) and int(elf1high) <= int(elf2high)):
        pairs += 1
    '''
    if (int(elf2low) <= int(elf1low) <= int(elf2high)) or (int(elf1low) <= int(elf2low) <= int(elf1high)):
        pairs += 1
    input_str = input()
print(pairs)
