from matplotlib import pyplot as plt

n = 10000
r = 2
x1_i = 0.5
x2_i = 0.501

X1 = [x1_i]*n
X2 = [x2_i]*n

t = [0]*n

for i in range(1,n):
	X1[i] = r * X1[i-1] * (1 - X1[i-1])
	X2[i] = r * X2[i-1] * (1 - X2[i-1])
	t[i] = i

plt.plot(t,X1,t,X2)
plt.show()
