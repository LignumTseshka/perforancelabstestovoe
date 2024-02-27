import fileinput, sys

nums = []

with open(sys.argv[1]) as file: 
    cnt = 0
    for line in file:
        if line != "\n":
            cnt += 1
    assert cnt != 0, 'No arguments.'

for line in fileinput.input(files=sys.argv[1]):
    if line != "\n":
        nums.append(int(line))



middleValue = 0

for i in nums:
    middleValue += i
middleValue = round(middleValue / len(nums))

res = 0
for i in nums:
    res += abs(i - middleValue)

print(res)