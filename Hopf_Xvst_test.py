import matplotlib.pyplot as plt
import math

N = 10000
step = 0.01
r_i = 0.11

T = [0]*N
r = [0]*N
theta = [0]*N
i = 0

r[0] = r_i

while i < N-1:
	r[i+1] = r[i]  + step*(r[i] - r[i]**3)
	theta[i+1] = theta[i] + step*40
	T[i+1] = T[i] + step
	i+=1
X = []
for i in range(len(r)):
	X.append(r[i]*math.cos(theta[i]))

plt.plot(X,T)
plt.show()