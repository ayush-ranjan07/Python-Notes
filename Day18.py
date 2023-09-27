

## Exception Handling in Python

# Exception handling is a crucial aspect of Python programming. It allows you to gracefully manage errors and unexpected situations in your code, ensuring that your program doesn't crash. Here's a comprehensive section on exception handling in Python:

### **1. What is an Exception?**

# An exception is an event that occurs during the execution of a program, disrupting the normal flow of instructions. Python raises exceptions when it encounters errors or unexpected conditions, such as division by zero or trying to access a non-existent file.

### **2. The `try` and `except` Blocks**

# To handle exceptions, Python provides the `try` and `except` blocks:


try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception


# - The `try` block contains the code that might raise an exception.
# - If an exception occurs, the program immediately jumps to the `except` block.
# - You specify the type of exception you want to catch in the `except` block (e.g., `ZeroDivisionError`, `FileNotFoundError`).

### **3. Handling Multiple Exceptions**

# You can handle multiple exceptions by adding multiple `except` blocks:


try:
    # Code that might raise an exception
except ExceptionType1:
    # Code to handle ExceptionType1
except ExceptionType2:
    # Code to handle ExceptionType2


# Python will execute the appropriate `except` block based on the type of exception raised.

### **4. The `else` Block**

# You can also include an `else` block after all the `except` blocks. Code inside the `else` block will run if no exceptions occur in the `try` block.


try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code to execute if no exception occurred


### **5. The `finally` Block**

# The `finally` block is used to clean up resources, regardless of whether an exception occurred or not. It's often used for tasks like closing files or releasing network connections.


try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
finally:
    # Code that always runs, even if there was an exception


### **6. Raising Exceptions**

# You can raise exceptions intentionally using the `raise` statement. This is useful when you want to indicate an error condition in your code.


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y


### **7. Common Exception Types**

# Python has a wide range of built-in exception types, including:

# - `ZeroDivisionError`: Raised when dividing by zero.
# - `FileNotFoundError`: Raised when attempting to open a non-existent file.
# - `TypeError`: Raised when performing an operation on an inappropriate data type.
# - `ValueError`: Raised when a function receives an argument of the correct data type but an inappropriate value.

### **8. Custom Exception Classes**

# You can create your own custom exception classes by inheriting from the built-in `Exception` class. This allows you to define specific error conditions for your applications.


class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    if something_is_wrong:
        raise CustomError("Something went wrong")
except CustomError as ce:
    print(ce)


# Exception handling is a fundamental skill in Python development. It ensures your programs are robust and can gracefully recover from errors, enhancing the reliability of your software.