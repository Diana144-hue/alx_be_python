def perform_operation(num1, num2, operation):
    """
    
    perfom basic arithmetic operations between two numbers.
    
    parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation(str): The operation to perform 'add', 'subtract',
        
    Returns:
        float or str: The result of the operation, or a specific message in case of error.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"