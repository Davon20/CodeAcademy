# #Python is able to take multiple data types in a single list
def listIntro():
    ints_and_strings = [1, 2, 3, 4, "four", "five", "six"]
    sam_height_and_testscore = ["Sam", 67, 85.5, True]
#Lists can have methods attached
    example_list = [1, 2, 3, 4]
    example_list.append(5)
    example_list.remove(5)
# #Concatenating Lists using +
    orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
    new_orders = ["lilac", "iris"]
    broken_prices = [5, 3, 4, 5, 4] + [4]
    print(broken_prices)
    print(orders + new_orders)
# Assigns variable for the list elements
    employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
    employee_four = employees[3]
    print(employee_four)
# #Uses negative index values
    shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
    last_element = shopping_list[-1]
    index5_element = shopping_list[5]
# #Modifying List Elements
    garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
    garden_waitlist[-3] = "Calla"
# #Shrinking A List
    order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
#Removing Element from List
    order_list.remove("Flatbread")
# #Removing the spare Mango
    new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
    print(new_store_order_list)
    new_store_order_list.remove("Mango")
    print(new_store_order_list)
#Removing Onions
    new_store_order_list.remove("Onions")
    print(new_store_order_list)

# 2D Lists: Lists Inside of Lists
def two_d_lists():
    heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
    ages = [["Aaron", 15], ["Dhruti", 16]]
#Accessing 2D Lists
    class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
    print(class_name_test)
    sams_score = class_name_test[2][1]
    print(sams_score)
    ellies_score = class_name_test[-1][-1]
    print(ellies_score)
#Modifying 2D Lists
    incoming_class = [
      ["Kenny",	"American",	9],
      ["Tanya",	"Russian",	9],
      ["Madison", "Indian",	7]
    ]
    incoming_class[2][2] = 8
# #Modifying Using Negative Indices
    incoming_class[-3][-3] = "Ken"
    print(incoming_class)
#Collective List Example
    first_names = ["Ainsley", "Ben", "Chani", "Depak"]
    preferred_size = ["Small", "Large", "Medium"]
    preferred_size.append("Medium")

    customer_data = [
      ["Ainsley", "Small", True],
      ["Ben", "Large", False],
      ["Chani", "Medium", True],
      ["Depak", "Medium", False]
    ]

    customer_data[2][2] = False
    customer_data[1].remove(False)

    customer_data_final = customer_data + [
      ["Amit", "Large", True], 
      ["Karim", "X-Large", False]
      ]
    print(customer_data_final)
    
# #Gradebook Exammple
def masterList():
    last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
    subjects = "physics", "calculus", "poetry", "history"
    grades = 98, 97, 85, 88
    gradebook =[
      ["physics",	98],
      ["calculus",	97],
      ["poetry",	85],
      ["history",	88]
    ]
    gradebook.append(["computer science", 100])
    gradebook.append(["visual arts", 93])
    gradebook[5][1] = 98
    gradebook[2].remove(85)
    gradebook[2].append("Pass")
    print(gradebook)
    full_gradebook = last_semester_gradebook + gradebook
    print(full_gradebook)

#Working with List Methods
def usingListMethods():
    #Insert
    car_models = ["Toyota", "Nissian", "Ford", "GMC", "Cheverlot", "Kia"]
    car_models.insert(7, "Dodge")
    
    #Pop
    car_models.pop()
    car_models.pop(1)
    
    #Range
    numbers = range(15)
    #Using list prints each iteration
    print(list(numbers))
    #Another function of ranges is skipping by the third input of the method
    max_range = range(0, 100, 25)
    
    #Length
    print(len(car_models)) #or define a variable that stores len() then just call the variable
    
    #Slicing Lists
    big_three = car_models[0:3]
    
    #Alternate Slicing
    last_cars = car_models[-2:]
    first_car = car_models[:-3]
    
    #Count
    car_count = car_models.count("Toyota")
    
    #Sort
    car_models.sort()
    
    #Reversed Sorting
    car_models.sort(reverse=True)
    
    # List Sorting = Sorted() Function
    car_models_sorted = sorted(car_models)

#Using Multiple List Methods
def multiListMethods():
    toppings = "pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"

    prices = 2, 6, 1, 3, 2, 7, 2

    num_two_dollar_slices = prices.count(2)
    print(num_two_dollar_slices)
    num_pizzas = len(toppings)
    print(num_pizzas)
    print("We sell " + str(num_pizzas) + " different kinds of pizza!")

    pizza_and_prices = [
      [2, "pepperoni"],
      [6,	"pineapple"],
      [1,	"cheese"],
      [3,	"sausage"],
      [2,	"olives"],
      [7,	"anchovies"],
      [2,	"mushrooms"]
    ]

    pizza_and_prices.sort()

    cheapest_pizza = pizza_and_prices[1]
    pizza_and_prices.sort()
    priciest_pizza = pizza_and_prices[-1]

    pizza_and_prices.pop()

    pizza_and_prices.insert(4, [2.5, "peppers"])

    three_cheapest = pizza_and_prices[0:3]
    print(three_cheapest)