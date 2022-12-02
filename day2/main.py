import argparse

strategy = [1, -1, 0]
# Rock is A or X
# Paper is B or Y
# Scissors is C or Z
equivalent_moves = {'A': ['X'], 'B': ['Y'], 'C': ['Z'], 'X': ['A'], 'Y': ['B'], 'Z': ['C']}


moves = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3 }



total_score = 0 

def determine_outcome(move_1, move_2):
    if equivalent_moves[move_1][0] == move_2:
        return 3
    # Loses
    elif move_1 == 'A' and move_2 == 'Z':
        return 0
    elif move_1 == 'C' and move_2 == 'Y':
        return 0
    elif move_1 == 'B' and move_2 == 'X':
        return 0
    # Wins
    elif move_1 == 'B' and move_2 == 'Z':
        return 6
    elif move_1 == 'C' and move_2 == 'X':
        return 6
    elif move_1 == 'A' and move_2 == 'Y':
        return 6
   


win_dict = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
   }
lose_dict = {
    'A': 'Y',
    'B': 'Z',
    'C': 'A',
     }




def determine_alternate(move_1, move_2):
    if move_2 == 'Z':
        return moves[lose_dict[move_1]] + 6
    elif move_2 == 'Y':
        return moves[equivalent_moves[move_1][0]] + 3
    elif move_2 == 'X':
        return moves[win_dict[move_1]] + 0
  # lose

def main(args):
    move_list = open(args.input, 'r')
    total_score = 0
    game_score = 0
    current_move = 0
    for line in move_list:
        move_1 = line[0]
        move_2 = line[2]
        total_score += determine_outcome(move_1, move_2) + moves[move_2]
        # total_score += determine_alternate(move_1, move_2)
    print(total_score) 




if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)