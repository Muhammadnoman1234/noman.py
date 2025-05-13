# Python Examples for Learning
# Author: Noman Anwar

def basic_example():
    """Basic Python example with input and control flow"""
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        
        if age >= 18:
            print(f"Welcome {name}! You are eligible.")
        else:
            print(f"Sorry {name}, you must be 18 or older.")
    except ValueError:
        print("Please enter a valid age (numbers only)")

def data_structures_example():
    """Example of Python data structures and list comprehension"""
    # List of dictionaries
    students = [
        {"name": "John", "score": 85},
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 78}
    ]
    
    # List comprehension
    high_scorers = [
        student["name"] 
        for student in students 
        if student["score"] >= 85
    ]
    print("High scorers:", high_scorers)

class Student:
    """Example of Object-Oriented Programming in Python"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

def main():
    print("Welcome to Python Examples!")
    print("\n1. Basic Example:")
    basic_example()
    
    print("\n2. Data Structures Example:")
    data_structures_example()
    
    print("\n3. OOP Example:")
    student = Student("Alex", 20)
    print(student.introduce())

if __name__ == "__main__":
    main() 
