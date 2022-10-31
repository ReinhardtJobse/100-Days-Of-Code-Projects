#Calculator

# Add
def add(n1, n2):
  return n1 + n2 

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract, 
  "*":  multiply,
  "/": divide 
}

from art import logo

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()



    
    
    
    
    
    
# if calculate_another == "y":
#   calculator(num1(first_answer), num2)
# else:
#   clear()
  


# operation_symbol = input("Pick another operation:")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

# Reinhardt's Solution - Out of scope but worked
# if operation_symbol == "+":
#   answer = num1 + num2
# elif operation_symbol == "-":
#   answer = num1 - num2
# elif operation_symbol == "*":
#   answer = num1 * num2
# elif operation_symbol == "/":
#   answer = num1 / num2

# print(f"{num1} {operation_symbol} {num2} = {answer}")

