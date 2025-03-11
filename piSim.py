import random
import math
import sys

pointsIn = 0
N = int(sys.argv[1])

for loop in range(N):
	x = random.random()
	y = random.random()
	if ((x**2+y**2)**(1/2) <= 1):
		pointsIn += 1

approx = (pointsIn/N) * 4
absError = approx - math.pi
relError = absError/math.pi

print("Approx: " + str(approx) +  "\nN: " + str(N) + "\nAbsolute Error " + str(absError) + "\nRelative Error " + str(relError))
