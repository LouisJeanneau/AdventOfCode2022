import os
import shutil
import string

for i in range(1, 26):
    '''
    f = open("me_day" + str(i) + ".py", "w")
    f.close()
    f = open("GPT_day" + str(i) + ".py", "w")
    f.close()
    '''
    # f = os.mkdir(f'day{i:0>2}')
    # shutil.move(f'me_day{i}.py', f'day{i:0>2}/')
    # shutil.move(f'GPT_day{i}.py', f'day{i:0>2}/')

    f = open(f'day{i:0>2}/input.txt', "w")
    f.close()
    f = open(f'day{i:0>2}/demo.txt', "w")
    f.close()