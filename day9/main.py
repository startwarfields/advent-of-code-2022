import argparse
import copy
def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    head_position = (0,0) # Head & Tail
    Head = Knot(head_position)
    local_head = Head

    # Part 2 lmao
    for i in range(9):
        tail_position = (0,0)
        Tail = Knot(copy.deepcopy(tail_position))
        local_head.next = Tail
        Tail.prev = local_head
        Tail.next = None
        local_head = Tail

    local_head = Head
    while local_head.next is not None:
        local_head = local_head.next
    
    # Head is where movement will be
    # Tail has specific movement rules
    grid = {}
    grid[0] = {0: 1}
    first_move = True
    for idx, movement in enumerate(elf_lines):
        move = parse_move(movement)
        for i in range(move[1]):
            head_position = Head.coordinate
            if move[0] == 'R':
                head_position = (head_position[0] + 1, head_position[1])
                grid = update_dict(grid, head_position[0], head_position[1])
            elif move[0] == 'L':
                head_position = (head_position[0] - 1, head_position[1])
                grid = update_dict(grid, head_position[0], head_position[1])
                
            elif move[0] == 'U':
                head_position = (head_position[0], head_position[1] + 1)
                grid = update_dict(grid, head_position[0], head_position[1])
               
            elif move[0] == 'D':
                head_position = (head_position[0], head_position[1] - 1)
                grid = update_dict(grid, head_position[0], head_position[1])

            Head.coordinate = head_position
            print("Head", head_position)
            local_tail = Head.next
      
            while local_tail is not None:
                head_position = local_tail.prev.coordinate
                tail_position = local_tail.coordinate
                tail_position = move_tail(head_position, tail_position)
                print("Moved", local_tail.coordinate, "to", tail_position)
                is_tail = local_tail.next is None
                grid = update_dict(grid, tail_position[0], tail_position[1], is_tail)
                local_tail.coordinate = tail_position
                local_tail = local_tail.next

        # if idx == 2:
        #     exit()
            # total_count = 0
        #     for y in grid:
        #         for x in grid[y]:
        #             total_count += grid[y][x]
        #     print("Count", total_count)
        # exit()


            
            # first_move = False
            # Print the grid in a nice format
            
     
    local_tail = Head
    while local_tail.next is not None:
        local_tail = local_tail.next

    # Print count of dictionary values
    total_count = 0
    for y in grid:
        for x in grid[y]:
            total_count += grid[y][x]
    print("Count", total_count)

# Create a dynamic grid. The starting point of the grid is 0,0, but may go negative
# The grid is a dictionary of dictionaries. The first key is the y coordinate, the second key is the x coordinate
# The value of the grid is the number of times that coordinate has been visited

def update_dict(grid, x, y, tail = False):
    if y not in grid:
        grid[y] = {}
    if x not in grid[y]:
        grid[y][x] = 0
    if tail:
        print("Tail", x, y)
        grid[y][x] = 1
       
    return grid




def move_tail(head_position, tail_position):
    sign = lambda x: (-1, 1)[x > 0]
    # Rule 1: If the head is ever two steps directly up, down, left, or right from the tail, 
    if head_position[0] == tail_position[0] and abs(head_position[1] - tail_position[1]) == 2:
        tail_position = (tail_position[0], tail_position[1] + sign(head_position[1] - tail_position[1]))

    elif head_position[1] == tail_position[1] and abs(head_position[0] - tail_position[0]) == 2:
        tail_position = (tail_position[0] + sign(head_position[0] - tail_position[0]), tail_position[1])

    elif abs(head_position[0] - tail_position[0]) == 2 or abs(head_position[1] - tail_position[1]) == 2:
        tail_position = (tail_position[0] + sign(head_position[0] - tail_position[0]), tail_position[1] + sign(head_position[1] - tail_position[1]))
    
    # the tail must also move one step in that direction so it remains close enough:

    # Rule 2: Otherwise, if the head and tail aren't touching and aren't in the same row or column, 
    # the tail always moves one step diagonally to keep up:
    return tail_position



# Create a LinkedLIst of Knots
# Each knot has a coordinate and a pointer to the next knot

class Knot:
    def __init__(self, coordinate, local_head = None, local_tail = None):
        self.coordinate = coordinate
        self.prev = local_head
        self.next =  local_tail
        self.visits = 0



def parse_move(line):
    line = line.split(' ')
    direction = line[0]
    distance = int(line[1])
    return direction, distance




if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)
