from functools import cache


def modify_stones(stones: dict[str, int], stone: str, value: int):
    if stone not in stones.keys():
        if value == -1:
            print("stone didnt exist and is already -1")
        stones[stone] = value
        return
    stones[stone] += value


# @cache
# def parse(stones: tuple, blink_target: int, blink_count: int = 0) -> tuple:
#     if blink_count == blink_target:
#         return stones

#     new_stones = []
#     for stone in stones:
#         if stone == 0:
#             new_stones.extend(parse((1, ), blink_target, blink_count + 1))
#         elif len(str(stone)) % 2 == 0:
#             length = len(str(stone))
#             new_stones.extend(parse((int(str(stone)[:length//2]), ), blink_target, blink_count + 1))
#             new_stones.extend(parse((int(str(stone)[length//2:length]), ), blink_target, blink_count + 1))
#         else:
#             new_stones.extend(parse((stone * 2024, ), blink_target, blink_count + 1))

#     return tuple(new_stones)


def main():
    stones: dict[str, int] = {}
    with open("./sample.txt") as f:
        for stone in f.read().strip("\n").split(" "):
            stones[stone] = 1

    for blink in range(75):
        print(blink)
        new_stones = stones.copy()
        for i, stone in enumerate(stones.keys()):
            count = stones[stone]
            for _ in range(count):
                if stone == 0:
                    modify_stones(new_stones, "1", 1)
                elif len(str(stone)) % 2 == 0:
                    length = len(str(stone))
                    modify_stones(new_stones, str(stone)[:length//2], 1)
                    modify_stones(new_stones, str(stone)[length//2:length], 1)
                else:
                    modify_stones(new_stones, str(int(stone) * 2024), 1)
                modify_stones(new_stones, stone, -1)
        stones = new_stones

    total_stones = 0
    for key in stones.keys():
        total_stones += stones[key]

    print(stones)
    print(len(stones))

if __name__ == "__main__":
    main()
