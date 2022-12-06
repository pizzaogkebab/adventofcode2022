def char_quantity(records: str, len_of_packet: int) -> int:
    unique = []
    num = 0
    for ind, elem in enumerate(records):
        if len(unique) == len_of_packet:
            num = ind
            break
        if elem in unique:
            if unique[0] == elem:
                unique.remove(elem)
            elif unique[-1] == elem:
                unique.clear()
            else:
                unique = unique[unique.index(elem) + 1:]
        unique.append(elem)
    return num


with open('6.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 1. solution: {char_quantity(data, 4)}")
print(f"part 2. solution: {char_quantity(data, 14)}")
