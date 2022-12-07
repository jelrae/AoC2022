import re
import copy

# directory_dict = {'/' : []}
directory_dict = {}
# size_dict = {'/' : 0}
size_dict = {}
cur_dir = ''
cur_path_array = []
cur_path_string = ''

with open("input.txt") as f:
    print("We opened the file")
    while True:
        line = f.readline().strip()
        # print(line)
        # breakpoint()
        if not line:
            break
        has_digit = bool(re.search(r'\d', line))
        # Handles the cd's
        if line[0:4] == '$ cd':
            # print("Were in the cd handling loop")
            # Remove the cd part
            change_dir = re.sub('.', '', line,count = 5)
            # If we need to go up a path, remove the last item from the path
            if change_dir == '..':
                # cur_path_array = cur_path_array.strip()
                cur_path_array.pop()
                # cur_path_string = str(cur_path_array)
            else:
                # cur_path_array = cur_path_array + '/' + change_dir
                cur_path_array.append(change_dir)
                # if ~directory_dict.has_key(cur_path_array):
                cur_path_string = str(cur_path_array)
                if ~ (cur_path_string in directory_dict):
                    # print("Are we  adding shit?")
                    directory_dict[cur_path_string] = []
                    size_dict[cur_path_string] = 0
        # Handle the ls staments
        elif line[0:4] == '$ ls':
            # print("Were in the ls handling loop")
            continue
        # Handle the new directory statements
        elif line[0:3] == 'dir':
            # print("Were in the dir handling loop")
            # remove the dir, append to path and check for if it exists
            new_folder = re.sub('.', '', line,count = 3).strip()
            new_dir_array = copy.deepcopy(cur_path_array)
            new_dir_array = new_dir_array.append(new_folder)
            # breakpoint()
            new_dir_string = str(new_dir_array)
            if ~ (new_dir_string in directory_dict):
                directory_dict[new_dir_string] = []
                size_dict[new_dir_string] = 0
        # Handle if there is a digit in the string
        elif has_digit:
            # print("Were in the digit handling loop")
            # print("the current path array is: " + str(cur_path_array))
            # Find the number
            filesize = int(re.findall('\d+', line)[0])
            add_path = copy.deepcopy(cur_path_array)
            add_path_string = str(add_path)
            # breakpoint()
            size_dict[add_path_string] += filesize
            # # For each of the paths in this parth, add the filesize
            for i in range(0, len(cur_path_array)-1):
                # print(cur_path_array)
                add_path.pop()
                # print(add_path)
                add_path_string = str(add_path)
                size_dict[add_path_string] += filesize
                # print(add_path_string)

# breakpoint()
print(size_dict["['/']"])
total_space = 70000000
free_space = total_space - size_dict["['/']"]

could_be_removed = {}

for key, value in size_dict.items():
    if value >= 30000000 - free_space:
        could_be_removed[key] = value

print("Directory with the minimum space required is")
print(min(could_be_removed, key=could_be_removed.get))
print('The space taken up by this directory is')
print(min(could_be_removed.values()))
