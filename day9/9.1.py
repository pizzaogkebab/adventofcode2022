def positions_quantity(records:str) -> int:
    h = [0, 0]
    t = [0, 0]
    unique = {(0, 0)}
    for line in records.splitlines():
        line = line.split()
        direction, number = line[0], int(line[1])

        # left
        if direction == 'L':
            h[0] -= number
            if abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2:  # check if move is necessary
                t[1] = h[1]  # setting on proper height or width
                for i in range(h[0], t[0] - 1):
                    t[0] -= 1
                    unique.add(tuple(t))

        # right
        elif direction == 'R':
            h[0] += number
            if abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2:
                t[1] = h[1]
                for i in range(t[0], h[0] - 1):
                    t[0] += 1
                    unique.add(tuple(t))

        # down
        elif direction == 'D':
            h[1] -= number
            if abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2:
                t[0] = h[0]
                for i in range(h[1], t[1] - 1):
                    t[1] -= 1
                    unique.add(tuple(t))

        # up
        elif direction == 'U':
            h[1] += number
            if abs(h[0] - t[0]) >= 2 or abs(h[1] - t[1]) >= 2:
                t[0] = h[0]
                for i in range(t[1], h[1] - 1):
                    t[1] += 1
                    unique.add(tuple(t))
    return len(unique)


with open('9.txt', 'r') as input_str:
    data = input_str.read()
print(f"part 1. solution: {positions_quantity(data)}")
