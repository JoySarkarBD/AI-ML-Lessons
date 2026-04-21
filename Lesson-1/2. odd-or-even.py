# Odd or even
# Write a program that checks if a number is odd or even. 
# The program should read a number from the user and print "odd" if the number is odd, and "even" if the number is even.

# Taking user input
number = input("Enter a number: ")
number = int(number)  # Convert the input to an integer

# Checking if the number is odd or even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Explanation:
# We take input from the user and convert it to an integer.
# We then use the modulus operator (%) to check if the number is divisible by 2.
# If the result is 0, it means the number is even; otherwise, it is odd.