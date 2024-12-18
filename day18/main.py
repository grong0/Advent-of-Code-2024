from sys import displayhook


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


def main():
    sample_max = 6 + 1
    input_max = 70 + 1
    sample_bytes = 12
    input_bytes = 1024
    using_sample = False
    grid = [list("." * (sample_max if using_sample else input_max)) for _ in range(sample_max if using_sample else input_max)]
    with open("./sample.txt" if using_sample else "./input.txt") as f:
        for index, row in enumerate(f):
            if index == (sample_bytes if using_sample else input_bytes):
                break
            spl = row.strip("\n").split(",")
            x = int(spl[0])
            y = int(spl[1])
            grid[y][x] = "#"

    queue = [(0, 0)]
    visited = {(0, 0): (-1, -1)}
    while len(queue) != 0:
        curr_node = queue.pop(0)
        if curr_node == ((sample_max if using_sample else input_max) - 1, (sample_max if using_sample else input_max) - 1):
            break
        neighbors = get_valid_cardinal_neighbors(grid, curr_node)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited[neighbor] = curr_node
        
    whole_gamer_path_kachow = []
    curr_node = ((sample_max if using_sample else input_max) - 1, (sample_max if using_sample else input_max) - 1)
    while curr_node != (0, 0):
        whole_gamer_path_kachow.append(curr_node)
        curr_node = visited[curr_node]
    
    display_grid_path(grid, whole_gamer_path_kachow)
    print(len(whole_gamer_path_kachow))
        


if __name__ == "__main__":
    main()
