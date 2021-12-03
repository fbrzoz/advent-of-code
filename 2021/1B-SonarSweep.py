# Day 1, puzzle 2: Sonar Sweep

with open("input", "r") as fd:
	depths = [int(x) for x in fd.readlines()]

	# this solution is largely going to be similar with 1-1's, but repeated to
	# create appropriate sliding windows (which then get zipped for comparison)
	window_a = zip(depths, depths[1:], depths[2:])
	window_b = zip(depths[1:], depths[2:], depths[3:])
	depth_increases = sum([1 if sum(x) < sum(y) else 0 for x, y in zip(window_a, window_b)])
	print(depth_increases)
