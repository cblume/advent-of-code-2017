import sys

def checksum_per_line(line):
	current_max = 0
	current_low = sys.maxsize
	values = line.split("\t")
	for value in [int(value) for value in values]:
		if value > current_max:
			current_max = value
		if value < current_low:
			current_low = value
	return current_max - current_low


def checksum():
	checksum = 0
	with open("input/02a.txt", 'r') as f:
		for line in f:
			checksum += checksum_per_line(line)
	return checksum

print(checksum())