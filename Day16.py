## Object-Oriented Programming (OOP) in Python

# Object-Oriented Programming (OOP) is a programming paradigm that uses objects to structure and organize code. In Python, OOP is a fundamental concept, and the language provides robust support for defining and working with objects. Here's a comprehensive section on OOP in Python:

### **1. Objects and Classes**:

# - **Objects**: In Python, everything is an object. An object is a self-contained unit that bundles both data (attributes) and functions (methods) that operate on the data.

# - **Classes**: A class is a blueprint or template for creating objects. It defines the structure and behavior of objects. You can think of a class as a factory that produces objects with specific characteristics.

# **Example**:


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"


# In this example, `Dog` is a class, and `name` and `breed` are attributes. `bark` is a method.

### **2. Instantiation**:

# - **Instantiation**: To create an object from a class, you instantiate it by calling the class constructor (typically `__init__` method) with specific arguments.

# **Example**:


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "Husky")


# Here, `dog1` and `dog2` are two distinct instances of the `Dog` class.

### **3. Attributes and Methods**:

# - **Attributes**: Attributes are variables that store data within an object. They represent the object's state.

# - **Methods**: Methods are functions defined within a class that operate on the object's attributes and perform actions associated with the object.

# **Example**:


print(dog1.name)  # Accessing the 'name' attribute
print(dog2.bark())  # Calling the 'bark' method


### **4. Encapsulation**:

# - **Encapsulation**: OOP promotes encapsulation, which means bundling data and methods together within a class and hiding the internal details from outside access. In Python, encapsulation is achieved through access modifiers like private (denoted by a single underscore `_`) and protected (denoted by a double underscore `__`) attributes.

# **Example**:


class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number  # Protected attribute

    def get_account_info(self):
        return f"Account Number: {self._account_number}"


### **5. Inheritance**:

# - **Inheritance**: Inheritance allows you to create a new class (subclass or derived class) that inherits attributes and methods from an existing class (superclass or base class). It promotes code reuse and specialization.

# **Example**:


class Cat(Dog):  # Cat inherits from Dog
    def purr(self):
        return "Purr!"


### **6. Polymorphism**:

# - **Polymorphism**: Polymorphism is the ability of different classes to be treated as instances of a common base class. It allows objects of different classes to be used interchangeably when they share a common interface.

# **Example**:


def animal_sound(animal):
    return animal.bark()  # Works for both Dog and Cat objects

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

print(animal_sound(dog))  # Woof!
print(animal_sound(cat))  # Purr!


### **7. Composition and Aggregation**:

# - **Composition**: Composition is a design principle where complex objects are created by combining simpler objects as attributes.

# - **Aggregation**: Aggregation is a form of composition where objects represent a "has-a" relationship with other objects.

# **Example**:


class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return f"Driving with {self.engine.start()}"


# Here, a `Car` is composed of an `Engine`.

### **8. Object-Oriented Principles**:

# - OOP principles, including encapsulation, inheritance, and polymorphism, help create clean, modular, and maintainable code. They are the foundation of designing robust and flexible software systems.

