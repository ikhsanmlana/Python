
# x(0.2pi) = a + a(0.2pi) = 0.5878
# x(0.3pi) = a + a(0.3pi) = 0.8090
# a1 = 0.7041  a0 = 0.1454
# 0.1454 +

#Data
# 0.1pi , 0.3090
# 0.2pi, 0.5878
#0.3pi, 0.8090
#0.4pi, 0.9511
#0.5pi, 1
import numpy as np
from math import pi
# Newton Interpolation
y = [0.3090, 0.5878, 0.8090, 0.9511]
x = [(0.1*pi),(0.2*pi),(0.3*pi),(0.4*pi)]
# x = [10, 15, 20, 22.5]
# y = [227.04,362.78,517.35,602.97]
b1 = []
b2 = []
b3 = []
t = 0.28 * pi
answer = 0
for i in range(0, len(x)):
    if i == (len(x) -1):
        break
    answer = (y[i+1] - y[i])/(x[i+1] - x[i])
    b1.append(answer)

for i in range(0, len(b1)):
    if i == (len(b1) - 1):
        break
    answer = (b1[i+1] - b1[i]) / (x[i+2] - x[i])
    b2.append(answer)

for i in range(0, len(b2)):
    if i == (len(b2) - 1):
        break
    answer = (b2[i+1] - b2[i]) / (x[i-1] - x[i])
    b3.append(answer)

print("b0: ", y[0])
print("b1: ", b1[0])
print("b2: ", b2[0])
print("b3: ", b3[0])
estimateNewton1 = y[0] + (b1[0]*(t - x[0]))
estimateNewton2 = y[0] + (b1[0]*(t - x[0])) + (b2[0] * (t - x[0]) *(t - x[1]))
estimateNewton3 = y[0] + (b1[0]*(t - x[0])) + (b2[0] * (t - x[0]) *(t - x[1])) + (b3[0]* (t - x[0]) *(t - x[1]) * (t-x[2]))
print("Newton Estimate(Order 1): ", estimateNewton1)
print("Newton Estimate(Order 2): ", estimateNewton2, "Absolute Error: ", ((estimateNewton2 - estimateNewton1)/estimateNewton2) * 100, "%")
print("Newton Estimate(Order 3): ", estimateNewton3, "& Absolute Error: ", ((estimateNewton3 - estimateNewton2)/estimateNewton3) * 100, "%")

# Direct Interpolation

x1 = np.array([[1,0.2*np.pi], [1,0.3*np.pi]])
s1 = np.array([0.5878,0.8090])

x2 = np.array([[1,0.2*np.pi, (0.2*np.pi)**2] , [1,0.3*np.pi, (0.3*np.pi)**2] , [1,0.4*np.pi , (0.4*np.pi)**2]])
s2 = np.array([0.5878, 0.8090 , 0.9511])

x3 = np.array([[1,0.1*np.pi, (0.1*np.pi)**2 , (0.1*np.pi) **3] , [1,0.2*np.pi, (0.2*np.pi)**2 , (0.2*np.pi) **3] ,
               [1,0.3*np.pi, (0.3*np.pi)**2 , (0.3*np.pi) **3] , [1,0.4*np.pi, (0.4*np.pi)**2 , (0.4*np.pi) **3]])
s3 = np.array([0.3090,0.5878,0.8090,0.9511])

sol1 = np.linalg.solve(x1,s1)
sol2 = np.linalg.solve(x2,s2)
sol3 = np.linalg.solve(x3,s3)

est1 = sol1[0] + sol1[1]*0.28*np.pi
est2 = sol2[0] + sol2[1]*(0.28*np.pi) + sol2[2]*(0.28*np.pi)**2
est3 = sol3[0] + sol3[1]*(0.28*np.pi) + sol3[2]*(0.28*np.pi)**2 + sol3[3]*(0.28*np.pi)**3

print("a0: ", sol3[0])
print("a1: ", sol3[1])
print("a2: ", sol3[2])
print("a3: ", sol3[3])
print("Direct Estimate(Order 1): ", est1)
print("Direct Estimate(Order 2): ", est2, "& Absolute Error: ", ((est2 - est1)/est2)*100)
print("Direct Estimate(Order 3): ", est3, "& Absolute Error: ", ((est3 - est2)/est3)*100)

print("FINAL ANSWERS: \t")
print("Newton Estimate(Order 1): ", estimateNewton1)
print("Newton Estimate(Order 2): ", estimateNewton2, "Absolute Error: ", ((estimateNewton2 - estimateNewton1)/estimateNewton2) * 100, "%")
print("Newton Estimate(Order 3): ", estimateNewton3, "& Absolute Error: ", ((estimateNewton3 - estimateNewton2)/estimateNewton3) * 100, "%")
print("Direct Estimate(Order 1): ", est1)
print("Direct Estimate(Order 2): ", est2, "& Absolute Error: ", ((est2 - est1)/est2)*100)
print("Direct Estimate(Order 3): ", est3, "& Absolute Error: ", ((est3 - est2)/est3)*100)



# a1 = np.array([[1, 10, 100, 1000], [1,15, 225 , 15**3], [1, 20, 400, 20**3], [1, 22.5, 22.5**2, 22.5**3]])
# b1 = np.array([227.04, 362.78, 517.35, 602.97])
# print(np.linalg.solve(a1,b1)[3])
