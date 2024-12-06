import os
import time


def display_grid(grid):
    for row in grid:
        print(str(row))

def contains_guard(grid):
    for row in grid:
        if "^" in row or ">" in row or "<" in row or "v" in row:
            return True
    return False

def move(grid, pos) -> tuple[int, int]:
    state = grid[pos[0]][pos[1]]

    next_pos = (-1, -1)
    turn_pos = (-1, -1)
    next_state = "_"
    match state:
        case "^":
            next_pos = pos[0]-1,pos[1]
            turn_pos = pos[0],pos[1]+1
            next_state = ">"
        case ">":
            next_pos = pos[0],pos[1]+1
            turn_pos = pos[0]+1,pos[1]
            next_state = "v"
        case "<":
            next_pos = pos[0],pos[1]-1
            turn_pos = pos[0]-1,pos[1]
            next_state = "^"
        case "v":
            next_pos = pos[0]+1,pos[1]
            turn_pos = pos[0],pos[1]-1
            next_state = "<"

    if next_pos == (-1, -1):
        return pos

    grid[pos[0]][pos[1]] = "X"
    
    if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[pos[0]]):
        return -2, -2

    next_tile = grid[next_pos[0]][next_pos[1]]
    match next_tile:
        case ".":
            grid[next_pos[0]][next_pos[1]] = state
            return next_pos
        case "X":
            grid[next_pos[0]][next_pos[1]] = state
            return next_pos
        case "#":
            grid[turn_pos[0]][turn_pos[1]] = next_state
            return turn_pos
        case _:
            return pos

def main():
    grid = []
    pos = (-1, -1)
    with open("./input.txt") as f:
        for row, line in enumerate(f):
            if "^" in line:
                pos = row, line.index("^")
            grid.append(list(line.strip("\n")))

    while contains_guard(grid):
        pos = move(grid, pos)
        
        # print
        # os.system("clear")
        # display_grid(grid)
        # time.sleep(0.2)

        if pos == (-2, -2):
            break
    
    x_count = 0
    for row in grid:
        x_count += str(row).count("X")
    print(x_count)

if __name__ == "__main__":
    main()
