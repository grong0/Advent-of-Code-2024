def get_locations(grid: list[list[str]], frequency: str) -> list[tuple[int, int]]:
    locations = []
    for y, row in enumerate(grid):
        if frequency in row:
            locations.append(tuple((y, x) for x in range(len(row)) if row[x] == frequency)[0])
    return locations


def main():
    grid = []
    grid2 = []
    with open("./input.txt") as f:
        for row in f:
            grid.append(list(row.strip("\n")))
            grid2.append(list(row.strip("\n")))

    frequencies = set()
    for row in grid:
        for col in row:
            if col != ".":
                frequencies.add(col)

    antinode_locations = set()
    for frequency in frequencies:
        locations = get_locations(grid, frequency)
        antinode_locations.update(locations)
        for loc_1 in locations:
            for loc_2 in locations:
                if loc_1[0] == loc_2[0] and loc_1[1] == loc_2[1]:
                    continue
                row_distance = loc_1[0] - loc_2[0]
                col_distance = loc_1[1] - loc_2[1]
                # from loc_1
                anti_loc = (loc_1[0] + row_distance, loc_1[1] + col_distance)
                while anti_loc[0] >= 0 and anti_loc[0] < len(grid) and anti_loc[1] >= 0 and anti_loc[1] < len(grid[0]):
                    antinode_locations.add(anti_loc)
                    grid2[anti_loc[0]][anti_loc[1]] = "#"
                    anti_loc = (anti_loc[0] + row_distance, anti_loc[1] + col_distance)
                # from loc_2
                anti_loc = (loc_2[0] - row_distance, loc_2[1] - col_distance)
                while anti_loc[0] >= 0 and anti_loc[0] < len(grid) and anti_loc[1] >= 0 and anti_loc[1] < len(grid[0]):
                    antinode_locations.add(anti_loc)
                    grid2[anti_loc[0]][anti_loc[1]] = "#"
                    anti_loc = (anti_loc[0] - row_distance, anti_loc[1] - col_distance)

    for row in grid:
        print("".join(row))
    for row in grid2:
        print("".join(row))

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
