import cadquery as cq

red_beam = cq.Workplane().box(10, 20, 60)
blue_beam = cq.Workplane().box(30, 20, 10)

a = cq.Assembly()
a.add(red_beam, name='red_beam', color=cq.Color('red'))
a.add(blue_beam, name='blue_beam', color=cq.Color('blue'))
a.constrain('red_beam@faces@>X', 'blue_beam@faces@<X', 'Plane')
a.solve()

show_object(a)
