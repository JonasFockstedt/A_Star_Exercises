# ----------
# User Instructions:
#
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------
# Grid format:
# 0 = Navigable space
# 1 = Occupied space
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]  # starting position
goal = [len(grid)-1, len(grid[0])-1]  # goal position
delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # do right
delta_name = ['^', '<', 'v', '>']  # ignore for now
cost = 1  # each move costs 1
expand = [[-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1]]


def search():
    g_value = 0     # The cost to reach the goal.
    open_list = [[0, 0]]
    current_state = [0] + init  # [cost, y-coordinate, x-coordinate]
    visited_states = []
    expansion_nbr = 0

    # Run as long as the goal state has not been found.
    while current_state[1:] != goal:
        possible_new_states = []
        # Move through the move options from the current state.
        for action in delta:
            new_state = [action[0] + current_state[1],
                         action[1] + current_state[2]]
            # Check whether the next state has been visited before.
            if new_state not in visited_states and new_state not in [position[1:] for position in open_list]:
                next_state = [current_state[0]+1, new_state[0], new_state[1]]

                # -1 not in next_state - check whether the next state is outside of the map.
                # next_state[1] < 5 - check if we are inside the map on the x-axis.
                # next_state[2] < 6 - check if we are inside te map on the y-axis.
                # grid[next_state[1]][next_state[2]] != 1 - check so the value of the next state is not 1 (obstacle).
                # next_state[1:] not in visited_states - check if we have already been in the next state.
                if -1 not in next_state and next_state[1] < 5 and next_state[2] < 6 and grid[next_state[1]][next_state[2]] != 1 and next_state[1:] not in visited_states:
                    # Next state is a valid move, add it to the list of possible new states.
                    possible_new_states.append(next_state)

        # Remove current state from open list.
        del open_list[0]
        # Add current state to the list of visited states.
        visited_states.append(current_state[1:])
        # Add new current state to the open list.
        open_list.extend(possible_new_states)
        # Note which node has been expanded and in which order it was opened.
        expand[current_state[1]][current_state[2]] = expansion_nbr
        # If the open list is empty, there are no more nodes to check and the search failed.
        if not open_list:
            return 'Fail'
        # Change state to the latest discovered one.
        current_state = open_list[0]
        expansion_nbr += 1

    # Expansion of final node.
    expand[current_state[1]][current_state[2]] = expansion_nbr
    return current_state


if __name__ == '__main__':
    # Do the search.
    print(search())

    print_string = ''
    for row in expand:
        print_string += '['
        for element in row:
            print_string += f'{element},\t'
        print_string += ']\n'

    # Print out the expansion map, showing in which order the nodes where expanded.
    print(print_string)
