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

def listToInt(listZ):
	return sum([reversed(listZ)[i] * (10**i) for i in range(len(listZ)-1)])

def part2(input):
	total = 0
	for line in input:
		a = []
		b = line
		c = []
		while (len(c) + len(b)) != 12:
			x = b[len(c) + len(b) - 11]
			a = b[:x] 
			b = b[x:]
			a = a[a.index(max(a))]
			b = a[1:] + b
			c.append(a[0])
		total += listToInt(sum(c + b))
	return total

	
print(f"Part 1: {part1(input)} \Part 2: {part2(input)}")