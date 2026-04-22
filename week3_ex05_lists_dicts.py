# Week 3 Exercise 05 - Lists and Dictionaries

# --------------------------------------------------
# Question 1: Creating and Modifying Lists
# --------------------------------------------------
fruits = ["apple", "banana", "orange"]
fruits.append("mango")           # Add to end
fruits.insert(0, "strawberry")   # Insert at beginning  
fruits.remove("banana")          # Remove item
print("Question 1 - Modified fruits list:", fruits)

# --------------------------------------------------
# Question 2: List Operations
# --------------------------------------------------
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("\nQuestion 2 - Original numbers:", numbers)
print("Question 2 - Squared numbers:", squared_numbers)
print("Question 2 - Sum:", total_sum)
print("Question 2 - Average:", average)

# --------------------------------------------------
# Question 3: Creating and Modifying Dictionaries
# --------------------------------------------------
capitals = {"South Africa": "Pretoria", "Nigeria": "Abuja", "Kenya": "Nairobi"}
capitals["Ghana"] = "Accra"           # Add new pair
capitals["South Africa"] = "Cape Town" # Update existing
capitals.pop("Kenya")                 # Remove pair
print("\nQuestion 3 - Modified capitals dictionary:", capitals)

# --------------------------------------------------
# Question 4: Dictionary Operations
# --------------------------------------------------
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
print("\nQuestion 4 - All fruits:", list(fruit_colors.keys()))
print("Question 4 - All colors:", list(fruit_colors.values()))
print("Question 4 - Fruit and color pairs:")
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")
fruit_to_check = "apple"
if fruit_to_check in fruit_colors:
    print(f"Question 4 - {fruit_to_check} is {fruit_colors[fruit_to_check]}")
else:
    print(f"Question 4 - {fruit_to_check} is not in the dictionary")
