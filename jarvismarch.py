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

def jarvis_march(points):
    on_hull = min(points)
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = orientation(on_hull, next_point, point)
            if next_point == on_hull or o == 1:
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break
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


def InputandStart():
     num_points = int(input("Enter the number of points: "))
     a = []

     for i in range(num_points):
         x = float(input(f"Enter x-coordinate for point {i + 1}: "))
         y = float(input(f"Enter y-coordinate for point {i + 1}: "))
         a.append((x, y))
     convex_hull = jarvis_march(a)

# Plot points before and after convex hull
     plot_points(a)
     plot_points(a, convex_hull)

