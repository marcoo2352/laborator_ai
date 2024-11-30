import polars as pl 
import numpy as np
print("____________________________________\n\n")


data = pl.read_csv("C:\\Users\\Marco\\Documents\\Uni\\dataset\\padua_weather.csv")

nd = data.to_numpy()
n = nd.shape
#print(nd.shape) >(52, 7)

#a
counter = 0
for i in range(nd.shape[0]):
    if nd[i, 5] == 3: 
        counter += 1
    elif  nd[i, 6] == 3:
        counter += 1
    
#print(counter/52)

#b expected weather per day
day = list()

for dw in range(nd.shape[1]):
    counter = [0, 0, 0]
    for w in range(nd.shape[0]):
          if nd[w, dw] == 1: 
             counter[0] += 1
          elif nd[w, dw] == 2:
              counter[1] += 1
          elif nd[w, dw] == 3:
              counter[2] += 1
    
    day.append(counter.index(max(counter)) + 1)

#print(day) > [3, 1, 2, 1, 1, 1, 1]

#c most probable day knowing its raining

day = list()

for dw in range(nd.shape[1]):
    counter = 0
    for w in range(nd.shape[0]):
          if nd[w, dw] == 1: 
             counter += 1

    day.append(counter)

# print(day) >[17, 19, 16, 19, 19, 20, 27]

#ESERCIZIO 2

X = np.array([0.5, 0.5])
Z = np.array([0.75, 0.25])
W = np.array([[
    [0.98, 0.02], #probablità X=F, Z=F
    [0.90, 0.10]], #probablità X=F, Z=T

    [[0.15, 0.85], #probablità X=T, Z=F
    [0.10, 0.90]]  #probablità X=T, Z=T
])
Y = np.array([[
    [0.95, 0.05], #probablità W=F, Z=F
    [0.85, 0.15]], #probablità W=F, Z=T

    [[0.25, 0.75], #probablità W=T, Z=F
    [0.20, 0.80]]  #probablità W=T, Z=T
])

#let's find P(Y|/x)
# print(W.shape) > (4, 2)

#print(W[0]) >[[0.98 0.02]
#            >[0.9  0.1 ]]

pro = W[0].T @ np.diag(Z)
print(pro)
XZW = np.sum(pro, axis=1)
print(XZW)

pro = W[0].T @ np.diag(Z)
#print(pro) >[[0.735 0.225]
#           > [0.015 0.025]]

XZW = np.sum(pro, axis=1)
#print(XZW) >[0.96 0.04]

Y1= Y[0] * XZW[0]
Y2 = Y[1] * XZW[1]
proy1 = Y1.T @ np.diag(Z) 
proy2 = Y2.T @ np.diag(Z) 
#print(proy1) >[[0.684 0.204]
#             > [0.036 0.036]]

#print(proy2) >[[0.0075 0.002 ]
#             >[0.0225 0.008 ]]