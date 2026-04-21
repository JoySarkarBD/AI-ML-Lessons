# Conditional statements are used to perform different actions based on different conditions.

# In Python, we use if, elif, and else statements to implement conditional logic.

# Example 1: Using if statement
age = 18
if age >= 18:
    print("You are an adult.")

# Example 2: Using if-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 3: Using if-elif-else statement
age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Example 4: Taking user input and using conditional statements
age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")