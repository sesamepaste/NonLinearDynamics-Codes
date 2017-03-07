import matplotlib.pyplot as plt

mu = float(input())
n = int(input())
step = float(input())
X_i = float(input())
V_i = float(input())


X = [0]*n
t = [0]*n
V = [0]*n
i=0
X[0] = X_i
V[0] = V_i
#markers_on = [0,3,567]
while i<n-1:
	X[i+1] = X[i] + V[i]*step
	V[i+1] = V[i] - ( X[i] + mu*(X[i]*X[i]-1)*V[i] )*step
	t[i+1] = t[i] + step
	i+=1

plt.plot(X,V,'r--')
#plt.gca().set_ylim([0,10])
plt.show()
