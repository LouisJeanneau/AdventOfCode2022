from sympy import symbols, solve
import sympy as sp

dict = {}


def calculus(name: str):
    # assert name != "humn", "pas bon"
    funct = dict[name]
    if isinstance(funct, int):
        return funct

    oper = funct[1]
    left = calculus(funct[0])
    right = calculus(funct[2])
    ans = eval(str(left) + oper + str(right))
    return ans


def print_equation(name: str):
    if name == "humn":
        return "x"
    funct = dict[name]
    if isinstance(funct, int):
        return str(funct)

    oper = funct[1]
    left = print_equation(funct[0])
    right = print_equation(funct[2])
    s = "(" + left + oper + right + ")"
    return s


with open("input.txt") as f:
    input = f.read().splitlines()
    for i in range(len(input)):
        s = input[i].split()
        if len(s) > 2:
            dict[s[0][:-1]] = tuple(s[1:])
        else:
            dict[s[0][:-1]] = int(s[1])

    # print(dict)
    # Part 1
    print(calculus("root"))

    # Did some search with assert, the right part of root is non dependant of "humn", so we do the calculus of the right part
    r = calculus(dict["root"][2])
    print(r)

    eq = print_equation(dict["root"][0]) + "-" + str(r)
    print(eq)
    peq = sp.parse_expr(eq)
    print(peq)
    print(int(solve(peq)[0]))
