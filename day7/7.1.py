def sum_of_dirs(records):
    directories = {'/': [0]}
    path = []
    curr_dir = '/'
    if_ls = False
    for line in records.splitlines():
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd':
                if_ls = False
                if line[2] != "..":
                    path.append(line[2])
                else:
                    path.pop()
                curr_dir = '/'.join(path)
            else:
                if_ls = True

        else:
            if if_ls:
                if line[0] == 'dir':
                    directories[curr_dir + '/' + line[1]] = [0]
                    for ind, place in enumerate(path):
                        ps = '/'.join(path[0:ind+1])
                        directories[ps].insert(0, (curr_dir + '/' + line[1]))
                else:
                    directories[curr_dir][-1] += int(line[0])

    dirs_sum = 0
    for k, v in directories.items():
        if len(v) == 1:
            if v[0] <= 100000:
                dirs_sum += v[0]
        else:
            suma = v[-1]
            for x in range(0, len(v) - 1):
                suma += directories[v[x]][-1]
            if suma <= 100000:
                dirs_sum += suma

    return dirs_sum


with open('7.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 1. answer: {sum_of_dirs(data)}")
