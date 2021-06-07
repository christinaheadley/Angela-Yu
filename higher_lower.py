from art import higher_lower_logo, vs
# import game_data print(game_data.data)
from game_data import data
from random import randint
import os
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')

score = 0
play = True
a = (data[randint(0, len(data) - 1)])
# print(a)

name_a = (a["name"])
description_a = (a["description"])
country_a = (a["country"])
follower_count_a = (a["follower_count"])
while play == True:
    b = (data[randint(0, len(data) - 1)])
    if b == a:
        b = (data[randint(0, len(data) - 1)])
    # print(b)

    name_b = (b["name"])
    description_b = (b["description"])
    country_b = (b["country"])
    follower_count_b = (b["follower_count"])

    if follower_count_a > follower_count_b:
        answer = "A"
    elif follower_count_b > follower_count_a:
        answer = "B"
    
    print(higher_lower_logo)
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == answer:
        score += 1
        screen_clear()
        print(f"You're right! Current score: {score}")
        if answer == "B":
            name_a = (b["name"])
            description_a = (b["description"])
            country_a = (b["country"])
            follower_count_a = (b["follower_count"])
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False
# import modules
# print statements and art
# select random choice a and b
# ask user to choose
# compare a and b and return results
# if win: b becomes a and select new random choice for b
# screen clears and next question appears
# if wrong: game over

# ****************************************************************
# AY solution:
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()