import math

def part1():
	side1 = []
	side2 = []
	with open("./input.txt") as f:
		for line in f:
			split = line.split("   ")
			side1.append(int(split[0]))
			side2.append(int(split[1]))

	side1.sort()
	side2.sort()

	total = 0
	for l, r in zip(side1, side2):
		total += abs(l - r)

	print(total)

if __name__ == "__main__":
	part1()