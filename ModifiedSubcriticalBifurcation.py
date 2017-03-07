import matplotlib.pyplot as plt

n = int(input())
step = float(input())
X_i = float(input())
r_no = int(input())
r_step = float(input())
r_i = float(input())

r=[0]*r_no
r[0]=r_i
X_f = [0]*r_no

i=1

while i < r_no:
	r[i] = r[i-1] + r_step
	X = X_i
	j=0
	while j <= n-1:
		X += (r[i]*X + X**3 -X**5)*step
		j+=1
	X_f[i] = X
	i+=1
X = X_i
j=0
while j <= n-1:
	X += (r[0]*X + X**3 -X**5)*step
	j+=1
X_f[0] = X

plt.plot(r,X_f,'r+')
plt.show()
#Plots relation between r and fixed point		
		
		
		
	 
