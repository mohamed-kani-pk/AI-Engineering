
# Modules

# import arithmetic
# Imports the entire arithmetic module.
# Python executes the top-level code in arithmetic.py when importing it.
# Functions inside the module are not automatically called.
# To call them, use: arithmetic.add(5, 3)


# Importing specific functions from the arithmetic module.
# We can directly call these functions without writing arithmetic. before each function name.

from arithmetic import add, subtract, multiply, divide, modulus, power


# Calling the add() function and storing its returned result.
result1 = add(5, 3)

# Calling the subtract() function.
result2 = subtract(10, 4)

# Calling the multiply() function.
result3 = multiply(6, 7)

# Calling the divide() function.
result4 = divide(20, 5)

# Calling the modulus() function.
# Modulus (%) returns the remainder after division.
result5 = modulus(10, 3)

# Calling the power() function.
# Power (**) raises the first number to the power of the second number.
result6 = power(2, 3)


# Displaying all the results using an f-string.
# \n creates a new line between each result.

print(
    f"Addition: {result1}\n"
    f"Subtraction: {result2}\n"
    f"Multiplication: {result3}\n"
    f"Division: {result4}\n"
    f"Modulus: {result5}\n"
    f"Power: {result6}"
)

""""
# Import the arithmetic module and give it an alias (new name) called Math.
import arithmetic as Math

# Call the add() function using the alias name Math.
# This is CORRECT.
result = Math.add(5, 3)

# Call the add() function using math.
# This is INCORRECT because Python is case-sensitive.
# We imported the module as Math, not math.
# result = math.add(5, 3)

# Call the add() function using arithmetic.
# This is INCORRECT because we imported the module using the alias Math.
# result = arithmetic.add(5, 3)

print(result)
"""