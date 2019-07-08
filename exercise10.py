
def equationA(x):
    return (4*(x)**3) - (6 * (x)**2 )+ (7*x) - 23

def equationB(x):
    return -26 + (85 * x) - (91 * (x)**2) + (44 * (x)**3) - (8*(x)**4) + (x)**5

def derivedA(x):
    return (12*(x)**2) - (12*x) + 7

def derivedB(x):
    return 85 - (182 * x) + (132 * (x)**2) - (32 * (x)**3) + (5 *(x)**4)

def bisectionA(xl, xu, es):
    eserr = 1
    fxm = 1
    while(eserr > es):
        fxl = equationA(xl)
        fxu = equationA(xu)
        xm = (xl + xu)/2
        fxmprev = fxm
        fxm = equationA(xm)
        eserr = ((fxm - fxmprev) /fxm) * 100
        if (fxl * fxm ) < 0:
            xu = xm
        elif (fxl * fxm) > 0:
            xl = xm
        elif (fxl * fxm) == 0:
            return xm
    return xm
def bisectionB(xl, xu, es):
    eserr = 1
    fxm = 1
    while(eserr > es):
        fxl = equationB(xl)
        fxu = equationB(xu)
        xm = (xl + xu)/2
        fxmprev = fxm
        fxm = equationB(xm)
        eserr = ((fxm - fxmprev) /fxm) * 100
        if (fxl * fxm ) < 0:
            xu = xm
        elif (fxl * fxm) > 0:
            xl = xm
        elif (fxl * fxm) == 0:
            return xm
    return xm

def newtonA(x0, es):
    eserr = 1
    while(eserr > es):
        xi = x0 - (equationA(x0) / derivedA(x0))
        eserr = ((xi-x0)/xi) * 100
        x0 = xi
    return xi

def newtonB(x0, es):
    eserr = 1
    while(eserr > es):
        xi = x0 - (equationB(x0) / derivedB(x0))
        eserr = ((xi-x0)/xi) * 100
        x0 = xi
    return xi

xu = 2.025
xl = 2.035
es = 0.005
xlb = 0.5575
xub = 0.5565
x0 = 2.025
print("Bisection Equation A: " , bisectionA(xl,xu,es))
print("Bisection Equation B: ", bisectionB(xlb,xub,es))
print("Newton - Raphson Equation A: ", newtonA(x0, es))
print("Newton - Raphson Equation B: ", newtonB(x0, es))

