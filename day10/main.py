from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

continue_same_operation = True
list_of_operations=['+', '-', '*', '/']

def add(a, b):
  return a + b

def div(a, b):
  return a / b

def multiply(a, b):
  return a * b

def substract(a, b):
  return a - b

def set_first_number():
  first_number = float(input("What is the first number?: "))
  return first_number

def set_operation():
  print(*list_of_operations, sep="\n")
  operation = input("Pic an operation: ")
  return operation

def set_next_number():
  next_number = float(input("What's the next number?: "))
  return next_number

def operation_calculation(number1, number2, operation):
  if operation == '+':
    return add(number1, number2)
  if operation == "-":
    return substract(number1, number2)
  if operation == '*':
    return multiply(number1, number2)
  if operation == '/':
    return div(number1, number2)

def initial_set():
  first_number = set_first_number()
  operation = set_operation()
  next_number = set_next_number()
  total = operation_calculation(first_number, next_number, operation)
  print("%.1f %s %.1f = %.1f" % (first_number, operation, next_number, total))
  return total

print(art.logo)



   
total = initial_set()
while continue_same_operation:
  continue_response = input("Type 'y' to continue calculating with %.2f, or type 'n' to start a new calculation:" % total)
  if continue_response == 'n':
    #continue_same_operation=False
    clear()
    initial_set()
  else:
    new_operation = set_operation()
    new_next_number = set_next_number()
    total = (operation_calculation(total, new_next_number, new_operation))
    print(total)
