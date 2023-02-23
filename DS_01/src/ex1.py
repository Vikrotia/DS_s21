import math

def quadratic_equation(a, b, c):
    t = tuple()
    D = math.pow(b, 2.0) - 4.0 * a * c
    if (D < 0):
        t = None   
    elif (D > 0):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        t = (x1, x2)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        t = (x1,)
    return t

#  Запуск   
t = tuple()
t = quadratic_equation(1, 2, -3)