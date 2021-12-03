# Day 2, puzzle 2: Dive!

distance = 0
depth = 0
aim = 0

with open("input", "r") as fd:
	commands = [(cmd, int(amt)) for cmd, amt in [line.split(" ") for line in fd.readlines()]]

	for command, amount in commands:
		if command == "forward":
			distance += amount
			depth += aim * amount
		elif command == "up":
			aim -= amount
		elif command == "down":
			aim += amount
		else:
			# what
			pass

print(distance * depth)
