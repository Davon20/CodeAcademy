import math 
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
# def trip_planner_welcome(name): 
#   print("Welcome to trip planner v1.0 " + name)
# trip_planner_welcome("Davon")
# #A function that is passed a variable that needed to be returned
# def estimated_time_rounded(estimated_time):
#   rounded_time = round(estimated_time)
#   return rounded_time
# estimate = estimated_time_rounded(.10)
#A function that passes 4 parameters that are called with the calling of the function
# def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
#   print("Your trip starts off in " + origin)
#   print("And you are traveling to " + destination)
#   print("You will be traveling by " + mode_of_transport)
#   print("It will take approximately " + str(estimated_time) + " hours")
# destination_setup("Chicago", "Florida", estimate, "Train")

def optionalExercises():
  #I've added this function as I forgot to use () for if
  def divisible_by_ten(num):
    if (num % 10 == 0): return True
    else: return False
  print(divisible_by_ten(20))
  print(divisible_by_ten(25))
  #In Python, && is and
  def in_range(num, lower, upper):
    if (num >= lower and num <= upper): return True
    else: return False
  print(in_range(10, 10, 10))
  print(in_range(5, 10, 20))
  #Uses multiple conditions
  def movie_review(rating):
    if(rating <= 5):
      return "Avoid at all costs!"
    if(rating < 9):
      return "This one was fun."
    return "Outstanding!"
  print(movie_review(9))
  print(movie_review(4))
  print(movie_review(6))
  #Appends list length to the end of the list
  def append_size(lst):
    lst.append(len(lst))
    return lst
  print(append_size([23, 42, 108]))
  #Lists function using conditional statements
  def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
      return lst1[-1]
    else:
      return lst2[-1]
  print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
  #Uses the count function to determine if n appears the most
  def more_than_n(lst, item, n):
    if lst.count(item) > n:
      return True
    return False
  print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
  #This function combines seperate lists then sorts them
  def combine_sort(lst1, lst2):
    #variable to be passed to sorted()
    unsorted = lst1 + lst2
    #sorted() requires a variable to be passed to it to sort
    sortedList = sorted(unsorted)
    return sortedList
  print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
  
def optionalListChallenges():
  #Build an iterator of every 3 num
  def every_three_nums_long(start):
    if start < 100:
      print(list(range(start, 100, 3)))
    if start > 100: 
      print("")
  def every_three_num_short(start):
    return list(range(start, 101, 3))
  
  #Double Index without Changing Original List
  #By far the most difficult challenge
  def double_index(lst, index):
    # Checks to see if index is too big
    if index >= len(lst):
      return lst
    else:
      # Gets the original list up to index
      new_lst = lst[0:index]
    # Adds double the value at index to the new list 
    new_lst.append(lst[index]*2)
    #  Adds the rest of the original list
    new_lst = new_lst + lst[index+1:]
    return new_lst
  # print(double_index([3, 8, -10, 12], 2))
  
  #Find the avg of middle integers
  def middle_element(lst):
    if len(lst) % 2 == 0:
      sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
      return sum / 2
    else:
      return lst[int(len(lst)/2)]
  # print(middle_element([5, 2, -10, -4, 4, 5]))
  
def loopingChallenges():
  #Print the total number of numbers that are divisible by 10
  def divisible_by_ten(nums):
    count = 0
    for num in nums:
      if(num % 10 == 0):
        count += 1
    return count
  # print(divisible_by_ten([20, 25, 30, 35, 40]))
  
  #Append through a list of names
  def add_greetings(names):
  #empty list containing a greeting per name
    greeters = []
    for name in names:
      greeters.append("Hello, " + name)
    return greeters
  # print(add_greetings(["Owen", "Max", "Sophie"]))
      
  #Deletes any number that is even at the start of the list
  def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
      lst = lst[1:]
    return lst
  # print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
  # print(delete_starting_evens([4, 8, 10, 12, 15]))
  
  #Adds odd numbers to a new list
  #I am proud having solved this challenge through research
  def odd_indices(lst):
    new_list = []
    for i in range(1, len(lst), 2):
      new_list.append(lst[i])
    return new_list
  # print(odd_indices([4, 3, 7, 10, 11, -2]))
  #Return a new list that raises every num in bases to every num in powers
  def exponents(bases, powers):
    newlist = []
    for num in bases:
      for nums in powers:
        newlist.append(math.pow(num, nums))
    return newlist
  # print(exponents([2, 3, 4], [1, 2, 3]))
  
  def over_nine_thousand(lst):
    sum = 0 
    for element in lst:
      sum += element
      if sum > 9000:
        break
    return "IT'S OVER 9000!!!!"
  # print(over_nine_thousand([8000, 900, 120, 5000]))
  
  #Max Number Function
  def max_num(nums):
    max = 0
    for i in nums:
      if i > max:
        max = i
    return max
  # print(max_num([50, -10, 0, 75, 20]))
  
  #Compare and Print shared Values
  def same_values(lst1, lst2):
    newlst = []
    #It was struggle to understand that I needed range since I wasn't considering that index would be needed for the if statement
    for index in range(len(lst1)):
    #Index is used to loop through every number rather than a specific number called by it's location in the list
      if lst1[index] == lst2[index]:
        newlst.append(index)
    return newlst
  # print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
  
  #Working w/Reversed List
  def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
      if lst1[index] != lst2[len(lst2) - 1 - index]:
        return False
    else: return True
  print(reversed_list([1, 2, 3], [3, 2, 1]))
  print(reversed_list([1, 5, 3], [3, 2, 1]))
  
#Functions Challenges
def functionsChallenge():
  def tenth_power(num):
    return num ** 10
  # print(tenth_power(0))
  # print(tenth_power(1))
  # print(tenth_power(2))
  
  #Converting Win Percent
  def win_percentage(wins, losses):
    percent = wins / (wins + losses) * 100
    return percent
  # print(win_percentage(5, 5)) 