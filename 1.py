def list_of_cal(records: list) -> list:
    sums = []
    for x in records:
        sums.append(sum(map(int, x)))
    return sorted(sums, reverse= True)


with open('1.txt', 'r') as input_str:
    s = input_str.read()
    data = list(element.splitlines() for element in s.split('\n\n'))

print(f"Part 1 answer: {list_of_cal(data)[0]}")
print(f"Part 2 answer: {sum(list_of_cal(data)[0:3])}")