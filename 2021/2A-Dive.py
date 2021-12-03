# Day 2, puzzle 1: Dive!

distance = 0
depth = 0

with open("input", "r") as fd:
	commands = [(cmd, int(amt)) for cmd, amt in [line.split(" ") for line in fd.readlines()]]

	for command, amount in commands:
		if command == "forward":
			distance += amount
		elif command == "up":
			depth -= amount
		elif command == "down":
			depth += amount
		else:
			# what
			pass

print(distance * depth)
