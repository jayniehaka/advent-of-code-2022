with open('input_4.txt') as input:
    lines = input.read()

elf_pairs = lines.split("\n")

def get_elf_pair_sections(elf_pair):
    sections = elf_pair.split(',')
    return sections
# '2-4,6-8' => ['2-4', '6-8']

def get_section_list(section):
    section_range = section.split('-')
    section_range_int = list(map(int, section_range))
    section_list = list(range(section_range_int[0], section_range_int[1] + 1))
    return section_list
# '2-4' => [2, 3, 4]

def check_subset_pairs(section_a, section_b):
    set_a = set(section_a)
    set_b = set(section_b)

    if set_a.issubset(set_b):
        return True
    elif set_b.issubset(set_a):
        return True
    else:
        return False
# [2, 3, 4], [6, 7, 8] => False

problematic_elf_pairs = []

# loop through elf pairs and if one is a subset of the other then add to list
for elf_pair in elf_pairs:
    sections = get_elf_pair_sections(elf_pair = elf_pair)
    section_list_a = get_section_list(sections[0])
    section_list_b = get_section_list(sections[1])
    outcome = check_subset_pairs(section_list_a, section_list_b)

    problematic_elf_pairs.append(outcome)
exit

print(sum(problematic_elf_pairs))

# part 2

def check_intersect_pairs(section_a, section_b):
    return bool(set(section_a) & set(section_b))

problematic_elf_pairs_2 = []

for elf_pair in elf_pairs:
    sections = get_elf_pair_sections(elf_pair = elf_pair)
    section_list_a = get_section_list(sections[0])
    section_list_b = get_section_list(sections[1])
    outcome = check_intersect_pairs(section_list_a, section_list_b)

    problematic_elf_pairs_2.append(outcome)
exit

print(sum(problematic_elf_pairs_2))