# Week 3 Exercise 04 - Loops and Modules

# ---------------- Question 1: Using a for loop with a list ----------------
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
for fruit in fruits:
    print(fruit)

# ---------------- Question 2: Using a while loop for countdown ----------------
count = 5
while count >= 1:
    print(count)
    count -= 1

# ---------------- Question 3: Using a for loop with range() ----------------
for i in range(1, 11):
    print(i * i)

# ---------------- Question 4: Using the random module ----------------
import random
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
for _ in range(3):
    print(random.choice(colors))

# ---------------- Question 5: Creating and using a custom module ----------------
import math_operations

print(f"10 + 5 = {math_operations.add(10, 5)}")
print(f"10 - 5 = {math_operations.subtract(10, 5)}")
print(f"10 * 5 = {math_operations.multiply(10, 5)}")
print(f"10 / 5 = {math_operations.divide(10, 5)}")

# ---------------- Simple calculator using while loop ----------------
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "5":
        print("Goodbye!")
        break
        
    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"Result: {math_operations.add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {math_operations.subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {math_operations.multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {math_operations.divide(num1, num2)}")
        except ValueError:
            print("Please enter valid numbers")
    else:
        print("Invalid choice. Try again.")
