from sympy import solveset, symbols, solve, N
from sympy import sqrt

m, d, X1, X2, Y1, Y2= symbols("m d X1 X2 Y1 Y2")


def calcDistance():
    while True:
        try:
            x1In = input("X1 = ")
            y1In = input("Y1 = ")
            x2In = input("X2 = ")
            y2In = input("Y2 = ")
            expr = sqrt((X2 - X1)**2 + (Y2 - Y1)**2) - d
            expr2 = ((X2 - X1)**2 + (Y2 - Y1)**2)**(1/2) - d
            expr = expr.subs(X1, x1In)
            expr = expr.subs(X2, x2In)
            expr = expr.subs(Y1, y1In)
            expr = expr.subs(Y2, y2In)
            expr2 = expr2.subs(X1, x1In)
            expr2 = expr2.subs(X2, x2In)
            expr2 = expr2.subs(Y1, y1In)
            expr2 = expr2.subs(Y2, y2In)
            print("\nResults:")
            sol = N(expr2)
            sol = solve(sol, d)
            expr = solve(expr, d)
            print("Sqrt:\t\t", expr)
            print("Decimal:\t", str(sol))
            closer = str(input("\nEnter 1 to exit.\n"
            "Press any key to continue.\n"))
            if(closer == '1'):
                return
        except:
            print("Invalid Character")


def calcMidpoint():
    while True:
        try:
            x1In = input("X1 = ")
            y1In = input("Y1 = ")
            x2In = input("X2 = ")
            y2In = input("Y2 = ")
            xexpr =(X1 + X2)/2 - m
            yexpr =(Y1 + Y2)/2 - m
            xexpr = xexpr.subs(X1, x1In)
            xexpr = xexpr.subs(X2, x2In)
            yexpr = yexpr.subs(Y1, y1In)
            yexpr = yexpr.subs(Y2, y2In)
            print("\nResults:")
            xexpr = solve(xexpr, m)
            yexpr = solve(yexpr, m)
            print("Midpoint:\t", xexpr, ", ", yexpr, sep='')
            closer = str(input("\nEnter 1 to exit.\n"
            "Press any key to continue.\n"))
            if(closer == '1'):
                return
        except:
            print("Invalid Character")



