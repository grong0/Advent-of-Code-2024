def valid_before(rules: dict, pages: list[str], page: str) -> bool:
    start_index = pages.index(page)

    for i in range(start_index, len(pages)):
        if page in rules[pages[i]]["after"]:
            # print(page, "was in", rules[pages[i]]["after"], "after")
            # print(page, pages[pages.index(page)])
            # print(page, "was bad in", pages)
            return False
    return True

# def valid_after(rules: dict, pages: list[str], page: str) -> bool:
#     start_index = pages.index(page)

#     for i in range(start_index, -1, -1):
#         if page in rules[pages[i]]["before"]:
#             # print(page, "was in", rules[pages[i]]["before"], "before")
#             # print(page, pages[pages.index(page)])
#             return False
#     return True

def all_valid(rules: dict, pages: list) -> bool:
    for i in range(len(pages)):
        # is_valid_after, index_after = valid_after(rules, pages, pages[i])
        if not valid_before(rules, pages, pages[i]):
            # print(pages, "not valid")
            # print(pages[index_before])
            return False
    return True

def part1():
    rules = {}
    valid_pages = []
    with open("./input.txt") as f:
        logging_rules = True
        for line in f:
            if len(line) < 2:
                logging_rules = False
                continue

            if logging_rules:
                split = line.split("|")
                start = split[0]
                end = split[1].strip("\n")

                if start not in rules.keys():
                    rules[start] = {"before": [], "after": []}
                if end not in rules.keys():
                    rules[end] = {"before": [], "after": []}

                rules[end]["before"].append(start)
                rules[start]["after"].append(end)

            else:
                pages = line.split(",")
                pages[-1] = pages[-1].strip("\n")
                if all_valid(rules, pages):
                    valid_pages.append(pages)

    total = 0
    for valid_page in valid_pages:
        total += int(valid_page[len(valid_page)//2])
    print(total)

def part2():
    rules = {}
    invalid_pages: list[list[str]] = []
    with open("./input.txt") as f:
        logging_rules = True
        for line in f:
            if len(line) < 2:
                logging_rules = False
                continue

            if logging_rules:
                split = line.split("|")
                start = split[0]
                end = split[1].strip("\n")

                if start not in rules.keys():
                    rules[start] = {"before": [], "after": []}
                if end not in rules.keys():
                    rules[end] = {"before": [], "after": []}

                rules[end]["before"].append(start)
                rules[start]["after"].append(end)

            else:
                pages = line.split(",")
                pages[-1] = pages[-1].strip("\n")
                if not all_valid(rules, pages):
                    invalid_pages.append(pages)
    
    parsed_pages = []
    for pages in invalid_pages:
        bad_pages = []
        good_pages = []
        
        for page in pages:
            good_pages.append(page)
            if not all_valid(rules, good_pages):
                good_pages.remove(page)
                bad_pages.append(page)
        
        for page in bad_pages:           
            for i in range(len(good_pages)+1):
                good_pages.insert(i, page)
                if all_valid(rules, good_pages):
                    break
                good_pages.remove(page)                
        
        parsed_pages.append(good_pages)

    total = 0
    for pages in parsed_pages:
        total += int(pages[len(pages)//2])
    print(total)

def main():
    part2()

if __name__ == "__main__":
    main()
