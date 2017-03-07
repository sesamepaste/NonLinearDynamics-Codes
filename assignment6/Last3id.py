import matplotlib.pyplot as plt


n = 10000
step = 0.001
sigma = 10
# python doesn't treat 085 as 85 and throws error
r = 85/2
b = 2.6667

X_i = 0.0
Y_i = 8.0
Z_i = 5.0

X = [0.0]*n
Y = [0.0]*n
Z = [0.0]*n
t = [0.0]*n


i=0
X[0] = X_i
Y[0] = Y_i
Z[0] = Z_i


while i < n-1:
	X[i+1] = X[i] + step*sigma*(Y[i] - X[i])
	Y[i+1] = Y[i] + step*(X[i]*(r-Z[i]) - Y[i])
	Z[i+1] = Z[i] + step*(X[i]*Y[i]-b*Z[i])
	t[i+1] = t[i] + step
	# print(t[i],X[i],Y[i],Z[i])
	i+=1

# Call any one of the following 3 statements at a time
# plt.plot(Z,X)
# plt.plot(Z,Y)
plt.plot(Z,t)
plt.show()
