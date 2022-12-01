import argparse
import numpy as np

def generate_input_dataset(num_elves):
    with open('large_input.txt', 'w') as f:
        for i in range(num_elves):
            elf_sz = np.random.randint(1, 15)
            items = generate_random_numpy_array(elf_sz)
            for j in items:
                f.write(str(j) + '\n')
            f.write('\n')
    

def generate_random_numpy_array(size):
    return np.random.randint(1000, 100000, size)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 1 Advent of Code 2022: Challenge",
                                    description = "Extend the first day of Advent of Code 2022 with MIPS Scale Elves" )
    parser.add_argument('-n', '--num_elves', help = 'Number of elves', required = False, default = 10_000_000)

    args = parser.parse_args()
    generate_input_dataset(args.num_elves)