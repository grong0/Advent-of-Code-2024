def display_grid(area: list[list[str]], robots: list[dict[str, tuple[int, int]]], dont_display: bool = False) -> list[list[str]]:
    new_area = [row.copy() for row in area]
    for robot in robots:
        if new_area[robot["pos"][0]][robot["pos"][1]]:
            new_area[robot["pos"][0]][robot["pos"][1]] = "1"
            continue
        new_area[robot["pos"][0]][robot["pos"][1]] = str(int(new_area[robot["pos"][0]][robot["pos"][1]]) + 1)
    if not dont_display:
        for row in new_area:
            print("".join(row))
    return new_area


def if_line_exists(area: list[list[str]], robots: list[dict[str, tuple[int, int]]], threshold: int = 3) -> bool:
    area = display_grid(area, robots, True)
    max_streak = 0
    for row in area:
        non_period_streak = 0
        for char in row:
            if char != ".":
                non_period_streak += 1
                continue

            if non_period_streak > max_streak:
                max_streak = non_period_streak
            non_period_streak = 0

        if non_period_streak > max_streak:
            max_streak = non_period_streak
        non_period_streak = 0
    return max_streak >= threshold

def main():
    USING_SAMPLE = False
    width = 11 if USING_SAMPLE else 101
    height = 7 if USING_SAMPLE else 103
    area = [list("." * width) for _ in range(height)]
    robots = []
    with open("./sample.txt" if USING_SAMPLE else "./input.txt") as f:
        for line in f:
            position = line.split(" ")[0]
            velocity = line.strip("\n").split(" ")[1]
            robots.append({
                "pos": (int(position[position.find(",")+1:]), int(position[position.find("=")+1:position.find(",")])),
                "vel": (int(velocity[velocity.find(",")+1:]), int(velocity[velocity.find("=")+1:velocity.find(",")]))
            })

    second = 0
    while True:
        second += 1
        for robot in robots:
            robot["pos"] = ((robot["pos"][0] + robot["vel"][0]) % height, (robot["pos"][1] + robot["vel"][1]) % width)
        # display_grid(area, robots)
        if if_line_exists(area, robots, 10):
            display_grid(area, robots)
            break
        print("SECOND", second, "\n")


if __name__ == "__main__":
    main()
