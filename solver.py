import numpy as np


def solve_complete_square(a, b, c, sign):
    sgn_a = -1 if a < 0 else 1
    a *= sgn_a
    b *= sgn_a
    c *= sgn_a
    sign *= sgn_a
    D = b**2 - 4*a*c
    if D <= 0:
        return '∅' if sign == -1 else '(-∞; +∞)'
    x1 = (-b - np.sqrt(D)) / (2 * a)
    x2 = (-b + np.sqrt(D)) / (2 * a)
    if sign == -1:
        return f'({x1}; {x2})'
    return f'(-∞; {x1}) U ({x2}; +∞)'
    

