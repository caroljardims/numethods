import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

X = np.array([-2., -1., 0, 1., 2., 6.])
Y = np.array([19.01, 3.99, -7.00, 4.01, 9, 45.00])

# Calcula os elementos das marizes
A11 = np.sum(X**4)
A12 = np.sum(X**3)
A13 = np.sum(X**2)
A23 = np.sum(X)
A33 = len(X)
B1 = np.sum(X**2*Y) 
B2 = np.sum(X*Y)
B3 = np.sum(Y)

# Monta e resolve o sistema
A = np.array([[A11,A12, A13],[A12, A13, A23], [A13, A23, A33]])
B = np.array([B1,B2,B3])
a = solve(A, B)
print (a)

# define a funcao g(x) para plotar 
g = lambda x: a[0]*x*x+a[1]*x+a[2]

# cria pontos (x, y) da reta 
Xr = np.arange(X[0], X[-1]+1, 0.2)
Yr = []
for x in Xr:
    Yr.append(g(x))    

# Plota os pontos e a reta
plt.plot(X, Y, ".", Xr, Yr, "-") 
plt.grid()
plt.show()