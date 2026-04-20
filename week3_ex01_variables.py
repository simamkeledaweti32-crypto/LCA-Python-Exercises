# Week 3 Exercise 01 - Introduction and Variables
# Trainee: Simamkele Daweti

# Question 1: Variable Assignment and String Manipulation
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

print()  # blank line

# Question 2: Integer Operations
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

print()  # blank line

# Question 3: Working with Floats
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit:.2f}°F")
