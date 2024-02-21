import fileinput, math, sys

coords = None; radius = None


circleFile = fileinput.input(files=sys.argv[1])
coords = circleFile.readline().split()

radius = int(circleFile.readline())
circleFile.close()


dotsFile = fileinput.input(files=sys.argv[2])


for line in dotsFile:
    dotCoords = line.split()
    aSquared = math.pow(int(coords[0]) - int(dotCoords[0]), 2)
    bSquared = math.pow(int(coords[1]) - int(dotCoords[1]), 2)
    distance = math.sqrt(aSquared + bSquared)
    if distance > radius:
        print(2)
    elif distance < radius:
        print(1)
    else:
        print(0)
