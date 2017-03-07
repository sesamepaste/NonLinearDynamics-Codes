from matplotlib import pyplot as plt

n= 600
X_i = 0.4

X_f1 = []
X_f2 =[]
X_f3 = []
X_f4 = []
r = []

X= [X_i]*n

r_value = 0.0

while r_value < 4:
	for i in range(1,n):
		X[i] = r_value * X[i-1] * (1 - X[i-1])

	X_f1.append(X[n-1])
	r.append(r_value)
	X_f2.append(X[n-2])
	X_f3.append(X[n-3])
	X_f4.append(X[n-4])
	r_value += .00005


# plt.plot(r,X_f1,r,X_f2)
plt.plot(r,X_f1,'k.',r,X_f2,'k.',r,X_f3,'k.',r,X_f4,'k.',)
plt.show()