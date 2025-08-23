# from functools import cache
import datetime
from enum import Enum
from typing import Optional


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def rotate_clockwise(self) -> "Direction":
        return Direction((self.value + 1) % 4)

    def rotate_counter_clockwise(self) -> "Direction":
        return Direction((self.value + 3) % 4)


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def same_as(self, point: "Point") -> bool:
        return self.x == point.x and self.y == point.y

    def as_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def move(self, direction: Direction, distance: int) -> "Point":
        new_point = Point(self.x, self.y)
        match direction:
            case Direction.NORTH:
                new_point.y -= distance
            case Direction.EAST:
                new_point.x += distance
            case Direction.SOUTH:
                new_point.y += distance
            case Direction.WEST:
                new_point.x -= distance
        return new_point


class Deer:
    point: Point
    direction: Direction
    score: int
    path: set[Point]

    def __init__(self, point: Point, direction: Direction, score: int, path: set[Point]) -> None:
        self.point = point
        self.direction = direction
        self.score = score
        self.path = path

    def print(self) -> None:
        print(f"point: {self.point.__dict__}")
        print(f"direction: {self.direction.name}")
        print(f"score: {self.score}")
        print(f"path: {self.path}")

    def as_left(self) -> "Deer":
        new_dir = Direction.rotate_counter_clockwise(self.direction)
        new_point = self.point.move(new_dir, 1)
        new_path = self.path.copy()
        new_path.add(self.point)
        return Deer(new_point, new_dir, self.score + 1001, new_path)

    def as_right(self) -> "Deer":
        new_dir = Direction.rotate_clockwise(self.direction)
        new_point = self.point.move(new_dir, 1)
        new_path = self.path.copy()
        new_path.add(self.point)
        return Deer(new_point, new_dir, self.score + 1001, new_path)

    def as_forward(self) -> "Deer":
        new_point = self.point.move(self.direction, 1)
        new_path = self.path.copy()
        new_path.add(self.point)
        return Deer(new_point, self.direction, self.score + 1, new_path)

    def is_valid(self, maze: list[list[str]], visited_points: dict[Point, "Deer"]) -> bool:
        # bounds
        if not (0 <= self.point.x < len(maze[0])) or not (0 <= self.point.y < len(maze)):
            return False

        # tile
        if maze[self.point.y][self.point.x] == "#":
            return False

        # been there in global path
        for point in visited_points:
            if self.point.same_as(point) and visited_points[point].score + 2000 <= self.score:
                return False

        return True


def display_maze(maze: list[list[str]], start: Point, end: Point, path: dict[Point, Deer], deer: Deer):
    maze_copy = [row.copy() for row in maze]
    for point in path:
        maze_copy[point.y][point.x] = "\033[0;31mo\033[0m"
    for y, row in enumerate(maze_copy):
        new_row = row.copy()
        if y == start.y:
            new_row[start.x] = "S"
        elif y == end.y:
            new_row[end.x] = "E"
        if y == deer.point.y:
            icon = "$"
            match deer.direction:
                case Direction.NORTH:
                    icon = "^"
                case Direction.EAST:
                    icon = ">"
                case Direction.SOUTH:
                    icon = "v"
                case Direction.WEST:
                    icon = "<"
            new_row[deer.point.x] = f"\033[0;32m{icon}\033[0m"
        print("".join(new_row))


def add_deer(queue: dict[int, list[Deer]], deer: Deer):
    if deer.score not in queue.keys():
        queue[deer.score] = []
    queue[deer.score].append(deer)


def get_new_deer(queue: dict[int, list[Deer]]) -> Optional[Deer]:
    sorted_keys = list(queue.keys())
    sorted_keys.sort()
    for key in sorted_keys:
        if len(queue[key]) == 0:
            continue
        deer = queue[key].pop(0)
        if len(queue[key]) == 0:
            queue.pop(key)
        return deer


def run(maze: list[list[str]], start: Point, end: Point) -> dict[int, list[Deer]]:
    queue: dict[int, list[Deer]] = {0: [Deer(start, Direction.EAST, 0, set())]}
    visisted_points: dict[Point, Deer] = {}

    completed_runs: dict[int, list[Deer]] = {}
    while len(queue) != 0:
        deer = get_new_deer(queue)
        if deer is None:
            break

        if deer.point not in visisted_points:
            visisted_points[deer.point] = deer
        elif visisted_points[deer.point].score > deer.score:
            print("\n\n\n ===================FORTNITE=================== \n\n\n")
        deer.path.add(deer.point)

        # end check
        if deer.point.same_as(end):
            if deer.score not in completed_runs.keys():
                completed_runs[deer.score] = []
            completed_runs[deer.score].append(deer)
            continue

        # update queue
        if deer.as_left().is_valid(maze, visisted_points):
            add_deer(queue, deer.as_left())
        if deer.as_right().is_valid(maze, visisted_points):
            add_deer(queue, deer.as_right())
        if deer.as_forward().is_valid(maze, visisted_points):
            add_deer(queue, deer.as_forward())

        # debug
        # os.system("clear")
        # display_maze(maze, start, end, visisted_points, deer)
        # print(f"queue length: {len(queue)}")
        # print(f"queue keys: {queue.keys()}")
        # total_deer = 0
        # for key in queue.keys():
        #     total_deer += len(queue[key])
        # print(f"total deer: {total_deer}")
        # deer.print()
        # _ = input()

    return completed_runs


def main():
    maze: list[list[str]] = []
    start = Point(-1, -1)
    end = Point(-1, -1)
    with open("./input.txt") as f:
        for y, row in enumerate(f):
            if row.find("S") != -1:
                start = Point(row.find("S"), y)
                row = row.replace("S", ".")
            elif row.find("E") != -1:
                end = Point(row.find("E"), y)
                row = row.replace("E", ".")
            maze.append(list(row.strip("\n")))

    start_time = datetime.datetime.now()
    complete_runs = run(maze, start, end)
    end_time = datetime.datetime.now()
    sorted_keys = list(complete_runs.keys())
    sorted_keys.sort()
    print(f"part1: {complete_runs[sorted_keys[0]][0].score}")
    points: set[tuple[int, int]] = set()
    for deer in complete_runs[sorted_keys[0]]:
        points = points.union(map(lambda i: i.as_tuple(), deer.path))
    print(f"part2: {len(points)}")
    print(f"runtime: {(end_time - start_time).seconds}")


if __name__ == "__main__":
    main()
