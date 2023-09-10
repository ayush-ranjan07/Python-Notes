# DATATYPES

# In Python, there is a distinction between "primitive" or "built-in" data types and "user-defined" data types. Primitive or built-in data types are the fundamental data types that are provided by the Python language itself. These data types are used to represent basic values and have operations that are directly supported by the Python interpreter.

# Some Common Datatypes in Python
# 1. Integers (`int`): Used to represent whole numbers, both positive and negative, without a decimal point. For example: `42`, `-10`, `0`.

# 2. Floating-Point Numbers (`float`): Used to represent numbers with a decimal point. For example: `3.14`, `-0.001`, `2.0`.

# 3. Strings (`str`): Used to represent text. Strings are enclosed in single or double quotes. For example: `"Hello, World!"`, `'Python'`, `"123"`.

# 4. Lists: Ordered collections of elements, which can be of different data types. Lists are mutable, which means you can modify their contents. For example: `[1, 2, 3]`, `['apple', 'banana', 'cherry']`.

# 5. Tuples: Similar to lists but immutable, meaning their elements cannot be changed after creation. For example: `(1, 2, 3)`, `('John', 25, 'New York')`.

# 6. Dictionaries (`dict`): Key-value pairs used for mapping. Each key is unique, and you can use it to retrieve the associated value quickly. For example: `{'name': 'Alice', 'age': 30, 'city': 'Paris'}`.

# 7. Sets: Unordered collections of unique elements. Sets are useful for performing mathematical set operations like union, intersection, and difference. For example: `{1, 2, 3}`, `{'apple', 'banana', 'cherry'}`.

# 8. Booleans (`bool`): Represents either `True` or `False`, and is often used in conditional statements and logical operations.

# 9. None Type (`NoneType`): Represents the absence of a value or a null value. It is commonly used to initialize variables when no value is available.

# 10. Bytes and Byte Arrays: Used for handling binary data, such as reading and writing files in binary mode.

# 11. Custom Objects and Classes: You can create your own data types by defining classes in Python.



# Zero-based indexing means that the first element in a sequence, such as a list or string, is located at index 0. In many programming languages, including Python, arrays, lists, and other data structures are indexed starting from 0. This can be a bit counterintuitive for people who are used to counting from 1, but it's a common convention in computer science and programming.

#Let me explain zero-based indexing with an example in Python:


my_list = [10, 20, 30, 40, 50]

# In this list, we have five elements. Here's how they are indexed:

# - Element at index 0: `10`
# - Element at index 1: `20`
# - Element at index 2: `30`
# - Element at index 3: `40`
# - Element at index 4: `50`

# To access a specific element in the list, you use square brackets and specify the index:


print(my_list[0])  # This will print 10
print(my_list[2])  # This will print 30
print(my_list[4])  # This will print 50


# As you can see, the index is zero-based, so the first element is accessed with `[0]`, the second element with `[1]`, and so on.

# Here's a simple code snippet that demonstrates this with a string:


my_string = "Hello, World!"

# Accessing characters using zero-based indexing
first_character = my_string[0]  # 'H'
second_character = my_string[1]  # 'e'

# Zero-based indexing is a standard convention in many programming languages, and it's important to understand and use it correctly when working with arrays, lists, strings, and other data structures in Python.


## Type Error, Type Checking, and Type Conversion

# Type Error: Occurs when incompatible data types are used together.

# Example:

num = 42
text = "Hello, World!"
result = num + text  # Type Error


# Type Checking: Verifying data types before operations.

# Example:

value = 42
if type(value) == int:
    print("value is an integer")


# Type Conversion: Changing one data type to another.

# Example:
num_str = "42"
num = int(num_str)
result = num * 2


## Mathematical Operations in Python


### Addition


a = 5
b = 3
result = a + b  # result is 8


### Subtraction


x = 10
y = 7
result = x - y  # result is 3


### Multiplication


p = 6
q = 4
result = p * q  # result is 24


### Division


m = 20
n = 5
result = m / n  # result is 4.0 (float division)


### Floor Division


p = 20
q = 6
result = p // q  # result is 3 (integer division, rounded down)


### Modulus (Remainder)

x = 17
y = 5
result = x % y  # result is 2 (remainder after division)


### Exponentiation


base = 2
exponent = 3
result = base ** exponent  # result is 8 (2^3)


### Square Root


import math
number = 16
result = math.sqrt(number)  # result is 4.0


