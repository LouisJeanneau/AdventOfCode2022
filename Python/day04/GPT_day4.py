# Parse the input into pairs of ranges
pairs = []
while True:
  line = input()
  if line == '':
    break
  parts = line.strip().split(',')
  start1, end1 = map(int, parts[0].split('-'))
  start2, end2 = map(int, parts[1].split('-'))
  pairs.append(((start1, end1), (start2, end2)))

'''
# Count the number of pairs in which one range fully contains the other
count = 0
for pair in pairs:
  if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
    count += 1
  elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
    count += 1
'''
# Count the number of pairs that overlap
count = 0
for pair in pairs:
  if not (pair[0][1] < pair[1][0] or pair[1][1] < pair[0][0]):
    count += 1
# Print the result
print(count)
