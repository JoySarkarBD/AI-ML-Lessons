# Style guide
# 1. Use meaningful variable names
# 2. Use consistent indentation (4 spaces)
# 3. Use comments to explain your code
# 4. Avoid using global variables
# 5. Use functions to organize your code
# 6. Use docstrings to document your functions
# 7. Avoid using magic numbers (use constants instead)
# 8. Use snake_case for variable and function names
# 9. Use PascalCase for class names
# 10. Avoid using unnecessary code (keep it simple)

# Example of a function with a docstring
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle

    Returns:
    float: The area of the circle
    """
    import math
    area = math.pi * radius ** 2
    return area
    
# Example of using the function
circle_radius = 5
area = calculate_area(circle_radius)
print(f"The area of the circle with radius {circle_radius} is {area:.2f}.")