#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################\


##                                                              Dictionaries

# A dictionary in Python is an unordered collection of data that is stored as key-value pairs. Dictionaries are widely used in Python because they provide a way to store and access data with a unique key rather than using numeric indices, as in lists or arrays. Here's an overview of dictionaries in Python:

### Creating a Dictionary

# You can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces `{}`.

# **Example**:


student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}


# In this example, `student` is a dictionary with three key-value pairs.

### Accessing Values

# You can access the values in a dictionary by using the corresponding key inside square brackets `[]` or by using the `get()` method.

# **Example**:


name = student["name"]  # Accessing value using square brackets
age = student.get("age")  # Accessing value using get() method


### Modifying and Adding Values

# You can modify the values of a dictionary by assigning a new value to a specific key. You can also add new key-value pairs to an existing dictionary.

# **Example**:


student["age"] = 21  # Modifying the 'age' value
student["year"] = 3   # Adding a new key-value pair


### Removing Key-Value Pairs

# You can remove a key-value pair from a dictionary using the `del` statement or the `pop()` method.

# **Example**:


del student["year"]  # Removing the 'year' key-value pair
age = student.pop("age")  # Removing and retrieving the 'age' value


### Dictionary Methods

# Python dictionaries come with several useful methods, including:

# - `keys()`: Returns a list of all the keys in the dictionary.
# - `values()`: Returns a list of all the values in the dictionary.
# - `items()`: Returns a list of key-value pairs (tuples) as a sequence.
# - `clear()`: Removes all items from the dictionary.
# - `copy()`: Creates a shallow copy of the dictionary.
# - `update()`: Merges two dictionaries, updating the values of existing keys and adding new key-value pairs.
# - `len()`: Returns the number of key-value pairs in the dictionary.

### Checking for Key Existence

# You can check if a key exists in a dictionary using the `in` keyword.

# **Example**:


if "name" in student:
    print("Name exists in the dictionary.")


### Dictionary Comprehensions

# Python supports dictionary comprehensions, which allow you to create dictionaries using a concise syntax.

# **Example**:


squared_numbers = {x: x**2 for x in range(1, 6)}


# In this example, a dictionary of squared numbers is created using a comprehension.

# Dictionaries are versatile data structures in Python, suitable for a wide range of tasks, such as storing configuration settings, representing data records, and implementing lookup tables. Their flexibility, ability to store heterogeneous data, and efficient key-based retrieval make them a fundamental tool for Python programmers.


#########################################################################################################################################################################################################################################################################################################################################################################################


##                                              Nesting Lists and Dictionaries

# Nesting is a powerful concept in Python that allows you to store complex and structured data by embedding one data structure (like a list or a dictionary) inside another. This enables you to represent hierarchical and multi-dimensional data in a flexible and organized way. Here's an overview of how to nest lists and dictionaries in Python:

### Nesting Lists:

#### Creating a Nested List:

# You can create a nested list by placing one or more lists inside another list, essentially creating a list of lists.

# **Example**:


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# In this example, `matrix` is a nested list containing three inner lists, each representing a row of values.

#### Accessing Elements:

# To access elements in a nested list, you use multiple sets of square brackets to specify the indices at each level of nesting.

# **Example**:


element = matrix[0][1]  # Accessing the element at row 0, column 1 (value: 2)


#### Modifying Nested Lists:

# Nested lists are mutable, which means you can change their contents.

# **Example**:


matrix[1][2] = 99  # Modifying an element (changing 6 to 99)


#### Iterating Through Nested Lists:

# You can use nested loops to iterate through the elements of a nested list.

# **Example**:


for row in matrix:
    for element in row:
        print(element)


# This code will print all elements of the nested list one by one.

###                                                 Nesting Dictionaries:

#### Creating a Nested Dictionary:

# You can nest dictionaries by placing one or more dictionaries inside another dictionary, creating a dictionary of dictionaries.

# **Example**:


student = {
    "name": "Alice",
    "age": 20,
    "courses": {
        "math": 95,
        "history": 88,
        "programming": 92
    }
}


# In this example, the `student` dictionary contains a nested dictionary under the "courses" key, representing course grades.

#### Accessing Values:

# To access values in a nested dictionary, you use keys to navigate through the hierarchy.

# **Example**:


math_grade = student["courses"]["math"]  # Accessing the math grade (value: 95)


#### Modifying Nested Dictionaries:

# You can modify values in a nested dictionary by using the appropriate keys.

# **Example**:


student["courses"]["programming"] = 95  # Modifying the programming grade


#### Iterating Through Nested Dictionaries:

# To iterate through the keys and values of a nested dictionary, you can use nested loops.

# **Example**:


for subject, grade in student["courses"].items():
    print(f"Subject: {subject}, Grade: {grade}")


# This code will print each subject and its corresponding grade from the nested dictionary.

# Nesting lists and dictionaries is a fundamental technique in Python for representing complex and structured data. It's commonly used in scenarios like working with tables, hierarchical data, JSON data, and more. Understanding how to create, access, modify, and iterate through nested data structures is essential for handling diverse data in your Python programs.