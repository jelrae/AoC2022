import numpy as np

# Declare variables
total_calories = []
elf_calories = []

# Loop over the input and find the calories per elf
with open("input.txt") as f:
    print("We are open")
    while True:
        line = f.readline()
        if line == '\n':
            total_calories.append(np.sum(elf_calories))
            print(np.sum(elf_calories))
            print("New elf!")
            elf_calories = []
        elif not line:
            break
        else:
            elf_calories.append(float(line.replace('\n', '')))

# Tell me which has the most and how much
total_calories = np.array(total_calories)
print('Elf ' + str(total_calories.argmax()) + ' has the most calories with ' +
            str(int(total_calories[total_calories.argmax()])) + ' calories.')

# Detemrine the calories by the top n elves
n = 3
top_n = total_calories.argsort()[-n:]

total_top_n = np.sum(total_calories[top_n])

print('The total of the top ' + str(n) + ' elves is ' + str(int(total_top_n)) + ' calories')
