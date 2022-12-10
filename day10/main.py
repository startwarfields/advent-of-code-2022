import argparse

def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()

    screen = dict(
        (i, ['.'] * 40) for i in range(6)
    )
   
    print_screen(screen)

    clock_cycle = 1
    regiser_x = 1
    add_next_cycle = False
    idx = 0
    # line = elf_lines[idx].strip()
    total_signal = 0
    busy_cycles = 0
    cache = 0
    see_clocks = [20, 40]
    while(idx < len(elf_lines)):
        line = elf_lines[idx].strip()
        line = line.split(' ')
        if line[0] == 'noop':
            busy_cycles = 0
        elif line[0] == 'addx':
            busy_cycles = 1
            cache = int(line[1])

        
        draw_pixel(screen, regiser_x, clock_cycle)

        while busy_cycles > 0:
            clock_cycle += 1
            draw_pixel(screen, regiser_x, clock_cycle)
           
            # clock_cycle += 1
            if clock_cycle == 20 or (clock_cycle-20) % 40 == 0:
                print("Cycle", clock_cycle, "Register", regiser_x)
                print("Signal Strength", regiser_x*clock_cycle)
                total_signal += regiser_x*clock_cycle
            busy_cycles -= 1
      
        # clock_cycle += 1
       
        
        idx += 1

        
        if cache != 0:
            regiser_x += cache
            cache = 0 
        clock_cycle += 1
        draw_pixel(screen, regiser_x, clock_cycle)
     
        if clock_cycle == 20 or (clock_cycle-20) % 40 == 0:
            print("Cycle", clock_cycle, "Register", regiser_x)
            print("Signal Strength", regiser_x*clock_cycle)
            total_signal += regiser_x*clock_cycle
        
       

    print("Total Signal", total_signal)
    print_screen(screen)
    # for line in elf_lines:
    #     line = line.strip()
    #     line = line.split(' ')
    #     if line[0] == 'noop':
    #         clock_cycle += 1
    #     elif line[0] == 'addx':
    #         regiser_x += int(line[1])
    #         clock_cycle += 2
    #     if clock_cycle % 20 == 0:
    #         print("Cycle", clock_cycle)
    #         print("Signal Strength", regiser_x*clock_cycle)
def draw_pixel(screen, sprite_position, clock_cycle):
    sprite_positions = [sprite_position -1 , sprite_position, sprite_position + 1]
    i = clock_cycle // 40 
    j = clock_cycle % 40 - 1
    for spritey in sprite_positions:
        if spritey == j:
            print("Drawing pixel at", i, j, "clock cycle", clock_cycle, "sprite position", spritey)
            screen[i][j] = '#'
    return screen



def print_screen(screen):
    for i in range(6):
        print(''.join(screen[i]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)

