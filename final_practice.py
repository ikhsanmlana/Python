import numpy as np
import math

#no 1
print("Number 1")

p = np.array([44 * math.pi/180 , 46 * math.pi/180])
q = np.ones(len(p))
print(len(p))
for i in range(len(p)):
    q[i] = math.tan(p[i])



def newton_interpolation(p,q,p1):
    b0 = q[0]
    b1 = (q[1] - q[0])/(p[1] - p[0])

    order_1 = b0
    order_2 = b0 + b1 * (p1-p[0])

    return order_2

print("Second order Newton's interpolation method , tan 45 estimated: ", newton_interpolation(p,q,45*math.pi/180))



def larange_interpolation(p,q,p1):

    b0 = q[0]* ((p1-p[1]) / (p[0]-p[1]))
    b1 = q[0]* ((p1-p[0]) / (p[1]-p[0]))

    return b0+b1

print("Second order larange interpolation method , tan 45 estimated: ", larange_interpolation(p,q,45*math.pi/180))
exact = 1
newton = round(abs(((exact - newton_interpolation(p,q,45*math.pi/180))/exact) * 100),3)
larange = round(abs(((exact - larange_interpolation(p,q,45*math.pi/180))/exact) * 100),3)

print("Relative errors : Newton : ",newton,"\n Larange : ", larange)
print("Hence, Newton interpolation method is the best estimation\n\n")

def equation(x,y):
    return (2*x*y) + (2*x) + (x**2) - (2*(y**2))

def derived_x(x,y):
    return (2*y) + 2 + (2*x)

def derived_y(x,y):
    return (2*x) - (4*y)

def optimization(x,y,set):
    sx = (set * derived_x(x,y))
    sy = (set * derived_y(x,y))
    iteration = 0
    while(iteration <= 10):
        x_new = (x - sx)
        y_new = (y - sy)
        print("Iteration: ", iteration, "X: ", x, "Y: ", y, "f(x): ", equation(x,y))
        x = x_new
        y = y_new
        iteration += 1

optimization(0.5, 1, 0.1)

