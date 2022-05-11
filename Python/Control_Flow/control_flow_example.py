user_name = "Dave"
if user_name == "Dave":
  print("Get off my computer Dave!")
user_name = "angela_catlady_87"
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
  
  
x = 20
y = 20
credits = 120
gpa = 1.8
if(x == y):
  print("These numbers are the same")
if(credits >= 120):
  print("You have enough credits to graduate!")
if(credits >= 120 or gpa >= 2.0):
  print("You have met at least one of the requirements.")
if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
else:
    print("You will graduate! ")
      
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!") 
  
  
grade = 86
if(grade >= 90):
  print("A")
elif(grade >= 80):
  print("B")
elif(grade >= 70):
  print("C")
elif(grade >= 60):
  print("D")
else:
  print("F")

import random

name = "Davon"
question = "Can I win big gambling in Vegas?"
answer = ""

random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"
  
print(name + " asks: " + question)
print("Magic 8 Ball's answer: " + answer)


weight = 8.4
#Ground Shipping
if weight <= 2:
  print(1.50 * weight + 20)
elif weight >= 2 and (weight <= 6):
  print(3 * weight + 20)
elif weight > 6 and (weight <= 10):
  print(4 * weight + 20)
else:
  print(4.75 * weight + 20)