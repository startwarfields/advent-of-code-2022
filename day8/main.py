import argparse
import numpy as np
def main(args):
    with open(args.input, 'r') as f:
        lines = f.readlines()
    tree_grid = np.zeros((len(lines), len(lines[0].strip()) ))
    tree_visible = np.zeros((len(lines), len(lines[0].strip()) ))
    for idx, line in enumerate(lines):
        line = line.strip()
        tree_grid[idx, :] = [int(x) for x in line]
    
   
    tree_grid, tree_visible = find_visible(tree_grid, tree_visible, first = True)
    # Rotate the grid 90 degrees
    for i in range(3):
        tree_grid = np.rot90(tree_grid)
        tree_visible =  np.rot90(tree_visible)
        tree_grid, tree_visible = find_visible(tree_grid, tree_visible)

    tree_grid = np.rot90(tree_grid)
    # print (tree_visible)
    # Sum the visible trees
    # print("Number of visible trees", np.sum(tree_visible))
    # loop from every direction
    trees_visible = find_max_visible_at_spot(tree_grid)
    print(tree_grid)
    print(trees_visible)
    print("Max visible trees", np.max(trees_visible))
    # savve trees_visible to file
    np.savetxt("trees_visible.txt", trees_visible, fmt='%d')
 
def find_visible(tree_grid, tree_visible, first = False):
    for row_index, row in enumerate(tree_grid):
        for idx, tree in enumerate(row):
            if idx == 0 or row_index == 0 or row_index == len(tree_grid) - 1 or idx == len(row) - 1 and first == False:
                tree_visible[row_index, idx] = 1
            # check if all previous trees shorter than current tree in row
            elif np.all(row[:idx] < tree):
                tree_visible[row_index, idx] = 1

    return tree_grid, tree_visible

def find_max_visible_at_spot(tree_grid):
    # From each position, find the number of visible trees in each direction
    trees_visible = np.zeros((len(tree_grid), len(tree_grid[0])))
    for row_index, row in enumerate(tree_grid):
        for idx, tree in enumerate(row):
            # Look right
          
            right_trees = tree_grid[row_index, idx+1:]
            # flip if idx above half
           
            down_trees = tree_grid[row_index+1:, idx]
            left_trees = tree_grid[row_index, :idx]
            left_trees = np.flip(left_trees)
            up_trees = tree_grid[:row_index, idx]
            up_trees = np.flip(up_trees)
          
            trees_visible[row_index, idx] = 1
            trees_visible[row_index, idx] *= helper(right_trees, tree)
            print (trees_visible[row_index, idx])
            trees_visible[row_index, idx] *= helper(left_trees, tree)
            print (trees_visible[row_index, idx])
            trees_visible[row_index, idx] *= helper(up_trees, tree)
            print (trees_visible[row_index, idx])
            trees_visible[row_index, idx] *= helper(down_trees, tree)
            print (trees_visible[row_index, idx])
           
        
         
            # Look left
    return trees_visible
          

def helper(right_trees, tree):
    tree_sum = 0
    # Get the first tree that is taller than the current tree
    max_height = 0
    for c_idx, c_tree in enumerate(right_trees):
        if c_tree >= tree:
            tree_sum += 1
            break
        if c_tree <= max_height:
            tree_sum += 1
        else:
            max_height = c_tree
            tree_sum += 1
            
      
    
    

    return tree_sum

           
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)