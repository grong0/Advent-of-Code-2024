def get_neighbors(grid: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] == str(
        int(grid[pos[0]][pos[1]]) + 1
    ):
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(grid) and grid[pos[0] + 1][pos[1]] == str(
        int(grid[pos[0]][pos[1]]) + 1
    ):
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] == str(
        int(grid[pos[0]][pos[1]]) + 1
    ):
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(grid[pos[0]]) and grid[pos[0]][pos[1] + 1] == str(
        int(grid[pos[0]][pos[1]]) + 1
    ):
        neighbors.append((pos[0], pos[1] + 1))
    return neighbors


def search(
    grid: list[list[str]],
    current_node: tuple[int, int],
    visited_peaks: set[tuple[int, int]] = set(),
) -> set[tuple[int, int]]:
    neighbors = get_neighbors(grid, current_node)
    if len(neighbors) == 0:
        if grid[current_node[0]][current_node[1]] == "9":
            visited_peaks.add(current_node)
        return visited_peaks
    for neighbor in neighbors:
        new_visited_peaks = search(grid, neighbor, visited_peaks)
        visited_peaks.update(new_visited_peaks)
    return visited_peaks


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
        visisted_peaks = search(grid, trailhead, set())
        total += len(visisted_peaks)
    print(total)


if __name__ == "__main__":
    main()
