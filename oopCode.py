# #class

# class Vehicle:
#     # contructor initialize veriables
#     def __init__(self, brand, model, prize):
#         self.brand = brand #veriables
#         self.model = model
#         #Encapsulation means bundling attributes and methods into one unit (class) and restricting direct access to some data.
#         self.__prize = prize # private variable

#     # function / method
#     def start(self):
#         print(f"{self.brand} {self.model} is starting and sound like rearing beast")

#     # when you have to access private veriables
#     def get_prize(self):
#         return self.__prize

# #class with inherites property of anather calss
# class Car(Vehicle):
#     def __init__(self, brand, model, prize,seats):
#         super().__init__(brand, model, prize)# veriables from super class or parent class
#         self.seats =  seats
# # Polymorphism allows objects of different classes to be treated as objects of a common base class. 
#     def start(self):
#         # Use the getter method to access the private attribute `__prize`
#         prize = self.get_prize()
#         print(f"{self.brand} {self.model} is starting and sound like rearing beast but it has only {self.seats} seats. A prize is {prize} million doller!!")

# #object of class 
# my_vehicle = Vehicle('ford','mastang', 1)

# my_car = Car('W-moters','lykan Hyper sports',3.6, 2)

# #calls the function or method

# my_vehicle.start()
# my_car.start()
        
#=============================================================================================================
# Basic Concepts: Classes and Objects
#     1. Create a Car class with attributes like make, model, and year. Instantiate a few objects.
# class Car:
#     model = "Lykan Hyper Sports"
#     year = 2017

# my_car = Car()
# print(f"{my_car.model} is my fevirate car made in year {my_car.year}")
#=============================================================================================================

#     2. Write a Dog class with a bark method. Call the method from an instance.
# class Dog:
#     name = "tommy"

#     def bark(self):
#         print(f"{self.name} is good dag")


# my_dog = Dog()
# my_dog.bark()
#=============================================================================================================

#     3. Create a Person class with attributes name and age. Add a method to display a greeting message.

# class Person:
#     name = "ashwajit"
#     age =27

#     def messege(self):
#         print(f"Hello {self.name} of age {self.age} Happy Birthday !")

# my_info = Person()
# my_info.messege()
#=============================================================================================================

#     4. How do you initialize attributes using the __init__ method? Write an example.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# name = str(input("Enter Name :- "))
# age = int(input("Enter Age:- "))
# my_info = Person(name,  age)

# print(f"Hello {my_info.name} We wish you happy {my_info.age}th birthaday to you!")

#=============================================================================================================

#     5. What happens if you forget to include self in a method definition?
# class Car:
#     name = "Ashwajit"

#     def my_info(name):
#         print(f"my name is {name}")

# my_name = Car()
# Car.my_info()

# TypeError: greet() takes 0 positional arguments but 1 was given {this error message will accur}
#=============================================================================================================

#     6. What is the difference between a class variable and an instance variable? Demonstrate with code.

#explanation :-- class variable is define  after class get created and by normal way like in following code but in intance variable 
# can be created in constructer methed
# class Car:
#     # class veriables
#     model  = "Lykan Hyper sport"
#     def __init__(self, brand):
#         self.brand = brand # instance variables

# my_car = Car('w moters')
# print(f"{my_car.brand}'s {my_car.model}")

#=============================================================================================================

# Inheritance
#     7. Create a Vehicle class and derive Car and Bike classes from it.

# class Vehicle:

#     def __init__(self, model):
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, model, brand):
#         super().__init__(model)
#         self.brand = brand

# class Bike(Car):
#     def __init__(self, model, brand, engine):
#         super().__init__(model, brand)
#         self.engine = engine

# my_vehicle = Vehicle('BMW')
# my_car = Car('BMW', 'GT')
# my_bike = Bike('BMW', 'RR 310', 'v-2')


# print(f"{my_vehicle.model}")
# print(f"{my_car.model}'s {my_car.brand}")
# print(f"{my_bike.model}'s {my_bike.brand} with {my_bike.engine} engine")


        
#=============================================================================================================

#     8. Add a method describe() in the Vehicle class and override it in the Car and Bike subclasses.

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def describe(self):
#         return f"{self.brand} is a vehicle."

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def describe(self):
#         return f"{self.brand}'s {self.model} is a car."

# class Bike(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def describe(self):
#         return f"{self.brand}'s {self.model} is a bike."

# # Create instances of Car and Bike
# my_car = Car("BMW", "GT")
# my_bike = Bike("TVS", "RR 310")

# # Call describe methods and print the output
# print(my_car.describe())
# print(my_bike.describe())


#=============================================================================================================

#     9. Implement a multi-level inheritance example with three levels of classes.

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"{self.name} is an animal."

# class Mammal(Animal):class Animal:
#     def __init__(self, name):
#         self.name = name

#     def describe(self):
#         return f"{self.name} is an animal."

# class Mammal(Animal):
#     def __init__(self, name, is_warm_blooded=True):
#         super().__init__(name)
#         self.is_warm_blooded = is_warm_blooded

#     def describe(self):
#         return f"{self.name} is a mammal and {'is' if self.is_warm_blooded else 'is not'} warm-blooded."

# class Dog(Mammal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def describe(self):
#         return f"{self.name} is a {self.breed} dog, which is a mammal and warm-blooded."

# # Create an instance of each class
# animal = Animal("Generic Animal")
# mammal = Mammal("Generic Mammal")
# dog = Dog("Buddy", "Golden Retriever")

# # Call the describe method for each object
# print(animal.describe())
# print(mammal.describe())
# print(dog.describe())

#     def __init__(self, name, is_warm_blooded=True):
#         super().__init__(name)
#         self.is_warm_blooded = is_warm_blooded

#     def describe(self):
#         return f"{self.name} is a mammal and {'is' if self.is_warm_blooded else 'is not'} warm-blooded."

# class Dog(Mammal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def describe(self):
#         return f"{self.name} is a {self.breed} dog, which is a mammal and warm-blooded."

# # Create an instance of each class
# animal = Animal("Generic Animal")
# mammal = Mammal("Generic Mammal")
# dog = Dog("Buddy", "Golden Retriever")

# # Call the describe method for each object
# print(animal.describe())
# print(mammal.describe())
# print(dog.describe())

#=============================================================================================================

#     10. How do you use super() in Python? Write an example.
# explanation:--The super() function in Python is used to call methods from a parent (or superclass) class. 
# #It is particularly useful in the context of inheritance, where a subclass wants to extend or customize behavior from 
#its parent class while still reusing its methods.

# class Vehicle:

#     def __init__(self, model):
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, model, brand):
#         super().__init__(model)
#         self.brand = brand

#my_car = Car("BMW", "GT")

#=============================================================================================================

# 11. Create a base class Animal and derived classes Dog and Cat. Add behaviors specific to each subclass.

# class Aminal:
#     def __init__(self, name):
#         self.name = name

# class Cat(Aminal):
#     def __init__(self, name, sound):
#         super().__init__(name)
#         self.sound = sound

#     def behavior(self):
#         print(f"{self.name} is my pet and make sound like {self.sound}")

# class Dog(Aminal):
#     def __init__(self, name, sound):
#         super().__init__(name)
#         self.sound = sound

#     def behavior(self):
#         print(f"{self.name} is my pet and make sound like {self.sound}")

# my_cat = Cat("kitty", "meowwww")
# my_dog = Dog("tommy","bhauuuuuu")

# my_cat.behavior()
# my_dog.behavior()
#=============================================================================================================

# Polymorphism
#  12. What is polymorphism? Write a Python program to demonstrate it with different classes.
   #     Polymorphism allows objects of different classes to be treated as objects of a common base class.
   #     It’s useful for overriding methods.

# class Bird:
#     def sound(self):
#         print(f"make a sound")

# class Duck:
#     def sound(self):
#         print(f"make a sound like quack! quack!")

# my_bird = Bird()
# my_duck = Duck()

# my_bird.sound()
# my_duck.sound()

#=============================================================================================================

#     13. Create a Shape class and subclasses like Circle and Rectangle. Add a method area() to calculate their areas.

# class Shape:
#     def area(self):
#         raise NotImplementedError("The area method must be implemented by subclasses.")

# class Circle(Shape):
#     def __init__(self, redius):
#         super().__init__()
#         self.redius = redius

#     def area(self):
#         return 3.147 * self.redius **2

# class Rectangle(Shape):
#     def __init__(self,length,height):
#         super().__init__()
#         self.length = length
#         self.height = height

#     def area(self):
#         return self.height*self.length

# area_circle = Circle(10)
# area_rectangle = Rectangle(10,12)

# print(f"Area of circle is {area_circle.area()}")
# print(f"Area of rectangle is {area_rectangle.area()}")

#=============================================================================================================

#  14. Write a function that takes objects of different classes and calls a common method (e.g., speak()).
# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# class Bird:
#     def speak(self):
#         return "Chirp!"

# def speak(animals):
#     for ani in animals:
#         print(f"{ani.speak()}")

# dog = Dog()
# cat = Cat()
# bird = Bird()

# animals = [dog, cat, bird]
# speak(animals)

#=============================================================================================================

#     15. How is polymorphism implemented using method overriding?
# Polymorphism using method overriding allows a subclass to provide a specific implementation 
# of a method that is already defined in its parent class. 
# The method in the subclass "overrides" the method in the parent class, 
# enabling objects of different subclasses to respond differently to the same method call.

# class Animal:
#     def speak(self):
#         return "I am an animal."

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# def animal_sounds(animal):
#     print(animal.speak())

# # Example usage
# dog = Dog()
# cat = Cat()
# generic_animal = Animal()

# animal_sounds(dog)           # Outputs: Woof!
# animal_sounds(cat)           # Outputs: Meow!
# animal_sounds(generic_animal) # Outputs: I am an animal.

#=============================================================================================================

#     16. Demonstrate polymorphism with a list of objects from different classes.
# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# class Cow:
#     def speak(self):
#         return "Moo!"

# class Bird:
#     def speak(self):
#         return "Chirp!"

# def sound(animals):
#     for i in animals:
#         print(i.speak())


# animals = [Dog(),Cat(), Cow(), Bird()]
# sound(animals)
#=============================================================================================================

# Encapsulation
#     17. What is encapsulation in Python? Explain with an example.
# encapsulation is the practice of restricting access to certain parts of an object’s data or behavior 
# to ensure that an object’s internal representation is hidden from the outside.

# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name  # Public veriables
#         self._department = department  # Protected veriables
#         self.__salary = salary  # Private veriables

#     # Public method to display employee details
#     def display_details(self):
#         print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

#     # Protected method: Should be used by the class or subclasses
#     def _change_department(self, new_department):
#         self._department = new_department
#         print(f"{self.name}'s department changed to {self._department}.")

#     # Private method: Can only be used within the class
#     def __update_salary(self, new_salary):
#         if new_salary > 0:
#             self.__salary = new_salary
#             print(f"Salary updated to ${self.__salary}.")
#         else:
#             print("Invalid salary amount.")

#     # Public method to allow controlled access to the private method
#     def update_salary(self, new_salary):
#         self.__update_salary(new_salary)


# # Subclass to demonstrate access to protected attributes and methods
# class Manager(Employee):
#     def promote_employee(self):
#         print(f"{self.name} is promoted within the {self._department} department.")


# # Example usage
# emp = Employee("John Doe", 50000, "Engineering")

# # Accessing public attribute
# print(emp.name)  # Output: John Doe

# # Accessing public method
# emp.display_details()  # Output: Name: John Doe, Department: Engineering, Salary: 50000

# # Accessing protected attribute (not recommended, but allowed)
# print(emp._department)  # Output: Engineering

# # Using protected method
# emp._change_department("Research and Development")  # Allowed, but should be avoided in practice

# # Accessing private attribute directly (will raise an error)
# # print(emp.__salary)  # AttributeError

# # Accessing private attribute through a public method
# emp.update_salary(60000)  # Safely updates the salary

# # Accessing private method directly (will raise an error)
# # emp.__update_salary(70000)  # AttributeError

# # Using name mangling to access private attributes/methods (not recommended)
# print(emp._Employee__salary)  # Output: 60000

# # Demonstrating protected access in a subclass
# manager = Manager("Alice Smith", 80000, "Marketing")
# manager.promote_employee()  # Output: Alice Smith is promoted within the Marketing department.

#=============================================================================================================

#     18. Create a BankAccount class with private attributes balance and account_number.
# class BankAccount:
#     def __init__(self, balance, account_number):
#         self.__balance = balance
#         self.__account_number = account_number

#     def get_account_num(self):
#         return self.__account_number

#     def get_balence(self):
#         return self.__balance

# account = BankAccount(1000, "123456789")
# print(f"Account Number: {account.get_account_num()}")
# print(f"Balance: ${account.get_balence()}")


#=============================================================================================================

#     19. Add getter and setter methods to access and modify private attributes.
# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         # Private attributes
#         self.__account_number = account_number
#         self.__balance = initial_balance

#     # Public method to get the account number
#     def get_account_number(self):
#         return self.__account_number

#     # Public method to get the balance
#     def get_balance(self):
#         return self.__balance

# account = BankAccount("123456789", 1000)
# # Accessing private attributes via getters
# print(f"Account Number: {account.get_account_number()}")
# print(f"Balance: ${account.get_balance()}")
# # Modifying private attributes via setters
# account.get_account_number("987654321")
# account.get_balance(1500)

#=============================================================================================================

#     20. How does Python implement access control (public, private, protected)? Demonstclass AccessControlExample:
# class AccessControlExample:
#     def __init__(self):
#         self.public_attr = "I am public!"  # Public attribute
#         self._protected_attr = "I am protected!"  # Protected attribute
#         self.__private_attr = "I am private!"  # Private attribute

#     # Public method
#     def public_method(self):
#         print("This is a public method.")

#     # Protected method
#     def _protected_method(self):
#         print("This is a protected method.")

#     # Private method
#     def __private_method(self):
#         print("This is a private method.")

#     # Method to access private attributes and methods internally
#     def access_private(self):
#         print(f"Accessing private attribute internally: {self.__private_attr}")
#         self.__private_method()


# # Example usage
# obj = AccessControlExample()

# # Accessing public attribute and method
# print(obj.public_attr)  # Output: I am public!
# obj.public_method()  # Output: This is a public method.

# # Accessing protected attribute and method (allowed, but not recommended)
# print(obj._protected_attr)  # Output: I am protected!
# obj._protected_method()  # Output: This is a protected method.

# # Attempting to access private attribute and method directly (not allowed)
# # print(obj.__private_attr)  # AttributeError
# # obj.__private_method()  # AttributeError

# # Accessing private attributes and methods using a public method
# obj.access_private()
# # Output:
# # Accessing private attribute internally: I am private!
# # This is a private method.

# # Accessing private attribute using name mangling (not recommended)
# print(obj._AccessControlExample__private_attr)  # Output: I am private!
# obj._AccessControlExample__private_method()  # Output: This is a private method.


#=============================================================================================================

#     21. Write an example showing how to use name mangling to access private attributes.
# class Example:
#     def __init__(self):
#         self.__private_attr = "I am private!"

#     # Private method
#     def __private_method(self):
#         print("This is a private method.")

# # Create an instance of the class
# obj = Example()

# # Attempting to access the private attribute and method directly (will raise an AttributeError)
# # print(obj.__private_attr)  # AttributeError
# # obj.__private_method()  # AttributeError

# # Using name mangling to access the private attribute and method
# print(obj._Example__private_attr)  # Output: I am private!
# obj._Example__private_method()  # Output: This is a private method.

#=============================================================================================================

# Abstraction
#     22. What is abstraction? How is it implemented in Python?
# Abstraction is a fundamental concept in object-oriented programming (OOP) that involves hiding 
# the complex implementation details and showing only the essential features of an object or system.
# In simple terms, abstraction allows the programmer to focus on what an object does instead 
# of how it does it.

# from abc import ABC, abstractmethod

# # Abstract class
# class Animal(ABC):

#     # Abstract method
#     @abstractmethod
#     def make_sound(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass

# # Subclass implementing abstract methods
# class Dog(Animal):

#     def make_sound(self):
#         return "Woof!"

#     def move(self):
#         return "The dog runs."

# # Subclass implementing abstract methods
# class Cat(Animal):

#     def make_sound(self):
#         return "Meow!"

#     def move(self):
#         return "The cat jumps."

# # Instantiate subclasses
# dog = Dog()
# cat = Cat()

# print(dog.make_sound())  # Output: Woof!
# print(cat.move())        # Output: The cat jumps.

#=============================================================================================================
#     23. Create an abstract class Animal with an abstract method speak(). Implement it in subclasses.
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "barks!!"

# dog = Dog()
# print(dog.speak())

#=============================================================================================================

#     24. Write a program using the abc module to define abstract methods.
# from abc import ABC, abstractmethod

# # Abstract class Vehicle
# class Vehicle(ABC):

#     @abstractmethod
#     def start_engine(self):
#         pass

# # Subclass Car that implements the abstract method
# class Car(Vehicle):

#     def start_engine(self):
#         return "Car engine started!"

# # Create an instance of Car
# car = Car()
# print(car.start_engine())  # Output: Car engine started!

#=============================================================================================================

#     25. Why can’t we instantiate an abstract class? Explain with an example.
# Abstract methods: An abstract class can have methods that are declared but not implemented. 
# If we try to instantiate an abstract class, Python would not know how to execute those abstract methods.
# Purpose of abstract classes: They are intended to be inherited by other classes that will implement the abstract methods. 
# Therefore, instantiating an abstract class would contradict this design pattern 
# because it would lack the required method implementations.

# from abc import ABC, abstractmethod

# # Abstract class with an abstract method
# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# # Attempting to instantiate the abstract class will raise an error
# animal = Animal()  # This will raise an error

#=============================================================================================================
#26. Implement a simple Payment system with CreditCardPayment and PayPalPayment as subclasses.
# from abc import ABC, abstractmethod

# # Abstract base class Payment
# class Payment(ABC):

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

# # CreditCardPayment subclass
# class CreditCardPayment(Payment):

#     def __init__(self, card_number):
#         self.card_number = card_number

#     def process_payment(self, amount):
#         # Simulate processing a credit card payment
#         return f"Processed payment of ${amount} using Credit Card ending in {self.card_number[-4:]}"

# # PayPalPayment subclass
# class PayPalPayment(Payment):

#     def __init__(self, email):
#         self.email = email

#     def process_payment(self, amount):
#         # Simulate processing a PayPal payment
#         return f"Processed payment of ${amount} using PayPal account {self.email}"

# # Testing the payment system
# def process_customer_payment(payment_method, amount):
#     print(payment_method.process_payment(amount))

# # Create instances of CreditCardPayment and PayPalPayment
# credit_card_payment = CreditCardPayment("1234-5678-9876-5432")
# paypal_payment = PayPalPayment("customer@example.com")

# # Process payments
# process_customer_payment(credit_card_payment, 100)  # $100 via Credit Card
# process_customer_payment(paypal_payment, 50)         # $50 via PayPal
#=============================================================================================================

# Constructors and Destructors
#     27. What is the purpose of the __init__ method in Python?
# The __init__ method in Python is a special method (also known as a constructor) used to 
# initialize an instance of a class. Its primary purpose is to set up the initial state of 
# the object by assigning values to instance attributes or 
# performing other setup tasks when the object is created.
# class Person:
#    def __init__(self, name):
#       self.name = name

# obj = Person("Ashwajit")
# print(f"Hello {obj.name} WELCOME ")
#=============================================================================================================

#     28. Write a class with a constructor that initializes attributes based on user input.
# class Person:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def info(self):
#       print(f"Hello {self.name} you are only {self.age} and youngest king of the pirate!")

# name = str(input("Enter Name"))
# age = str(input("Enter Age"))
# my_info = Person(name, age)
# my_info.info()


#=============================================================================================================

#     29. Demonstrate the use of destructors (__del__) in Python.
# the __del__ method is a special method called a destructor. It is used to define cleanup behavior 
# for an object before it is destroyed 
# (e.g., when it goes out of scope or is explicitly deleted using del).

# class FileHandler:
#    def __init__(self, filename):
#       self.filename = filename
#       self.file = open(filename, 'w')#open file to write
#       print(f"file {self.filename} opend !")

#    def writeData(self, data):
#       self.file.write(data)
#       print(f"data writen to {self.filename}")

#    def __del__(self):
#       if self.file:
#          self.file.close()
#          print(f"file {self.filename} closed successfully!")

# my_file = FileHandler("example.txt")
# my_file.writeData("My Name is uptimus prime!")
#=============================================================================================================

#     30. What happens if you don’t define a constructor in a class?
# If you don’t define a constructor (__init__ method) in a Python class, the class will use a default 
# constructor provided by Python. This default constructor doesn’t perform any custom 
# initialization but still allows you to create objects of the class.

# class Car:
#    pass

# my_car = Car()
# my_car.name = "Ace"
# print(my_car.name)
#=============================================================================================================

#     31. Can a class have multiple constructors? If yes, how can it be implemented?
#=============================================================================================================

# Static and Class Methods
#     32. What is a static method? How is it defined in Python?
# A static method in Python is a method that belongs to a class 
# rather than an instance of the class. It does not operate on an instance or 
# class-level attributes but serves as a utility function that logically belongs to the class. 
# Static methods are defined using the @staticmethod decorator.

# class Car:
#     @staticmethod
#     def info(self):
#         pass

#=============================================================================================================

#     33. Write a class with both static and instance methods.
# class Car:
#    @staticmethod
#    def info(): #static method
#         pass
   
#    def my_info(self):#instance method
#        pass 
   
    
#=============================================================================================================

#     34. How do class methods differ from static methods? Demonstrate with examples.
# Use class methods when you need to interact with or modify class-level attributes.
# Use static methods for utility functions that don't depend on the class or instance.
# class MyExample:
#     class_counter = 0  # Class-level attribute

#     @classmethod
#     def increment_counter(cls):
#         cls.class_counter += 1
#         print(f"Class counter incremented to: {cls.class_counter}")

#     @staticmethod
#     def greet(name):
#         return f"Hello, {name}! This is a static method."

# # Call class and static methods
# MyExample.increment_counter()  # Output: Class counter incremented to: 1
# MyExample.increment_counter()  # Output: Class counter incremented to: 2

# print(MyExample.greet("Alice"))  # Output: Hello, Alice! This is a static method.

#=============================================================================================================

#     35. Create a class with a class method that returns the number of objects created.
# class ObjectCounter:
#     # Class-level attribute to track the number of objects
#     object_count = 0

#     def __init__(self):
#         # Increment the object count whenever a new object is created
#         ObjectCounter.object_count += 1

#     @classmethod
#     def get_object_count(cls):
#         # Class method to return the current object count
#         return f"Number of objects created: {cls.object_count}"

# # Create objects of the class
# obj1 = ObjectCounter()
# obj2 = ObjectCounter()
# obj3 = ObjectCounter()

# # Call the class method to get the count
# print(ObjectCounter.get_object_count())  # Output: Number of objects created: 3

# # You can also call it using an instance
# print(obj1.get_object_count())           # Output: Number of objects created: 3

#=============================================================================================================

# Special Methods (Dunder Methods)
# Complete List of Dunder Methods
# Construction: __new__, __init__, __del__
# Representation: __str__, __repr__, __format__
# Arithmetic: __add__, __sub__, __mul__, __truediv__, etc.
# Comparison: __eq__, __lt__, __le__, etc.
# Container: __len__, __getitem__, __setitem__, etc.
# Callable: __call__
# Context Managers: __enter__, __exit__

#     36. What are dunder methods? List some commonly used ones.

# Dunder methods (short for double underscore methods) are special methods in Python 
# that have double underscores (__) at the beginning and end of their names. 
# They are also known as magic methods or special methods.

# These methods are predefined by Python and allow developers to define the behavior of 
# custom objects for built-in operations such as arithmetic, comparisons, and type casting. 
# For example, __init__ initializes an object, and __str__ defines how the object is represented 
# as a string.

# class Example:
#    def __init__(self, name):#Called when an object is created (constructor).
#         self.name = name

#    def __str__(self):
#     return f"Example(name={self.name})"#Defines the string representation of an object (used by str() and print()).
   
#    def __repr__(self):
#     return f"Example({self.name!r})"#Defines the official string representation of an object (used by repr() or in debugging).



#=============================================================================================================

#     37. Override the __str__ method in a class to customize the string representation of an object.
# class Person:
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     def __str__(self):
#         # Customize the string representation
#         return f"Person(name={self.name}, age={self.age}, occupation={self.occupation})"

# # Create an instance of the class
# person = Person("Alice", 30, "Software Engineer")

# # Print the object
# print(person)  # Output: Person(name=Alice, age=30, occupation=Software Engineer)

#=============================================================================================================

#     38. Implement the __add__ method to add two objects of a class.

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         # Check if the other object is also a Point
#         if isinstance(other, Point):
#             # Add the x and y coordinates
#             return Point(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

# # Create two Point objects
# p1 = Point(2, 3)
# p2 = Point(4, 5)

# # Add the two Point objects using the + operator
# p3 = p1 + p2

# # Print the result
# print(p3)  # Output: Point(6, 8)

#=============================================================================================================

#     39. Write a program to compare objects using __eq__ and __lt__.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             # Two rectangles are equal if their areas are equal
#             return self.area() == other.area()
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             # A rectangle is less than another if its area is smaller
#             return self.area() < other.area()
#         return NotImplemented

#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"

# # Create rectangle objects
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(2, 10)
# rect3 = Rectangle(3, 6)

# # Compare rectangles using == and <
# print(f"rect1: {rect1}")
# print(f"rect2: {rect2}")
# print(f"rect3: {rect3}")

# print(f"rect1 == rect2: {rect1 == rect2}")  # Output: True (both have area 20)
# print(f"rect1 < rect3: {rect1 < rect3}")    # Output: False (rect1's area is greater than rect3's area)
# print(f"rect3 < rect2: {rect3 < rect2}")    # Output: True (rect3's area is smaller than rect2's area)

#=============================================================================================================

#     40. How do you define an iterable class using __iter__ and __next__?
# class MyRange:
#     def __init__(self, start, stop):
#         self.start = start  # Starting number
#         self.stop = stop    # End number (exclusive)
#         self.current = start  # To track the current number

#     # Implement __iter__ method (returns the iterator itself)
#     def __iter__(self):
#         return self

#     # Implement __next__ method (returns the next value in the sequence)
#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration  # Stop iteration when we reach the end
#         current_value = self.current
#         self.current += 1  # Move to the next number
#         return current_value

# # Example usage
# my_range = MyRange(1, 5)  # Range from 1 to 4

# for num in my_range:
#     print(num)

#=============================================================================================================

# Composition and Aggregation
#     41. What is the difference between composition and inheritance?

# ------------------|-----------------------------------------------------|-------------------------------
#  Aspect	        |                   Inheritance	                    |               Composition
# ------------------|-----------------------------------------------------|------------------------------
#                   |
#  Relationship	  | "is-a" relationship (e.g., Dog is an Animal)        |"has-a" relationship (e.g., Car has an Engine)
# ------------------|-----------------------------------------------------|----------------------
# Flexibility	     | Less flexible due to tight coupling between classes |More flexible, allows combining behaviors more easily
# ------------------|-----------------------------------------------------|-----------------------
# Reuse	Reuses     | functionality by extending a class	Reuses           |functionality by including objects as attributes
# ------------------|----------------------------------------------------------------------------
# Coupling	        |High coupling between parent and child classes	     |Low coupling between classes, promoting independence
# ------------------|-----------------------------------------------------|-----------------------
# Extensibility	  |Subclass can override or extend parent class methods |Objects can be composed and their behavior delegated
# ------------------|-----------------------------------------------------|-----------------------
# Example	        |Dog inherits from Animal	                          | Car contains an Engine and delegates starting to it
                  # class Animal:
                  #     def speak(self):
                  #         print("Animal speaks")

                  # class Dog(Animal):  # Dog inherits from Animal
                  #     def speak(self):
                  #         print("Woof!")

                  # dog = Dog()
                  # dog.speak()  # Output: Woof!
# ------------------------------------------------------
# class Engine:
#     def start(self):
#         print("Engine starts")

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Car has an Engine (composition)

#     def start(self):
#         self.engine.start()  # Delegating the starting task to the engine

# car = Car()
# car.start()  # Output: Engine starts


#=============================================================================================================

#     42. Create a Library class that contains Book objects using composition.
# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn

#     def __str__(self):
#         return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

# class Library:
#     def __init__(self):
#         self.books = []  # List to store Book objects

#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.books.append(book)
#         else:
#             print("Only Book objects can be added!")

#     def list_books(self):
#         if not self.books:
#             print("No books in the library.")
#         for book in self.books:
#             print(book)

# # Example usage
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
# book2 = Book("1984", "George Orwell", "9780451524935")
# book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print("Books in the library:")
# library.list_books()

#=============================================================================================================

#     43. Implement a Car class that has an Engine object using aggregation.
# class Engine:
#     def __init__(self, type_of_engine):
#         self.type_of_engine = type_of_engine

#     def start(self):
#         print(f"{self.type_of_engine} engine is starting...")

# class Car:
#     def __init__(self, make, engine):
#         self.make = make
#         self.engine = engine  # Car "has-a" Engine

#     def start(self):
#         print(f"{self.make} is starting...")
#         self.engine.start()  # Delegates the start to Engine

# # Example usage
# engine1 = Engine("V6")
# car1 = Car("Toyota", engine1)

# car1.start()  # Output: Toyota is starting... V6 engine is starting...

#=============================================================================================================

#     44. Write a program to demonstrate the “has-a” relationship.
# class Address:
#     def __init__(self, street, city, postal_code):
#         self.street = street
#         self.city = city
#         self.postal_code = postal_code

#     def __str__(self):
#         return f"{self.street}, {self.city}, {self.postal_code}"

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address  # "has-a" relationship: Person has an Address

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Address: {self.address}")

# # Example usage
# address1 = Address("123 Elm St", "Springfield", "12345")
# person1 = Person("John Doe", 30, address1)

# person1.display_info()

#=============================================================================================================

# Error Handling in OOP
#     45. How do you handle exceptions in an OOP context?
# exceptions can be handled using try-except blocks, just as in procedural programming, 
# but the difference lies in how exceptions are managed within the structure of the objects 
# and classes. Typically, you raise exceptions to indicate errors or unusual conditions, 
# and you catch them to handle those conditions appropriately.

# #    print("Transaction process completed.")
#=============================================================================================================

#     46. Create a class Calculator with methods for basic arithmetic. Add error handling for division by zero.
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             return "Error: Division by zero is not allowed."

# # Example usage
# calculator = Calculator()

# # Performing operations
# print("Addition: ", calculator.add(10, 5))
# print("Subtraction: ", calculator.subtract(10, 5))
# print("Multiplication: ", calculator.multiply(10, 5))
# print("Division (valid): ", calculator.divide(10, 5))
# print("Division (by zero): ", calculator.divide(10, 0))

#=============================================================================================================

#     47. Write a program that raises a custom exception in a class.

# class InvalidAgeError(Exception):
#     """Custom exception for invalid age."""
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)

#     def set_age(self, age):
#         if age < 0 or age > 120:
#             raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120.")
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Example usage
# try:
#     person1 = Person("Alice", 25)  # Valid age
#     person1.display_info()

#     person2 = Person("Bob", -5)  # Invalid age, raises InvalidAgeError
#     person2.display_info()
# except InvalidAgeError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

#=============================================================================================================


# Advanced OOP Concepts
#     48. What is metaprogramming in Python? Write a basic example using a metaclass.
# Metaprogramming refers to writing code that manipulates or generates other code. In Python,
# metaprogramming is often achieved using metaclasses, which allow you to customize class creation. 
# A metaclass is a "class of a class," meaning it defines how classes behave, 
# just as a class defines how its objects behave.

# Define a metaclass
# class CustomMeta(type):
#     def __new__(cls, name, bases, dct):
#         # Automatically add a 'greet' method to the class being created
#         dct['greet'] = lambda self: f"Hello, I am an instance of {name}."
#         return super().__new__(cls, name, bases, dct)

# # Use the metaclass in a class definition
# class MyClass(metaclass=CustomMeta):
#     def __init__(self, value):
#         self.value = value

#     def show_value(self):
#         return f"My value is {self.value}"

# # Example usage
# obj = MyClass(42)
# print(obj.show_value())  # Output: My value is 42
# print(obj.greet())       # Output: Hello, I am an instance of MyClass.

#=============================================================================================================

#     49. Demonstrate how to dynamically add methods or attributes to a class.
#=============================================================================================================

#     50. Write a decorator for a class method.
#=============================================================================================================

#     51. What is monkey patching? Show an example where you modify the behavior of a class at runtime.
#=============================================================================================================

# Real-World Applications
#     52. Design a class-based system for a school that includes Student, Teacher, and Course classes.
#=============================================================================================================

#     53. Implement a shopping cart system with classes like Item, Cart, and User.
#=============================================================================================================

#     54. Create a Restaurant class with an aggregation of MenuItem objects.
#=============================================================================================================

#     55. Develop a simple banking system with classes for Account, Customer, and Transaction.
#=============================================================================================================
