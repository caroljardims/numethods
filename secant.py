#!/usr/bin/env python
import math

def P4(x):
	return (x**4)-(2.0*(x**3))-(4.0*(x**2))+(4.0*x)+4.0

def secant(x0,x1,e,nMax):
	if abs(x0) == abs(x1):
		print "equal initals variables"
		return

	xk = 0
	for k in range(0,nMax):
		print 
		print "iteration " + str(k)
		xk = ((P4(x1)*x0) - (P4(x0)*x1)) / (P4(x1) - P4(x0))
		print "x" + str(k+1) + " = " + str(xk)
		print "error: " + str(abs(x1-x0))
		if abs(x1-x0) < e:
			break
		x0 = x1
		x1 = xk
		
	print
	print "result: " + str(xk)

secant(0.0,3.0,(10**(-6)),100)
print math.pi