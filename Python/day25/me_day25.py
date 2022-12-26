match = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

reverse_match = {
    -2: "=",
    -1: "-",
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
    5: "0"
}


def int_to_snafu(total):
    i = 0
    snafu = ""
    c = 0
    while 5 ** (i - 1) < total:
        r = (total % 5 ** (i + 1)) // (5 ** i) + c
        c = r > 2
        # print(reverse_match[a])
        snafu = reverse_match[r] + snafu
        i += 1
    return snafu


def snafu_to_int(snafu):
    total = 0
    for i in range(0, len(snafu)):
        total += match[snafu[-i - 1]] * 5 ** i
    return total


with open("input.txt") as f:
    input = f.read().splitlines()
    total = 0
    for number in input:
        total += snafu_to_int(number)
    print(total)

    s = int_to_snafu(total)

    print(s)
    # pas 2-==00--=-0101==1201

