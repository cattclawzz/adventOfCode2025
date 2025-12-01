dial = 50
input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''
input = input.split("\n")

def part1(dial, input):
	password = 0
	
	for i in input:
		direction = i[0]
		clicks = int(i[1:])
		
		if direction == 'L':
			dial = abs((dial - clicks) % 100)
		elif direction == 'R':
			dial = (dial + clicks) % 100
			
		if dial == 0:
			password += 1
			
	return password
	
def part2(dial, input):
    password = 0

    for i in input:
        direction = i[0]
        clicks = int(i[1:])

        if direction == 'L':
            password += abs(((dial-1)%100-clicks) // 100)
            dial = (dial - clicks) % 100
        elif direction == 'R':
            password += abs((dial+clicks) // 100)
            dial = (dial + clicks) % 100
    return password

		
print(f"Part 1: {part1(50, input)} \nPart 2: {part2(50, input)}")