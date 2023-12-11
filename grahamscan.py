import math
import matplotlib.pyplot as plt
def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    d = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0
    
def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def polar_angle(p1, p2):
    if p1[1] == p2[1]:
        return -math.pi
    dy = p1[1]-p2[1]
    dx = p1[0]-p2[0]
    return math.atan2(dy, dx)

def graham(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))
    hull = []
    for i in range(len(points)):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 1:
            hull.pop()
        hull.append(points[i])
    return hull

def plot_points(points, hull=None):
    x, y = zip(*points)
    plt.scatter(x, y, color='blue', label='Points')

    if hull:
        hull.append(hull[0])  # Connect the last point to the first to close the hull
        hx, hy = zip(*hull)
        plt.plot(hx, hy, color='red', linestyle='-', linewidth=2, label='Convex Hull')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Convex Hull Visualization')
    plt.legend()
    plt.show()

# Example usage:


def InputandStart():
     num_points = int(input("Enter the number of points: "))
     a = []

     for i in range(num_points):
         x = float(input(f"Enter x-coordinate for point {i + 1}: "))
         y = float(input(f"Enter y-coordinate for point {i + 1}: "))
         a.append((x, y))
     convex_hull = graham(a)

# Plot points before and after convex hull
     plot_points(a)
     plot_points(a, convex_hull)

