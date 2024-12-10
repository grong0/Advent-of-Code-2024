def get_neighbors(grid: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] == str(int(grid[pos[0]][pos[1]]) + 1):
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(grid) and grid[pos[0] + 1][pos[1]] == str(int(grid[pos[0]][pos[1]]) + 1):
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] == str(int(grid[pos[0]][pos[1]]) + 1):
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(grid[pos[0]]) and grid[pos[0]][pos[1] + 1] == str(int(grid[pos[0]][pos[1]]) + 1):
        neighbors.append((pos[0], pos[1] + 1))
    return neighbors

def search(grid: list[list[str]], current_node: tuple[int, int], target: tuple[int, int]) -> list[list[tuple[int, int]]]:
    neighbors = get_neighbors(grid, current_node)
    if len(neighbors) == 0:
        if current_node == target:
            return [[current_node]]
        return [[(-1, -1)]]

    paths = []
    for neighbor in neighbors:
        new_paths = search(grid, neighbor, target)
        for path in new_paths:
            if (-1, -1) not in path:
                path.append(current_node)
                paths.append(path)
    return paths

def main():
    grid = []
    trailheads = []
    peaks = []
    with open("./input.txt") as f:
        for i, row in enumerate(f):
            grid.append(list(row.strip("\n")))
            for j, col in enumerate(row):
                if col == "0":
                    trailheads.append((i, j))
                elif col == "9":
                    peaks.append((i, j))

    total = 0
    for trailhead in trailheads:
        for peak in peaks:
            total += len(search(grid, trailhead, peak))
    print(total)


if __name__ == "__main__":
    main()
