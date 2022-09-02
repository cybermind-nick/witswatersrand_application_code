def meeting_point(x: int, y: int) -> int:
	return x - y

def earliest(line, middle, left_side, right_side) -> int:
	# The min on the right side is farthers to the right end of the line
	min_r = min(right_side)
	# The max on the left side is fartherest to the left end of the line
	max_l = max(left_side)
	# Calculate the true distance on the right side. Calculation not needed for the left side
	distance_r = line - min_r
	distance_l = max_l

	# Check the largest total distance and return it as the earliest time.
	if distance_r > distance_l:
		return distance_r
	else:
		return max_l
	
	
def main():
	seq = [214, 7, 11, 12, 7, 13, 176, 23, 191]
	# get your line length
	line = seq[0]

	# halve the line to distribute the starting points
	middle = line/2

	# sort the starting points to fall on the left or right side of the middle
	left_side = sorted([seq[i] for i in range(2, len(seq)) if seq[i] <= middle])
	right_side = sorted([seq[i] for i in range(2, len(seq)) if seq[i] > middle])
	
	print(earliest(line, middle, left_side, right_side))


if __name__ == "__main__":
	main()
