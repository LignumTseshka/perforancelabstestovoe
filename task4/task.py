import fileinput, sys

nums = []


for line in fileinput.input(files=sys.argv[1]):
    nums.append(int(line))



middleValue = 0

for i in nums:
    middleValue += i
middleValue = round(middleValue / len(nums) + 1)

res = 0
for i in nums:
    res += abs(i - middleValue)

print(res)