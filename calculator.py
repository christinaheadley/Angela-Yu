from art import calculator_logo
print(calculator_logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
 }

num1 = int( input( "What is the first number? "))
for operation in operations:
    print(operation)
selected_operation = input("Pick one of the above operations: ")
num2 = int( input( "What is the second number? "))
answer = (operations[selected_operation])(num1, num2)
print(f"{num1} {selected_operation} {num2} = {answer}")