import re
import numpy as np

#points table where the rows are the oppoents choice, and columns are players
points_table = np.array([[3, 6, 0],[0, 3, 6], [6, 0, 3]])
# print(points_table)

total_points = 0

# Loop ovver the input and find the total score

with open("input.txt") as f:
    print("We opened the file")
    while True:
        line = f.readline()

        if not line:
            break
        # Determine the points the win/loss
        if line[2] == 'X':
            win_points = 0
        elif line[2] == 'Y':
            win_points = 3
        elif line[2] == 'Z':
            win_points = 6

        # Read opponents choice
        if line[0] == 'A':
            op_choice = 1
        elif  line[0] == 'B':
            op_choice = 2
        elif  line[0] == 'C':
            op_choice = 3

        # Win conditions
        # 1:2 , 2:3, 3:1

        # Lose conditions
        # 2:1, 3:2, 1:3

        # Determine whats needed to get the desired output
        choice_points = np.where(points_table[op_choice-1] == win_points)[0]
        choice_points = int(choice_points) + 1

        # Add points to total points

        total_points += win_points+choice_points

print(total_points)
