def sum_in_cycles(records: str) -> int:
    cycle = 0
    x = 1
    sum_of_xs = 0
    for line in records.splitlines():
        instr, *value = line.strip().split()
        cycle += 1
        if (cycle - 20) % 40 == 0:
            sum_of_xs += x * cycle
        if instr == "addx":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                sum_of_xs += x * cycle
            x += int(*value)
    return sum_of_xs


with open('10.txt', 'r') as input_str:
    data = input_str.read()

print(sum_in_cycles(data))
