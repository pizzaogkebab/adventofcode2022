with open('9.txt', 'r') as input_str:
    data = input_str.read()

def compute(records):
    h = [0, 0]
    t = [0, 0]
    positions = {(0, 0)}
    for line in records.splitlines():
        line = line.split()
        direction, = line[0]
        number = int(line[1])
        if direction == 'L':
            h[0] -= number
            if abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2:
                if h[1] == t[1]:
                    for i in range(h[0], t[0] - 1):
                        t[0] -= 1
                        positions.add(tuple(t))
                else:
                    t[1] = h[1]
                    for i in range(h[0], t[0] - 1):
                        t[0] -= 1
                        positions.add(tuple(t))
        elif direction == 'R':
            h[0] += number
            if abs(h[0] - t[0]) >=2 or abs(h[1] - t[1]) >=2:
                if h[1] == t[1]:
                    for i in range(t[0], h[0] - 1):
                        t[0] += 1
                        positions.add(tuple(t))
                else:
                    t[1] = h[1]
                    for i in range(t[0], h[0] - 1):
                        t[0] +=1
                        positions.add(tuple(t))

        elif direction == 'D':
            h[1] -= number
            if abs(h[0] - t[0]) >=2 or abs(h[1] - t[1]) >=2:
                if h[0] == t[0]:
                    for i in range(h[1], t[1] - 1):
                        t[1] -= 1
                        positions.add(tuple(t))
                else:
                    t[0] = h[0]
                    for i in range(h[1], t[1] - 1):
                        t[1] -=1
                        positions.add(tuple(t))
        elif direction == 'U':
            h[1] += number
            if abs(h[0] - t[0]) >=2 or abs(h[1] - t[1]) >=2:
                if h[0] == t[0]:
                    for i in range(t[1], h[1] - 1):
                        t[1] += 1
                        positions.add(tuple(t))
                else:
                    t[0] = h[0]
                    for i in range(t[1], h[1] - 1):
                        t[1] += 1
                        positions.add(tuple(t))
        print(h, t)
    print(positions)
    print(len(positions))
compute(data)