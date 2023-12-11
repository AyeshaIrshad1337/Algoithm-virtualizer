import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

def vector_cross_product(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def vectors_on_opposite_sides(p1, p2, q1, q2):
    v1 = Point(q1.x - p1.x, q1.y - p1.y)
    v2 = Point(q2.x - p1.x, q2.y - p1.y)
    v3 = Point(p1.x - q1.x, p1.y - q1.y)
    v4 = Point(p2.x - q1.x, p2.y - q1.y)

    cross_product1 = vector_cross_product(v1, v2)
    cross_product2 = vector_cross_product(v3, v4)

    return (cross_product1 < 0 and cross_product2 > 0) or (cross_product1 > 0 and cross_product2 < 0)

def do_intersect(line1, line2):
    p1, q1 = line1.point1, line1.point2
    p2, q2 = line2.point1, line2.point2

    return vectors_on_opposite_sides(p1, q1, p2, q2) and vectors_on_opposite_sides(p2, q2, p1, q1)


def Vectorisation(line1,line2):
    if do_intersect(line1, line2):
      print("Lines intersect.")
    else:
      print("Lines do not intersect.")


    plt.plot([line1.point1.x, line1.point2.x], [line1.point1.y, line1.point2.y], label='Line 1')
    plt.plot([line2.point1.x, line2.point2.x], [line2.point1.y, line2.point2.y], label='Line 2')

    if do_intersect(line1, line2):
        plt.scatter([line1.point1.x, line1.point2.x, line2.point1.x, line2.point2.x], [line1.point1.y, line1.point2.y, line2.point1.y,line2.point2.y], color='red', label='Intersection Points')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()