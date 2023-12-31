#IDEA 2
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

def counterclockwise(ax,ay, bx,by, cx,cy):
    area = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if area < 0:
        return -1
    elif area == 0:
        return 0
    else:
        return 1

def intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
    test1 = counterclockwise(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point2X,line2Point2Y) * counterclockwise(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y)
    test2 = counterclockwise(line2Point1X,line2Point1Y,line2Point2X,line2Point2Y,line1Point1X,line1Point1Y) * counterclockwise(line2Point1X,line2Point1Y,line2Point2X,line2Point2Y,line1Point2X,line1Point2Y)
    return (test1 <= 0) and (test2 <= 0)



def IntersectbyOrient(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
    line1Point1X =int(line1Point1X)
    line1Point1Y=int(line1Point1Y)
    line1Point2X=int(line1Point2X)
    line1Point2Y=int(line1Point2Y)
    line2Point1X=int(line2Point1X)
    line2Point1Y=int(line2Point1Y)
    line2Point2X=int(line2Point2X)
    line2Point2Y=int(line2Point2Y)
    if intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
      print("Lines intersect.")
    else:
      print("Lines do not intersect.")

    fig,ax=plt.subplots(figsize=(10,10))
    plt.plot([line1Point1X,line1Point2X], [line1Point1Y,line1Point2Y], label='Line 1')
    plt.plot([line2Point1X,line2Point2X], [line2Point1Y,line2Point2Y], label='Line 2')

    if intersect(line1Point1X,line1Point1Y,line1Point2X,line1Point2Y,line2Point1X,line2Point1Y,line2Point2X,line2Point2Y):
        plt.scatter([line1Point1X,line1Point2X, line2Point1X,line2Point2X], [line1Point1Y,line1Point2Y, line2Point1Y,line2Point2Y], color='red', label='Intersection Points')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    canvas=FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return img