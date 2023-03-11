table = [[1.50, 15.132],
         [1.55, 17.422],
         [1.60, 20.393],
         [1.65, 23.994],
         [1.70, 28.160],
         [1.75, 32.812],
         [1.80, 37.857],
         [1.85, 43.189],
         [1.90, 48.689],
         [1.95, 54.225],
         [2.00, 59.653],
         [2.05, 64.817],
         [2.10, 69.550]]

x1 = 1.762
x2 = 1.779
x3 = 1.911
x4 = 1.649

h = table[1][0] - table[0][0]

length = len(table)
for _ in range(3):
    for i in range(length):
        if i != length - 1:
            table[i] = table[i] + [round(table[i + 1][-1] - table[i][-1], 6)]
    length -= 1

print('%-8s %-9s %-9s %-9s %-s' % ('x', 'y', 'd_y', 'd2_y', 'd3_y'))

for i in range(len(table)):
    for j in range(len(table[i])):
        if j == 0:
            print('%-8.2f' % table[i][j], end=" ")
        else:
            print('%-9.3f' % table[i][j], end=" ")
    print()

def get_x0(x):
    for i in range(len(table)):
        if i != len(table) - 1 and table[i][0] < x < table[i + 1][0]:
            return [table[i][0], i]
        if x < table[0][0]:
            return [table[0][0], 0]
        if x > table[-1][0]:
            return [table[-1][0], -1]

def solve_by_gauss(x, x0, y, d_y, d2_y, d3_y):
    t = (x - x0) / h
    return y + t * d_y + (t * (t-1) / 2) * d2_y + ((t+1) * t * (t-1) / 6) * d3_y

def solve_by_bessel(x, x0, y, y1, d_y, d2_y, d2_y1, d3_y):
    t = (x - x0) / h
    return ((y + y1) / 2) + (t-1/2) * d_y + (t * (t-1) / 2) * ((d2_y1 + d2_y) / 2) + ((t-1/2) * t * (t-1) / 6) * d3_y

def solve_by_stirling(x, x0, y, d_y1, d_y, d2_y, d3_y2, d3_y1):
    t = (x - x0) / h
    return y + t * ((d_y1 + d_y) / 2) + (t ** 2 / 2) * d2_y + (t * (t ** 2 - 1) / 6) * ((d3_y2 + d3_y1) / 2)

def solve_by_gauss2(x, x0, y, d_y, d2_y, d3_y):
    t = (x - x0) / h
    return y + t * d_y + ((t+1) * t / 2) * d2_y + ((t+1) * t * (t-1) / 6) * d3_y

y = [0 for i in range(4)]

x0, i = get_x0(x1)
y[0] = solve_by_gauss(x1, x0, table[i][1], table[i][2], table[i-1][3], table[i-1][4])

x0, i = get_x0(x2)
y[1] = solve_by_bessel(x2, x0, table[i][1], table[i+1][1], table[i][2], table[i][3], table[i-1][3], table[i-1][4])

x0, i = get_x0(x3)
y[2] = solve_by_stirling(x3, x0, table[i][1], table[i-1][2], table[i][2], table[i-1][3], table[i-2][4], table[i-1][4])

x0, i = get_x0(x4)
y[3] = solve_by_gauss2(x4, x0, table[i][1], table[i-1][2], table[i-1][3], table[i-2][4])

x = [x1, x2, x3, x4]

print('\n%-8s %-s' % ('x', 'y(x)'))
for i in range(4):
    print('%-8.3f %-.3f' % (x[i], y[i]))

