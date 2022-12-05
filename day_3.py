import string

# part 1

with open('input_3.txt') as input:
    rucksacks = input.read().split("\n")

def find_wrong_item (rucksack):
    middle = int(len(rucksack) / 2)
    compartment_a = rucksack[:middle]
    compartment_b = rucksack[-middle:]
    wrong_item = set(compartment_a).intersection(compartment_b).pop()
    return str(wrong_item)

wrong_items = list(map(find_wrong_item, rucksacks))

keys = list(string.ascii_lowercase) + list(string.ascii_uppercase)
values = range(1, 53)
alpha_dict = dict(zip(keys, values))

priorities = [*map(alpha_dict.get, wrong_items)]

print(sum(priorities))

# part 2

number_of_groups = int(len(rucksacks) / 3)

def find_badge (group_rucksacks):
    badge = set(group_rucksacks[0]) & set(group_rucksacks[1]) & set(group_rucksacks[2]) 
    return badge.pop()

badges = []

for group in range(1, number_of_groups + 1):
    group_rucksacks = rucksacks[group * 3 - 3:group * 3]
    badge = find_badge(group_rucksacks)
    badges.append(badge)

badge_priorities = [*map(alpha_dict.get, badges)]

print(sum(badge_priorities))
