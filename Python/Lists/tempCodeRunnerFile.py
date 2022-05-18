#Python is able to take multiple data types in a single list
# ints_and_strings = [1, 2, 3, 4, "four", "five", "six"]
# sam_height_and_testscore = ["Sam", 67, 85.5, True]

# #Lists can have methods attached
# example_list = [1, 2, 3, 4]
# example_list.append(5)
# print(example_list)
# example_list.remove(5)
# print(example_list)

# #Concatenating Lists using +
# orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# # Create new orders here:
# new_orders = ["lilac", "iris"]
# orders_combined = orders + new_orders
# #Contatenating int requires list[], not just the integer alone
# broken_prices = [5, 3, 4, 5, 4] + [4]

# #Assigns variable for the list elements
# employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
# employee_four = employees[3]
# print(employees[6])

# #Uses negative index values
# shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
# last_element = shopping_list[-1]
# index5_element = shopping_list[5]
# print(last_element)
# print(index5_element)

# #Modifying List Elements
# garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
# garden_waitlist[-3] = "Calla"
# print(garden_waitlist)

# #Shrinking A List
# order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
# print(order_list)
# #Removing Element from List
# order_list.remove("Flatbread")
# print(order_list)
# #Removing the spare Mango
# new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
# print(new_store_order_list)
# new_store_order_list.remove("Mango")
# print(new_store_order_list)
# #Removing Onions
# new_store_order_list.remove("Onions")
# print(new_store_order_list)

# #2D Lists: Lists Inside of Lists
# heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
# ages = [["Aaron", 15], ["Dhruti", 16]]
# #Accessing 2D Lists
# class_name_test = [
#   ["Jenny", 90],
#   ["Alexus", 85.5],
#   ["Sam", 83],
#   ["Ellie", 101.5]
# ]
# print(class_name_test)
# sams_score = class_name_test[2][1]
# print(sams_score)
# ellies_score = class_name_test[-1][-1]
# print(ellies_score)
# #Modifying 2D Lists
# incoming_class = [
#   ["Kenny",	"American",	9],
#   ["Tanya",	"Russian",	9],
#   ["Madison",	"Indian",	7]
# ]
# incoming_class[2][2] = 8
# #Modifying Using Negative Indices
# incoming_class[-3][-3] = "Ken"
# print(incoming_class)
# #Collective List Example
# first_names = ["Ainsley", "Ben", "Chani", "Depak"]
# preferred_size = ["Small", "Large", "Medium"]

# preferred_size.append("Medium")

# customer_data = [
#   ["Ainsley",	"Small",	True],
#   ["Ben",	"Large",	False],
#   ["Chani",	"Medium",	True],
#   ["Depak",	"Medium",	False]
# ]

# customer_data[2][2] = False
# customer_data[1].remove(False)

# customer_data_final = customer_data + [
#   ["Amit", "Large", True], 
#   ["Karim", "X-Large", False]
#   ]

# print(customer_data_final)

# #Gradebook Assignment
# last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# # Your code below: 
# subjects = "physics", "calculus", "poetry", "history"
# grades = 98, 97, 85, 88

# gradebook =[
#   ["physics",	98],
#   ["calculus",	97],
#   ["poetry",	85],
#   ["history",	88]
# ]
# gradebook.append(["computer science", 100])
# gradebook.append(["visual arts", 93])
# gradebook[5][1] = 98
# gradebook[2].remove(85)
# gradebook[2].append("Pass")

# # print(gradebook)
# full_gradebook = last_semester_gradebook + gradebook
# # print(full_gradebook)
