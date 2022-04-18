from cl.box import box

b1 = box(80, 20, 20)
b2 = box(20, 80, 20)

obj = b1 + b2
obj = obj.edges("Z").fillet(2)


# Show
if 'show_object' not in globals():
    def show_object(*args, **kwargs):
        pass
if 'show' not in globals():
    def show(*args, **kwargs):
        pass
show_object(obj)
show(obj)
