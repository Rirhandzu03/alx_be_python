
#Defining global conversion factors

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9

def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit

#User  Interaction
if __name__ == "__main__":
    try:
        temperature = float(input("Enter the temperature to convert:  "))
        unit = input("Is this temperature in Celcius or Fahnheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celcius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Inavalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")





