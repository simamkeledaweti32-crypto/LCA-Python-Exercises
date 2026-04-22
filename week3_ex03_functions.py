# Week 3 Exercise 03 - Functions

# ---------------- Question 1: Basic Function Definition and Calling ----------------
def greet():
    print("Hello, World!")
greet()

# ---------------- Question 2: Function with Parameters ----------------
def personalized_greeting(name):
    print(f"Hello, {name}!")
personalized_greeting("Simamkele")

# ---------------- Question 3: Function with Return Value ----------------
def square(number):
    return number * number
result = square(5)
print(f"The square of 5 is {result}")

# ---------------- Question 4: Function with Multiple Parameters and Return Value ----------------
def rectangle_area(length, width):
    return length * width
area = rectangle_area(4, 5)
print(f"The area of the rectangle is {area}")

# ---------------- Question 5: Using a Function as an Argument ----------------
def apply_operation(func, number):
    return func(number)

def double(number):
    return number * 2
result_double = apply_operation(double, 7)
print(f"7 doubled is {result_double}")
result_square = apply_operation(square, 3)
print(f"3 squared is {result_square}")
