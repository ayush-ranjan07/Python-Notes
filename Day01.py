# Below 3 lines are used to print  

print("Day 1 - Python Print Function")
print("The Functions is declared like this:")
print("print('what to print')")   


# Below line takes name as input with the the help of input() function
# and prints the length of the name with the help of len() function
print(len(input("What is your name?")))


# Below line takes name as input with the the help of input() function
# and stores in a variable name and then length of the name is calculated with the help of len() function and stored in length variable
# and then length is printed
name=input("What is your name")
length=len(name)
print(length)


#Program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

temp=a
a=b
b=temp

print("a: " + a)
print("b: " + b)


# Here are the key rules for naming variables in Python:

# 1. Valid Characters: Variable names can include letters (both uppercase and lowercase), digits, and underscores. They must start with a letter (a-z, A-Z) or an underscore (_).

# 2. Case Sensitivity: Python is case-sensitive, so variable names with different letter cases are considered distinct. For example, myVariable and myvariable are treated as different variables.

# 3. Reserved Keywords: You cannot use reserved keywords as variable names. Keywords are predefined words in Python that have special meanings and purposes. Examples of reserved keywords include if, while, for, class, and import. Attempting to use a reserved keyword as a variable name will result in a syntax error.

# 4. Whitespace: Variable names cannot contain spaces or other whitespace characters. If you need to represent multiple words in a variable name, you can use underscores (e.g., my_variable_name) or follow the convention of writing words together in camelCase (e.g., myVariableName) or with underscores (e.g., my_variable_name).

# 5. Cannot Start with a Digit: Variable names cannot start with a digit (0-9). They must begin with a letter or an underscore.

# Naming Conventions:

# It's a convention in Python to use lowercase letters for variable names (e.g., my_variable).
# For constants, it's common to use all uppercase letters with underscores (e.g., PI, MAX_VALUE).
# For class names, use CamelCase, also known as PascalCase, where each word starts with an uppercase letter (e.g., MyClass, PersonInfo).
# Avoid using single-character variable names unless they represent simple loop counters (e.g., i, j, k).
# Descriptive and Meaningful: Choose variable names that are descriptive and convey the purpose or content of the variable. This makes your code more readable and understandable.