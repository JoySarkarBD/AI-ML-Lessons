# Operators
# Operators are special symbols that perform specific operations on one or more operands. In Python, there are several types of operators, including arithmetic, assignment, comparison, logical, bitwise, and more. Here are some common operators in Python:

# Arithmetic Operators
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# // (Floor Division)
# % (Modulus)
# ** (Exponentiation)

# Assignment Operators
# = (Assignment)
# += (Addition Assignment)
# -= (Subtraction Assignment)
# *= (Multiplication Assignment)
# /= (Division Assignment)
# //= (Floor Division Assignment)
# %= (Modulus Assignment)
# **= (Exponentiation Assignment)

# Comparison Operators
# == (Equal to)
# != (Not equal to)
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)

# Logical Operators
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT) 

# Bitwise Operators
# & (Bitwise AND)
# | (Bitwise OR)
# ^ (Bitwise XOR)
# ~ (Bitwise NOT)
# << (Left Shift)
# >> (Right Shift)

# You can use these operators to perform various operations on variables and values in your Python code. For example:
a = 10
b = 5

# Using arithmetic operators
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print(a // b) # Output: 2
print(a % b)  # Output: 0
print(a ** b) # Output: 100000

# Using comparison operators
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

# Using logical operators
x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
print(not y)    # Output: True  

# Using assignment operators
c = 10
c += 5  # Equivalent to c = c + 5
print(c)  # Output: 15
c *= 2  # Equivalent to c = c * 2
print(c)  # Output: 30
c /= 3  # Equivalent to c = c / 3
print(c)  # Output: 10.0
c //= 4  # Equivalent to c = c // 4
print(c)  # Output: 2.0
c %= 2  # Equivalent to c = c % 2
print(c)  # Output: 0.0
c **= 3  # Equivalent to c = c ** 3
print(c)  # Output: 0.0

# Using bitwise operators
d = 5  # In binary: 0101
e = 3  # In binary: 0011
print(d & e)  # Output: 1 (In binary: 0001)
print(d | e)  # Output: 7 (In binary: 0111)
print(d ^ e)  # Output: 6 (In binary: 0110)
print(~d)     # Output: -6 (In binary: 1010)
print(d << 1) # Output: 10 (In binary: 1010)
print(d >> 1) # Output: 2 (In binary: 0010)
