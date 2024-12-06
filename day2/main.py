def intify_sequence(sequence):
	new_sequence = []
	for i in sequence:
		new_sequence.append(int(i))
	return new_sequence

def is_all_decreasing(sequence):
	last_item = -1
	for i in sequence:
		if last_item == -1:
			last_item = i
			continue

		if last_item <= i:
			return False
		last_item = i

	return True

def is_all_increasing(sequence):
	last_item = -1
	for i in sequence:
		if last_item == -1:
			last_item = i
			continue

		if last_item >= i:
			return False
		last_item = i

	return True

def gap_is_ok(sequence):
	last_item = -1
	for i in sequence:
		if last_item == -1:
			last_item = i
			continue

		distance = abs(last_item - i)

		if distance < 1 or distance > 3:
			return False

		last_item = i
	return True

def main():
	safe_reports = 0
	with open("./input.txt") as f:
		for row in f:
			sequence = intify_sequence(row.split(" "))

			if (is_all_decreasing(sequence) or is_all_increasing(sequence)) and gap_is_ok(sequence):
				safe_reports += 1
			else:
				for i in range(len(sequence)):
					new_sequence = sequence.copy()
					new_sequence.pop(i)

					if (is_all_decreasing(new_sequence) or is_all_increasing(new_sequence)) and gap_is_ok(new_sequence):
						safe_reports += 1
						break

	print(safe_reports)

if __name__ == "__main__":
	main()
