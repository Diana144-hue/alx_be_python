# arithmetic_operation.py

def perform_operation(num1, num2, operation):
  if operation == 'Add':
    return num1 + num2
  elif operation == 'Subtract':
    return num1 - num2
  elif operation == 'Multiply':
    return num1 * num2
  elif operation == ' divide':
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
  else:
       return "Error: Invalid operation"
    
