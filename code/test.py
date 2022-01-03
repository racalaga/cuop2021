#Evaluation and optimization of hepatocyte culture media factors by design of experiments (DoE) methodology
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n = 4
upbound = np.array([1,6,15,15])
bound =np.array([upbound*i/10 for i in range(11)])
relation = list(combinations([1,2,3,4],2))
factor = np.array(np.random.randn(15))
value = []
index = []
for i in range(11):
    for j in range(11):
        for k in range(11):
            for l in range(11):
                x1 = bound[i][0]
                x2 = bound[j][1]
                x3 = bound[k][2]
                x4 = bound[l][3]
                eq = np.array([x1**2,x2**2,x3**2,x4**2,x1*x2,x1*x3,x1*x4,x2*x3,x2*x4,x3*x4,x1,x2,x3,x4,1])
                value.append(np.dot(factor,eq))
                index.append([i,j,k,l])


value = np.array(value)
index = np.array(index)
x = np.linspace(0, 15, 11)
X = np.tile(x, (11, 1))
Y = np.transpose(X)
Z1 = np.reshape(value[:121],(11,11))
Z2 = np.reshape(value[6050:6171],(11,11))
Z3 = np.reshape(value[1099:1210],(11,11))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
ax.plot_surface(X, Y, Z3)
