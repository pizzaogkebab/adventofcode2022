def top_of_stacks(init_stacks: str, steps: str) -> str:
    last_line = init_stacks.splitlines()[-1]
    stacks = [[] for _ in range((len(last_line) + 2) // 4)]
    for line in init_stacks.splitlines():

        for element in range(1,len(line),4):
            if line[element] == ' ':
                continue
            else:
                stacks[int(last_line[element]) - 1].insert(0, line[element])

    for step in steps.splitlines():
        q, a, b = int(step.split(' ')[1]), int(step.split(' ')[3]), int(step.split(' ')[5])
        for x in range(q):
            stacks[b - 1].append(stacks[a - 1].pop())

    s = ""
    for stack in stacks:
        s += stack.pop()

    return s


with open('5.txt', 'r') as input_str:
    stacks, instructions= input_str.read().split('\n\n')

print(top_of_stacks(stacks, instructions))
