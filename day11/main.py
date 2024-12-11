import datetime
import functools
import sys

memo = {}

# @functools.cache
def parse(stones: tuple, blink_target: int, blink_count: int = 0) -> tuple:
    # if (stones, blink_target, blink_count) in memo.keys():
    #     return memo[((stones, blink_target, blink_count))]

    if blink_count == blink_target:
        # memo[(stones, blink_target, blink_count)] = stones
        return stones

    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.extend(parse((1, ), blink_target, blink_count + 1))
        elif len(str(stone)) % 2 == 0:
            length = len(str(stone))
            new_stones.extend(parse((int(str(stone)[:length//2]), ), blink_target, blink_count + 1))
            new_stones.extend(parse((int(str(stone)[length//2:length]), ), blink_target, blink_count + 1))
        else:
            new_stones.extend(parse((stone * 2024, ), blink_target, blink_count + 1))

    # memo[(stones, blink_target, blink_count)] = tuple(new_stones)
    return tuple(new_stones)

def main():
    stones = []
    with open("./sample.txt") as f:
        stones = [int(item) for item in f.read().strip("\n").split(" ")]

    # for i in range(75):
    #     print(i)

    #     new_stones = []
    #     for stone in stones:
    #         if stone in memo.keys():
    #             # print("memo was used for", stone, "equated to", memo[stone])
    #             new_stones.extend(memo[stone])
    #             continue
    #         if stone == 0:
    #             memo[stone] = (1, )
    #             new_stones.append(1)
    #         elif len(str(stone)) % 2 == 0:
    #             length = len(str(stone))
    #             memo[stone] = (int(str(stone)[:length//2]), int(str(stone)[length//2:length]))
    #             new_stones.append(int(str(stone)[:length//2]))
    #             new_stones.append(int(str(stone)[length//2:length]))
    #         else:
    #             memo[stone] = (stone * 2024, )
    #             new_stones.append(stone * 2024)
    #     stones = new_stones

    stones = parse(tuple(stones), 40)

    print(stones)
    print(len(stones))

if __name__ == "__main__":
    main()
