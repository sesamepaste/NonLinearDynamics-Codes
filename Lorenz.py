import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab

n = 10000
step = 0.01
sigma = 10
r = 28
b = 2.6667
X_i = 0
Y_i = 1
Z_i = 0

X = [0]*n
Y = [0]*n
Z = [0]*n
t = [0]*n


i=0
X[0] = X_i
Y[0] = Y_i
Z[0] = Z_i


while i < n-1:
	X[i+1] = X[i] + step*sigma*(Y[i] - X[i])
	Y[i+1] = Y[i] + step*(X[i]*(r-Z[i]) - Y[i])
	Z[i+1] = Z[i] + step*(X[i]*Y[i]-b*Z[i])
	t[i+1] = t[i] + step
	i+=1

# fig = pylab.figure()
# ax = Axes3D(fig)

# ax.scatter(X,Y,Z,'r')
plt.plot(X,Z)
plt.show()

