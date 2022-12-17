# On lit la liste des rucksacks depuis l'entrée standard
rucksacks = []

# On lit les rucksacks depuis l'entrée standard, jusqu'à ce que l'utilisateur entre une ligne vide
while True:
  rucksack = input().strip()
  if rucksack == "":
    break
  rucksacks.append(rucksack)

# On initialise la somme des priorités à zéro
sum_of_priorities = 0

'''
# Pour chaque rucksack
for rucksack in rucksacks:
  # On calcule la longueur des compartiments (on suppose qu'ils ont la même longueur)
  compartment_length = len(rucksack) // 2

  # On extrait les deux compartiments du rucksack
  compartment1 = rucksack[:compartment_length]
  compartment2 = rucksack[compartment_length:]

  # On calcule l'intersection des deux compartiments (les éléments qui apparaissent dans les deux compartiments)
  intersection = set(compartment1) & set(compartment2)

  # On calcule la priorité de l'élément de l'intersection
  item = list(intersection)[0]
  priority = ord(item) - ord('a') + 1 if item.islower() else ord(item) - ord('A') + 27

  # On ajoute la priorité à la somme des priorités
  sum_of_priorities += priority

# On affiche la somme des priorités
print("Somme des priorités :", sum_of_priorities)
'''


# Initialize a variable to keep track of the sum of the priorities of the
# items that appear in all three rucksacks in each group
total = 0

# Iterate through the list of rucksacks in groups of three
for i in range(0, len(rucksacks), 3):
    # Find the items that appear in all three rucksacks in the group
    # by creating three sets from the items in each rucksack, and then
    # taking the intersection of the three sets
    common_items = set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])
    # Iterate through the common items
    for item in common_items:
        # Add the priority of the item to the total
        if item.islower():
            total += ord(item) - 96
        else:
            total += ord(item) - 38

# Print the sum of the priorities of the items that appear in all three
# rucksacks in each group
print(total)
