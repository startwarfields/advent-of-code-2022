import argparse
import networkx as nx
# Example Map
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi

# Destination is 'E', goal is to get there in as few steps as possible
# Letters represent height, you can't move to a square more than 1 height above you


height_map = {
    'S': 1,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'E': 26
}


def main(args):
    elf_file = open(args.input, 'r')
    elf_lines = elf_file.readlines()
    # Get the map
    my_map = []
    starting_position = None
    goal_position = None
    for line in elf_lines:
        line = line.strip()
        print(line)
        for idx, char in enumerate(line):
            if char == 'S':
                # Get height
                starting_position = (idx, len(my_map), height_map[char])
            if char == 'E':
                goal_position = (idx, len(my_map), height_map[char])

        my_map.append(line)
    print(my_map)

    # Convert my_map to a graph with the node values being the height
    # Drop edges that are more than 1 height higher than the current node
    # Directional graph
    G = nx.DiGraph()
    # Set Node Attributes
    mapping = {0:'x', 1:'y', 2:''}

    for y, line in enumerate(my_map):
        for x, char in enumerate(line):
            G.add_node((x, y, height_map[char]))
            # Add edges
            # Check if we can move right
    # Go through adding edges
    # Get number of nodes
    print(len(G.nodes))
    for node in G.nodes:
        x, y, z = node
        # Check if we can move right
        if x < len(my_map[0]) - 1:
            # Check if the height is the same
            if  height_map[my_map[y][x+1]] - z<= 1:
                height_diff = abs(height_map[my_map[y][x+1]] - z)
                G.add_edge(node, (x+1, y, height_map[my_map[y][x+1]]))
        # Check if we can move left
        if x > 0:
            # Check if the height is the same
            if height_map [my_map[y][x-1]] - z <= 1:
                height_diff = abs(height_map[my_map[y][x-1]] - z)
                G.add_edge(node, (x-1, y, height_map[my_map[y][x-1]]))
        # Check if we can move down
        if y < len(my_map) - 1:
            # Check if the height is the same
            if height_map[my_map[y+1][x]] - z  <= 1:
                height_diff = abs(height_map[my_map[y+1][x]] - z)
                G.add_edge(node, (x, y+1, height_map[my_map[y+1][x]]))
        # Check if we can move up
        if y > 0:
            # Check if the height is the same
            if height_map[my_map[y-1][x]] - z <= 1:
                height_diff = abs(height_map[my_map[y-1][x]] - z)
                G.add_edge(node, (x, y-1, height_map[my_map[y-1][x]]))
    print(len(G.nodes))


            
    print(G)
    # Get the shortest path
    shortest_path = nx.shortest_path(G, starting_position, goal_position)
    # Get the shortest path length
    shortest_path_lenght = nx.shortest_path_length(G, starting_position, goal_position)
    # Find shortest path with the lowest sum of the heights
    # Find shortest weighted path
    # Find shortest path from any node 0 height to E
    canddiate_nodes = []
    for node in G.nodes:
        if node[2] == 1:
            canddiate_nodes.append(node)
    
    # shortest_path_2_length = nx.shortest_path_length(G, canddiate_nodes[0], goal_position)
    # canddiate_nodes.remove(canddiate_nodes[0])
    shortest_path_2_length = 1e9
    for node in canddiate_nodes:
        # Check if path is possible
        if not nx.has_path(G, node, goal_position):
            continue
        shortest_path_2 = nx.shortest_path(G, node, goal_position)
        print(nx.shortest_path_length(G, node, goal_position))
        if shortest_path_2_length > nx.shortest_path_length(G, node, goal_position):
            shortest_path_2_length = nx.shortest_path_length(G, node, goal_position)
            shortest_path_2 = nx.shortest_path(G, node, goal_position)


    print(shortest_path_2_length)
    exit()
    for path_step in shortest_path:
        print(path_step)
    print(shortest_path_lenght)
    print(starting_position, goal_position)
   
    # 1. We want to find a possible path to the goal that respects the height limitation of movement

    queue = [starting_position]
    history_cost = 0
    visited = set()
    
   



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Day 4 Advent of Code 2022",
                                    description = "Solve the first day of Advent of Code 2022"
                                     )

    parser.add_argument('-i', '--input', help = 'Input file', required = True)
    args = parser.parse_args()
    main(args)


