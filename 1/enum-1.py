from enum import Enum
class Color(Enum): #Even though we use the class syntax to create Enums, Enums are not normal Python classes
    RED = 1
    GREEN = 2
    BLUE = 3

#Color.RED.name = 'ORANGE'  # This action will raise exeption
myenum = Color # Make a copy of Color enum object
print(myenum.RED.value)