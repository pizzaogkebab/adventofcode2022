def scenic_score(records: str) -> int:
    grid = []

    for x in records.splitlines():
        grid.append(list(map(int, x)))

    visibility_score = {}
    for y_ind, y in enumerate(grid):
        for x_ind, x in enumerate(grid[y_ind]):

            # left
            left = 0
            for i in range(x_ind - 1, -1, -1):
                left += 1
                if grid[y_ind][i] >= x:
                    break
            # right
            right = 0
            for i in range(x_ind + 1, len(grid[0])):
                right += 1
                if grid[y_ind][i] >= x:
                    break
            # up
            up = 0
            for i in range(y_ind - 1, -1, -1):
                up += 1
                if grid[i][x_ind] >= x:
                    break
            # down
            down = 0
            for i in range(y_ind + 1, len(grid[0])):
                down += 1
                if grid[i][x_ind] >= x:
                    break

            visibility_score[(y_ind, x_ind)] = left * right * up * down
    return max(list(visibility_score.values()))


with open('8.txt', 'r') as input_str:
    data = input_str.read()

print(f"part 2. solution: {scenic_score(data)}")
