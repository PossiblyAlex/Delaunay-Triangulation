import tkinter as tk
import Functions as f

print("Program is running...")
root = tk.Tk()
canvas = tk.Canvas(root, width=1045, height=554, bg="white")
canvas.pack()

points = []
adjMatrix = []


# Checks if the edge will intersect any of the other edges
# starting from the index of start
# Does not check for intersection with the edge immediately
# before edge, as it should never intersect
#
# Edge should be a tuple containing two index values
def has_intersect(start, end, edge):
    if len(points) < 3:
        return False

    for i in range(start, end):
        for j in range(start, end):
            if adjMatrix[i][j] == 1:
                if f.intersect(points[edge[0]], points[edge[1]], points[i], points[j]):
                    return True
    return False


def reset_matrix():
    global adjMatrix;
    # Either  or
    if len(points) > len(adjMatrix):
        for col in adjMatrix:
            col.append(0)
        tempCol = [0] * len(points)
        adjMatrix.append(tempCol)
    elif len(points) < len(adjMatrix):
        length = len(points)
        for i in range(0, len(adjMatrix)):
            adjMatrix[i] = adjMatrix[i][:length]
        adjMatrix = adjMatrix[:length]


def add_point(point):
    global points
    points.append(point)

    reset_matrix()

    if len(points) > 1:
        adjMatrix[len(points)-2][len(points)-1] = 1

    if len(points) > 3 and has_intersect(0, len(points)-2, (-2, -1)):
        points = points[:-1]
        reset_matrix()


# Function will go through the matrix and
# check every edge except for the first
# and last edge for an intersection with
# an edge from the last point to the first
#
# If no intersection is found, it will make the matrix at [length-1][0] 1,
# completing the polygon
def complete_polygon():
    if len(points) < 3:
        return
    hasIntersection = has_intersect(1, len(points)-1, (len(points)-1, 0))
    if hasIntersection == False:
        adjMatrix[len(points)-1][0] = 1
        update()


def left_click(event):
    x = event.x
    y = event.y

    add_point((x,y))
    update()


def enter_press(event):
    global points
    global adjMatrix
    points = []
    adjMatrix = []
    update()


def key_pressed(event):
    if event.char == 'f':
        print("User pressed f")
        complete_polygon()


def update():
    for item in canvas.find_all():
        canvas.delete(item)

    r = 4
    for point in points:
        canvas.create_oval(point[0]-r, point[1]-r, point[0]+r, point[1]+r, fill="red")

    for i, col in enumerate(adjMatrix):
        for j, edge in enumerate(col):
            if edge == 1:
                canvas.create_line(points[i][0], points[i][1], points[j][0], points[j][1])
    canvas.pack()


canvas.bind("<Button-1>", left_click)
canvas.bind_all("<Return>", enter_press)
canvas.bind_all("<Key>", key_pressed)
#add_point((100,100))
#add_point((200,200))
#add_point((208,37))
#add_point((150,150))

root.mainloop()

