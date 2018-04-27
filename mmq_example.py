#!/usr/bin/env python

import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([0, 1, 2, 3, 4])
Y = np.array([0.98, -3.01, -6.99, -11.01, -15.0])

# Calcula os elementos das marizes
a11 = np.sum(X**2)
a12 = np.sum(X)
a22 = len(X)
b1 = np.sum(X * Y)
b2 = np.sum(Y)

# Monta e resolve o sistema
A = np.array([[a11, a12], [a12, a22]])

B = np.array([b1,b2])

a = solve(A, B)
print (a)

# define a funcao g(x) para plotar 
g = lambda x: a[0]*x+a[1]

# cria pontos (x, y) da reta 
Xr = np.arange(-1, 5, 0.5)

# Plota os pontos e a reta
plt.plot(X, Y, ".", Xr, g(Xr), "-") 
plt.grid()
plt.show()