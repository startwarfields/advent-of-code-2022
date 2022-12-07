import argparse
import sys
def main(args):
    print("Recursion Limit", sys.getrecursionlimit())
    # sys.setrecursionlimit(100000)
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    
   
    tree = None
    i = 0
    for idx in range(len(elf_lines)):
        print("Index", idx, " At depth", i)
        print("Current line", elf_lines[idx])
        line = elf_lines[idx] 
        parsed_line = parse_command(line)
        if parsed_line[1] == "cd":
            print(parsed_line)
            if parsed_line[0] == '..' and tree.parent is not None:
                tree = tree.parent
                i -= 1
            elif parsed_line[0] == '.':
                pass

            elif parsed_line[0] == "/" and tree is None:
                tree = tree_node(parsed_line[0], "dir", 0, depth=i)
 
            elif parsed_line[0] in [child.name for child in tree.children]:
                for child in tree.children:
                    if child.name == parsed_line[0]:
                        tree = child
                        i += 1
           
            elif parsed_line[0] not in [child.name for child in tree.children]:
                i += 1
                tree.children.append(tree_node(parsed_line[0], "dir", 0,children=[], depth=i, parent=tree))
                tree = tree.children[-1]
            

        elif parsed_line[1] == "dir":
            if parsed_line[0] not in [child.name for child in tree.children]:
                # i += 1
                tree.children.append(tree_node(parsed_line[0], "dir", 0,children=[], depth=i, parent=tree))
               
        # check if a parsed line is an int
        elif parsed_line[1] == "output":
            line = line.split(' ')
            weight = int(line[0])
            name = line[1]
            tree.children.append(tree_node(name, "file", weight, children=[], depth=i, parent=tree))
   
                    
    # Print entire tree
    while tree.parent is not None:
        tree = tree.parent
    tree.set_directory_weight()
    print (tree)
    # print(tree)
    dir_list = tree.get_directories_over_n_weight(100000)
    total_weight = 0
    for d in dir_list:
        total_weight += d[1]
    print(total_weight)
    print("Total Space", tree.weight)
    used_space = tree.weight
    free_space = 70000000 - used_space
    required_free_space = 30000000
    needed_weight = required_free_space - free_space
    print("Needed Weight", needed_weight)

    # find directory with weight greater than needed weight
    closest_weight = dir_list[0][1]
    for d in dir_list:
        if d[1] > needed_weight and d[1] < closest_weight:
            closest_weight = d[1]
    print("Closest Weight", closest_weight)
        
    # find closest weight to needed weight from dir_list
  





def parse_command(line):
    line = line.split(' ')
    line = [l.strip() for l in line]
    if line[0] == 'dir':
        return ['a', 'dir', None]
    if line[1] == 'cd':
        return [line[2], 'cd', None]
    elif line[1] == 'ls':
        return ['ls', 'ls', None]
    return ['output', 'output', 'output']



class tree_node:
    def __init__(self, name, ntype, weight, children=[], parent=None, depth=0):
        self.name = name
        self.ntype = ntype
        if weight is not None:
            self.weight = int(weight)
        else:
            self.weight = 0
        self.children = children
        self.parent = parent
        self.depth = depth
    # Override print function
    def __str__(self):
        return self.print_tree()

    def print_tree(self):
        # Print parent and children as a formatted tree
        tree_print = ''
        tree_print += self.name + ", " + self.ntype + ", " + str(self.weight) + '\n'
        for child in self.children:
            if child.weight is None:
                child.weight = 0
            tree_print += '-' * (child.depth)
            tree_print += child.name + ", " + child.ntype + ", " + str(child.weight)
            tree_print += '\n'

        return tree_print
    def set_directory_weight(self):
        # Set the weight of the directory
        # If no children, return weight
        if self.ntype != 'dir':
            return self.weight
        # If children, add weight of children
        else:
            self.weight = 0
            for child in self.children:
                self.weight += child.set_directory_weight()
            return self.weight

    def get_directories_over_n_weight(self, n=1000):
        # Return directories that are over n weight
        # If no children, return weight
        if self.ntype != 'dir':
            return []
        # If children, add weight of children
        else:
            directories = []
            if self.weight > n:
                directories =  [(self.name, self.weight)]
            for child in self.children:
                directories += child.get_directories_over_n_weight(n)
            return directories
       



    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)