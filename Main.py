import tkinter as tk

print("Program is running...")
root = tk.Tk()
canvas = tk.Canvas(root, width=1045, height=554, bg="white")
canvas.pack()

points = []


def leftClick(event):
    print("Left")
    print(event.x)
    print(event.y)
    points.append((event.x, event.y))
    x=event.x
    y=event.y
    r=4
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
    canvas.pack()


canvas.bind("<Button-1>", leftClick)

root.mainloop()

