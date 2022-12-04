import argparse

def main(args):
    # Read in the file
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    total_subsets = 0
    for line in elf_lines:
        # Parse the line
        line = line.strip()
        line = line.split(',')
        
        first_set = section_parser(line[0])
        second_set = section_parser(line[1])
        # check if either is a subset of the other
       # if first_set <= second_set or second_set <= first_set:
        #    total_subsets += 1
        # check if either overlaps the other
        if len(first_set.intersection(second_set)) > 0:
            total_subsets += 1

    print(total_subsets)


def section_parser(section_str):
    # String '2-4' represents sections 2, 3, and 4
    # return a set of integers
    section_str = section_str.split('-')
    section_set = set()
    for i in range(int(section_str[0]), int(section_str[1]) + 1):
        section_set.add(i)
    return section_set


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)