#magical energy
# snack => star
# fifty stars
def main():
    input_str="0"
    total_calories = [0]
    index = 0

    while input_str != "end":
        print(input_str)
        if input_str =="":
            total_calories.append(0)
        else:
            total_calories[-1] += int(input_str)
        input_str = input()
    total_calories.sort()
    print(total_calories)
    return sum(total_calories[:-4:-1])

print(main())