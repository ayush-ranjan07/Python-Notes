#                                                           Creating Your Own Class in Python

### 1. **Class Definition**

# - Python uses the `class` keyword to define a class, which serves as a blueprint for creating objects.
# - It is conventional to start class names with a capital letter.


class MyClass:
    pass  # Acts as a placeholder for the class body


### 2. **Attributes and Data**

# - Attributes are variables that store data within an object.
# - You define attributes within a class to represent the state of an object.


class Person:
    def __init__(self, name, age):
        self.name = name  # 'name' is an attribute
        self.age = age    # 'age' is an attribute


# - The `__init__` method is a special constructor used to initialize object attributes.
# - `self` refers to the instance being created, and additional parameters set attribute values during object instantiation.


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)


### 3. **Methods**

# - Methods are functions defined within a class that encapsulate an object's behavior.
# - They operate on the object's attributes and define how the object interacts with the outside world.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


### 4. **Working with Instances**

# - Instances represent individual objects created from a class.
# - Create instances to work with objects and access their attributes and methods.


# Creating instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

# Calling methods
rectangle = Rectangle(5, 4)
area = rectangle.calculate_area()
print(area)  # Output: 20


### 5. **Encapsulation**

# - Encapsulation is a core OOP concept that involves bundling data (attributes) and the methods that operate on that data within a class.
# - Python uses naming conventions to indicate attribute visibility:
#   - A single underscore `_` suggests an attribute is protected (intended for internal use).
#   - A double underscore `__` indicates an attribute is private.

### 6. **Inheritance**

# - Inheritance allows you to create a new class (subclass) that inherits attributes and methods from an existing class (superclass).
# - Subclasses can extend or override superclass functionality.


class Animal:
    def speak(self):
        pass  # A generic animal doesn't have a specific sound

class Dog(Animal):
    def speak(self):
        return "Woof!"


### 7. **Polymorphism**

# - Polymorphism enables objects of different classes to be treated as instances of a common base class.
# - This promotes flexibility and dynamic behavior in your code.


def make_speak(animal):
    return animal.speak()  # Works for both Animal and Dog objects

generic_animal = Animal()
dog = Dog()

print(make_speak(generic_animal))  # None (generic animals don't have a specific sound)
print(make_speak(dog))             # Woof!


### 8. **Composition and Aggregation**

# - Composition involves creating complex objects by combining simpler objects as attributes.
# - Aggregation represents a "has-a" relationship between objects.
# - These principles contribute to building more sophisticated and modular software.


class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return f"Driving with {self.engine.start()}"

