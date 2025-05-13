// ... existing code ...

        .python-section {
            background-color: #fff;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        .python-module {
            border: 1px solid #e1e1e1;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            background: #f8f9fa;
            transition: transform 0.3s;
        }

        .python-module:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .code-example {
            background-color: #2c3e50;
            color: #fff;
            padding: 1.5rem;
            border-radius: 8px;
            font-family: 'Consolas', monospace;
            margin: 1rem 0;
            position: relative;
        }

        .code-title {
            position: absolute;
            top: -12px;
            left: 20px;
            background-color: #3498db;
            padding: 0.3rem 1rem;
            border-radius: 15px;
            font-size: 0.9rem;
        }

        .module-title {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .duration-badge {
            background-color: #3498db;
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.9rem;
        }

// ... existing code ...

        <section class="python-section">
            <h2>Python Programming Course</h2>
            <p>Master Python programming from basics to advanced concepts with hands-on projects.</p>

            <div class="python-module">
                <div class="module-title">
                    <h3>Module 1: Python Basics</h3>
                    <span class="duration-badge">Week 1-2</span>
                </div>
                <ul class="feature-list">
                    <li>Introduction to Python</li>
                    <li>Variables and Data Types</li>
                    <li>Basic Operations and Operators</li>
                    <li>Control Flow (if-else, loops)</li>
                </ul>
                <div class="code-example">
                    <span class="code-title">Example Code</span>
                    <pre>
# Basic Python Example
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome {name}! You are eligible.")
else:
    print(f"Sorry {name}, you must be 18 or older.")</pre>
                </div>
            </div>

            <div class="python-module">
                <div class="module-title">
                    <h3>Module 2: Data Structures</h3>
                    <span class="duration-badge">Week 3-4</span>
                </div>
                <ul class="feature-list">
                    <li>Lists and Tuples</li>
                    <li>Dictionaries and Sets</li>
                    <li>List Comprehension</li>
                    <li>Working with Collections</li>
                </ul>
                <div class="code-example">
                    <span class="code-title">Example Code</span>
                    <pre>
# Data Structures Example
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
print("High scorers:", high_scorers)</pre>
                </div>
            </div>

            <div class="python-module">
                <div class="module-title">
                    <h3>Module 3: Functions & OOP</h3>
                    <span class="duration-badge">Week 5-6</span>
                </div>
                <ul class="feature-list">
                    <li>Function Definition and Arguments</li>
                    <li>Lambda Functions</li>
                    <li>Classes and Objects</li>
                    <li>Inheritance and Polymorphism</li>
                </ul>
                <div class="code-example">
                    <span class="code-title">Example Code</span>
                    <pre>
# OOP Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

# Creating an object
student = Student("Alex", 20)
print(student.introduce())</pre>
                </div>
            </div>

            <div class="python-module">
                <div class="module-title">
                    <h3>Module 4: Advanced Topics</h3>
                    <span class="duration-badge">Week 7-8</span>
                </div>
                <ul class="feature-list">
                    <li>File Handling and JSON</li>
                    <li>Error Handling (Try-Except)</li>
                    <li>Working with APIs</li>
                    <li>Database Operations</li>
                </ul>
                <div class="code-example">
                    <span class="code-title">Example Code</span>
                    <pre>
# API and Error Handling Example
import requests
try:
    response = requests.get('https://api.example.com/data')
    data = response.json()
    print("Data fetched successfully!")
except requests.RequestException as e:
    print(f"Error fetching data: {e}")</pre>
                </div>
            </div>

            <div class="python-module">
                <div class="module-title">
                    <h3>Course Features</h3>
                </div>
                <ul class="feature-list">
                    <li>Live Coding Sessions</li>
                    <li>Real-world Projects</li>
                    <li>24/7 Support via WhatsApp</li>
                    <li>Certificate on Completion</li>
                    <li>Job Interview Preparation</li>
                    <li>Course Duration: 2 Months</li>
                    <li>Course Fee: ₹1000 Only</li>
                </ul>
                <a href="#admissionForm" class="hosting-link">Enroll Now</a>
            </div>
        </section>

// ... rest of the existing code ...
