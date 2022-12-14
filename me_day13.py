def compare(left, right):
    a = []
    if len(left) == len(right) == 0:
        return -1
    elif len(left) == 0 or len(right) == 0:
        return len(left) < len(right)
    elif isinstance(left[0], int) and isinstance(right[0], int):
        if left[0] == right[0]:
            a = compare(left[1:], right[1:])
        else:
            return left < right
    elif type(left[0]) == type(right[0]) == list:
        a = compare(left[0], right[0])
    elif type(left[0]) == int:
        t = [left[0]]
        a = compare(t, right[0])
    elif type(right[0]) == int:
        t = [right[0]]
        a = compare(left[0], t)
    if isinstance(a, bool):
        return a
    else:
        return compare(left[1:], right[1:])

'''
part 1
with open("input.txt") as f:
    input = f.read().splitlines()
    pairs = (len(input)+1)//3
    sum = 0
    for i in range(pairs):
        sum += (i+1) * compare(eval(input[3*i]), eval(input[3*i+1]))
    print(sum)
'''

def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(lst) - 1):
            if not compare(lst[i], lst[i + 1]):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True

    return lst

with open("input.txt") as f:
    input = f.read().splitlines()
    while input.count(""):
        input.remove("")
    for i in range(len(input)):
        input[i] = eval(input[i])
    input.append([[2]])
    input.append([[6]])
    res = bubble_sort(input)
    print( (res.index([[2]])+1) * (res.index([[6]])+1) )