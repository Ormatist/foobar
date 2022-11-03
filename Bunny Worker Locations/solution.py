def solution(x, y):
    test =  (0.5 * (x**2)) + (0.5 * x)
    a = 0.5
    b = ((test + x) - (test)) - 1.5
    c = test - a - b
    value = (a * (y**2)) + (b*y) + c
    return str(int(value))