import tkinter as tk


print("Program is running...")
root = tk.Tk()
canvas = tk.Canvas(root, width=1045, height=554, bg="white")
canvas.pack()

points = []
adjMatrix = []

def add_point(point):
    points.append(point)

    for col in adjMatrix:
        col.append(0)

    tempCol = [0] * len(points)
    adjMatrix.append(tempCol)

    for x in adjMatrix:
        print(x)


def left_click(event):
    print("Left")
    print(event.x)
    print(event.y)
    x = event.x
    y = event.y
    r = 4
    add_point((x,y))
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
    canvas.pack()
    print(len(points))
    if len(points) > 2:
        print("todo")
    """print(points)"""


canvas.bind("<Button-1>", left_click)

root.mainloop()

