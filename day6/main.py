def get_new_grid():
    grid = []
    pos = (-1, -1)
    with open("./input.txt") as f:
        for row, line in enumerate(f):
            if "^" in line:
                pos = row, line.index("^")
            grid.append(list(line.strip("\n")))
    return grid, pos, "^"

def display_grid(grid, pos, state):
    mod_grid = [row.copy() for row in grid]
    mod_grid[pos[0]][pos[1]] = state
    for row in grid:
        print("".join(row))

def move(grid, pos, state) -> tuple[tuple[int, int], str]:
    next_pos = (-1, -1)
    turn_pos = (-1, -1)
    next_state = "_"
    next_mark = "o"
    next_corner = "b"
    match state:
        case "^":
            next_pos = pos[0]-1,pos[1]
            turn_pos = pos[0],pos[1]+1
            next_state = ">"
            next_mark = "u"
            next_corner = ";"
        case ">":
            next_pos = pos[0],pos[1]+1
            turn_pos = pos[0]+1,pos[1]
            next_state = "v"
            next_mark = "r"
            next_corner = "k"
        case "<":
            next_pos = pos[0],pos[1]-1
            turn_pos = pos[0]-1,pos[1]
            next_state = "^"
            next_mark = "l"
            next_corner = "i"
        case "v":
            next_pos = pos[0]+1,pos[1]
            turn_pos = pos[0],pos[1]-1
            next_state = "<"
            next_mark = "d"
            next_corner = "j"

    if next_pos == (-1, -1):
        return pos, state

    if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[pos[0]]):
        grid[pos[0]][pos[1]] = next_mark
        return (-2, -2), state

    current_tile = grid[pos[0]][pos[1]]
    next_tile = grid[next_pos[0]][next_pos[1]]

    # corners
    if next_tile in ["i", "j", "k", ";"] and next_tile == next_corner:
        return (-3, -3), state

    # empty
    if next_tile in [".", "u", "r", "l", "d", "+", "-", "|", "%", "i", "j", "k", ";"]:
        if next_mark == get_value(grid, next_pos) or (next_mark in ["l", "r"] and get_value(grid, next_pos) == "-") or (next_mark in ["u", "d"] and get_value(grid, next_pos) == "|") or current_tile == next_tile == "%":
            return (-3, -3), state

        if (current_tile == "r" and next_mark == "l") or (current_tile == "l" and next_mark == "r"):
            next_mark = "-"
        elif (current_tile == "u" and next_mark == "d") or (current_tile == "u" and next_mark == "d"):
            next_mark = "|"
            
        elif (current_tile in ["l", "r", "-"] and next_mark in ["u", "d"]) or (current_tile in ["u", "d", "|"] and next_mark in ["l", "r"]):
            next_mark = "+"

        # dont overwrite corners and crosses
        if get_value(grid, pos) not in ["+", "%", "i", "j", "k", ";"]:
            grid[pos[0]][pos[1]] = next_mark

        return next_pos, state

    # obsticle
    elif next_tile in ["#", "O"]:
        if get_value(grid, turn_pos) in ["#", "O"]:
            next_corner = "%"
        if get_value(grid, pos) != "%":
            grid[pos[0]][pos[1]] = next_corner
        return pos, next_state

    else:
        print("NEXT TILE NOT ACCOUNTED FOR", next_tile)

    return (-1, -1), state

def get_value(grid, pos) -> str:
    return grid[pos[0]][pos[1]]

def valid_grid(grid):
    # check corners
    if "+" in [grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1]]:
        return False

    # check sides
    if "l" in [row[0] for row in grid] or "r" in [row[-1] for row in grid]:
        return False

    # check top and bottom
    if "u" in grid[0] or "d" in grid[-1]:
        return False

    return True

def main():
    base_grid, base_pos, base_state = get_new_grid()
    grid, pos, state = get_new_grid()

    valid_grids = 0
    for i, row in enumerate(base_grid):
        for z, col in enumerate(row):
            current_item = (i * len(base_grid[i])) + z + 1
            max_item = len(grid * len(grid[0]))
            percent_done = (current_item / max_item) * 100
            print(round(percent_done, 1), "% (", current_item, "/", max_item, ")", sep="")

            # skip non empty
            if col != ".":
                continue

            grid[i][z] = "O"

            while pos not in [(-2, -2), (-3, -3)]:
                pos, state = move(grid, pos, state)

            if valid_grid(grid):
                valid_grids += 1

            grid, pos, state = get_new_grid()

    print(valid_grids)

if __name__ == "__main__":
    main()
