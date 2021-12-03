# Day 1, puzzle 1: Sonar Sweep

with open("input", "r") as fd:
	depths = [int(x) for x in fd.readlines()]
	depth_increases = sum([1 if x < y else 0 for x, y in zip(depths, depths[1:])])
	print(depth_increases)
