with open('input_1.txt') as input:
    lines = input.read()

elves = lines.split("\n\n")

def sum_calories(n):
    snacks = n.split("\n")
    snacks_int = list(map(int, snacks))
    total_calories = sum(snacks_int)
    return total_calories

elf_calories = list(map(sum_calories, elves))

print(max(elf_calories))

elf_calories_sorted = sorted(elf_calories, reverse = True)

top_three = elf_calories_sorted[0:3]

top_three_sum = sum(top_three)

print(top_three_sum)