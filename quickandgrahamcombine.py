import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO

def findSide(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def lineDist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0]))
    
def quickHull(points, p1, p2, side):
    hull = []
    max_dist = 0
    farthest_point = None

    for point in points:
        temp = findSide(p1, p2, point)
        if temp == side:
            dist = lineDist(p1, p2, point)
            if dist > max_dist:
                max_dist = dist
                farthest_point = point

    if farthest_point is not None:
        hull.extend(quickHull(points, p1, farthest_point, -findSide(p1, farthest_point, p2)))
        hull.append(farthest_point)
        hull.extend(quickHull(points, farthest_point, p2, -findSide(farthest_point, p2, p1)))

    return hull

def grahamScan(points):
    points.sort(key=lambda p: (p[0], p[1]))
    hull = []

    for point in points:
        while len(hull) >= 2 and findSide(hull[-2], hull[-1], point) != 1:
            hull.pop()
        hull.append(point)

    return hull

def proposedConvexHull(points):
    points.sort(key=lambda p: (p[0], p[1]))

    # Step 1: QuickHull
    hull_quickhull = quickHull(points, points[0], points[-1], 1)

    # Step 2: Discard points inside the convex hull
    remaining_points = [point for point in points if point not in hull_quickhull]

    # Step 3: Sort remaining points and apply Graham Scan
    hull_grahamscan = grahamScan(remaining_points)

    return hull_quickhull + hull_grahamscan

def plot_points(points, hull=None):
    fig, ax = plt.subplots()
    x, y = zip(*points)
    ax.scatter(x, y, color='blue', label='Points')

    if hull:
        hull.append(hull[0])  # Close the convex hull
        hx, hy = zip(*hull)
        ax.plot(hx, hy, color='red', linestyle='-', linewidth=2, label='Convex Hull')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Proposed Convex Hull Visualization')
    ax.legend()

    # Save the figure to a BytesIO buffer instead of displaying
    buffer = BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)
    plt.close(fig)
    return buffer.getvalue()


  
