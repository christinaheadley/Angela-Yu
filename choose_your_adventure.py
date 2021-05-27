print("Welcome to kitty island!")

print('''
    Zzzzz  |\      _,,,--,,_       
           /,`.-'`'   ._  \-;;,_    
          |,4-  ) )_   .;.(  `'-'   
         '---''(_/._)-'(_\_)      
''')

choice_l_r = input("Would you like to go left or right? (L, R) ").upper()
if choice_l_r == "L":
  print("Good choice. More cats ahead!")

  cat_name = input("I see a cat! What should we call her? ").capitalize()
  print('''
  _._     _,-'""`-._
  (,-.`._,'(       |\`-/|
      `-.-' \ )-`( , o o)
            `-    \`_`"'-  
  ''')

  choice_comfort = input(f"{cat_name} looks scared. Should we try to comfort her? Y or N? ").upper()
  if choice_comfort == ("Y"):
    print(f"{cat_name} is afraid of people and runs to the other side of the island.")

    choice_follow = input(f"Should we follow {cat_name}? Y or N ").upper()
    if choice_follow == "Y":
      print("You run to the other side of the island and see another cat! ")
      print('''
        |\---/|
        | ,_, |
          \_`_/-..----.
      ___/ `   ' ,""+ \  
      (__...'   __\    |`.___.';
        (_,...'(_,.`__)/'.....+
      ''')
      cat_name_2 = input("What do you want to call this cat? ").capitalize()
      print(f"{cat_name_2} wants to come home and live with you. Yay! \nThe End!")
    elif choice_follow == "N":
      print("You liked seeing the cats, but it's time to go home now.\nThe End!")
    else:
      print("Try again. You must select Y or N.")

  elif choice_comfort == "N":
    print(f"{cat_name} likes that you gave her space. She comes up to you and asks to be your pet. You take {cat_name} home with you!\nThe End")
  else:
    print("Try again. You must select Y or N.")

elif choice_l_r == "R".upper():
  print("Sorry, no cats that way. Story is over")
else:
  print("Try again. You must select L or R.")