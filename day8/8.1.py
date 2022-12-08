def visible_quantity(records: str) -> int:
    grid = []

    for x in records.splitlines():
        grid.append(list(map(int, x)))

    visible = set()
    for y_ind, y in enumerate(grid[1:-1], start=1):
        for x_ind, x in enumerate(grid[y_ind][1:-1], start=1):
            # left
            for elem in grid[y_ind][0:x_ind]:
                if elem >= x:
                    break
            else:
                visible.add((y_ind, x_ind))
                continue
            # right
            for elem in grid[y_ind][x_ind+1:]:
                if elem >= x:
                    break
            else:
                visible.add((y_ind, x_ind))
                continue
            # up
            for i in range(y_ind):
                if grid[i][x_ind] >= x:
                    break
            else:
                visible.add((y_ind, x_ind))
                continue
            # down
            for i in range(y_ind+1, len(grid)):
                if grid[i][x_ind] >= x:
                    break
            else:
                visible.add((y_ind, x_ind))
                continue
    return len(visible) + 2*len(grid) + 2*len(grid[0]) - 4


with open('8.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 1. solution: {visible_quantity(data)}")
