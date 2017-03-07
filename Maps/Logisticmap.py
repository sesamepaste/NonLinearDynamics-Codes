from matplotlib import pyplot as plt

n = int(input())
X_i = float(input())
r = float(input())


X = [-1]*n
t = [0]*n

X[0] = X_i


for i in range(1,n):
	X[i] = r * X[i-1] * (1 - X[i-1])
	t[i] = i

plt.plot(t,X,'g*')
plt.show()

print(X[n-2])
print(X[n-1]) 