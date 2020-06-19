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
    g_value = 0     # The cost to reach the goal.
    open_list = [[0, 0]]
    current_state = init
    visited_states = []

    while current_state != goal:
        possible_new_states = []
        # Move through the move options from the current state.
        for action in delta:
            # Check whether the next state has been visited before.
            if [action[0] + current_state[0], action[1] + current_state[1]] not in visited_states:
                next_state = [action[0] + current_state[0],
                              action[1] + current_state[1]]

                # -1 not in next_state - check whether the next state is outside of the map.
                # next_state[0] < 5 - check if we are inside the map on the x-axis.
                # next_state[1] < 6 - check if we are inside te map on the y-axis.
                # grid[next_state[0]][next_state[1]] is not 1 - check so the value of the next state is not 1 (obstacle).
                # next_state not in visited_states - check if we have already been in the next state.
                # next_state not in open_list - check if the next state is not a state which has already been discovered.
                if -1 not in next_state and next_state[0] < 5 and next_state[1] < 6 and grid[next_state[0]][next_state[1]] != 1 and next_state not in visited_states and next_state not in open_list:
                    # Next state is a valid move, add it to the list of possible new states.
                    possible_new_states.append(next_state)

        # Remove current satte from open list.
        open_list.remove(current_state)
        # Add current state to the list of visited states.
        visited_states.append(current_state)
        # Add new current state to the open list.
        open_list.extend(possible_new_states)
        # Change state to the most recently discovered one.
        current_state = open_list[-1]
        g_value += cost

    return [g_value, current_state[0], current_state[1]]


if __name__ == '__main__':
    print(search())
