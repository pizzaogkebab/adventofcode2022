def compute(records: list) -> list:
    sums = []
    for x in records:
        sums.append(sum(map(int, x)))
    return sorted(sums, reverse= True)


with open('1.txt' , 'r') as input_s:
    s = input_s.read()
    data = list(part.splitlines() for part in s.split('\n\n'))

print(f"Part 1 answer: {compute(data)[0]}")
print(f"Part 2 answer: {sum(compute(data)[0:3])}")