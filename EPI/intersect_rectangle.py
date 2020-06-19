"""Test if two rectangles have a nonempty intersection, if True return the
rectangle formed by their intersection.
"""
from collections import namedtuple
Rectangle = namedtuple("Rectangle", ("x", "y", "width", "height"))


# If the set of X-values for the rectangles intersect and the set of Y-values
# of the rectangles intersect, then all points with those X- and Y-values are
# common to the two rectangles, so there is a nonempty intersection.
def intersect_rectangle(r1, r2):
    def is_intersect(r1, r2):
        return (r1.x <= r2.x + r2.width and r1.x + r1.width >= r2.x
                and r1.y <= r2.y + r2.height and r1.y + r1.height >= r2.y)
    if not is_intersect(r1, r2):
        return Rectangle(0, 0, -1, -1)
    return Rectangle(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))


if __name__ == "__main__":
    r1 = None
    r2 = None
    print(intersect_rectangle(r1, r2))
