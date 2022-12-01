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
    return sorted(elves.values(), reverse=True)


def main(args):

    elf_list = open(args.input, 'r')
    max_calories = get_max_calorie_elf(elf_list)
    elf_list.close()
    
    # print("The max calories is: {}".format(max_calories))
    print("The top {} elves are: {}".format(args.num_top_elves, max_calories[:args.num_top_elves]))
    print("The total sum is {}".format(sum(max_calories[:args.num_top_elves])))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 1 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    parser.add_argument('-n', '--num_top_elves', help = 'Input file', required = False, default = 3)
    args = parser.parse_args()
    main(args)