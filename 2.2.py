transitions = {'A': 'R', 'B': 'P', 'C': 'S'}
should_win = {'S': 'R', 'R': 'P', 'P': 'S'}
should_lose = {value: key for key, value in should_win.items()}
points = {'R': 1, 'P': 2, 'S': 3}


def final_score(records: str) -> int:
    for key, value in transitions.items():
        records = records.replace(key, value)

    score = 0
    for line in records.splitlines():
        choose_1, choose_2 = line.split(" ")
        if choose_2 == 'X':
            score += points[should_lose[choose_1]]
        elif choose_2 == "Y":
            score += points[choose_1] + 3
        else:
            score += points[should_win[choose_1]] + 6
    return score


with open('2.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 2. answer: {final_score(data)}")
