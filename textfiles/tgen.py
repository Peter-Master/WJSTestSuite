# testfile gen

import sys
import random

#random.seed(1488)

n = int(sys.argv[1])
output = sys.argv[2]

with open(output, 'w') as ofile:
	for i in range(n):
		s = random.randint(0,9999)
		f = random.randint(s+1,10000)
		p = random.randint(1,100)

		ofile.write(str(s) + " " + str(f) + " " + str(p) + "\n")
