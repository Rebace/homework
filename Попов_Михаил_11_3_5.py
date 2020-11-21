def calc_linear_equation(b,c):
    return -c / b

def calc_quadration_equation(a,b,c):
    D = b**2 - 4*a*c
    if D < 0:
        return 'no roots'
    else: 
        x1 = (-b + D**(0.5)) / 2*a
        x2 = (-b - D**(0.5)) / 2*a
        return x1, x2
            
def calc_incompletequadration_equation(a,c):
    if ((c < 0) and (a > 0)) or ((c > 0) and (a < 0)):
        return (-c / a)**(1/2), -1*(-c / a)**(1/2)
    elif c == 0:
        return 0.0, 0.0
    else:
        return 'no roots'

a, b, c = map(int, input('Введите коэффициенты уравнения: ').split())
if a == 0:
        if b == 0:
            if c == 0:
                print('the root of any number')
            else:
                print('no roots')
        elif c == 0:
            print(0.0)
        else:
            print(calc_linear_equation(b,c))
    
elif b == 0:
    print(calc_incompletequadration_equation(a,c))
    
elif c == 0:
    print(calc_linear_equation(a,b), 0.0)

else:
    print(calc_quadration_equation(a,b,c))

input()