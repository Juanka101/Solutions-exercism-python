def is_a_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

def equilateral(sides):
    a, b, c = sides
    if is_a_triangle(sides):
        return a == b == c
    return False

def isosceles(sides):
    a, b, c = sides
    if is_a_triangle(sides):
        return a == b or b == c or a == c
    return False

def scalene(sides):
    a, b, c = sides
    if is_a_triangle(sides):
        return a != b and b != c and a != c
    return False
