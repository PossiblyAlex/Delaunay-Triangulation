

# This function will return 2 times the signed area of a triangle
# defined by tuples a,b,c in the format of (int,int).
# If triangle abc defines a counter-clockwise circuit, it returns a positive number
# If triangle abc defines a clockwise circuit, it returns a negative number
def area(a, b, c):
    # IMPORTANT: tkinter has flipped y axis.
    # When flipped, clockwise ordered points will be counter clockwise and vice versa.
    # To compensate for this, I will make y values negative, which will factor out to
    # the negation of the whole area.
    two_area = a[0]*b[1] - a[1]*b[0] + a[1]*c[0] - a[0]*c[1] + b[0]*c[1] - b[1]*c[0]
    return two_area * -1


# This function will return a boolean value if the point c
# is to the left of the directional line a->b
def left(a, b, c):
    isLeft = area(a, b, c) > 0
    return isLeft


# This function will return a boolean value if point c
# is colinear with the line ab
def colinear(a, b, c):
    is_cl = area(a, b, c) == 0
    return is_cl


# returns true iff abc are colinear and point c
# lies on the closed segment ab
# so, c[0] must be somewhere between a[0] and b[0]; likewise with the y coordinate
def between(a, b, c):
    # if points are not coliniear, trivial case and we're done
    if not colinear(a, b, c):
        return False

    # if ab not vertical, check betweenness of x; else on y
    if a[0] != b[0]:
        return (a[0] <= c[0] <= b[0]) or (a[0] >= c[0] >= b[0])
    else:
        return (a[1] <= c[1] <= b[1]) or (a[1] >= c[1] >= b[1])
