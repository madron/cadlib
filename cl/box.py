import cadquery as cq


def box(x, y, z):
    return cq.Workplane("XY").box(x, y, z)
