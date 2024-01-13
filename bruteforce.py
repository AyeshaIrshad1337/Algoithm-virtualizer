import matplotlib.pyplot as plt
from functools import cmp_to_key

mid = [0, 0]

def quad(p):
    if p[0] >= 0 and p[1] >= 0:
        return 1
    if p[0] <= 0 and p[1] >= 0:
        return 2
    if p[0] <= 0 and p[1] <= 0:
        return 3
    return 4

def orientation(a, b, c):
    res = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if res == 0:
        return 0
    if res > 0:
        return 1
    return -1

def compare(p1, q1):
    p = [p1[0]-mid[0], p1[1]-mid[1]]
    q = [q1[0]-mid[0], q1[1]-mid[1]]
    one = quad(p)
    two = quad(q)

    if one != two:
        if one < two:
            return -1
        return 1
    if p[1]*q[0] < q[1]*p[0]:
        return -1
    return 1

def merger(a, b):
    n1, n2 = len(a), len(b)
    ia, ib = 0, 0

    for i in range(1, n1):
        if a[i][0] > a[ia][0]:
            ia = i

    for i in range(1, n2):
        if b[i][0] < b[ib][0]:
            ib = i

    inda, indb = ia, ib
    done = 0
    while not done:
        done = 1
        while orientation(b[indb], a[inda], a[(inda+1) % n1]) >= 0:
            inda = (inda + 1) % n1

        while orientation(a[inda], b[indb], b[(n2+indb-1) % n2]) <= 0:
            indb = (indb - 1) % n2
            done = 0

    uppera, upperb = inda, indb
    inda, indb = ia, ib
    done = 0
    g = 0
    while not done:
        done = 1
        while orientation(a[inda], b[indb], b[(indb+1) % n2]) >= 0:
            indb = (indb + 1) % n2

        while orientation(b[indb], a[inda], a[(n1+inda-1) % n1]) <= 0:
            inda = (inda - 1) % n1
            done = 0

    ret = []
    lowera, lowerb = inda, indb

    ind = uppera
    ret.append(a[uppera])
    while ind != lowera:
        ind = (ind+1) % n1
        ret.append(a[ind])
        plot_points_and_hull(a, ret)

    ind = lowerb
    ret.append(b[lowerb])
    while ind != upperb:
        ind = (ind+1) % n2
        ret.append(b[ind])
        plot_points_and_hull(a, ret)

    return ret

def divide(a, iteration):
    if len(a) <= 5:
        return bruteHull(a, iteration)

    left, right = [], []
    start = int(len(a) / 2)
    for i in range(start):
        left.append(a[i])
    for i in range(start, len(a)):
        right.append(a[i])

    left_hull = divide(left, iteration)
    right_hull = divide(right, iteration)

    return merger(left_hull, right_hull, iteration)

def bruteHull(a, iteration):
    global mid
    s = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x1, x2 = a[i][0], a[j][0]
            y1, y2 = a[i][1], a[j][1]
            a1, b1, c1 = y1-y2, x2-x1, x1*y2-y1*x2
            pos, neg = 0, 0
            for k in range(len(a)):
                if (k == i) or (k == j) or (a1*a[k][0]+b1*a[k][1]+c1 <= 0):
                    neg += 1
                if (k == i) or (k == j) or (a1*a[k][0]+b1*a[k][1]+c1 >= 0):
                    pos += 1
            if pos == len(a) or neg == len(a):
                s.add(tuple(a[i]))
                s.add(tuple(a[j]))

    ret = []
    for x in s:
        ret.append(list(x))

    mid = [0, 0]
    n = len(ret)
    for i in range(n):
        mid[0] += ret[i][0]
        mid[1] += ret[i][1]
        ret[i][0] *= n
        ret[i][1] *= n
    ret = sorted(ret, key=cmp_to_key(compare))
    for i in range(n):
        ret[i] = [ret[i][0]/n, ret[i][1]/n]
        plot_points_and_hull(a, ret, iteration)  # Add the 'iteration' argument

    return ret

def plot_points_and_hull(points, hull, iteration):
    plt.clf()
    points_x, points_y = zip(*points)
    hull_x, hull_y = zip(*hull)
    plt.scatter(points_x, points_y, color='blue', marker='o')
    plt.plot(hull_x + (hull_x[0],), hull_y + (hull_y[0],), color='red')

    # Save the plot as an image
    image_path = f'static/bruteforce_iteration_{iteration}.png'
    plt.savefig(image_path)

    # Return the path to the saved image
    return image_path



def InputandStart(a):
    a.sort()
    ans = divide(a,0)

    print('Convex Hull:')
    for x in ans:
        print(int(x[0]), int(x[1]))

    # Generate images for each iteration
    for i in range(len(ans)):
        print(f'Iteration {i}')
        plot_points_and_hull(a, ans[:i+1], i)

    plt.close()
