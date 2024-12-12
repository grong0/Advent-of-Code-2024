def get_perimeter_score(grid: list[list[str]], point: tuple[int, int]) -> int:
    plant = grid[point[0]][point[1]]
    perimeter_score = 0
    if point[0] - 1 < 0:
        perimeter_score += 1
    elif grid[point[0] - 1][point[1]] != plant:
        perimeter_score += 1
    if point[0] + 1 >= len(grid):
        perimeter_score += 1
    elif grid[point[0] + 1][point[1]] != plant:
        perimeter_score += 1
    if point[1] - 1 < 0:
        perimeter_score += 1
    elif grid[point[0]][point[1] - 1] != plant:
        perimeter_score += 1
    if point[1] + 1 >= len(grid[point[0]]):
        perimeter_score += 1
    elif grid[point[0]][point[1] + 1] != plant:
        perimeter_score += 1
    return perimeter_score


def get_outside_points(grid: list[list[str]], point: tuple[int, int]) -> set[tuple[int, int]]:
    plant = grid[point[0]][point[1]]
    outside_points = set()
    if point[0] - 1 < 0:
        outside_points.add((point[0] - 1, point[1]))
    elif grid[point[0] - 1][point[1]] != plant:
        outside_points.add((point[0] - 1, point[1]))
    if point[0] + 1 >= len(grid):
        outside_points.add((point[0] + 1, point[1]))
    elif grid[point[0] + 1][point[1]] != plant:
        outside_points.add((point[0] + 1, point[1]))
    if point[1] - 1 < 0:
        outside_points.add((point[0], point[1] - 1))
    elif grid[point[0]][point[1] - 1] != plant:
        outside_points.add((point[0], point[1] - 1))
    if point[1] + 1 >= len(grid[point[0]]):
        outside_points.add((point[0], point[1] + 1))
    elif grid[point[0]][point[1] + 1] != plant:
        outside_points.add((point[0], point[1] + 1))
    return outside_points


def find_neighbors(grid: list[list[str]], point: tuple[int, int], neighbors: set[tuple[int, int]], do_once: bool = False) -> set[tuple[int, int]]:
    plant = grid[point[0]][point[1]]
    neighbors.add(point)
    if point[0] - 1 >= 0 and grid[point[0] - 1][point[1]] == plant and (point[0] - 1, point[1]) not in neighbors:
        neighbors.add((point[0] - 1, point[1]))
        if not do_once:
            neighbors.update(find_neighbors(grid, (point[0] - 1, point[1]), neighbors))
    if point[0] + 1 < len(grid) and grid[point[0] + 1][point[1]] == plant and (point[0] + 1, point[1]) not in neighbors:
        neighbors.add((point[0] + 1, point[1]))
        if not do_once:
            neighbors.update(find_neighbors(grid, (point[0] + 1, point[1]), neighbors))
    if point[1] - 1 >= 0 and grid[point[0]][point[1] - 1] == plant and (point[0], point[1] - 1) not in neighbors:
        neighbors.add((point[0], point[1] - 1))
        if not do_once:
            neighbors.update(find_neighbors(grid, (point[0], point[1] - 1), neighbors))
    if point[1] + 1 < len(grid[point[0]]) and grid[point[0]][point[1] + 1] == plant and (point[0], point[1] + 1) not in neighbors:
        neighbors.add((point[0], point[1] + 1))
        if not do_once:
            neighbors.update(find_neighbors(grid, (point[0], point[1] + 1), neighbors))
    return neighbors


def diagonally_connected(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]] | None:
    if (p1[0] - 1, p1[1] - 1) == p2:
        return ((p1[0] - 1, p1[1]), (p1[0], p1[1] - 1))
    if (p1[0] - 1, p1[1] + 1) == p2:
        return ((p1[0] - 1, p1[1]), (p1[0], p1[1] + 1))
    if (p1[0] + 1, p1[1] - 1) == p2:
        return ((p1[0] + 1, p1[1]), (p1[0], p1[1] - 1))
    if (p1[0] + 1, p1[1] + 1) == p2:
        return ((p1[0] + 1, p1[1]), (p1[0], p1[1] + 1))
    return None


def same_region(grid: list[list[str]], *args: tuple[int, int]) -> bool:
    inter = find_neighbors(grid, args[0], set())
    for arg in args[1:]:
        inter = inter.intersection(find_neighbors(grid, arg, set()))
    return inter is not None and len(inter) > 0


def valid_inside_corner(grid: list[list[str]], point: tuple[int, int]) -> bool:
    if point[1] - 1 >= 0 and point[0] - 1 >= 0 and same_region(grid, (point[0], point[1] - 1), (point[0] - 1, point[1])):
        return True
    if point[0] - 1 >= 0 and point[1] + 1 < len(grid[0]) and same_region(grid, (point[0] - 1, point[1]), (point[0], point[1] + 1)):
        return True
    if point[1] + 1 < len(grid[0]) and point[0] + 1 < len(grid) and same_region(grid, (point[0], point[1] + 1), (point[0] + 1, point[1])):
        return True
    if point[0] + 1 < len(grid) and point[1] - 1 >= 0 and same_region(grid, (point[0] + 1, point[1]), (point[0], point[1] - 1)):
        return True
    return False


def main():
    grid = []
    with open("./input.txt") as f:
        for row in f:
            grid.append(list(row.strip("\n")))

    visited_points = set()
    regions = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i, j) in visited_points:
                continue
            neighbors = find_neighbors(grid, (i, j), set())
            visited_points.update(neighbors)

            visited = {}
            for point in neighbors:
                outside_points = get_outside_points(grid, point)
                for outside_point in outside_points:
                    if outside_point in visited.keys():
                        visited[outside_point]["count"] += 1
                        continue
                    visited[outside_point] = {"count": 1, "plant": grid[point[0]][point[1]]}

            sides = 0
            completed_sets = []
            for op1 in visited.keys():
                if visited[op1]["count"] == 2 and valid_inside_corner(grid, op1):
                    sides += 1
                if visited[op1]["count"] == 3:
                    sides += 2
                if visited[op1]["count"] == 4:
                    sides += 4
                for op2 in visited.keys():
                    if op1 == op2:
                        continue

                    diagnal = diagonally_connected(op1, op2)
                    diagnal_value = col + col
                    opposite_diagnal_value = ""
                    crossing = False
                    threading_needle = False
                    all_same_region = False
                    jumping = False
                    if diagnal is not None:
                        crossing = True in [point[0] < 0 or point[0] >= len(grid) for point in diagnal] or True in [point[1] < 0 or point[1] >= len(grid[0]) for point in diagnal]
                    if diagnal is not None and not crossing:
                        opposite_diagnal_value = grid[diagnal[0][0]][diagnal[0][1]] + grid[diagnal[1][0]][diagnal[1][1]]
                        threading_needle = diagnal_value == opposite_diagnal_value and same_region(grid, diagnal[0], diagnal[1])
                        all_same_region = same_region(grid, op1, op2, diagnal[0], diagnal[1])
                        jumping = diagnal[0] not in neighbors and diagnal[1] not in neighbors
                    thing_happened = threading_needle and not crossing
                    if diagnal is not None and not thing_happened and not all_same_region and not jumping and set((op1, op2)) not in completed_sets:
                        sides += 1
                        completed_sets.append(set((op1, op2)))
            regions.append({
                "points": neighbors,
                "area": len(neighbors),
                "sides": sides
            })
    total_price = 0
    for region in regions:
        print(region["area"], "*", region["sides"], "=", region["area"] * region["sides"])
        total_price += region["area"] * region["sides"]
    print(total_price)


if __name__ == "__main__":
    main()
