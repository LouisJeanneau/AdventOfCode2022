import string

for i in range(5, 26):
    f = open("me_day" + str(i) + ".py", "w")
    f.close()
    f = open("GPT_day" + str(i) + ".py", "w")
    f.close()
