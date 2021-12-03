# Day 3, puzzle 1: Binary Diagnostics

ones = [0 for _ in range(12)]

with open("input", "r") as fd:
	file = fd.readlines()
	file_lines = len(file)
	reports = [int(x, 2) for x in file]

for report in reports:
	for i in range(report.bit_length()):
		bit = (report & (1 << i)) >> i
		ones[i] += bit

# NOTE: the ones array is still little-endian, we need to fix this
ones = list(reversed(ones))
bits = [1 if bit > (file_lines / 2) else 0 for bit in ones]
gamma = int("".join([str(x) for x in bits]), 2)
epsilon = gamma ^ 0x0FFF

print(f"γ: {gamma}, ε: {epsilon}, power consumption: {gamma * epsilon}")
