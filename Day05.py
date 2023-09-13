                                            ## For Loops in Python

# A `for` loop in Python is used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence. Here's an overview of `for` loops and how to use them effectively:

### Basic `for` Loop Syntax

# The basic syntax of a `for` loop in Python consists of the `for` keyword followed by a loop variable, the `in` keyword, and an iterable object. The loop variable takes on the value of each item in the iterable, one at a time.

# **Example**:


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# In this example, the loop variable `fruit` takes on each item in the `fruits` list, and the code block inside the loop (indented) is executed for each item, resulting in the printing of each fruit.

### Using the `range()` Function

# The `range()` function is often used to generate a sequence of numbers for `for` loops. It generates a sequence of numbers from a starting value (inclusive) to an ending value (exclusive).

# **Example**:


for i in range(5):
    print(i)


# This loop prints numbers from 0 to 4.

### Looping Through Strings

# `for` loops can iterate through characters in a string.

# **Example**:


word = "Python"

for char in word:
    print(char)


# This loop prints each character of the string "Python" on a separate line.

### Looping with an Index

# You can use the `enumerate()` function to loop through elements of an iterable along with their indices.

# **Example**:


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


### Nested `for` Loops

# You can nest `for` loops to iterate through multiple sequences or create patterns.

# **Example**:


for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")


# This nested loop generates coordinates in a grid.

# `for` loops are a fundamental tool for iterating over data and performing repetitive tasks in Python. They provide great flexibility and can be used in a wide range of programming scenarios.

########################################################################################################################################################################################################################################################################################

