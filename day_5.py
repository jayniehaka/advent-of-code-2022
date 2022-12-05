import re

with open('input_5.txt') as input:
    raw = input.read()

input_sections = raw.split("\n\n")

# CRATES

# parse crate stacks
stacks = input_sections[0].split("\n")

# remove last row which has the stack numbers
stacks.pop()

def get_crates_on_level(level, number_of_stacks):
    crates = []
    for stack_number in range(number_of_stacks):
        crate = level[(stack_number + 1) * 4 - 3]
        crates.append(crate)
    exit
    return crates

number_of_stacks = int((len(stacks[0]) + 1 ) / 4)

# iterate through each level and extract the crates
all_crates = []
for level in stacks:
    crates_on_level = get_crates_on_level(level=level, number_of_stacks=number_of_stacks)
    all_crates.append(crates_on_level)
exit

# transpose and turn it back into a list of lists
all_crates = [list(tup) for tup in zip(*all_crates)]

# get rid of spaces
tidy_crates = []
for stack in all_crates:
    no_space_stack = list(filter((' ').__ne__, stack))
    tidy_crates.append(no_space_stack)
exit

# MOVES

def get_move_info(move_str):
    move_info = re.findall("\d+", move_str)
    return [int(x) for x in move_info]

def do_the_move(move_info, stack_list):
    numer_of_crates = move_info[0]
    crate_moves = range(numer_of_crates)
    source_stack = move_info[1]
    target_stack = move_info[2]

    for crate_move in crate_moves:
        source_crate = stack_list[source_stack - 1].pop(0)
        stack_list[target_stack - 1].insert(0, source_crate)
    exit

    return stack_list

moves = input_sections[1].split("\n")

moved_crates = tidy_crates

for move in moves:
    move_info = get_move_info(move_str = move)
    moved_crates = do_the_move(move_info, moved_crates)
exit

# get letter at the top of each stack
top_crates = [stack[0] for stack in moved_crates]
print("".join(top_crates))

