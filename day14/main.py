import argparse
rock = '#'
air = '.'
sand = '+'
sand_coordiante = [0, 500]

def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    # Each line is a series of paths of rock from one coordinate to another
   
    sand_coordiante = [0, 500]
    grid = dict()
    grid[0] = dict()
    grid[0][500] = sand
    for line in elf_lines:
        line = line.strip()
        line = line.split('->')
        prev = line[0]
        prev_x = int(prev.split(',')[0])
        prev_y = int(prev.split(',')[1])
        for idx, item in enumerate(line):
            if idx == 0:
                continue
            line[idx] = item.split(',')
            cur_x = int(line[idx][0])
            cur_y = int(line[idx][1])
            print("Adding rocks from", prev_x, prev_y, "to", cur_x, cur_y)
            grid = add_rocks_to_grid(prev_x, prev_y, cur_x, cur_y, grid)
            prev_x = cur_x
            prev_y = cur_y
            print("Grid is now", grid)
           
    # Make grid square
    count = 0
    grid = make_grid_square(grid, extend_height=True)

    # Add sand to grid
    grid, result = add_sand_to_grid(grid)
    while result !=2:
        count += 1
        grid, result = add_sand_to_grid(grid)
        if result == 2:
           break
    print("Count is", count)
        # if count > 10:
           

    for key, row in sorted(grid.items()):
        print(key, end=': ')
        first_col = True
        for cey, col in sorted(row.items()):
            if first_col:
                print(cey, end=': ')
                first_col = False
        
            print(col, end='')
        print()
    print("Count is", count)

    
def make_grid_square(grid, extend_height=False):
    # Fill in with air  
    max_width = 0
    max_height = max(grid.keys())
    # Add floor to max height + 2
    # grid[max_height+1] = dict()
    
    min_width = 99999

    for row in grid.values():
        if max(row.keys()) > max_width:
            max_width = max(row.keys()) 
        if min(row.keys()) < min_width:
            min_width = min(row.keys())


    # Fill in floor
 
    if extend_height:
        max_height += 2
        # min_width -= 8
        # max_width += 8

    grid[max_height] = dict()
    for i in range(min_width, max_width+1):
        grid[max_height][i] = rock    


    for i in range(max_height+1):
        if i not in grid:
            grid[i] = dict()
        for j in range(min_width, max_width+1):
            # print("Adding air at", i, j)
            if j not in grid[i]:
                grid[i][j] = air
    print("Max width:", max_width)
    return grid


def add_sand_to_grid(grid):
    # Add sand to grid from sand coordinate
    # If sand is on top of air, move down until it hits rock
    # If sand is on top of sand, move diagonally down and left until it hits rock
    # then move diagonally down and right until it hits rock
    # If all possible moves are blocked, it comes to rest (1)
    # If the sand extends beyond the grid - end condition (2)

    new_sand_coordiante = sand_coordiante
    # Check if sand is on top of air
    try:
        sand_x = sand_coordiante[0]
        sand_y = sand_coordiante[1]
        while(True):
            # Check if sand is on top of air, if so, move down
            if grid[sand_x+1][sand_y] == air:
                sand_x += 1
            # Check if sand is on top of sand, if so, move diagonally down and left
            else:
                # Goes down until blocked
                # Then Tries to go down & left until blocked
                # Then goes down & right until blocked
                # If all blocked, it comes to rest
                while(True):
                    # Check if grid needs to be extended
                    if grid[0][500] == 'O':
                        return[grid, 2]

                    if sand_x+1 not in grid:
                        grid[sand_x+1] = dict()
                        grid = make_grid_square(grid)
                    # elif sand_y+1 not in grid[sand_x]:
                    #     grid[sand_x][sand_y+1] = air
                    #     print("Extending grid for ", sand_x, sand_y+1)
                    #     grid = make_grid_square(grid)
                    
                    if sand_y-1 not in grid[sand_x+1]:
                        grid[sand_x+1][sand_y-1] = air
                        print("Extending grid for ", sand_x+1, sand_y-1)
                        # Add one to the other side for shits
                        # width = max(grid[sand_x+1].keys()) + 5
                        # grid[sand_x+1][width+1] = air
                        grid = make_grid_square(grid)
                    


                    if grid[sand_x+1][sand_y] != air:
                        if grid[sand_x+1][sand_y-1] != air:
                            if grid[sand_x+1][sand_y+1] in [rock, 'O', sand]:
                                grid[sand_x][sand_y] = 'O'
                                return [grid, 1]
                            else:
                                sand_y += 1
                                if sand_y+1 not in grid[sand_x]:
                                    grid[sand_x][sand_y+1] = air
                                    print("Extending grid for ", sand_x, sand_y+1)
                                    grid = make_grid_square(grid)
                                
                                break
                        else:
                            sand_y -= 1
                            # break
                    else:
                        sand_x += 1
                        # break
                    

                
    except:
    
        print("Sand coordinate is", sand_x, sand_y)
        return [grid, 2]
        
    return [grid, 2]


            


def add_rocks_to_grid(prev_x, prev_y, cur_x, cur_y, grid):
    if prev_x == cur_x:
        # Vertical line
        if prev_y < cur_y:
            for y in range(prev_y, cur_y + 1):
                if y not in grid:
                    grid[y] = dict()
                    print("Adding row", y)
                grid[y][prev_x] = rock
        else:
            for y in range(cur_y, prev_y + 1):
                if y not in grid:
                    grid[y] = dict()
                grid[y][prev_x] = rock
    else:
        if prev_y not in grid:
            grid[prev_y] = dict()
        # Horizontal line
        if prev_x < cur_x:
            for x in range(prev_x, cur_x + 1):
                grid[prev_y][x] = rock
        else:
            for x in range(cur_x, prev_x + 1):
                grid[prev_y][x] = rock
    return grid


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)




