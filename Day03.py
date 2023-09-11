# If - else - elseif Conditions

## Conditional Statements in Python (if-else)

# Conditional statements in Python allow you to make decisions in your code based on certain conditions. The `if` and `else` statements are fundamental for controlling the flow of your program.

# The `if` Statement

# The `if` statement is used to execute a block of code if a specified condition is `True`.

# Example:
age = 20

if age >= 18:
    print("You are eligible to vote.")

# In this example, the code inside the `if` block will only execute if the condition `age >= 18` is `True`.

# The `else` Statement

# The `else` statement is used to execute a block of code if the condition in the `if` statement is `False`.

# Example:


age = 15

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# Here, if the condition `age >= 18` is `False`, the code inside the `else` block will execute.

# The `elif` Statement

# The `elif` (short for "else if") statement is used to check multiple conditions one by one.

# Example:

score = 85

if score >= 90:
    print("You got an A grade.")
elif score >= 80:
    print("You got a B grade.")
elif score >= 70:
    print("You got a C grade.")
else:
    print("You got an F grade.")





## Nested Conditional Statements in Python (if-else)

# You can nest `if` and `if-else` statements to handle complex conditions in Python.

# Example:


x = 10
y = 5

if x > 5:
    if y > 2:
        print("Both conditions are met.")
    else:
        print("Inner condition not met.")
else:
    print("Outer condition not met.")


# In this example, nested `if` statements are used to check conditions step by step.


age = 20

if age >= 18:
    if age >= 21:
        print("You can vote and drink.")
    else:
        print("You can vote but not drink.")
else:
    print("You cannot vote or drink.")


# Nested conditional statements help you manage intricate logic in your code.





## Multiple `if` Statements in Succession

# In Python, you can use multiple `if` statements in succession to evaluate multiple conditions independently. Each `if` statement is checked regardless of the outcomes of the others.

# Example:

x = 10

if x > 5:
    print("x is greater than 5.")

if x < 15:
    print("x is less than 15.")

if x == 10:
    print("x is equal to 10.")


# In this example, three `if` statements are used one after the other. Each statement independently checks a condition, and if the condition is `True`, the associated code block is executed. All three messages will be printed because all three conditions are `True` for `x` in this case.

# Multiple `if` statements in succession are useful when you want to perform separate actions based on various conditions without any mutual exclusion. Each `if` statement acts independently of the others, and multiple blocks of code can execute if their respective conditions are met.




## Logical Operators in Python

# Logical operators in Python are used to perform logical operations on one or more Boolean values (True or False). Python provides three main logical operators: `and`, `or`, and `not`.

### 1. `and` Operator

# The `and` operator returns `True` if both operands are `True`; otherwise, it returns `False`.

# Example:


x = True
y = False

result = x and y  # result is False


# In this example, `result` is `False` because both `x` and `y` are not `True`.

### 2. `or` Operator

# The `or` operator returns `True` if at least one of the operands is `True`; it returns `False` only if both operands are `False`.

# **Example**:


a = True
b = False

result = a or b  # result is True


# In this example, `result` is `True` because `a` is `True`, even though `b` is `False`.

### 3. `not` Operator

# The `not` operator returns the opposite Boolean value of the operand. If the operand is `True`, `not` makes it `False`, and vice versa.

# Example:

flag = True

result = not flag  # result is False


# In this example, `result` is `False` because `not` negates the value of `flag`.

# Logical operators are commonly used in conditional statements (`if`, `elif`, `else`) to make decisions based on multiple conditions. They allow you to create complex conditions by combining multiple Boolean values.