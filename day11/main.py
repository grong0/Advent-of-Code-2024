def main():
    stones = []
    with open("./input.txt") as f:
        stones = [int(item) for item in f.read().strip("\n").split(" ")]

    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:len(str(stone))//2]))
                new_stones.append(int(str(stone)[len(str(stone))//2:len(str(stone))]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    print(len(stones))

if __name__ == "__main__":
    main()
