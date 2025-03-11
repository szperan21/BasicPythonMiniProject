import math
import sys

TOL = float(sys.argv[1])
N = 0
approx = 0
absError= math.e

outFile = open("approxE.txt", "w")

while(abs(absError) > TOL):
	N += 100
	approx = (1+1/N)**N
	absError = approx - math.e
	relError = absError/math.e

outFile.write("Approximation: " + str(approx) + "\n" + "N: " + str(N) + "\n" + "Absolute Error: " + str(absError) + "\n" + "Relative Error: " + str(relError)) 



