def f_to_c(fahrenheit):
    celsius = 5 * (fahrenheit - 32) / 9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = f_to_c(fahrenheit)
print(f"{fahrenheit}°F is equal to {round(celsius, 2)}°C.")