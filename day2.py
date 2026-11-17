# Python has two main types of loops: for loops and while loops.

# 1. for Loop (Repeat for each item)
# Use a for loop when you know how many times you want to repeat
#  something, or when you want to go through every item in a collection 
# (like a list or text).

# for i in range (5):
#        print( i, "Good morning! 😎")

# 2. while Loop (Repeat as long as a condition is true)
# Use a while loop when you want to keep repeating until 
# a certain condition changes—useful when you don't know 
# upfront how many loops it will take.

# i=0
# while i < 5:
#     print(i, "Good morning! 😎")
# i += 1

#$$$$$ FUNCTION $$$$$

# def greet():
#     print("Hello Student")
#     print("Welcome to Python Training")
# greet()

# def add(a,b):
#     result = a+b
#     return result
# print(add(10, 20))


# ==========================================
# MAJOR DIFFERENCES: LIST vs TUPLE
# ==========================================

# 1. SYNTAX (Brackets)
#my_list = [10, 20, 30]     # Uses Square Brackets []
#my_tuple = (10, 20, 30)    # Uses Round Parentheses ()

# 2. MUTABILITY (Can you change it after creating?)
#my_list[0] = 99            # ✅ WORKS: Lists are MUTABLE (can add, edit, remove)
# my_tuple[0] = 99         # ❌ ERROR: Tuples are IMMUTABLE (locked once created)

# 3. METHODS AVAILABLE
#my_list.append(40)         # ✅ WORKS: Has methods like append(), insert(), remove(), pop()
# my_tuple.append(40)      # ❌ ERROR: Only has count() and index()

# 4. MEMORY & SPEED
# - List: Uses MORE memory, slightly SLOWER (because it needs extra space to grow)
# - Tuple: Uses LESS memory, slightly FASTER (fixed size)

# 5. WHEN TO USE WHICH?
# - Use LIST when data needs to change (e.g., shopping cart, task list, user scores)
# - Use TUPLE when data must stay constant (e.g., GPS coordinates, RGB colors, days of week)#

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits[0] = "mango"
# print(fruits)
# fruits.remove("banana")
# print("Removed :", fruits)
# fruits.pop(1)
# print("After popping:", fruits)
# fruits.sort()
# print("Sorted fruits:", fruits)
# fruits.reverse()
# print("Reversed fruits:", fruits)
# fruits.insert(1, "kiwi")
# print("Fruits with kiwi inserted:", fruits)

# students_details = ("satyam",23,85,True)
# print(students_details[0])

#===Dictionary (Key-Value Pairs)===

# 1. CREATE (Uses {key: value})
#student = {"name": "Rahul", "age": 20}

# 2. READ (Get value using key)
# print(student["name"])       # Output: Rahul

# 3. ADD / UPDATE (Changeable)
#student["age"] = 21          # Updates age to 21
#student["grade"] = "A"       # Adds new key 'grade'

# 4. DELETE
#student.pop("age")           # Removes 'age'

# 5. KEY POINTS
# - Uses Curly Braces {}
# - Stores data as Key : Value pairs
# - Keys must be unique (no duplicate keys)
# - Best for labeled data (user profiles, JSON data)


#$$$$$ example dictionary of students details $$$$$
# students_details = {"name": "satyam", "age": 23, "usn": "1GD24CS134", "dept": "CSE", "is_passed": True}
# students_details["course"] = "Python"  
# print(students_details["name"])
# print(students_details["age"])
# print(students_details["usn"])
# print(students_details["dept"])
# print(students_details["is_passed"])
# print(students_details["course"])

# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Marks:",self.marks)
# s1 = Student("Satyam", 23, 85)
# s2 = Student("Rohith", 22, 90)
# s1.display()
# s2.display()

# class Student:
#     def __init__(self):

#         self.marks = 0

#     def set_marks(self, marks):
#         self.marks = marks

#     def show_marks(self):
#         print("Marks:", self.marks)

# s1 = Student()
# s1.set_marks(85)
# s1.show_marks()

#$$$$$ single level inheritance $$$$$
# class father:
#     def House(self):
#         print("father has house")
# class son(father):
#     def car(self):
#         print("son has a car")
# s= son()
# s.House()
# s.car()

#$$$$$ multilevel inheritance $$$$$
# class Grandfather:
#     def land(self):
#         print("Grandfather has land")
# class Father(Grandfather):
#     def house(self):
#         print("Father has house")
# class Son(Father):
#     def car(self):
#         print("Son has a car")
# s = Son()
# s.land()
# s.house()
# s.car()

#$$$$$ multilevel inheritance $$$$$
# class Father:
#     def skill_cooking(self):
#         print("Father cooks great food.")
# class Mother:
#     def skill_painting(self):
#         print("Mother paints beautifully.")
# class Child(Father, Mother):  
#     def skill_coding(self):
#         print("Child codes software.")
# me = Child()
# me.skill_cooking()   
# me.skill_painting()  
# me.skill_coding()    

#$$$$$ hierarchical inheritance $$$$$
# class Animal:
#     def eat(self):
#         print("This animal is eating...")
# class Dog(Animal):
#     def bark(self):
#         print("Dog says: Woof! Woof!")
# class Cat(Animal):
#     def meow(self):
#         print("Cat says: Meow!")
# dog = Dog()
# dog.eat()
# dog.bark()
# cat = Cat()
# cat.eat()
# cat.meow()

#polymorphism
# class Animal:
#     def sound(self):
#         print("This animal makes a sound.")
# class Dog(Animal):
#     def sound(self):
#         print("Dog says: Woof! Woof!")
# class Cat(Animal):
#     def sound(self):
#         print("Cat says: Meow!")
# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.sound()  


# Abstraction

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")
class Card(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")      
p1 = UPI()
p2 = Card()
p1.pay(1000)
p2.pay(2000)
