
dict = {}

def calculus(name: str):
    funct = dict[name]
    if isinstance(funct, int):
        return funct

    oper = funct[1]
    left = calculus(funct[0])
    right = calculus(funct[2])
    ans = eval(str(left) + oper + str(right))
    return ans

with open("input.txt") as f:
    input = f.read().splitlines()
    for i in range(len(input)):
        s = input[i].split()
        if len(s) > 2:
            dict[s[0][:-1]] = tuple(s[1:])
        else:
            dict[s[0][:-1]] = int(s[1])

    # print(dict)
    print(calculus("root"))
