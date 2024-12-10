def find_group_from_reverse_not_empty(lst: list[str], ignored_targets: list[str]) -> tuple[int, int]:
    new_lst = lst.copy()
    new_lst.reverse()
    target = None
    end_index = -1
    # print("ignoring", ignored_targets)
    for index, item in enumerate(new_lst):
        # print(index, item)
        if item != "." and target is None and item not in ignored_targets:
            target = item
            # print("target is", target)
            end_index = len(new_lst) - index - 1
        elif target is not None and item != target:
            # print("found end")
            start_index = len(new_lst) - index
            return start_index, end_index + 1 - start_index
    return -1, -1


def get_gap_of_empty(lst: list[str], start_index: int) -> int:
    gap = 0
    for i in range(lst.index(".", start_index), len(lst)):
        if lst[i] != ".":
            break
        gap += 1
    return gap


def main():
    # getting data
    data = ""
    with open("./input.txt") as f:
        data = f.read().strip("\n")

    # expanding
    parsed = ""
    id = 0
    groups_of_empty = 0
    for index, char in enumerate(data):
        if index % 2 == 0:
            parsed += str((str(id) + ",") * int(char))
            id += 1
        else:
            parsed += str(("." + ",") * int(char))
            groups_of_empty += 1
    parsed = parsed.strip(",").split(",")

    # sorting
    ignored_targets = []
    for i in range(id):
        print(i, "/", id)
        # print("".join(parsed))
        start_index_of_id, id_length = find_group_from_reverse_not_empty(parsed, ignored_targets)
        # print("index id", start_index_of_id)
        # print("id length", id_length)
        if start_index_of_id == -1 and id_length == -1:
            # print("no group")
            break
        index_of_empty = -1 # parsed.index(".")
        empty_length = -1 # get_gap_of_empty(parsed, 0)
        index = 0
        gap = 0
        # print("empty groups", groups_of_empty)
        for _ in range(groups_of_empty):
            try:
                index = parsed.index(".", index + gap)
            except:
                # print("yada yada, cya")
                break
            gap = get_gap_of_empty(parsed, index)
            if gap >= id_length:
                index_of_empty = index
                empty_length = gap
                break
            # print("gap at", index, "is too small, continuing search...")
        ignored_targets.append(parsed[start_index_of_id])
        if index_of_empty == -1 or empty_length == -1 or index_of_empty > start_index_of_id:
            # print("no gap available, going to next group...")
            # print()
            continue
        # print("index empty", index_of_empty)
        # print("empty length", empty_length)
        amount_parsed = 0
        for i in range(index_of_empty, index_of_empty + empty_length):
            # print("i", i)
            # print("start", start_index_of_id)
            # print("end", start_index_of_id + (i - index_of_empty))
            # print("amount parsed", i - index_of_empty)
            # print("max parse", id_length - 1)
            if amount_parsed >= id_length:
                break
            parsed[i] = parsed[start_index_of_id]
            amount_parsed += 1
        # print("adding .s")
        for j in range(start_index_of_id, start_index_of_id + amount_parsed):
            parsed[j] = "."
        # print()
        # break

    print("".join(parsed))

    # calculating total
    total = 0
    for index, item in enumerate(parsed):
        if item == ".":
            continue
        total += index * int(item)
    print(total)


if __name__ == "__main__":
    main()
