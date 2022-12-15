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
    records = [x.split() for x in record.split('\n\n')]
    for ind, (first, second) in enumerate(records, start=1):
        if compute(eval(first),eval(second)) < 0:
            pairs += ind
    return pairs
print(f"first part answer: {pairs_count(data)}")
