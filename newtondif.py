#!/usr/bin/env python
import matplotlib.pyplot as plt
import sys
import time

X=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0]
Y=[11.08,11.41,11.44,11.58,11.84,12.02,12.04,12.04,12.13,12.34,12.92,13.54,14.2]

def main():
    tic = time.clock()
    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        print "Example:"
        print "python lagrange.py 2.4"
        exit()
    arg=sys.argv
    x=float(sys.argv[1])
    if x > 13.0 or x < 1.0:
        print "dado invalido. selecione um valor entre 1 e 13"
        exit()
    Px=P(x)
    print Px
    toc = time.clock()
    print toc - tic

    plt.plot(X,Y,'bo',X,Y,'b-',x,Px,'ro')
    plt.show()

def P(x):
    divDiff=[] 
    divDiff.append(Y)
    for i in range(1, len(X), 1):
        divDiff.append([])
        for j in range(0, len(X)-i, 1): 
            y=(divDiff[i-1][j+1]-divDiff[i-1][j])/(X[j+i]-X[j])    
            divDiff[i].append(y)
    return sumDiff(x,divDiff)

def prod(x,i):
    prod=1.0
    for j in range(i):
        prod=prod * (x-X[j])
    return prod

def sumDiff(x,divDiff):
    s=divDiff[0][0]
    for i in range(1,len(X)):
        s += prod(x,i)*divDiff[i][0]
    return s

if __name__ == "__main__":
    main()