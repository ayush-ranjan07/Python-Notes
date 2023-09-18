##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


##                                                     Functions with Return Values

# In Python, functions can return values, allowing you to compute a result within the function and then use or store that result in your program. Functions with return values are a fundamental part of Python programming, enabling you to encapsulate logic and produce reusable code. Here's an overview of functions with return values and how to use them effectively:

### Defining a Function with a Return Value

# To define a function that returns a value, you use the `def` keyword followed by the function name, parameters (if any), a colon, and an indented code block. You use the `return` statement to specify the value to be returned.

# **Example**:


def add(a, b):
    """This function returns the sum of two numbers."""
    result = a + b
    return result


# In this example, the `add` function takes two parameters, `a` and `b`, and returns their sum using the `return` statement.

### Calling a Function with a Return Value

# When you call a function that returns a value, you can assign the returned value to a variable.

# **Example**:


sum_result = add(5, 3)  # Calling the add function and storing the result
print(sum_result)  # Output: 8


# In this case, the result of the `add` function (the sum of 5 and 3) is stored in the variable `sum_result`.

### Multiple Return Values

# Python functions can return multiple values as a tuple. You can unpack these values into separate variables when calling the function.

# **Example**:


def divide_and_remainder(a, b):
    """This function returns both the quotient and remainder of the division."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

result, remainder = divide_and_remainder(10, 3)
print(f"Quotient: {result}, Remainder: {remainder}")


# In this example, the `divide_and_remainder` function returns both the quotient and remainder of the division operation.

### Using Return for Early Exit

# The `return` statement can be used to exit a function prematurely. If a `return` statement is encountered, the function immediately exits, and the specified value is returned.

# **Example**:


def find_index(item, items):
    """This function finds the index of an item in a list."""
    if item in items:
        return items.index(item)
    else:
        return -1

index = find_index("apple", ["banana", "apple", "cherry"])
print(f"Index: {index}")  # Output: Index: 1


# In this example, the `find_index` function returns either the index of the item if found or -1 if the item is not in the list.

### Docstrings and Function Documentation

# Including docstrings (as shown in the examples) is good practice for documenting the purpose and usage of your functions. You can access this documentation using the `help()` function or by viewing the function's `__doc__` attribute.

# Functions with return values are a powerful tool in Python for encapsulating logic, producing results, and making your code more modular and reusable. They are essential for tasks that involve computations, data processing, and decision-making in your programs.


#################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


##                                                                          Docstrings

# Docstrings are a way to document your Python functions, providing information about their purpose, parameters, return values, and usage. They are essential for improving code readability and maintainability. Here's an extended section on using docstrings effectively in Python functions:

### What is a Docstring?

# A docstring is a multi-line string that serves as a comment or documentation for a function. It is placed immediately after the function definition and enclosed in triple-quotes (either single or double). The docstring provides essential information about the function's behavior, parameters, and usage.

# **Example**:


def add(a, b):
    """This function returns the sum of two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of 'a' and 'b'.
    """
    result = a + b
    return result


# In this example, the docstring provides a clear and concise description of the function's purpose, its parameters (`a` and `b`), and the return value.

### Benefits of Using Docstrings:

# 1. **Documentation**: Docstrings serve as self-contained documentation within the code, making it easier for developers (including yourself) to understand how to use the function correctly.

# 2. **Readability**: Well-structured docstrings improve code readability and help others quickly grasp the purpose and usage of the function.

# 3. **Introspection**: Python's built-in help system and documentation tools can extract docstrings to provide interactive help and documentation for functions.

### Docstring Format and Guidelines:

# When writing docstrings, it's essential to follow certain conventions and guidelines for consistency and clarity:

# - Start with a one-line summary that briefly describes the function's purpose and what it does.
# - Include a blank line after the one-line summary.
# - Use the "Args" section to list each parameter with its data type and a brief description.
# - Use the "Returns" section to describe the return value and its data type.
# - Include additional sections as needed, such as "Raises" to describe exceptions that the function may raise.

# **Example**:


def divide(a, b):
    """Divides two numbers.
    
    Args:
        a (float): The dividend.
        b (float): The divisor.
    
    Returns:
        float: The result of 'a' divided by 'b'.
    
    Raises:
        ZeroDivisionError: If 'b' is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    result = a / b
    return result


### Accessing Docstrings:

# You can access a function's docstring using the `help()` function or by accessing the `__doc__` attribute of the function.

# **Example**:


help(add)  # Display the docstring for the 'add' function
print(add.__doc__)  # Access the docstring directly


##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


### `return` Statement:

# 1. **Purpose**: The `return` statement is used inside functions to specify the result or value that the function should produce as output. It allows a function to compute a value or perform an operation and then send that value back to the caller.

# 2. **Usage**: `return` is used specifically within functions. When a `return` statement is encountered, it immediately exits the function, and the specified value is passed back to the caller.

# 3. **Example**:

  
   def add(a, b):
       result = a + b
       return result
 

#    In this example, the `add` function returns the sum of `a` and `b` as its result.

# 4. **Value Availability**: When a function returns a value, that value can be assigned to a variable or used in expressions outside the function.


   sum_result = add(5, 3)


### `print` Statement/Function:

# 1. **Purpose**: The `print` statement or function is used to display information or values on the console or in an output stream. It is primarily used for debugging, providing user feedback, or showing intermediate results during program execution.

# 2. **Usage**: `print` can be used anywhere in your code, not just within functions. It does not affect the flow of your program or return values to the caller.

# 3. **Example**:


   print("Hello, world!")


#    In this example, the `print` statement displays the string "Hello, world!" in the console.

# 4. **Value Availability**: The `print` function does not produce a value that can be captured or used for further computation. It sends output to the console or a file but does not provide a return value.

   
   result = print("Hello, world!")  # 'result' will be None


# In summary, the key difference between the `return` statement and the `print` statement is their purpose and behavior:

# - `return` is used to provide a result or value from a function to the caller, allowing the function's result to be used in other parts of the program.

# - `print` is used to display information or values in the console or output stream for debugging and user interaction but does not provide a return value.

# It's crucial to understand when to use each statement based on the desired outcome in your code. Typically, `return` is used for computations and data processing, while `print` is used for communication and debugging purposes.