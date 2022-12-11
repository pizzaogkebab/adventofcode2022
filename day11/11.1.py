def square(value, base_value):
    return value * value

def addition(op_val, base_value):
    return op_val + base_value

def mulitplication(op_val, base_value):
    return op_val * base_value


class Monkey:
    def __init__(self, lista, function, num, condition, t_target, f_target, items_count = 0):
        self.items = lista
        self.operation = function
        self.value = num
        self.cond = condition
        self.if_true = t_target
        self.if_false = f_target
        self.items_count = items_count


def monkeys_init(records):
    monkeys = []
    for part in records.split('\n\n'):
        lines = part.splitlines()
        lista = [int(num) for num in lines[1].split(': ')[1].split(',')]
        if "old * old" in lines[2]:
            function = square
            value = 0
        elif " * " in lines[2]:
            function = mulitplication
            value = int(lines[2].split()[5])
        elif " + " in lines[2]:
            function = addition
            value = int(lines[2].split()[5])
        condition = int(lines[3].split()[3])
        t_target = int(lines[4].split()[5])
        f_target = int(lines[5].split()[5])
        monkeys.append(Monkey(lista, function, value, condition, t_target, f_target))

    return monkeys


def count(ile, monkeys):
    for round in range(ile):
        for monkey in monkeys:
            while monkey.items:
                worry_level = monkey.items.pop(0)
                monkey.items_count += 1
                worry_level = monkey.operation(worry_level, monkey.value) // 3
                if worry_level % monkey.cond == 0:
                    monkeys[monkey.if_true].items.append(worry_level)
                else:
                    monkeys[monkey.if_false].items.append(worry_level)
    monkey_business = [x.items_count for x in monkeys]
    monkey_business.sort(reverse= True)
    return monkey_business[0] * monkey_business[1]


with open("11.txt", 'r') as input_str:
    data = input_str.read()

print(f"part 1. solution: {count(20, monkeys_init(data))}")
