import matplotlib.pyplot as plt
def find_slope_and_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def find_intersection_point(line1x1, line1x2, line1y1, line1y2, line2x1, line2x2, line2y1, line2y2):
    x1=line1x1
    x2=line1x2
    y1=line1y1
    y2=line1y2
    x3=line2x1
    x4=line2x2
    y3=line2y1
    y4=line2y2


    m1, b1 = find_slope_and_intercept(x1, y1, x2, y2)
    m2, b2 = find_slope_and_intercept(x3, y3, x4, y4)

    if m1==m2:  #lines are parallel
      return None

    x_intersect = (b2 - b1) / (m1 - m2)
    y_intersect = m1 * x_intersect + b1

    return x_intersect, y_intersect




def plot_lines_and_intersection(line1x1, line1x2, line1y1, line1y2, line2x1, line2x2, line2y1, line2y2, intersection_point):
    x1=line1x1
    x2=line1x2
    y1=line1y1
    y2=line1y2
    x3=line2x1
    x4=line2x2
    y3=line2y1
    y4=line2y2
    plt.plot([x1, x2], [y1, y2], label='Line 1')
    plt.plot([x3, x4], [y3, y4], label='Line 2')

    if intersection_point:
        plt.scatter(*intersection_point, color='red', label='Intersection Point')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()
