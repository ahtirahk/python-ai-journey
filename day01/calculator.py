num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

try:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
except ZeroDivisionError:
    division = "Cannot divide by zero!"
    floor_division = "Cannot divide by zero!"
    modulus = "Cannot divide by zero!"

print("--- Results ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_division}")
print(f"{num1} % {num2} = {modulus}")