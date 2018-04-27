import matplotlib.pyplot as plt
import numpy as np

# Funcao a ser interpolada
f = lambda X:np.exp(X)+np.sin(X)

# Dados
X  = np.array([0., 0.5, 1.0])
Y  = f(X)    

dd = []
# Inserindo na lista de diferencas divididas a lista de dif. div. de ordem 0 
dd.append(Y) 
# ...imprimindo para conferir     
print (dd[0])

# Gerando a tabela de diferecas divididas a partir da ordem 1 em diante
for ordem in range(1, len(X), 1):
    dd.append([])   # Adiciona uma lista vazia para armazenar as dds de ordem 1
    
    # Para cada ordem, calcula a lista de valores resultantes
    for k in range(0, len(X)-ordem, 1): 
        #print (ordem, k)
        #print (dd[ordem-1][k+1],dd[ordem-1][k],x[k+ordem], x[k]) 
        valor = (dd[ordem-1][k+1]-dd[ordem-1][k])/(X[k+ordem]-X[k])    
        #print (valor)  
        dd[ordem].append(valor)
    print (dd[ordem])


def produtorio(x,n):
    prod = 1.
    for i in range(n):
        prod = prod * (x-X[i])
    return prod


def calculaP(x):
    soma = dd[0][0]
    for i in range(1,len(X)):
        soma = soma + produtorio(x,i)*dd[i][0]
    return soma

print (calculaP(0.7))