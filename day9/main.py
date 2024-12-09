def find_from_reverse_not_empty(lst: list[str]) -> int:
    new_lst = lst.copy()
    new_lst.reverse()
    for index, item in enumerate(new_lst):
        if item != ".":
            return len(new_lst) - index - 1
    return -1


def main():
    # getting data
    data = ""
    with open("./input.txt") as f:
        data = f.read().strip("\n")

    # expanding
    parsed = ""
    id = 0
    for index, char in enumerate(data):
        if index % 2 == 0:
            parsed += str((str(id) + ",") * int(char))
            id += 1
        else:
            parsed += str(("." + ",") * int(char))
    parsed = parsed.strip(",").split(",")

    # sorting
    while parsed.index(".") < find_from_reverse_not_empty(parsed):
        index_of_empty = parsed.index(".")
        index_of_id = find_from_reverse_not_empty(parsed)
        if index_of_id == -1:
            break
        parsed[index_of_empty] = parsed[index_of_id]
        parsed[index_of_id] = "."

    # calculating total
    total = 0
    for index, item in enumerate(parsed):
        if item == ".":
            break
        total += index * int(item)
    print(total)


if __name__ == "__main__":
    main()
