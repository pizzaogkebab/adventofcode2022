with open('13.txt', 'r') as input_str:
    data = input_str.read()

def compute(x, y) -> int:
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compute([x], y)
    else:
        if type(y) == int:
            return compute(x, [y])

    for a,b in zip(x,y):
        value = compute(a,b)
        if value:
            return value

    return len(x) - len(y)

def pairs_count(records: str) -> int:
    records = [x for x in records.split('\n') if x != '']
    two_ind = 1
    six_ind = 1
    for packet in records:
        if compute(eval(packet), eval('[[2]]')) <= 0:
            two_ind += 1
        if compute(eval(packet), eval('[[6]]')) <= 0:
            six_ind += 1
    six_ind += 1
    return two_ind * six_ind

print(f"second part answer: {pairs_count(data)}")
