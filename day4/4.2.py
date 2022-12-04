def overlap_num(records: str) -> int:
    counter = 0
    for line in records.splitlines():
        line = [list(map(int, elem.split('-'))) for elem in line.split(',')]
        f_1, f_2 = line[0][0], line[0][1]
        s_1, s_2 = line[1][0], line[1][1]
        if f_1 >= s_1 and f_1 <= s_2:
            counter += 1
        elif s_1 >= f_1 and s_1 <= f_2:
            counter += 1
    return counter


with open('4.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 2. answer: {overlap_num(data)}")
