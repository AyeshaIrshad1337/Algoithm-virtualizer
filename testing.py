import bruteforce
if __name__ == '__main__':
    a = [
        [0, 0],
        [1, -4],
        [-1, -5],
        [-5, -3],
        [-3, -1],
        [-1, -3],
        [-2, -2],
        [-1, -1],
        [-2, -1],
        [-1, 1]
    ]

    a.sort()
    ans = bruteforce.divide(a)

    print('Convex Hull:')
    for x in ans:
        print(int(x[0]), int(x[1]))

    bruteforce.plt.show()
