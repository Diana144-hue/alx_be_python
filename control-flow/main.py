# main.py

def greet_user(name):
    message = f"Hello, {name}! Welcome!"
    print(message)
    greet_user("Joyner") 

def calculate_area(length, width):
    area = length * width
    print("Area:", calculate_area(5, 3))
    return area

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
        check_even_odd(7)
        