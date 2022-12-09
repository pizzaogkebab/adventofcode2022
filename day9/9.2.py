def positions_quantity(records: str) -> int:
    positions = []
    unique = {(0, 0)}

    for x in range(10):
        positions.append([0, 0])

    for line in records.splitlines():
        line = line.split()
        direction, = line[0]
        number = int(line[1])
        for _ in range(number):
            if direction == 'L':
                positions[0][0] -= 1
            elif direction == 'R':
                positions[0][0] += 1
            elif direction == 'D':
                positions[0][1] -= 1
            elif direction == 'U':
                positions[0][1] += 1

            h = positions[0]
            for i in range(1, 10):
                t = positions[i]
                if abs(h[0] - t[0]) == 2 and abs(h[1] - t[1]) == 2:
                    positions[i] = [(h[0] + t[0]) // 2, (h[1] + t[1]) // 2]
                elif abs(h[0] - t[0]) == 2:
                    positions[i] = [(t[0] + h[0]) // 2, h[1]]
                elif abs(h[1] - t[1]) == 2:
                    positions[i] = [h[0], (t[1] + h[1]) // 2]
                h = positions[i]
            unique.add(tuple(positions[-1]))

    return len(unique)


with open('9.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 2. solution: {positions_quantity(data)}")
