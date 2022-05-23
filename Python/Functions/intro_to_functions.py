#the variable being passed to the function is a parameter
def kitchen_items(location):
  print("Looks like you need to look in the " + location )
  print("You can use the knife in the " + location )
#the string being passed to the function is an argument

#Types of Function Arguments
#final_destination variable is a Default Argument which given default values
# def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  # print("Here is what your trip will look like!")
  # print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
#Positional Arguments can be called by their position in the function definition.
# trip_planner("France", "Germany", "Denmark")
# trip_planner("Denmark", "France", "Germany")
# trip_planner("Iceland", "Germany", "India")
#Keyword Argument can be called by their name.
# trip_planner(first_destination="Iceland", second_destination="India", final_destination="Germany")


#Return Keyword
current_car_price = 35000
#budget is assigned the variable above value, while the function below calls it
def leftover_budget(budget):
  print("Your remaining budget is: $" + str(budget))
#this function returns the calculation of the subtracting the budget from expense
def debuct_tires(budget, expense):
  return budget - expense
#this variable defines the expense value in the function above and below
tire_expense = 2000
#this variable stores the function containing parameters which become arguments from the variable above
new_budget_after_tires = debuct_tires(current_car_price, tire_expense)
#This function calls the variable which is storing another function by passing it as a parameter
# leftover_budget(new_budget_after_tires)

#Returning Multiple Return Statements
#This function is defining the return statement to the variables
def top_cars():
  first = "Toyota"
  second = "Chevy"
  third = "Ford"
  return first, second, third
#The variables are being renamed so they can be called by the function
most_car1, most_car2, most_car3 = top_cars()

#A simple function that passes the assigned name variable as the function is called
def trip_planner_welcome(name): 
  print("Welcome to trip planner v1.0 " + name)
trip_planner_welcome("Davon")
#A function that is passed a variable that needed to be returned
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(.10)
#A function that passes 4 parameters that are called with the calling of the function
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
destination_setup("Chicago", "Florida", estimate, "Train")