import fileinput, math, sys

coords = None; radius = None
boundry = pow(10, 38)
circleFile = fileinput.input(files=sys.argv[1])

coords = circleFile.readline().split()
for idx, cord in enumerate(coords):
        coords[idx] = int(cord)
        assert coords[idx] < boundry and coords[idx] > -(boundry)

radius = int(circleFile.readline())
assert radius > 0, "Radius is 0 or negative."

circleFile.close()

with open(sys.argv[2]) as file: 
    cnt = 0
    for line in file:
        if line != "\n":
            cnt += 1
        assert (cnt < 100), "Too many arguments."
    assert cnt != 0, 'There are no dots.'

dotsFile = fileinput.input(files=sys.argv[2])


for line in dotsFile:
    if line == "\n":
        break

    dotCoords = line.split()
    
    for idx, cord in enumerate(dotCoords):
        dotCoords[idx] = int(cord)
        assert dotCoords[idx] < boundry and dotCoords[idx] > -(boundry)

    aSquared = math.pow(coords[0] - dotCoords[0], 2)
    bSquared = math.pow(coords[1] - dotCoords[1], 2)

    distance = math.sqrt(aSquared + bSquared)
    if distance > radius:
        print(2)
    elif distance < radius:
        print(1)
    else:
        print(0)
