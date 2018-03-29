#!/usr/bin/env python
import math

def P4(x):
	return (x**4)-(2.0*(x**3))-(4.0*(x**2))+(4.0*x)+4.0

def bissection(a,b,nMax,e):
	x = 0.0
	for k in range(0,nMax):
		print 
		print "iteration " + str(k)
		x = (a+b)/2
		print "x = " + str(x)
		if P4(a)*P4(b) < 0:
			b = x
		else:
			a = x
		print "error: " + str(abs(b-a))
		if abs(b-a) < e:
			break		
	print
	print "result: " + str(x)

bissection(0.0,3.0,100,(10**(-6)))