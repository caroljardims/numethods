def LU(A):
	n = len(A)
	U = A
	L = [[0 for x in range(n)] for y in range(n)] 

	for i in range(0,n):
		for j in range(0,n):
			if i == j:
				L[i][j] = 1

	for k in range(0, n-1):
		for i in range(k+1, n):
			L[i][k] = U[i][k]/U[k][k]
			for j in range(k,n):
				U[i][j] = U[i][j]-L[i][k]*U[k][j]

	for l in L: print l
	print
	for u in U: print u
	print 


A = [[1.0, 1.0, 1.0, 0.0, 2.0],
	[0.0, 1.0, 2.0, 1.0, 1.0], 
	[2.0, 1.0, 1.0, 2.0, 0.0],
	[3.0, 2.0, 1.0, 2.0, 1.0],
	[2.0, 1.0, 2.0, 3.0, 1.0]]


for a in A: print a
print
LU(A)
