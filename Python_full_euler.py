import matplotlib.pyplot as plt
n=int(input())
dt=float(input())
xi=int(input())
X = [0]*n
t = [0]*n
X[0] = xi
i=0
#print("Here")
while i < n-1:
	X[i+1] = X[i] + (X[i]-(X[i])**3+(X[i])**5 )*dt
	t[i+1] = t[i] + dt
	i+=1
plt.plot(t,X,'r--')
plt.show()
