#!/usr/bin/env python
import math

def P4(x):
	return (x**4)-(2.0*(x**3))-(4.0*(x**2))+(4.0*x)+4.0

def dP4(x):
	return (4.0*(x**3))-(6.0*(x**2))-(8.0*x)+4.0

def newton(x0,e,nMax):
	xk = 0
	for k in range(1,nMax):
		print 
		print "iteration " + str(k-1)
		xk = x0 - (P4(x0)/dP4(x0))
		print "xk = " + str(xk)
		print "error: " + str(abs(xk-x0))
		if abs(xk-x0) < e:
			break
		x0 = xk
	print
	print "result: " + str(xk)

newton(1.5,(10**(-6)),100)