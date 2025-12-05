input = '''987654321111111
811111111111119
234234234234278
818181911112111'''

input = [[int(i) for i in line] for line in input.split('\n')]

def part1(input):
	joltage = 0
	for line in input:
		pivot = max(line)
		pivotIndex = line.index(pivot)
		listA = line[:pivotIndex]
		listB = line[pivotIndex+1:]
		a = 0 if len(listA) == 0 else max(listA)
		b = 0 if len(listB) == 0 else max(listB)
		
		if a <= b or (a < pivot and b != 0):
			joltage += (pivot * 10) + b
			print((pivot * 10) + b)
		else:
			joltage += (a * 10) + pivot
			print((a * 10) + pivot)
		
	return joltage
	
print(f"Part 1: {part1(input)}")