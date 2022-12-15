def sand_units(records: str):
    rocks = set()
    for line in records.splitlines():
        line = [(x.split(',')) for x  in line.split(' -> ')] 
        lowest_point = 0

        for i in range(len(line) - 1):
            first, second =list(map(int, line[i])),list(map(int, line[i+1]))
            if first[0] == second[0]:
                start_point = min([first[1], second[1]])
                if start_point > lowest_point:
                    lowest_point = start_point
                for x in range(abs(first[1] - second[1]) + 1):
                    rocks.add((first[0], start_point + x ))
            else:
                start_point = min([first[0], second[0]])
                if first[1] > lowest_point:
                    lowest_point = first[1]
                for x in range(abs(first[0] - second[0]) + 1):
                    rocks.add((start_point + x,first[1]))

    count = 0
    while True:
        sand = [500, 0]
        while True:
            if sand[1] > lowest_point:
                return count
            if (sand[0], sand[1] + 1) not in rocks:
                sand = [sand[0], sand[1] + 1]
            elif (sand[0] - 1, sand[1] + 1) not in rocks:
                sand = [sand[0] - 1, sand[1] + 1]
            elif (sand[0] + 1, sand[1] + 1) not in rocks:
                sand = [sand[0] + 1, sand[1] + 1]
            else:
                rocks.add((sand[0], sand[1]))
                count += 1
                break;
    

test_data = '''
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''

with open('14.txt' , 'r') as input_str:
    data = input_str.read()

print(f"first part answer: {sand_units(data)}")
