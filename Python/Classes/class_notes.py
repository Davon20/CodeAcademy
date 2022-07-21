#Writing a Class
class Facade:
    #pass serves as a placeholder in Python so no error is thrown before the class receives any functionality
  pass
#creates an object from the class. objects are variables that store classes
facade_1 = Facade()
#this variable is storing the type of class
facade_1_type = type(facade_1)
print(facade_1_type)

class Millionaire:
    #a variable in the class
  minimum_required = 1000000
#A class variable is a variable that’s the same for every instance of the class
money = Millionaire
print(money.minimum_required)

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#Methods using Arguments
class Circle:
  #class variable
  pi = 3.14
  #class method containing formula
  def area(self, radius):
    return Circle.pi * radius ** 2
#instantiates class into object
circle = Circle()
#calls the object into the variables
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

#Constructors
class Circle:
  pi = 3.14
  #constructor which takes diameter as an argument
  def __init__(self, diameter):
      #the argument in the constructor can't be passed a value without .format() because it's undefined without it.
    print("New circle with diameter: {diameter}".format(diameter=diameter))
teaching_table = Circle(36)

#Instance Variables
class Store:
  pass
#instatiating the class into an object
alternative_rocks = Store()
isabelles_ices = Store()
#following the . is called a instance attribute
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#Attributes
#this variable contains a dictionary, a string, an integer, and a list
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
#the for loops goes through each element of the variable to assesss which has the characteristic of being countable and which don't
for element in can_we_count_it:
    #hasattr is the python method that examines the elements of the variable
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!") 
  else: print(str(type(element)) + " does not have the count attribute :(")
  
#Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = 1/2 * diameter
  def circumference(self):
    return 2 * self.pi * self.radius
#Defining 3 different objects which have diameters
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
#the constructor needs to be passed through the object containing the diameter
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#Object Example
#everyhting is an object that can assessed using dir()
print(dir(5))
def this_function_is_an_object(num):
  return "{} is my favorite number".format(num)
#this method as an object is being assessed and displayed 
print(dir(this_function_is_an_object))


#String Representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
#this method referencing the string name of the object, unlike __init__ which provides default representation
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

#Objects Review
class Student:
    #this is the constructor of the class. self is always a parameter of constructors
  def __init__(self, name, year):
    self.name = name
    self.year = year
    #an emty list
    self.grades = []
    #method for adding grades
  def add_grade(self, grade):
      #checks if the grades added are of type Grade
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_average():
    pass
#variable instances of the class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  
  def is_passing(self, passing):
    if self.score > Grade.minimum_passing:
      return "Passing"

pieter.add_grade(Grade(100))
#Challenge: Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values.
#that indicate whether the student attended school that day.