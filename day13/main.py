import argparse
import json
from functools import cmp_to_key
def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    # Convert "[1,1,3,1,1]" to [1,1,3,1,1]
    answer = 0
    list_pairs = []
    pair_index = 1
    # Index skips by 3
    lists = []
    for idx, line in enumerate(elf_lines):
       
        if idx % 3 != 0:
             continue

      

        # print("On line:", idx)
        left = elf_lines[idx]

        right = elf_lines[idx + 1]
        # print("Left is:", left, idx)
        # print("Right is:", right)
        left_list = json.loads(str(left))
        
        right_list = json.loads(str(right))
        print('-'*20)
        print("Pair ", pair_index, " is ", left_list)
        print("and ", right_list)
        # Print nested list as a tree
      

        answer_res = compare_items(left_list, right_list)
        if answer_res == 1:
            print("Adding to answer", pair_index)
            answer += pair_index
        else:

            print("Error code:", answer_res)
            # pass
        pair_index += 1
        # print(left_list, "\n", right_list)
        # print("\n")
        lists.append(left_list)
        lists.append(right_list)
    
    # Sort lists using compare_items
    lists = sorted(lists, key=cmp_to_key(compare_items), reverse=True)

    key_a = [[2]]
    key_b = [[6]]

    # get index of key_a
    index_a = lists.index(key_a)
    index_b = lists.index(key_b)

    print("Answer 2", (index_a+1) * (index_b+1))
    print(lists)

       

    print("Total Pairs:", pair_index)
    print("Answer:", answer)


def print_tree(tree, level=0):
    for item in tree:
        if type(item) == list:
            print_tree(item, level + 1)
        else:
            print("  "*level, item)

def compare_items_wrapper(left, right):
    if compare_items(left,  right) == 1:
        return True
    else:
        return False



def compare_items(left, right):
    
    # If both values are integers, the left integer should be less than the right integer
    if isinstance(left, int) and isinstance(right, int):
       
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            print("Hit false on ", left, right)
            return -1
    # If both values are lists, compare the first item in each list
    elif isinstance(left, list) and isinstance(right, list):
        # Check if empty
        idx = 0

        while idx < len(left) and idx < len(right):
            comparison = compare_items(left[idx], right[idx])
            if comparison == -1:
                return -1
            elif comparison == 1:
                return 1
            
            idx += 1
        # If the left list is longer than the right list, compare the first item in the left list to the last item in the right list
        if len(left) > len(right):
            print("Left is longer")
            return -1
        if len(left) < len(right):
            return 1
        return 0
                    

    # If the left value is a list and the right value is an integer, compare the first item in the list to the integer
    elif isinstance(left, list) and isinstance(right, int):
        return compare_items(left, [right])
    # If the left value is an integer and the right value is a list, compare the integer to the first item in the list
    elif isinstance(left, int) and isinstance(right, list):
        return compare_items([left], right)
            
    else:
        print("I shouldn't exist!")
    
        return -3


# Outline
# Compare Every 2 lines as pairs
# Each line contains a tree of numbers represented as lists of lists or integers






if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)


