import argparse
def get_max_calorie_elf(elf_list):
    current_elf = 0
    elves = dict()
    for line in elf_list:
        if line == '\n':
            current_elf += 1
        else:
            if current_elf not in elves:
                elves[current_elf] = 0
            elves[current_elf] += int(line)
    return max(elves.values())


def main(input_file):

    elf_list = open(input_file, 'r')
    max_calories = get_max_calorie_elf(elf_list)
    elf_list.close()
    
    print("The max calories is: {}".format(max_calories))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 1 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args.input)