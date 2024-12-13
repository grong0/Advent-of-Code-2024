def in_the_span_of(Ax: int, Ay: int, Bx: int, By: int, x: int, y: int) -> tuple[int, int] | None:
    a = Ax
    b = Ay
    c = Bx
    d = By
    c2 = ((b * x) - (a * y)) / ((c * b) - (d * a))
    c1 = (x - (c2 * c)) / a
    if c1 == int(c1) and c2 == int(c2):
        return int(c1), int(c2)
    return None


def main():
    machines = []
    with open("./input.txt") as f:
        for machine in f.read().strip("\n").split("\n\n"):
            lines = machine.split("\n")
            machines.append(
                {
                    "A": {
                        "X": int(lines[0][lines[0].find("+") + 1 : lines[0].find(",")]),
                        "Y": int(lines[0][lines[0].find("+", lines[0].find(",") + 1) + 1 :]),
                    },
                    "B": {
                        "X": int(lines[1][lines[1].find("+") + 1 : lines[1].find(",")]),
                        "Y": int(lines[1][lines[1].find("+", lines[1].find(",") + 1) + 1 :]),
                    },
                    "prize": {
                        "X": int(lines[2][lines[2].find("=") + 1 : lines[2].find(",")]) + 10000000000000,
                        "Y": int(lines[2][lines[2].find("=", lines[2].find(",") + 1) + 1 :]) + 10000000000000,
                    },
                }
            )

    price = 0
    for machine in machines:
        span = in_the_span_of(
            machine["A"]["X"],
            machine["A"]["Y"],
            machine["B"]["X"],
            machine["B"]["Y"],
            machine["prize"]["X"],
            machine["prize"]["Y"]
        )
        if span is not None:
            price += (span[0] * 3) + span[1]
    print(price)


if __name__ == "__main__":
    main()
