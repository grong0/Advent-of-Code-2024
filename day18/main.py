SAMPLE_MAX = 6 + 1
INPUT_MAX = 70 + 1


def get_valid_cardinal_neighbors(grid: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] != "#":
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] + 1 < len(grid) and grid[pos[0] + 1][pos[1]] != "#":
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] != "#":
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] + 1 < len(grid[0]) and grid[pos[0]][pos[1] + 1] != "#":
        neighbors.append((pos[0], pos[1] + 1))
    return neighbors


def display_grid_path(grid: list[list[str]], path: list[tuple[int, int]]):
    cpy = [row.copy() for row in grid]
    for node in path:
        cpy[node[0]][node[1]] = "O"
    for row in cpy:
        print("".join(row))


def populate_grid(using_sample: bool, cut_off: int) -> tuple[list[list[str]], tuple[int, int]]:
    grid = [list("." * (SAMPLE_MAX if using_sample else INPUT_MAX)) for _ in range(SAMPLE_MAX if using_sample else INPUT_MAX)]
    last_node = (-1, -1)
    with open("./sample.txt" if using_sample else "./input.txt") as f:
        for index, row in enumerate(f):
            if index == cut_off:
                break
            spl = row.strip("\n").split(",")
            x = int(spl[0])
            y = int(spl[1])
            grid[y][x] = "#"
            last_node = (x, y)
    return grid, last_node


def get_path_from_visited(visited: dict[tuple[int, int], tuple[int, int]], using_sample: bool) -> list[tuple[int, int]]:
    whole_gamer_path_kachow = []
    curr_node = ((SAMPLE_MAX if using_sample else INPUT_MAX) - 1, (SAMPLE_MAX if using_sample else INPUT_MAX) - 1)
    if curr_node not in visited.keys():
        return list(visited.keys())
    while curr_node != (0, 0):
        whole_gamer_path_kachow.append(curr_node)
        curr_node = visited[curr_node]
    return whole_gamer_path_kachow


def main():
    using_sample = False
    bytes = 0
    with open("./sample.txt" if using_sample else "./input.txt") as f:
        bytes = len(f.readlines())
    
    breaking_point = (-1, -1)
    for i in range(bytes):
        grid, last_node = populate_grid(using_sample, i)
        
        queue = [(0, 0)]
        visited = {(0, 0): (-1, -1)}
        while len(queue) != 0:
            curr_node = queue.pop(0)
            if curr_node == ((SAMPLE_MAX if using_sample else INPUT_MAX) - 1, (SAMPLE_MAX if using_sample else INPUT_MAX) - 1):
                break
            neighbors = get_valid_cardinal_neighbors(grid, curr_node)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited[neighbor] = curr_node
        
        if ((SAMPLE_MAX if using_sample else INPUT_MAX) - 1, (SAMPLE_MAX if using_sample else INPUT_MAX) - 1) not in visited.keys():
            breaking_point = last_node
            break
    
    print(breaking_point)   


if __name__ == "__main__":
    main()
