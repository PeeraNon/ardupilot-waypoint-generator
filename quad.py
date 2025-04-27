import matplotlib.pyplot as plt


def get_line_points(points, buffer_dist):
    line_points = []

    for i in range(len(points)):
        A = points[i]
        B = points[(i+1)%4]

        # vector AB
        dx = B[0] - A[0]
        dy = B[1] - A[1]

        # normal vector
        normal_vector = (-dy, dx)
        length = (normal_vector[0]**2 + normal_vector[1]**2)**0.5

        # buffer vector
        buffer_vector = (normal_vector[0]/length*buffer_dist, normal_vector[1]/length*buffer_dist)
        A_buffer = (A[0] + buffer_vector[0], A[1] + buffer_vector[1])
        B_buffer = (B[0] + buffer_vector[0], B[1] + buffer_vector[1])

        line_points.append(A_buffer)
        line_points.append(B_buffer)

    # print(line_points)
    return line_points


def get_straight_line(x1, y1, x2, y2):    
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b


def get_intersect(m1, b1, m2, b2):
    x = (b2 - b1)/(m1 - m2)
    y = m1 * x + b1
    return (x, y)


def get_inner_points(line_points):
    inner_points = []

    for i in range(0, len(line_points), 2):
        x1, y1 = line_points[i]
        x2, y2 = line_points[(i+1)%8]
        x3, y3 = line_points[(i+2)%8]
        x4, y4 = line_points[(i+3)%8]

        m1, b1 = get_straight_line(x1, y1, x2, y2)
        m2, b2 = get_straight_line(x3, y3, x4, y4)

        intersect = get_intersect(m1, b1, m2, b2)
        inner_points.append(intersect)

    return(inner_points)


points = [(0, 0), (100, 0), (90, 50), (-20, 30)]
buffer_dist = 5 
line_points = get_line_points(points, buffer_dist)
inner_points = get_inner_points(line_points)
print(inner_points)

# visualize points
x, y = zip(*points)
inner_x, inner_y = zip(*inner_points)
plt.plot(x + (x[0],), y + (y[0],), marker='o', label='Original Points', color='blue')
plt.plot(inner_x + (inner_x[0],), inner_y + (inner_y[0],), marker='s', label='Inner Points', color='red')
plt.title("Quadrilateral")
plt.grid(True)
plt.show()