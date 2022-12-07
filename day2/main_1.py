import re

total_points = 0

# Loop ovver the input and find the total score

with open("input.txt") as f:
    print("We opened the file")
    while True:
        line = f.readline()

        if not line:
            break
        # Determine the points for yourself
        if line[2] == 'X':
            choice_points = 1
        elif line[2] == 'Y':
            choice_points = 2
        elif line[2] == 'Z':
            choice_points = 3

        if line[0] == 'A':
            op_choice = 1
        elif  line[0] == 'B':
            op_choice = 2
        elif  line[0] == 'C':
            op_choice = 3

        # Win conditions
        # 1:2 , 2:3, 3:1
        if op_choice == 1 and choice_points == 2:
            win_points = 6
        elif op_choice == 2 and choice_points == 3:
            win_points = 6
        elif op_choice == 3 and choice_points == 1:
            win_points = 6
        # Draw cnditions
        elif op_choice == choice_points:
            win_points = 3
        else:
            win_points = 0

        # Add points to total points

        total_points += win_points+choice_points

print(total_points)
