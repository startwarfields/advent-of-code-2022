import argparse

def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    ## Example Monkey format:
# Monkey 0:
#   Starting items: 56, 56, 92, 65, 71, 61, 79
#   Operation: new = old * 7
#   Test: divisible by 3
#     If true: throw to monkey 3
#     If false: throw to monkey 7
    monkey_dict = dict()
    for idx, line in enumerate(elf_lines):
        line = elf_lines[idx].strip()
        line = line.split(' ')
        if line[0] == 'Monkey':
            monkey_number = int(line[1][:-1].strip(':'))
            # Next Line is the starting items
            starting_items = elf_lines[idx+1].split(':')[1:]
            starting_items = get_starting_items(starting_items)
            # Next Line is the operation
            operation = elf_lines[idx+2].split(' ')[2:]
            operation = ' '.join(operation)
            operation = operation.split('=')
            operation = parse_operation(operation[1])
            # Next Line is the test
            test = elf_lines[idx+3].split(' ')[2:]
            test = ' '.join(test)
            # Just get the test number
            test = int(test.split(' ')[-1])
            # Next Line is the if true
            if_true = elf_lines[idx+4].split(' ')[2:]
            if_true = ' '.join(if_true)
            # Next Line is the if false
            if_false = elf_lines[idx+5].split(' ')[2:]
            if_false = ' '.join(if_false)
            # Just get the monkey number
            if_false = int(if_false.split(' ')[-1])
            if_true = int(if_true.split(' ')[-1])
            # Create Monkey
            # print(monkey_number, starting_items, operation, test, if_true, if_false)
            monkey = Monkey(starting_items, operation, test, if_true, if_false)
            # Test Monkey
            monkey_dict[monkey_number] = monkey
    # Run all monkeys in order for one cycle
    # Print all monkeys items
    # for monkey_number in monkey_dict:
    #     monkey = monkey_dict[monkey_number]
    #     print(monkey_number, monkey.starting_items)
    
    # Get total number of items
  

    # get LCM of all divisors
    lcm = 1
    for monkey_number in monkey_dict:
        monkey = monkey_dict[monkey_number]
        lcm = lcm * monkey.divisible_by
    print("LCM", lcm)
    
    i = 0
    while i < 10000:
        i += 1
        if i % 1000 == 0:
            print("-------------------- Cycle", i, "---------------------")
        for monkey_number in monkey_dict:
            # print("Running Monkey", monkey_number)
            monkey = monkey_dict[monkey_number]
            # print("Monkey", monkey_number, "has items", monkey.starting_items)
            item_list_to_move = []
            for item in monkey.starting_items:
                
                # print("Item", item, "moved to", item_new)
                item_list_to_move.append(monkey.move(item, lcm))
            monkey.starting_items = []
            # print("Items to move", item_list_to_move)
            for item in item_list_to_move:
                monkey_dict[item[0]].starting_items.append(item[1])
    # Print all monkeys items
        for monkey_number in monkey_dict:
            monkey = monkey_dict[monkey_number]
            # print(monkey_number, monkey.starting_items)

    # Print all monkeys inspection counts
    inspection_counts = []
    for monkey_number in monkey_dict:
        monkey = monkey_dict[monkey_number]
        inspection_counts.append(monkey.inspection_count)
        # print(monkey_number, " has ", monkey.inspection_count)
    print("Total Inspections", sum(inspection_counts))
    inspection_counts = sorted(inspection_counts, reverse=True)
    print(inspection_counts[0]*inspection_counts[1])
    # Parse all Monkeys into Monkey_Dict

    # Run all monkeys in order

def get_starting_items(starting_items):
    
    for i in range(len(starting_items)):
        starting_items[i] = starting_items[i].strip()
        # Remove new line
        starting_items = ' '.join(starting_items).split(',')
    
        starting_items = [int(item) for item in starting_items]
    return starting_items


def parse_operation(operation):
    operation = operation.strip().split(' ')
    op_code = get_op(operation[1])
    if operation[0] == 'old' and operation[2] == 'old':
        return lambda x: op_code(x, x)
    else:
        
        return lambda x: op_code(x, int(operation[2]))
    

def get_op(op_code):
    if op_code == '*':
        return lambda x, y: (x * y)
    elif op_code == '+':
        return lambda x, y: (x + y)

class Monkey(object):
    def __init__(self, starting_items, operation, test, if_true, if_false):
        self.starting_items = starting_items
        self.operation = operation
        self.if_true = if_true
        self.if_false = if_false
        # Must return a tuple where keys are the monkey's items and values are worry number of each item
        self.divisible_by = int(test)
        self.inspection_count = 0

    def move(self, item, lcm):
        self.inspection_count += 1
        # print ("Item", item, "is divisible by", self.divisible_by, ":", item % self.divisible_by == 0)
        item = self.operation(item)
        # Reduce item without changing its divisibility
      
        # If Item near max int, reset to 1
        # if item > 2147483647:
            # item = 1
        if item % self.divisible_by == 0:
            if item > lcm:
                item = item % lcm

            return self.if_true, int(item)
        else:
            # if item > 2147483640:
            #     item -= 2147483640 
            
            return self.if_false, int(item)







if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)

