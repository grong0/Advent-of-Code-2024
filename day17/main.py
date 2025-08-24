import datetime
from math import ceil, floor, log


def get_program_output(a: int, b: int, c: int, program: list[int]) -> list[int]:
    combo_array = [0, 1, 2, 3, a, b, c, -1]
    output = []
    index = 0
    while index < len(program):
        opcode = program[index]
        operand = program[index + 1]
        match opcode:
            case 0:
                combo_array[4] = floor(combo_array[4] / pow(2, combo_array[operand]))
            case 1:
                combo_array[5] = combo_array[5] ^ operand
            case 2:
                combo_array[5] = combo_array[operand] % 8
            case 3:
                index = operand - 2 if combo_array[4] != 0 else index
            case 4:
                combo_array[5] = combo_array[5] ^ combo_array[6]
            case 5:
                output.append(combo_array[operand] % 8)
                # if output[-1] != program[len(output)-1]:
                #     break
            case 6:
                combo_array[5] = floor(combo_array[4] / pow(2, combo_array[operand]))
                pass
            case 7:
                combo_array[6] = floor(combo_array[4] / pow(2, combo_array[operand]))

        index += 2

    return output


def main():
    a = -1
    b = -1
    c = -1
    program: list[int]

    with open("./input.txt") as f:
        file = f.readlines()
        a = int(file[0][file[0].find(": ") + 2 :])
        b = int(file[1][file[1].find(": ") + 2 :])
        c = int(file[2][file[2].find(": ") + 2 :])
        program = [int(i) for i in file[4][file[4].find(": ") + 2 :].split(",")]

    """
    a | how long the gaps are    | what number it starts at in output    | the pattern of each column
    --+--------------------------+---------------------------------------+------------------------------
    0 | 16 long gaps of 8        | starts at 0                           | increases by 1
    1 | 8 long gaps of 8         | starts at 1                           | 1 0 3 2 5 4 7 6
    2 | 4 long gaps of 8         | starts at 2                           | 2 3 0 1 6 7 4 5
    3 | 2 long gaps of 8         | starts at 3                           | decreases by 1
    4 | 1 long gap of 8          | starts at 4                           | increases by 1
    5 | 1 long gap of 8          | starts at 4                           | increases by 2
    6 | 1 long gap of 8          | starts at 5                           | flips between 5 and 1
    7 | 1 long gap of 8          | starts at 0                           | is only 0

    a increment equation: 8^(i+1) | i is the column index
    a starting position: p * 8^i | p is the original starting position, i is the column index

    0,3,5,4,3,0
    """

    STARTING_A = 4
    COLUMN = 0

    a = STARTING_A * pow(8, COLUMN)
    while a < 10000:
        output = get_program_output(a, b, c, program)
        print(f"{a} {output}")
        a += pow(8, COLUMN+1)

    def start_of_gap(start: int, column: int, target: int):
        # the size of each batch
        base_duplicates = ceil(pow(2, 4 - start))
        print(f"base_duplicates: {base_duplicates}")
        # how many outputs are skipped in between pattern values
        skipping = pow(8, column+1)
        print(f"skipping: {skipping}")
        # the min a could be to potentially have a value
        min_a = start + pow(8, column+1)
        print(f"min_a: {min_a}")
        # the amount of batches to look over to get to the target
        steps = ((target - (min_a % 8)) + 8) % 8
        print(f"steps: {steps}") 

        # assuming the pattern: increasing by 1,
        return steps * skipping * base_duplicates

    ans = start_of_gap(STARTING_A, COLUMN, 2)
    print(ans)

    output = get_program_output(ans, b, c, program)
    print(f"{output}")

if __name__ == "__main__":
    main()
