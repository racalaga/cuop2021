#Evaluation and optimization of hepatocyte culture media factors by design of experiments (DoE) methodology
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
from numpy.random.mtrand import beta

M1 = 0.7
alpha_1 = np.array([1,2,3,4,5,6,7,8,9,10])/10
temp = []
log = []
for  i in range(1000):
    beta_1 = -np.random.rand(1)-0.5
    temp = []
    for j in alpha_1:
        v = beta_1*(j-M1)**2+np.random.randn(1)
        temp.append(v)
    temp=np.array(temp)
    log.append(temp)
log = np.array(log)
plt.plot(log.mean(axis=1))

M2 = 0.3
M3 = 1
alpha_2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])/10
alpha_3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])/10
temp = []
log = []
for  i in range(1000):
    beta_2 = -np.random.rand(1)-0.5
    beta_3 = -np.random.rand(1)-0.5
    beta_5 = np.random.rand(1)*2-1.2
    beta_6 = np.random.rand(1)*2-0.6
    beta_9 = np.random.rand(1)
    temp = []
    for j in alpha_2:
        for k in alpha_3:
            v =  beta_2*i**2+beta_3*j**2+beta_5*i+beta_6*j+beta_9
            temp.append(v)
    temp=np.array(temp)
    log.append(temp)
log = np.array(log)

x = np.linspace(0, 15, 15)
X = np.tile(x, (15, 1))
Y = np.transpose(X)
Z1 = np.reshape(log[1],(15,15))
Z2 = np.reshape(log[400],(15,15))
Z3 = np.reshape(log[300],(15,15))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1)
plt.close()




