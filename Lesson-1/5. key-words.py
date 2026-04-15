# Keywords
# Keywords are reserved words in Python that have special meaning and cannot be used as variable names, function names, or any other identifiers. They are part of the syntax of the language and are used to define the structure and behavior of the code.
# All keywords in Python are in lowercase, except for True, False, and None, which are capitalized. Here is a list of some common keywords in Python:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# You can get a complete list of keywords in Python by using the built-in keyword module:
import keyword # This module provides a list of all the keywords in Python. You can use the keyword.kwlist attribute to get the list of keywords.
print(keyword.kwlist)

# Output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# It's important to remember that you cannot use these keywords as variable names or identifiers in your code, as it will result in a syntax error. For example, if you try to use "if" as a variable name, you will get an error because "if" is a keyword used for conditional statements in Python.

# Example of using a keyword as a variable name (this will cause an error):
# if = 10  # This will cause a syntax error because "if" is a keyword.  

# To avoid this error, you should choose variable names that are not keywords. For example:
my_variable = 10  # This is a valid variable name and does not cause an error

# In summary, keywords are reserved words in Python that have special meaning and cannot be used as identifiers. They are an essential part of the language's syntax and are used to define the structure and behavior of the code. Always make sure to avoid using keywords as variable names or identifiers in your code to prevent syntax errors.

# Note: The list of keywords may vary depending on the version of Python you are using, so it's always a good idea to check the documentation or use the keyword module to get the most up-to-date list of keywords for your specific Python version.
