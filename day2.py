input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''
input = [i.split('-') for i in input.split(',')]

def part1(input):
    password = 0
    for rng in input:
        for i in range(int(rng[0]),int(rng[1])+1):
            j = str(i)
            k = len(j)//2
            if j[k:] == j[:k]:
                password += i
    return password

def part2(input):
    password = 0
    for rng in input:
        for i in range(int(rng[0]),int(rng[1])+1):
            j = str(i)
            k = len(j)//2
            if any([''.join(j.split(j[:x])) == '' for x in range(1,k+1)]):
                password += i
    return password

print(f"Part 1: {part1(input)} \nPart 2: {part2(input)}")