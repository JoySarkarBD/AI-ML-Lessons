# Type Conversion
# Type conversion is the process of converting one data type to another. In Python, there are several built-in functions that can be used for type conversion. Here are some common type conversion functions:
# int() - Converts a value to an integer
# float() - Converts a value to a floating-point number
# str() - Converts a value to a string
# bool() - Converts a value to a boolean
# Example of type conversion
x = "10"
y = int(x)  # Convert string to integer
print(y)    # Output: 10

z = 3.14
w = int(z)  # Convert float to integer (truncates the decimal part)
print(w)    # Output: 3

a = 5
b = float(a)  # Convert integer to float
print(b)      # Output: 5.0

c = 0
d = bool(c)  # Convert integer to boolean (0 is False, non-zero is True)
print(d)     # Output: False

e = 1
f = bool(e)  # Convert integer to boolean (0 is False, non-zero is True)
print(f)     # Output: True

g = "Hello"
h = bool(g)  # Convert string to boolean (empty string is False, non-empty string is True)
print(h)     # Output: True

i = ""
j = bool(i)  # Convert string to boolean (empty string is False, non-empty string is True)
print(j)     # Output: False

# You can also use type conversion in expressions. For example:
x = "5"
y = 10
z = int(x) + y  # Convert string to integer and add to another integer
print(z)        # Output: 15

# It's important to note that type conversion can sometimes lead to loss of information. For example, converting a float to an integer will truncate the decimal part, and converting a string that cannot be converted to a number will raise an error. Always be cautious when performing type conversions in your code.
