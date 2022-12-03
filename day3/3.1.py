def value(character : str) -> int:
    if character.isupper():
        return ord(character) - 38
    else:
        return ord(character) - 96


def sum_of_prior(records : str) -> int:
    sum_of_vals = 0
    for line in records.splitlines():
        split = len(line) // 2
        part_1 = set(line[0:split])
        part_2 = set(line[split:])
        element = part_1.intersection(part_2).pop()
        sum_of_vals += value(element)
    return sum_of_vals

with open("3.txt" , 'r') as input_str:
    data = input_str.read()

print(sum_of_prior(data))