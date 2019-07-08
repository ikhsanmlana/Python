
#2

def equationA(x):
    return (x**3) + (7*(x**2)) - 36

def derivedA(x):
    return (3*(x**2)) + (14*x)

def bisection(xl, xu, es):
    eserr = 1
    fxm = 1
    while(eserr > es):
        fxl = equationA(xl)
        fxu = equationA(xu)
        xm = (xl + xu)/2
        fxmprev = fxm
        fxm = equationA(xm)
        if(fxm == 0):
            return xm
        eserr = ((fxm - fxmprev) /fxm) * 100
        if (fxl * fxm ) < 0:
            xu = xm
        elif (fxl * fxm) > 0:
            xl = xm
        elif (fxl * fxm) == 0:
            return xm
    return xm

def newton(x0, es):
    eserr = 1
    while(eserr > es):
        xi = x0 - (equationA(x0) / derivedA(x0))
        eserr = abs((xi-x0)/xi) * 100
        x0 = xi
    return xi

es = 0.005
xl = -4
xu = -2
print("Bisection Equation: " , "-", bisection(-4,-2,es))
print("Newton - Raphson Equation: ", newton(-4, es))

#3

def equation(x):
    return x**4 - 3*(x**3) + 6*(x**2) - 10*x - 9

def derived1(x,h):
    return (equation(x+h) - equation(x-h)) / (2*h)

def derived2(x,h):
    return (equation(x+h) - 2*equation(x) + equation(x-h)) / (h**2)

def forward(x,h):
    return ((equation(x+h) - equation(x))/h)

def backward(x,h):
    return ((equation(x) - equation(x-h))/h)

def central(x,h):
    return ((equation(x+h) - equation(x-h))/ (2*h))

print("------------------------------------------------------")
print("h\t f'exact\t f'approximation\t f'relative error\t f''exact\t f''approximation\t f''relative error")
print("0.5\t", -10, "\t ", derived1(0,0.5), "\t\t\t\t ", ((-10-(derived1(0,0.5)))/-10) * 100, "\t\t\t\t 12\t\t\t", derived2(0,0.5), "\t\t\t\t", ((12-(derived2(0,0.5)))/12) * 100)
print("0.25 ", -10, "\t ", derived1(0,0.25), "\t\t\t\t ", ((-10-(derived1(0,0.25)))/-10) * 100, "\t\t\t 12\t\t\t", derived2(0,0.25), "\t\t\t\t", ((12-(derived2(0,0.25)))/12) * 100)
print("0.125", -10, "\t ", derived1(0,0.125), "\t\t\t ", ((-10-(derived1(0,0.125)))/-10) * 100, "\t\t\t 12\t\t\t", derived2(0,0.125), "\t\t\t\t", ((12-(derived2(0,0.125)))/12) * 100)
print("------------------------------------------------------")
print("h\t f'exact\tf'backward\t  f'forward\t  f'cental")
print("0.5\t", -10, "\t ", backward(0,0.5), "\t\t ", forward(0,0.5), "\t", central(0,0.5))
print("0.25", -10, "\t ", backward(0,0.25), "\t ", forward(0,0.25), "\t", central(0,0.25))
print("0.125", -10, "\t ", backward(0,0.125), "\t ", forward(0,0.125), "\t", central(0,0.125))

