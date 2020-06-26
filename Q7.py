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
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]  # starting position
goal = [len(grid)-1, len(grid[0])-1]  # goal position
delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # do right
delta_name = ['^', '<', 'v', '>']  # ignore for now
cost = 1  # each move costs 1


def search():
    open_list = [[0, 0, 0]]
    current_state = [0] + init  # [cost, y-coordinate, x-coordinate]
    visited_states = []

    # Run as long as the goal state has not been found.
    while current_state[1] != goal[0] or current_state[2] != goal[1]:
        possible_new_states = []
        # Move through the move options from the current state.
        for action in delta:
            new_state = [action[0] + current_state[1],
                         action[1] + current_state[2]]
            # Check whether the next state has been visited before.
            if new_state not in visited_states and new_state not in [position[1:] for position in open_list]:
                next_state = [current_state[0]+1, new_state[0], new_state[1]]

                # -1 not in next_state - check whether the next state is outside of the map.
                # next_state[0] < 5 - check if we are inside the map on the x-axis.
                # next_state[1] < 6 - check if we are inside te map on the y-axis.
                # grid[next_state[0]][next_state[1]] is not 1 - check so the value of the next state is not 1 (obstacle).
                # next_state[1:] not in visited_states - if the next state has not been visited before.
                if -1 not in next_state and next_state[1] < 5 and next_state[2] < 6 and grid[next_state[1]][next_state[2]] != 1 and next_state[1:] not in visited_states:
                    # Next state is a valid move, add it to the list of possible new states.
                    possible_new_states.append(next_state)

        # Remove current state from open list.
        del open_list[0]
        # Add current state to the list of visited states.
        visited_states.append(current_state[1:])
        # Add new current state to the open list.
        open_list.extend(possible_new_states)
        # If the open list is empty, there are no more nodes to check and the search failed.
        if not open_list:
            return 'Fail'
        # Change state to the most recently discovered one.
        current_state = open_list[0]

    return [current_state[0], current_state[1], current_state[2]]


if __name__ == '__main__':
    print(search())
