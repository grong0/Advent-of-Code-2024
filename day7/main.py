import math
from random import randint


def parse(values: list[int], operators: list[str]) -> int:
    total = values[0]
    for index, value in enumerate(values[1:]):
        match operators[index]:
            case "+":
                total += value
            case "*":
                total *= value
    return total

def generate_operators(length: int) -> list[list[str]]:
    operators = set()
    while len(operators) != math.pow(2, length):
        operators.add(("".join([("*" if randint(0, 1) == 1 else "+") + "," for _ in range(length)])))
    return [operator.split(",")[:-1] for operator in operators]

def main():
    operations = []
    with open("./input.txt") as f:
        for row in f:
            operations.append(row.split(": "))
            operations[-1][0] = int(operations[-1][0])
            operations[-1][1] = [int(val) for val in operations[-1][1].strip("\n").split(" ")]

    total = 0
    for operation in operations:
        for operators in generate_operators(len(operation[1])-1):
            if parse(operation[1], operators) == operation[0]:
                total += operation[0]
                break
    print(total)


if __name__ == "__main__":
    main()
