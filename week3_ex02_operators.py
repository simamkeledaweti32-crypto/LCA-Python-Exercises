# Question 1: Arithmetic and Assignment Operators
x = 5
y = 10

x += 3          # Add 3 to x using += operator
y *= 2          # Multiply y by 2 using *= operator
result = x / y  # Divide x by y and store in 'result'
print(result)   # Print the value of 'result'

#------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 15
b = 8
c = 12

condition1 = a > b              # checks if a is greater than b
condition2 = b % 2 == 0         # checks if b is even using modulus
condition3 = c <= a             # checks if c is less than or equal to a

# final_condition: True if (a > b) OR (b is even AND c <= a)
final_condition = condition1 or (condition2 and condition3)
print(final_condition)          # Print the value of 'final_condition'

#------------------------------------------------------
# Question 3: Conditional Statements
score = int(input("Enter a test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")        # Print the grade for the given score

#------------------------------------------------------
# Question 4: Combining Operators and Conditionals
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    calc_result = num1 + num2
elif operation == "-":
    calc_result = num1 - num2
elif operation == "*":
    calc_result = num1 * num2
elif operation == "/":
    if num2 == 0:
        calc_result = "Error: Cannot divide by zero"
    else:
        calc_result = num1 / num2
else:
    calc_result = "Error: Invalid operation"

print(f"Result: {calc_result}")
