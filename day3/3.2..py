def value(character : str) -> int:
    if character.isupper():
        return ord(character) - 38
    else:
        return ord(character) - 96


def sum_of_prior(records : str) -> int:
    sum_of_vals = 0
    records = records.splitlines()
    for x in range(0,len(records)-2,3):
        part_1, part_2, part_3 = set(records[x]), set(records[x+1]), set(records[x+2])
        character = (part_1 & part_2 & part_3).pop()
        sum_of_vals += value(character)
    return sum_of_vals


with open("3.txt" , 'r') as input_str:
    data = input_str.read()

print(sum_of_prior(data))