import argparse
def main(args):
    # Parse the input file
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    for packet in elf_lines:
        duplicates = list()
        current_set = list()
        for idx,letter in enumerate(packet):
            if len(current_set) < args.numberDistinct:
                current_set.append(letter)
            else:
                if letter in current_set or letter in duplicates:
                    # ensure in duplicates
                    if letter not in duplicates:
                        duplicates.append(letter)
                    # remove the first letter in the set
                    current_set.pop(0)
                    current_set.append(letter)
                else:
                    current_set.pop(0)
                    current_set.append(letter)
            # check current set is unique
            if len(set(current_set)) >= args.numberDistinct:
                print(idx+1)
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    parser.add_argument('-n', '--numberDistinct', help = 'Number of distinct letters',default=4, type=int)
    args = parser.parse_args()
    main(args)