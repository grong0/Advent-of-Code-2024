def display_grid(grid: list[list[str]], pos: tuple[int, int]):
    for index, row in enumerate(grid):
        line = row.copy()
        if index == pos[0]:
            line[pos[1]] = "@"
        print("".join(line))


def move_box(grid: list[list[str]], raw_pos: tuple[int, int], command: str) -> bool:
    mod = 1
    checking = ""
    pos = raw_pos
    if grid[raw_pos[0]][raw_pos[1]] == "]":
        pos = (raw_pos[0], raw_pos[1] - 1)
    next_pos = (-1, -1)
    match command:
        case "^":
            mod = -1
            t1 = grid[pos[0] - 1][pos[1]]
            t2 = grid[pos[0] - 1][pos[1] + 1]
            checking = t1 + t2
            next_pos = (pos[0] - 1, pos[1])
        case "v":
            mod = 1
            t1 = grid[pos[0] + 1][pos[1]]
            t2 = grid[pos[0] + 1][pos[1] + 1]
            checking = t1 + t2
            next_pos = (pos[0] + 1, pos[1])
        case "<":
            checking = grid[pos[0]][pos[1] - 1]
            next_pos = (pos[0], pos[1] - 2)
        case ">":
            checking = grid[pos[0]][pos[1] + 2]
            next_pos = (pos[0], pos[1] + 2)
        case _:
            raise Exception("not a command")

    if checking == "][":
        move_box(grid, (pos[0] + mod, pos[1] - 1), command)
        move_box(grid, (pos[0] + mod, pos[1] + 1), command)
    elif len(checking) == 1 and ("[" in checking or "]" in checking):
        move_box(grid, next_pos, command)
    elif checking == ".[":
        move_box(grid, (next_pos[0], next_pos[1] + 1), command)
    elif checking == "].":
        move_box(grid, (next_pos[0], next_pos[1] - 1), command)
    elif checking == "[]":
        move_box(grid, next_pos, command)

    match command:
        case "^":
            grid[pos[0] - 1][pos[1]] = "["
            grid[pos[0] - 1][pos[1] + 1] = "]"
            grid[pos[0]][pos[1]] = "."
            grid[pos[0]][pos[1] + 1] = "."
        case "v":
            grid[pos[0] + 1][pos[1]] = "["
            grid[pos[0] + 1][pos[1] + 1] = "]"
            grid[pos[0]][pos[1]] = "."
            grid[pos[0]][pos[1] + 1] = "."
        case "<":
            grid[pos[0]][pos[1] - 1] = "["
            grid[pos[0]][pos[1]] = "]"
            grid[pos[0]][pos[1] + 1] = "."
        case ">":
            grid[pos[0]][pos[1] + 1] = "["
            grid[pos[0]][pos[1] + 2] = "]"
            grid[pos[0]][pos[1]] = "."
        case _:
            raise Exception("not a command")
    return True


def can_push(grid: list[list[str]], raw_pos: tuple[int, int], command: str) -> bool:
    checking = ""
    pos = raw_pos
    if grid[raw_pos[0]][raw_pos[1]] == "]":
        pos = (raw_pos[0], raw_pos[1] - 1)
    match command:
        case "^":
            t1 = grid[pos[0] - 1][pos[1]]
            t2 = grid[pos[0] - 1][pos[1] + 1]
            checking = t1 + t2
        case "v":
            t1 = grid[pos[0] + 1][pos[1]]
            t2 = grid[pos[0] + 1][pos[1] + 1]
            checking = t1 + t2
        case "<":
            checking = grid[pos[0]][pos[1] - 1]
        case ">":
            checking = grid[pos[0]][pos[1] + 2]
        case _:
            raise Exception("not a command")

    if checking == ".." or checking == ".":
        return True
    elif "#" in checking:
        return False

    if len(checking) == 1:
        next_pos = (pos[0], pos[1] - 2)
        if checking == "[":
            next_pos = (pos[0], pos[1] + 2)
        return can_push(grid, next_pos, command)

    if checking[0] == "[":
        return can_push(grid, (pos[0] + (1 if command == "v" else -1), pos[1]), command)
    elif checking[1] == ".":
        return can_push(grid, (pos[0] + (1 if command == "v" else -1), pos[1] - 1), command)
    elif checking[0] == ".":
        return can_push(grid, (pos[0] + (1 if command == "v" else -1), pos[1] + 1), command)
    return can_push(grid, (pos[0] + (1 if command == "v" else -1), pos[1] - 1), command) and can_push(grid, (pos[0] + (1 if command == "v" else -1), pos[1] + 1), command)


def next_block(grid: list[list[str]], pos: tuple[int, int], command: str) -> tuple[str, tuple[int, int]]:
    match command:
        case "^":
            return grid[pos[0] - 1][pos[1]], (pos[0] - 1, pos[1])
        case "v":
            return grid[pos[0] + 1][pos[1]], (pos[0] + 1, pos[1])
        case "<":
            return grid[pos[0]][pos[1] - 1], (pos[0], pos[1] - 1)
        case ">":
            return grid[pos[0]][pos[1] + 1], (pos[0], pos[1] + 1)
        case _:
            return "", (-1, -1)


def main():
    grid = []
    commands = ""
    pos = (-1, -1)
    with open("./input.txt") as f:
        reading_area = True
        for i, row in enumerate(f):
            if len(row) < 2:
                reading_area = False
            if reading_area:
                final_row = []
                for j, col in enumerate(row):
                    match col:
                        case ".":
                            final_row.extend([".", "."])
                        case "@":
                            pos = (i, j * 2)
                            final_row.extend([".", "."])
                        case "#":
                            final_row.extend(["#", "#"])
                        case "O":
                            final_row.extend(["[", "]"])
                grid.append(final_row)
                continue

            commands += row.strip("\n")

    for command in commands:
        block, next_pos = next_block(grid, pos, command)
        if block in ["[", "]"] and can_push(grid, next_pos, command):
            move_box(grid, next_pos, command)
            pos = next_pos
        elif block == ".":
            pos = next_pos

    total_gps_coords = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "[":
                total_gps_coords += (i * 100) + j
    print(total_gps_coords)


if __name__ == "__main__":
    main()
