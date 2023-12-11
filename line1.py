import matplotlib.pyplot as plt
def find_slope_and_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def find_intersection_point(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2


    m1, b1 = find_slope_and_intercept(x1, y1, x2, y2)
    m2, b2 = find_slope_and_intercept(x3, y3, x4, y4)

    if m1==m2:  #lines are parallel
      return None

    x_intersect = (b2 - b1) / (m1 - m2)
    y_intersect = m1 * x_intersect + b1

    return x_intersect, y_intersect




def plot_lines_and_intersection(line1, line2, intersection_point):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    plt.plot([x1, x2], [y1, y2], label='Line 1')
    plt.plot([x3, x4], [y3, y4], label='Line 2')

    if intersection_point:
        plt.scatter(*intersection_point, color='red', label='Intersection Point')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()
