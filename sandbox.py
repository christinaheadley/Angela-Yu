# response = input("What is your name?")
# x= len(response)
# print(x)

# print( len ( input("What is your name? ") ) ) 

# response = input("What is your name? ")
# x = len(response)
# print(x)
# print(response)

# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# c = b
# b = a
# a = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)
# print("Welcome to the average band name generator!!")

# city = input("What city did you grow up in?\n")
# pet = input("What is your pet's name?\n")
# print("Your band name is " + city + " " + pet)

# type("Hello")
# type( str(len( "Hello")))

# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# num1 = (int(two_digit_number[0]))
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