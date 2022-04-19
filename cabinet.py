from cl.cabinet import Cabinet


cabinet = Cabinet()

obj = cabinet.get_obj()


# Show
if 'show_object' not in globals():
    def show_object(*args, **kwargs):
        pass
if 'show' not in globals():
    def show(*args, **kwargs):
        pass
show_object(obj)
show(obj)
