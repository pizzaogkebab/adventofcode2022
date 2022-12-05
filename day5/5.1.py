from collections import defaultdict
with open('5.txt', 'r') as input_str:
    graph, instrs = input_str.read().split('\n\n')


def dict_create(records: str) -> dict:
    d = defaultdict(list)
    for line in records.splitlines()[0:8]:
        for x in range(1,len(line),4):
            if line[x] == ' ':
                continue
            else:
                d[int(records.splitlines()[8][x])].append(line[x])
    for ind, x in enumerate(d,start=1):
        d[ind].reverse()
    return d

def word_formation(records, ddict):
    for records in records.splitlines():
        q, a, b = int(records.split(' ')[1]), int(records.split(' ')[3]), int(records.split(' ')[5])
        for x in range(q):
            elem = ddict[a].pop()
            ddict[b].append(elem)
    s = ""
    for x in range(1,10):
        if len(ddict[x]) >0:
            element = ddict[x].pop()
            s += element
    return s

print(word_formation(instrs , dict_create(graph)))
