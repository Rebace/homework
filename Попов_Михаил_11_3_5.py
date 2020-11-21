def cor(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 'Корень любое число'
            else:
                return 'Корней нет'
        elif c == 0:
            return 0
            
    elif (b == 0) and (c == 0):
        return 0
        
    elif a == 0:
        return -c / b
        
    elif b == 0:
        x = (-c / a)**(1/2)
        return x, -1*x
        
    elif c == 0:
        return (-c / b), 0
        
    else:
        D = b**2 - 4*a*c
        if D < 0:
            return 'Корней нет'
        else: 
            x1 = (-b + D**(0.5)) / 2*a
            x2 = (-b - D**(0.5)) / 2*a
            return x1, x2

a, b, c = map(int, input('Введите коэффициенты квадратного уравнения: ').split())
print(cor(a,b,c))
input()