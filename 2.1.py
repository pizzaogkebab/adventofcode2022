transitions = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', "Y": "P", "Z": "S"}
winners = ["RS", "PR", "SP"]
points = {'R': 1, 'P': 2, 'S': 3}


def final_score(records):
    for key, value in transitions.items():
        records= records.replace(key, value)

    score = 0
    for line in records.splitlines():
        choose_1, choose_2 = line.split(" ")
        score += points[choose_2]
        if (choose_2 + choose_1) in winners:
            score += 6
        elif choose_1 == choose_2:
            score += 3

    return score


with open('2.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 1. answer: {final_score(data)}")
