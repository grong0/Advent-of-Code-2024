import sys
from functools import cache


def display_maze(maze: list[list[str]], start: tuple[int, int] = (-1, -1), end: tuple[int, int] = (-1, -1), pos: tuple[int, int] = (-1, -1), direction: int = -1):
    for index, row in enumerate(maze):
        new_row = row.copy()
        if index == start[0]:
            new_row[start[1]] = "S"
        elif index == end[0]:
            new_row[end[1]] = "E"
        if index == pos[0]:
            icon = "$"
            match direction:
                case 0:
                    icon = "^"
                case 1:
                    icon = ">"
                case 2:
                    icon = "v"
                case 3:
                    icon = "<"
            new_row[pos[1]] = icon
        print("".join(new_row))


@cache
def get_valid_cardinal_neighbors(maze: list[list[str]], pos: tuple[int, int]) -> list[dict]:
    neighbors = []
    if pos[0] - 1 >= 0 and maze[pos[0] - 1][pos[1]] != "#":
        neighbors.append({
            "direction": 0,
            "pos": (pos[0] - 1, pos[1])
        })
    if pos[0] + 1 < len(maze) and maze[pos[0] + 1][pos[1]] != "#":
        neighbors.append({
            "direction": 2,
            "pos": (pos[0] + 1, pos[1])
        })
    if pos[1] - 1 >= 0 and maze[pos[0]][pos[1] - 1] != "#":
        neighbors.append({
            "direction": 3,
            "pos": (pos[0], pos[1] - 1)
        })
    if pos[1] + 1 < len(maze[0]) and maze[pos[0]][pos[1] + 1] != "#":
        neighbors.append({
            "direction": 1,
            "pos": (pos[0], pos[1] + 1)
        })
    return neighbors


# @cache
def run(maze: tuple[tuple[str]], pos: tuple[int, int], end: tuple[int, int], score: int, path: tuple[tuple[tuple[int, int], int], ...], direction: int) -> int:
    if pos == end:
        return score

    set_path = set(list(path))
    set_path.add((pos, direction))
    path = tuple(set_path)

    lowset_score = -1
    for neighbor in get_valid_cardinal_neighbors(maze, pos):
        if (neighbor["pos"], neighbor["direction"]) in path or (neighbor["pos"], abs(neighbor["direction"] - direction)) in path:
            continue

        neighbor_score = -1
        if neighbor["direction"] != direction and abs(direction - neighbor["direction"]) != 2:
            neighbor_score = run(maze, neighbor["pos"], end, score + 1001, path, neighbor["direction"])
        elif neighbor["direction"] == direction:
            neighbor_score = run(maze, neighbor["pos"], end, score + 1, path, direction)

        if lowset_score == -1 or (neighbor_score != -1 and neighbor_score < lowset_score):
            lowset_score = neighbor_score

    return lowset_score


def main():
    maze = []
    start = (-1, -1)
    end = (-1, -1)
    with open("./input.txt") as f:
        for index, row in enumerate(f):
            if row.find("S") != -1:
                start = (index, row.find("S"))
                row = row.replace("S", ".")
            elif row.find("E") != -1:
                end = (index, row.find("E"))
                row = row.replace("E", ".")
            maze.append(tuple(row.strip("\n")))

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(5000)
    print(run(tuple(maze), start, end, 0, tuple([]), 1))


if __name__ == "__main__":
    main()
