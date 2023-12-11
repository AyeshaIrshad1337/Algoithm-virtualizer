#IDEA 2
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

def counterclockwise(a, b, c):
    area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    if area < 0:
        return -1
    elif area == 0:
        return 0
    else:
        return 1

def intersect(l1, l2):
    test1 = counterclockwise(l1.point1, l1.point2, l2.point1) * counterclockwise(l1.point1, l1.point2, l2.point2)
    test2 = counterclockwise(l2.point1, l2.point2, l1.point1) * counterclockwise(l2.point1, l2.point2, l1.point2)
    return (test1 <= 0) and (test2 <= 0)



def IntersectbyOrient(line1,line2):
    if intersect(line1, line2):
      print("Lines intersect.")
    else:
      print("Lines do not intersect.")


    plt.plot([line1.point1.x, line1.point2.x], [line1.point1.y, line1.point2.y], label='Line 1')
    plt.plot([line2.point1.x, line2.point2.x], [line2.point1.y, line2.point2.y], label='Line 2')

    if intersect(line1, line2):
        plt.scatter([line1.point1.x, line1.point2.x, line2.point1.x, line2.point2.x], [line1.point1.y, line1.point2.y, line2.point1.y,line2.point2.y], color='red', label='Intersection Points')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()
'''
x1 = float(input("Enter x coordinate for point 1 of line 1: "))
y1 = float(input("Enter y coordinate for point 1 of line 1: "))
x2 = float(input("Enter x coordinate for point 2 of line 1: "))
y2 = float(input("Enter y coordinate for point 2 of line 1: "))

# Input points for line 2
x3 = float(input("Enter x coordinate for point 1 of line 2: "))
y3 = float(input("Enter y coordinate for point 1 of line 2: "))
x4 = float(input("Enter x coordinate for point 2 of line 2: "))
y4 = float(input("Enter y coordinate for point 2 of line 2: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)
point3 = Point(x3, y3)
point4 = Point(x4, y4)

line1 = Line(point1, point2)
line2 = Line(point3, point4)
IntersectbyOrient(line1,line2)
'''