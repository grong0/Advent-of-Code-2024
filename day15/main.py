def display_grid(grid: list[list[str]], pos: tuple[int, int]):
    for index, row in enumerate(grid):
        line = row.copy()
        if index == pos[0]:
            line[pos[1]] = "@"
        print("".join(line))


def parse_movements(grid: list[list[str]], pos: tuple[int, int], command: str) -> tuple[list[list[str]], tuple[int, int]]:
    next_pos = (-1, -1)
    next_tiles = []
    match command:
        case "^":
            # next_tile = grid[pos[0] - 1][pos[1]]
            next_pos = (pos[0] - 1, pos[1])
            next_tiles = [grid[i][pos[1]] for i in range(pos[0] - 1, -1, -1)]
        case "v":
            # next_tile = grid[pos[0] + 1][pos[1]]
            next_pos = (pos[0] + 1, pos[1])
            next_tiles = [grid[i][pos[1]] for i in range(pos[0] + 1, len(grid))]
        case "<":
            # next_tile = grid[pos[0]][pos[1] - 1]
            next_pos = (pos[0], pos[1] - 1)
            next_tiles = grid[pos[0]][:pos[1]]
            next_tiles.reverse()
        case ">":
            # next_tile = grid[pos[0]][pos[1] + 1]
            next_pos = (pos[0], pos[1] + 1)
            next_tiles = grid[pos[0]][pos[1] + 1:]
        case _:
            raise Exception("not a command")

    match next_tiles[0]:
        case "#":
            return grid, pos
        case ".":
            return grid, next_pos
        case "O":
            index_of_wall = next_tiles.index("#")
            try:
                index_of_blank = next_tiles.index(".")
            except:
                return grid, pos

            if index_of_blank < index_of_wall:
                first = True
                holding_box = False
                value = "."
                for index, item in enumerate(next_tiles):
                    if holding_box:
                        value = "O"
                    elif not first:
                        value = "."
                        break

                    if item != "0":
                        match command:
                            case "^":
                                grid[pos[0] - index - 1][pos[1]] = value
                            case "v":
                                grid[pos[0] + index + 1][pos[1]] = value
                            case "<":
                                grid[pos[0]][pos[1] - index - 1] = value
                            case ">":
                                grid[pos[0]][pos[1] + index + 1] = value
                            case _:
                                raise Exception("not a command")

                    if first:
                        first = False
                        holding_box = True
                    elif item == ".":
                        holding_box = False
                pos = next_pos
            return grid, pos

        case _:
            raise Exception("not a known tile")


def main():
    grid = []
    commands = ""
    robot_pos = (-1, -1)
    with open("./sample.txt") as f:
        reading_area = True
        for index, row in enumerate(f):
            if len(row) < 2:
                reading_area = False
            if reading_area:
                if row.find("@") != -1:
                    robot_pos = (index, row.find("@"))
                    row = row.replace("@", ".")
                grid.append(list(row.strip("\n")))
                continue
            commands += row.strip("\n")

    for command in commands:
        grid, robot_pos = parse_movements(grid, robot_pos, command)

    display_grid(grid, robot_pos)

    total_gps_coords = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "O":
                total_gps_coords += (i * 100) + j
    print(total_gps_coords)


if __name__ == "__main__":
    main()
