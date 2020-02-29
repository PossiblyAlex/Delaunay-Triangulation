

# This function will return 2 times the signed area of a triangle
# defined by tuples a,b,c in the format of (int,int).
# If triangle abc defines a counter-clockwise circuit, it returns a positive number
# If triangle abc defines a clockwise circuit, it returns a negative number
def area(a, b, c):
    # IMPORTANT: tkinter has flipped y axis.
    # When flipped, clockwise ordered points will be counter clockwise and vice versa.
    # To compensate for this, I will make y values negative, which will factor out to
    # the negation of the whole area
    two_area = a[0]*b[1] - a[1]*b[0] + a[1]*c[0] - a[0]*c[1] + b[0]*c[1] - b[1]*c[0]
    return two_area * -1
