import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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

def vectors_on_opposite_sides(p1x,p1y, p2x,p2y, q1x,q1y, q2x,q2y):
    v1 = Point(q1x - p1x, q1y - p1y)
    v2 = Point(q2x - p1x, q2y - p1y)
    v3 = Point(p1x - q1x, p1y - q1y)
    v4 = Point(p2x - q1x, p2y - q1y)

    cross_product1 = vector_cross_product(v1, v2)
    cross_product2 = vector_cross_product(v3, v4)

    return (cross_product1 < 0 and cross_product2 > 0) or (cross_product1 > 0 and cross_product2 < 0)

def do_intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
    
    p1x = line1Point1X
    p1y = line1Point1Y
    p2x = line2Point1X
    p2y = line2Point1Y
    q1x = line1Point2X
    q1y = line1Point2Y
    q2x = line2Point2X
    q2y = line2Point2Y
    return vectors_on_opposite_sides(p1x,p1y, q1x,q1y ,p2x,p2y, q2x,q2y) and vectors_on_opposite_sides(p2x,p2y, q2x,q2y, p1x,p1y, q1x,q1y)


def Vectorisation(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
    line1Point1X =int(line1Point1X)
    line1Point1Y=int(line1Point1Y)
    line1Point2X=int(line1Point2X)
    line1Point2Y=int(line1Point2Y)
    line2Point1X=int(line2Point1X)
    line2Point1Y=int(line2Point1Y)
    line2Point2X=int(line2Point2X)
    line2Point2Y=int(line2Point2Y)

    if do_intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
      print("Lines intersect.")
    else:
      print("Lines do not intersect.")
    fig,ax=plt.subplots(figsize=(10,10))
    

    plt.plot([line1Point1X, line1Point2X], [line1Point1Y, line1Point2Y], label='Line 1')
    plt.plot([line2Point1X, line2Point2X], [line2Point1Y, line2Point2Y], label='Line 2')

    if do_intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
        plt.scatter([line1Point1X, line1Point2X, line2Point1X, line2Point2X], [line1Point1Y, line1Point2Y, line2Point1Y, line2Point2Y], color='red', label='Intersection Points')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    canvas=FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return img