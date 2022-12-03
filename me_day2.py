"""
https://adventofcode.com/2022/day/2
"""
# rock paper scissors tournament

# A = Rock = 65, B = Paper = 66, C = Scissors = 67
# X = Rock = 88, Y = Paper = 89, Z = Scissors = 90

# Draw : 5720 or 5874 or 6030
# Win : 5896 or 5785 or 5940
score = 0

input_str=input()
while input_str != "":
    him, me = input_str.split(" ")
    h, m = ord(him), ord(me)
    r = h*m
    # Win for me
    if r == 5896 or r==5785 or r==5940:
        score += 6
    # Draw
    elif r==5720 or r==5874 or r==6030:
        score += 3
    score += (m-87)
    input_str = input()
print(score)