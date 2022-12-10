def image_render(records: str):
    image = []
    cycle = 0
    screen_line = []
    sprite_pos = 1
    h_line = 0

    for line in records.splitlines():
        instr, *value = line.strip().split()
        cycle += 1

        if cycle != 1 and (cycle - 1) % 40 == 0:
            image.append(screen_line)
            screen_line = []
            h_line += 1

        if abs(cycle - (40 * h_line) - 1 - sprite_pos) <= 1:
            screen_line.append('⬜')
        else:
            screen_line.append('⬛')

        if instr == "addx":
            cycle += 1

            if cycle != 1 and (cycle - 1) % 40 == 0:
                image.append(screen_line)
                screen_line = []
                h_line += 1

            if abs(cycle - (40 * h_line) - 1 - sprite_pos) <= 1:
                screen_line.append('⬜')
            else:
                screen_line.append('⬛')

            sprite_pos += int(*value)
    image.append(screen_line)

    return image


with open('10.txt', 'r') as input_str:
    data = input_str.read()

screen = image_render(data)

for y in screen:
    for x in y:
        print(x, end=' ')
    print('')
