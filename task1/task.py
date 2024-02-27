import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

assert(n > 0 and m > 0), "Invalid Arguments"

index = 0
res = ""

arr = [i + 1 for i in range(n)]

while True:
    res += str(arr[index])
    index = (index + m - 1) % n
    if index == 0:
        break

print(res)
