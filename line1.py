import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
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


    m1, b1 = find_slope_and_intercept(int(x1), int(y1), int(x2), int(y2))
    m2, b2 = find_slope_and_intercept(int(x3), int(y3), int(x4), int(y4))

    if m1==m2:  #lines are parallel
      return None

    x_intersect = (b2 - b1) / (m1 - m2)
    y_intersect = m1 * x_intersect + b1

    return x_intersect, y_intersect




def plot_lines_and_intersection(line1x1, line1x2, line1y1, line1y2, line2x1, line2x2, line2y1, line2y2, intersection_point):
    x1=int(line1x1)
    x2=int(line1x2)
    y1=int(line1y1)
    y2=int(line1y2)
    x3=int(line2x1)
    x4=int(line2x2)
    y3=int(line2y1)
    y4=int(line2y2)
    fig,ax=plt.subplots(figsize=(10,10))
    ax=sns.set_style("darkgrid")
    sns.lineplot([x1, x2], [y1, y2], label='Line 1')
    sns.lineplot([x3, x4], [y3, y4], label='Line 2')

    if intersection_point:
        plt.scatter([intersection_point[0]], [intersection_point[1]], color='red', label='Intersection Point')
    
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    canvas=FigureCanvas(fig)
    img=io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return img
