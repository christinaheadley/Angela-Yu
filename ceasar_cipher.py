    

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# # shift = int(input("Type the shift number:\n"))
# # text = input("Type your message:\n").lower()
# def encrypt(text, shift):
#     text_list = list(text)
#     encoded_word = ""
#     for i in range(0, len(text)):
#         position = alphabet.index(text_list[i])
#         new_position = position + shift
#         encoded_word = encoded_word + (alphabet[new_position])
#     print(f"print output: The encoded text is {encoded_word}.")
# encrypt("zulu", 5)        



#     for letter in text:
#         alphabet[i] = alphabet[i + shift]
# print(type(text))
# print(list(text))
# coded_alphabet = alphabet
# alpha_move = (coded_alphabet[:shift])
# del coded_alphabet[0:shift]
# coded_alphabet.extend(alpha_move)
# print(coded_alphabet)
# print(alphabet)


# print(f"text_list: {text_list}")

# index = alphabet.index(text_list[0])
# print(index)

# text_list[0] = 
# for i in range(0, len(text)):
#     position = alphabet.index(text_list[i])  #eg 7 for "h"
#     print(f"position : {position}")
#     print(f"shift: {shift}")
#     new_position = position + shift
#     if new_position > 25:
#         new_position = new_position - 25

#     print(f" a[p+s]: {alphabet[new_position]}")
#     # print(f"i: {i}")
#     encoded_word = ""
#     # encoded_word += (alphabet[new_position])
# print(type(encoded_word))
# print(type(alphabet[new_position]))


# list(text[index]) = list(text[index + 5])

# for index in range(len(alphabet)):
#     print(index, alphabet[index], end ="\n")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


# def ceasar(text, shift, direction):
#     encoded_text = ""
#     decoded_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position + shift
#             encoded_text += alphabet[new_position]
#         elif direction == "decode":
#             new_position = position - shift
#             decoded_text += alphabet[new_position]
#     if len(encoded_text) > 0:
#         print(f"The encoded text is CC {encoded_text}")
#     elif len(decoded_text) > 0:
#         print(f"The decoded text is DD {decoded_text}")
        
# # ceasar(plain_text=text, shift_amount=shift, direction=direction)
# ceasar("hello", 5, "encode")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
go_again = "yes"
while go_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
      shift *= -1
    for char in text:
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if char not in alphabet:
        char = char
        end_text += char
      else:
        position = alphabet.index(char)
        new_position = position + shift
        if new_position > 25:
          new_position = new_position % 26
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")
  caesar(text, shift, direction)   
  # caesar("he llo.;", 60, "encode")
  go_again = input("Would you like to play again? Type 'yes' or 'no'. \n")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

# caesar(text=text, shift=shift, direction=direction)
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     position = alphabet.index(char)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.
# from hangman_art import logo
# print(logo)
# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# #Try running the program and entering a shift number of 45.
# #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
# #Hint: Think about how you can use the modulus (%).

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)