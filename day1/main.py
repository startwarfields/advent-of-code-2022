import argparse
import time
import numpy as np

def get_max_calorie_elf(elf_list):
    current_elf = 0
    elves = dict()
    num_snacks = 0
    for line in elf_list:
        if line == '\n':
            current_elf += 1
        else:
            num_snacks += 1
            if current_elf not in elves:
                elves[current_elf] = 0
            elves[current_elf] += int(line)
    print("Number of snacks: {}".format(num_snacks))
    return sorted(elves.values(), reverse=True)


def main(args):

    elf_list = open(args.input, 'r')
    t1 = time.time()
    max_calories = get_max_calorie_elf(elf_list)
    t2 = time.time()
    elf_list.close()
    
    # print("The max calories is: {}".format(max_calories))
    print("Total time: {}".format(t2-t1))
    print("The top {} elves are: {}".format(args.num_top_elves, max_calories[:args.num_top_elves]))
    print("The total sum is {}".format(sum(max_calories[:args.num_top_elves])))
    print("The smallest elf is {}".format(max_calories[-1]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 1 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    parser.add_argument('-n', '--num_top_elves', help = 'Input file', required = False, default = 3)
    args = parser.parse_args()
    main(args)