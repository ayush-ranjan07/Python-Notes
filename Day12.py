###############################################################################################################################################################################################################################################################################################################################################################################################


##                                                          Namespaces: Local vs. Global Scope in Python

# In Python, a namespace is a container that holds a collection of identifiers (such as variable names, function names, class names, etc.) and their corresponding objects. Namespaces help in organizing and managing identifiers to avoid naming conflicts and maintain code clarity. There are two primary types of namespaces in Python: local and global.

### Local Namespace (Function Scope):

# 1. **Definition**: A local namespace, also known as function scope, is created whenever a function is called. It contains the identifiers (variables, function parameters, and other objects) that are defined within the function.

# 2. **Scope**: A local namespace is limited to the function in which it is created. The identifiers declared within the function are accessible only within that function and are not visible outside.

# 3. **Lifetime**: The local namespace is created when the function is called and destroyed when the function completes execution. This means that local variables do not persist beyond the function's execution.

# **Example**:


def my_function():
    local_variable = 42  # 'local_variable' is in the local namespace
    print(local_variable)

my_function()
# print(local_variable)  # This would result in a NameError because 'local_variable' is not defined in the global namespace


### Global Namespace (Module Scope):

# 1. **Definition**: The global namespace, also known as module scope, exists for the entire duration of the program and contains identifiers defined at the top level of a Python module or script.

# 2. **Scope**: Global variables and functions are accessible from any part of the module or script where they are defined, including within functions. They can be used both at the top level and within functions.

# 3. **Lifetime**: The global namespace is created when the module is imported or the script is executed and remains in existence until the program terminates.

# **Example**:


global_variable = 100  # 'global_variable' is in the global namespace

def my_function():
    print(global_variable)  # 'global_variable' is accessible within the function

my_function()
print(global_variable)  # 'global_variable' is also accessible outside the function


### Shadowing:

# In Python, if a variable with the same name exists in both the local and global namespaces, the local variable takes precedence within the function scope. This is known as "shadowing."

# **Example**:


# x = 10  # Global variable

def my_function():
    x = 20  # Local variable (shadows the global variable)
    print(x)  # Prints the value of the local variable

my_function()
print(x)  # Prints the value of the global variable


# In this example, the local variable `x` shadows the global variable `x` within the function `my_function`.

# Understanding the distinction between local and global namespaces is essential for managing variable scope, avoiding naming conflicts, and ensuring that variables are used in the intended context within your Python programs.


##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



#                                                                          Block Scope


# Python does not have block scope like some other programming languages (e.g., C++ or Java). Instead, Python primarily uses function scope, global scope, and the concept of namespaces for variable scope. In Python, variables defined within a block, such as a loop or an if statement, are typically accessible outside of that block, as long as they are defined within the same function or global scope.

# Here's a brief explanation of variable scope in Python:

# 1. **Function Scope**: Variables defined within a function are scoped to that function. They are accessible only within that function and are not visible outside of it.


   def my_function():
       x = 10  # 'x' is in function scope
       print(x)

   my_function()
   # print(x)  # This would result in a NameError because 'x' is not defined in the global scope


# 2. **Global Scope**: Variables defined at the top level of a Python module or script are in the global scope. They are accessible from any part of the module or script, including within functions.


   y = 20  # 'y' is in global scope

   def another_function():
       print(y)  # 'y' from global scope is accessible within the function

   another_function()


# 3. **Block Scope (Lack Thereof)**: Unlike some other programming languages, Python does not have block scope. Variables defined within a block, such as a loop or an if statement, are usually accessible outside of that block, as long as they are defined within the same function or global scope.

  
   for i in range(3):
       z = i  # 'z' is not in block scope; it's accessible outside of the loop
   print(z)  # 'z' is accessible here
  

# It's important to note that while Python lacks block scope, it does follow a rule called the "LEGB" rule (Local, Enclosing, Global, Built-in) to determine variable scope. This rule defines the order in which Python looks for a variable:

# - **Local**: Python first checks if the variable is defined in the local function scope.
# - **Enclosing**: If not found locally, Python looks in any enclosing (or "non-local") function scopes, starting from the innermost and moving outward.
# - **Global**: If the variable is not found in any enclosing scopes, Python checks in the global scope.
# - **Built-in**: If the variable is not found in any of the above scopes, Python checks in the built-in namespace for Python's standard library.

# Understanding variable scope in Python is crucial for writing clean and maintainable code and avoiding unexpected behavior related to variable visibility and shadowing.


################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#                                                                            Constants and Global Scope


# In Python, constants are typically defined as global variables with uppercase names to indicate that their values should not be changed. Python doesn't have built-in constants like some other languages, so you rely on conventions to indicate that a variable is intended to be treated as a constant.

# Here's an example of defining a constant in Python's global scope:


# Define a global constant
PI = 3.14159265359
GRAVITY = 9.81

# Functions and code can access these constants
def calculate_circle_area(radius):
    return PI * (radius ** 2)

def calculate_free_fall_distance(time):
    return 0.5 * GRAVITY * (time ** 2)

# Using the constants
radius = 5
time = 2
circle_area = calculate_circle_area(radius)
free_fall_distance = calculate_free_fall_distance(time)

print(f"Circle area with radius {radius}: {circle_area}")
print(f"Free fall distance after {time} seconds: {free_fall_distance}")


# In this example, `PI` and `GRAVITY` are defined as global constants, indicated by their uppercase names. These constants can be used throughout the program without modification, and their values are accessible in functions as well.
In Python, constants are typically defined as global variables with uppercase names to indicate that their values should not be changed. Python doesn't have built-in constants like some other languages, so you rely on conventions to indicate that a variable is intended to be treated as a constant.

# Here's an example of defining a constant in Python's global scope:


# Defobal constant
PI = 3.14159265359
GRAVITY = 9.81

# Functions and code can access these constants
def calculate_circle_area(radius):
    return PI * (radius ** 2)

def calculate_free_fall_distance(time):
    return 0.5 * GRAVITY * (time ** 2)

# Using the constants
radius = 5
time = 2
circle_area = calculate_circle_area(radius)
free_fall_distance = calculate_free_fall_distance(time)

print(f"Circle area with radius {radius}: {circle_area}")
print(f"Free fall distance after {time} seconds: {free_fall_distance}")


# In this example, `PI` and `GRAVITY` are defined as global constants, indicated by their uppercase names. These constants can be used throughout the program without modification, and their values are accessible in functions as well.

# Remember that Python does not enforce the immutability of variables with uppercase names; it's a naming convention. If you want to create truly immutable constants, you can use techniques like creating custom classes or using Python's `collections.namedtuple`.

# Using uppercase variable names for constants and defining them in the global scope is a common practice in Python to make your code more readable and maintainable.that Python does not enforce the immutability of variables with uppercase names; it's a naming convention. If you want to create truly immutable constants, you can use techniques like creating custom classes or using Python's `collections.namedtuple`.

# Using uppercase variable names for constants and defining them in the global scope is a common practice in Python to make your code more readable and maintainable.