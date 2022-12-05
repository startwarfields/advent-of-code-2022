import argparse
def main(args):
    # Read in the file
    
    stack_dict = dict()
    # Create a dictionary of stacks

    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    total_subsets = 0
    for line in elf_lines:
        if '[' in line:
            # This is a stack

            stack_dict = parse_current_crates(line, stack_dict)
            print(stack_dict) 
        if 'move' in line:
            # stack_dict = parse_moves(line, stack_dict)
            stack_dict = parse_alternate_moves(line, stack_dict)
         

    print(stack_dict)
    # loop through keys in dictionary in order
    result_string = ''
    for key in sorted(stack_dict.keys()):
        print(stack_dict[key][-1])
        result_string += stack_dict[key][-1]

    print(result_string)

def parse_current_crates(line, stack_dict):
    # Parse the line into a list of integers
    # [A] [B]
    #  1  2
    # means A is on stack 1 and B is on stack 2
    current_stack = 0
    for idx in range(1,len(line))[::4]:
        current_stack+=1
        if line[idx] == ' ':
            continue
        if current_stack not in stack_dict:
            stack_dict[current_stack] = list()
            stack_dict[current_stack].insert(0,line[idx])
        # reverse all the stacks
        else:
            stack_dict[current_stack].insert(0,line[idx])
    return stack_dict



def parse_moves(line, stack_dict):
    # Parse the line into a list of integers
    # move 1 from 2 to 1
    # means move the crate on stack 2 to stack 1
    line = line.split(' ')
    print(line)
    number_of_moves = int(line[1])
    source_stack = int(line[3])

    # remove '\n' from the end of the line, if it exists
    if line[5][-1] == '\n':
        line[5] = line[5][:-1]
    dest_stack = int(line[5])
    # Get index of target in source stack
    
    while number_of_moves > 0:
        # Remove first element from source stack
        # and add it to the destination stack
        
        stack_dict[dest_stack].append(stack_dict[source_stack].pop())
        number_of_moves-=1
        print(stack_dict)
    return stack_dict

def parse_alternate_moves(line, stack_dict):
    # Parse the line into a list of integers
    # move 1 from 2 to 1
    # means move the crate on stack 2 to stack 1
    line = line.split(' ')
    print(line)
    number_of_moves = int(line[1])
    source_stack = int(line[3])

    # remove '\n' from the end of the line, if it exists
    if line[5][-1] == '\n':
        line[5] = line[5][:-1]
    dest_stack = int(line[5])
    # Get index of target in source stack
    
   
        # Remove last n elements from source stack

    list_to_move = stack_dict[source_stack][-number_of_moves:]
    stack_dict[source_stack] = stack_dict[source_stack][:-number_of_moves]
    old_dest_stack = stack_dict[dest_stack]
    stack_dict[dest_stack] =  old_dest_stack + list_to_move
    number_of_moves-=1
    return stack_dict





if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)