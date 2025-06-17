# Global convesion factor                                               
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return(celsius * CELSIUS_TO_FARHENEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
           celsius = convert_to_celsius(temperature)
           print(f"'{temperature}°F is {celsius:.2f}°c")
        elif unit == 'C':
             fahrenheit = convert_to_farenheit(temperature)
             print(f"{temperature}°C is {fahrenheit:.2f}F")
        else:
            raise ValueError("Invalid temperature unit.Please enter 'C' or 'F'.")

     except ValueError as e:
         print("Invalid temperature.Please enter a numeric value.")


  if __name__ == "__main__":
       main()
    
      

          
          
