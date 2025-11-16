import math

def discriminant(a, b, c):
    return b*b - 4*a*c

def solve_quadratic(a, b, c):
    delta = discriminant(a, b, c)

    if a == 0:
        raise ValueError("Coefficient 'a' ne peut pas être 0 pour une équation du second degré.")

    if delta < 0:
        # solutions complexes
        real = -b / (2*a)
        imag = math.sqrt(-delta) / (2*a)
        return (complex(real, -imag), complex(real, imag))

    elif delta == 0:
        x = -b / (2*a)
        return (x,)

    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return (x1, x2)
