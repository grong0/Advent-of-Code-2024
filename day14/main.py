def main():
    USING_SAMPLE = False
    width = 11 if USING_SAMPLE else 101
    height = 7 if USING_SAMPLE else 103
    area = [list("." * width) for _ in range(height)]
    robots = []
    with open("./sample.txt" if USING_SAMPLE else "./input.txt") as f:
        for line in f:
            position = line.split(" ")[0]
            velocity = line.strip("\n").split(" ")[1]
            robots.append({
                "pos": (int(position[position.find(",")+1:]), int(position[position.find("=")+1:position.find(",")])),
                "vel": (int(velocity[velocity.find(",")+1:]), int(velocity[velocity.find("=")+1:velocity.find(",")]))
            })

    print(width, height)
    print(width // 2, height // 2)

    SECONDS = 100
    for robot in robots:
        robot["pos"] = ((robot["pos"][0] + (robot["vel"][0] * SECONDS)) % height, (robot["pos"][1] + (robot["vel"][1] * SECONDS)) % width)

    # for robot in robots:
    #     print(robot["pos"])

    tot_safety_factor = 0
    curr_safety_factor = 0
    for i in range(2):
        for j in range(2):
            match (i, j):
                # determine quadrant
                case (0, 0):
                    min_width = 0
                    max_width = width // 2 - 1
                    min_height = 0
                    max_height = height // 2 - 1
                case (0, 1):
                    min_width = width // 2 + 1
                    max_width = width
                    min_height = 0
                    max_height = height // 2 - 1
                case (1, 0):
                    min_width = 0
                    max_width = width // 2 - 1
                    min_height = height // 2 + 1
                    max_height = height
                case (1, 1):
                    min_width = width // 2 + 1
                    max_width = width
                    min_height = height // 2 + 1
                    max_height = height
                case _:
                    min_width = 0
                    max_width = width // 2 - 1
                    min_height = 0
                    max_height = height // 2 - 1

            curr_safety_factor = 0
            for robot in robots:
                if min_height <= robot["pos"][0] <= max_height and min_width <= robot["pos"][1] <= max_width:
                    curr_safety_factor += 1
                    
            if tot_safety_factor == 0:
                tot_safety_factor = curr_safety_factor
                continue
            tot_safety_factor *= curr_safety_factor
    print(tot_safety_factor)


if __name__ == "__main__":
    main()
