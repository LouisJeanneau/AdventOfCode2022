# create a dictionary to map letters to shapes
shapes = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

# initialize the total score to 0
total_score = 0

'''
# Part 1
i = input()
# loop through each line of the strategy guide
while i != "":
    # split the line into the opponent's choice and your response
    opponent, response = i.split()

    # look up the shapes using the dictionary
    opponent_shape = shapes[opponent]
    response_shape = shapes[response]

    # initialize the round score to the score for your response shape
    # (1 for Rock, 2 for Paper, 3 for Scissors)
    round_score = 0
    if response_shape == 'Rock':
        round_score = 1
    elif response_shape == 'Paper':
        round_score = 2
    else:
        round_score = 3

    # determine the outcome of the round
    if opponent_shape == response_shape:
        # if it's a draw, add 3 points to the round score
        round_score += 3
    elif (opponent_shape == 'Rock' and response_shape == 'Scissors') or (
            opponent_shape == 'Scissors' and response_shape == 'Paper') or (
            opponent_shape == 'Paper' and response_shape == 'Rock'):
        # if the opponent wins, add 0 points to the round score
        pass
    else:
        # if you win, add 6 points to the round score
        round_score += 6

    # add the round score to the total score
    total_score += round_score

    i = input()

# print the total score
print(total_score)
'''
# Part 2
i = input()
# loop through each line of the strategy guide
while i != "":
    # split the line into the opponent's choice and the desired outcome
    opponent, outcome = i.split()

    # look up the shapes using the dictionary
    opponent_shape = shapes[opponent]

    # determine the shape you should choose to achieve the desired outcome
    response_shape = None
    if opponent_shape == 'Rock':
        if outcome == 'X':
            response_shape = 'Scissors'
        elif outcome == 'Y':
            response_shape = 'Rock'
        else:
            response_shape = 'Paper'
    elif opponent_shape == 'Paper':
        if outcome == 'X':
            response_shape = 'Rock'
        elif outcome == 'Y':
            response_shape = 'Paper'
        else:
            response_shape = 'Scissors'
    else:
        if outcome == 'X':
            response_shape = 'Paper'
        elif outcome == 'Y':
            response_shape = 'Scissors'
        else:
            response_shape = 'Rock'

    # initialize the round score to the score for your response shape
    # (1 for Rock, 2 for Paper, 3 for Scissors)
    round_score = 0
    if response_shape == 'Rock':
        round_score = 1
    elif response_shape == 'Paper':
        round_score = 2
    else:
        round_score = 3

    # determine the outcome of the round
    if opponent_shape == response_shape:
        # if it's a draw, add 3 points to the round score
        round_score += 3
    elif (opponent_shape == 'Rock' and response_shape == 'Scissors') or (
            opponent_shape == 'Scissors' and response_shape == 'Paper') or (
            opponent_shape == 'Paper' and response_shape == 'Rock'):
        # if the opponent wins, add 0 points to the round score
        pass
    else:
        # if you win, add 6 points to the round score
        round_score += 6

    # add the round score to the total score
    total_score += round_score

    i = input()

# print the total score
print(total_score)
