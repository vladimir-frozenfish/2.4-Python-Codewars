"""
ask
Given two congruent circles a and b of radius r, return the area of their intersection rounded down to the nearest integer.

Code Limit
Javascript: Less than 94 characters.

Python: Less than 128 characters.

To remain consistent across version, your code should also not include the 'assignment operator' :=.

Example
For c1 = [0, 0], c2 = [7, 0] and r = 5,

the output should be 14.
"""
from math import*;circleIntersection=lambda a,b,r:r*r*(lambda h:h<1and acos(h)-h*(1-h*h)**.5)(hypot(b[0]-a[0],b[1]-a[1])/r/2)//.5 # не мое решение

import math as m; # circleIntersection=lambda a,b,r: 0 if (2*r-(((a[0]-b[0])**2+(a[1]-b[1])** 2)**0.5))/2<0 else int(2*(r*r*((2*m.acos(1-((2*r-(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5))/2)/r))-m.sin((2*m.acos(1-((2*r-(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5))/2)/r))))/2))
# circleIntersection=lambda a,b,r:0 if 4*r*r<(a[0]-b[0])**2+(a[1]-b[1])**2 else int(r*r*(2*m.acos(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5/2/r)-m.sin(2*m.acos(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5/2/r))))
# L=lambda a,b,r:2*m.acos(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5/2/r);circleIntersection=lambda a,b,r:0 if 4*r*r<(a[0]-b[0])**2+(a[1]-b[1])**2 else int(r*r*(L(a,b,r)-m.sin(L(a,b,r))))
# H=lambda a,b:(a[0]-b[0])**2+(a[1]-b[1])**2;L=lambda a,b,r:2*m.acos(H(a,b)**0.5/2/r);circleIntersection=lambda a,b,r:0if 4*r*r<H(a,b)else int(r*r*(L(a,b,r)-m.sin(L(a,b,r))))
# L=lambda a,b:(a[0]-b[0])**2+(a[1]-b[1])**2;A=lambda L,r:2*m.acos(L**0.5/2/r);circleIntersection=lambda a,b,r:0if 4*r*r<L(a,b)else int(r*r*(A(L(a,b),r)-m.sin(A(L(a,b),r))))
# L=lambda a,b,r:((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5/2/r;circleIntersection=lambda a,b,r:int(r*r*(2*m.acos(L(a,b,r))-m.sin(2*m.acos(L(a,b,r))))) if L(a,b,r)**2<=1 else 0


def circleIntersection_def(a,b,r):
    # сокращенный код
    # H = (2 * r - (((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)) / 2
    H = r - ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 / 2
    # return 0 if H < 0 else int(r * r * ((2 * m.acos(1 - H / r)) - m.sin((2 * m.acos(1 - H / r)))))
    return 0 if H < 0 else int(r * r * ((2 * m.acos(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 / 2 / r)) - m.sin((2 * m.acos(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 / 2 / r)))))


    """ # рассширенный код
    X = a[0] - b[0]             # горизотальный катет
    Y = a[1] - b[1]             # вертикальный катет
    R = (X*X + Y*Y) ** 0.5      # расстояние между центрами окружностей
    H = (2 * r - R) / 2         # высота сегмента
    if H < 0:
        return 0
    alpha = 2 * math.acos(1-H/r)    # угол, на хорду
    S = r*r * (alpha - math.sin(alpha)) / 2 # площадь сегмента
    return int(2 * S)
    """

    '''
    # приблизительный подсчет без угла
    X = a[0] - b[0]  # горизотальный катет
    Y = a[1] - b[1]  # вертикальный катет
    R = (X * X + Y * Y) ** 0.5  # расстояние между центрами окружностей
    if R > 2*r:
        return 0
    H = (2 * r - R) / 2  # высота сегмента
    H_rect = r - H         # высота треугольника сектора
    horda = 2 * ((r*r - H_rect*H_rect) ** 0.5) # хорда сегмента
    # S = 2/3*horda*H + H*H*H/(2*horda)
    L = (horda*horda + 16/3*H*H) ** 0.5 # длинна дуги сегмента
    S = L*r/2 - H_rect*horda/2
    print(2 * S)
    return int(2 * S)
    '''

print(circleIntersection([0, 0],[7, 0],5) == 14, end='\n\n')
print(circleIntersection([0, 0],[0, 10],10) == 122, end='\n\n')
print(circleIntersection([5, 6],[5, 6],3) == 28, end='\n\n')
print(circleIntersection([-5, 0],[5, 0],3) == 0, end='\n\n')
print(circleIntersection([10, 20],[-5, -15],20) == 15, end='\n\n')
print(circleIntersection([-7, 13],[-25, -5],17) == 132, end='\n\n')
print(circleIntersection([-20, -4],[-40, 29],7) == 0, end='\n\n')
print(circleIntersection([38, -18],[46, -29],10) == 64, end='\n\n')
print(circleIntersection([-29, 33],[-8, 13],15) == 5, end='\n\n')
print(circleIntersection([-12, 20],[43, -49],23) == 0, end='\n\n')
