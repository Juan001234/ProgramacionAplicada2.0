class Facade:
    pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


class Grade:
    minimum_passing = 65


class Rules:
    def washing_brushes(self):
        return "point bristles towards the basin while washing your brushes"


class Circle:
    pi = 3.14
    def area(self, radius):
        return Circle.pi * radius ** 2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)    
#print(round_room_area)
#print(pizza_area)
#print(teaching_table_area)

class Circle:
    pi = 3.14

# Add constructor here:
    def __init__(self, diameter):

       print('New circle with diameter: {}'.format(diameter))
teaching_table = Circle(36)

class Store:
    pass


alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ice"
print(isabelles_ices.store_name)

