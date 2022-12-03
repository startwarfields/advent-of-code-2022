import argparse



ascii_dict = {
'a': 1,
'b': 2,
'c': 3,
'd': 4,
'e': 5,
'f': 6,
'g': 7,
'h': 8,
'i': 9,
'j': 10,
'k': 11,
'l': 12,
'm': 13,
'n': 14,
'o': 15,
'p': 16,
'q': 17,
'r': 18,
's': 19,
't': 20,
'u': 21,
'v': 22,
'w': 23,
'x': 24,
'y': 25,
'z': 26,
'A': 27,
'B': 28,
'C': 29,
'D': 30,
'E': 31,
'F': 32,
'G': 33,
'H': 34,
'I': 35,
'J': 36,
'K': 37,
'L': 38,
'M': 39,
'N': 40,
'O': 41,
'P': 42,
'Q': 43,
'R': 44,
'S': 45,
'T': 46,
'U': 47,
'V': 48,
'W': 49,
'X': 50,
'Y': 51,
'Z': 52,


}
def main_old(args):
    # Read in the file
    elf_file = open(args.input, 'r')
    # Read in the file
    total_sum = 0
    for line in elf_file:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for i in range(len(first_half)):
                if first_half[i] in second_half:
                    print("Found a match: {}".format(first_half[i]))
                    print("Ord value is {}".format(ascii_dict[first_half[i]]))
                    total_sum += ascii_dict[first_half[i]]
                    
        
    print(total_sum)


def main(args):
    # Read in the file
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    # Read in the file
    total_sum = 0
    for idx in range(len(elf_lines))[::3]:
        first_word = elf_lines[idx].strip()
        second_word = elf_lines[idx+1].strip()
        third_word = elf_lines[idx+2].strip()

        for i in range(len(first_word)):
            if first_word[i] in second_word and first_word[i] in third_word:
                    print("Found a match: {}".format(first_word[i]))
                    print("Ord value is {}".format(ascii_dict[first_word[i]]))
                    total_sum += ascii_dict[first_word[i]]
                    break
        # idx+=2
        
    print(total_sum)

    # pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)