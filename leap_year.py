# year = int(input("Enter a year. "))
# if year % 400 == 0:
#   print("Leap year.")
# elif year % 100 == 0:
#   print("Not a leap year.")
# elif year % 4 == 0:
#   print("Leap year.")
# else:
#   print("Not a leap year.")


# AY solution:
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, And it will use this information to work out the number of days in the month, then return that as the output

def is_leap(year):
  '''Takes a year as a parameter, tests if is a leap year, and returns true or false'''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
         return True
      else:
         return False
    else:
       return True
  else:
     return False

def days_in_month(year, month):
    if is_leap(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month-1]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month-1]
  
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)