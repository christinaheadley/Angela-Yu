# response = input("What is your name?")
# x= len(response)
# print(x)

# print( len ( input("What is your name? ") ) ) 

# response = input("What is your name? ")
# x = len(response)
# print(x)
# print(response)

#
# a = input("a: ")
# b = input("b: ")
# 

####################################
#Write your code below this line 
# c = b
# b = a
# a = c
#Write your code above this line 
####################################

#  Don't change the code below 
# print("a: " + a)
# print("b: " + b)
# print("Welcome to the average band name generator!!")

# city = input("What city did you grow up in?\n")
# pet = input("What is your pet's name?\n")
# print("Your band name is " + city + " " + pet)

# type("Hello")
# type( str(len( "Hello")))

# two_digit_number = input("Type a two digit number: ")
# #  Don't change the code above 

# ####################################
# #Write your code below this line 
# num1 = (int(two_digit_number[0])
# num2 = (int(two_digit_number[1]))
# num3 = (int(two_digit_number[0])) + (int(two_digit_number[1]))
# # print((str(num1)) + " + " + (str(num2)) + " = " + (str(num3)))
# print(num3)
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = weight / (height ** 2)
# print(int(bmi))

# age = int(input("What is your current age?"))
# days_in_90 = 90 * 365
# weeks_in_90 = 90 * 52
# months_in_90 = 90 * 12

# input_in_days = age * 365
# input_in_weeks = age * 52
# input_in_months = age * 12

# remaining_days = days_in_90 - input_in_days
# remaining_weeks = weeks_in_90 - input_in_weeks
# remaining_months = months_in_90 - input_in_months
# print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

# # AY solution:
# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? "))
# tip = float(input("What percentage tip would you like to give? "))/100
# people = float(input("How many people to split the bill? "))
# total_per_person = (bill / people) * (1 + tip)
# # rounded_total = "{:.2f}".format(total_per_person)
# # print(f"Each person should pay ${rounded_total}.")
# print(f"Each person should pay ${'{:.2f}'.format(total_per_person)}.")
#If Else and Comparison Operators:
# https://www.udemy.com/course/100-days-of-code/learn/lecture/17878014#overview

# num = float( input( "Enter a number. " ))
# if num % 2 == 0:
#   print("That is an even number.")
# else:
#   print("That is an odd number.")

# Nested if/else
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = int((weight) / (height ** 2))
# if bmi < 18.5:
#   print(f"Your BMI is {bmi} and is less than 18.5")
# elif bmi < 25:
#   print("Your BMI is between 18.5 and 25")
# else:
#   print("Your BMI is fine.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# if size == "S":
#   price = 15
#   if add_pepperoni == "Y":
#     price += 2
# elif size == "M":
#   price = 20
#   if add_pepperoni == "Y":
#     price += 3
# elif size == "L":
#   price = 25
#   if add_pepperoni == "Y":
#     price += 3

# if extra_cheese == "Y":
#   price += 1

# print(f"Your final bill is: ${price}.")

# # AY solution:
# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}.")

# Logical Operators:
#  and (not &&)
#  or (not ||)
#  not (not !)

#Step 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)

#     #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

# Calculate area

# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# import math

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     print(f"You'll need {math.ceil((height * width) / cover)} cans of paint.")

# paint_calc(height=test_h, width=test_w, cover=coverage)

# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet(location, name):
#     print(f"hi {name}")
#     print("i'm here")
#     print(f"bye {location}")
# greet(name="Jamie", location="Eden") 

# Prime Number Checker

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# def prime_checker(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not a prime number.")
#             break
#         elif number % 1 == 0 and number % number == 0:
#             print(f"{number} is a prime number.")
#             break



#     # for i in range(2, number):
#     #     if i % number == 0:
#     #         break
#     # for number in range(1, number + 1):
#     #     if number % 1 == 0 and number % number == 0:
#     #         print("It's a prime number.")
#     #     else:

#     #         print("It's not a prime number.")
# n = int(input("Check this number: "))
# prime_checker(number=n)

#Dictionaries: Day 9 
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# for k in student_scores:
#     if student_scores[k] > 90:
#         student_grades[k] = "Outstanding"
#     elif student_scores[k] > 80:
#         student_grades[k] = "Exceeds Expectations"
#     elif student_scores[k] > 70:
#         student_grades[k] = "Acceptable"
#     else:
#         student_grades[k] = "Fail"

# #TODO-2: Write your code below to add the grades to student_grades.

# print(student_scores)
# print(student_grades)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 
def add_new_country(country, visits, cities):
    travel_log.append({"country":country, "visits":visits, "cities":cities})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# AY answer:
# def add_new_country(name, visit_count, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])