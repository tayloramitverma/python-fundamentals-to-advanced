# Python Learning Journey

A structured collection of Python learning materials covering fundamentals through advanced topics — sourced from Udemy bootcamps, YouTube tutorials, and hands-on practice projects.

---

## Repository Structure

```
Python/
├── Complete-Python-Bootcamp/       # Full Udemy bootcamp — basics to advanced
│   ├── 1-Python Basics/            # Variables, datatypes, operators
│   ├── 2-Control Flow/             # Conditionals, loops
│   ├── 3-Data Structures/          # Lists, tuples, sets, dictionaries
│   ├── 4-Functions/                # Functions, lambda, map, filter
│   ├── 5-Modules/                  # Imports, standard library, packages
│   ├── 6-File Handling/            # File I/O, paths
│   ├── 7-Exception Handling/       # try/except, custom errors
│   ├── 8-Class And Objects/        # OOP — inheritance, polymorphism, encapsulation
│   ├── 9-Advance Python Concepts/  # Iterators, generators, decorators
│   ├── 10-Data Analysis With Python/ # NumPy, Pandas, Matplotlib, Seaborn
│   ├── 11-Working With Databases/  # SQLite
│   ├── 12-Logging In Python/       # Logging module, multiple loggers
│   ├── 13-Flask/                   # Flask web framework, Jinja templates, REST APIs
│   ├── 14-Streamlit/               # Data dashboards, widgets, ML integration
│   ├── 15-Memory Management/       # Memory profiling, object lifecycle
│   └── 16-Multithreading and Multiprocessing/ # Concurrent programming
│
├── Python-YouTube/                 # YouTube tutorial series
│   ├── 01_basics/                  # Hello world, variables, f-strings
│   ├── 02-scopes/                  # Variable scope, closures
│   ├── 03-oop/                     # OOP — classes, inheritance, static methods
│   ├── 04-decorators/              # Decorator patterns (timer, etc.)
│   ├── 05-api/                     # HTTP requests, REST API consumption
│   └── 06-numpy/                   # NumPy deep dive (4-phase notebooks)
│
├── Python-Udemy/                   # Secondary Udemy course
│   ├── 1-Basics/                   # Python basics notebook
│   └── 2-ControlFlow/              # Conditional statements notebook
│
├── FastAPI/                        # FastAPI practice project
│   └── main.py                     # CRUD API with Pydantic models
│
└── python-envs.md                  # Conda environment setup notes
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Jupyter Notebooks | Interactive learning |
| NumPy / Pandas | Data analysis |
| Matplotlib / Seaborn | Data visualization |
| Flask | Web framework |
| FastAPI + Pydantic | Modern REST APIs |
| Streamlit | Data dashboards |
| SQLite | Database |
| requests | HTTP client |

---

## Environment Setup

This repo uses conda environments managed via Anaconda.

```bash
# Create a new environment
conda create --name <env_name> python=3.11

# Create with specific packages
conda create --name <env_name> python=3.11 numpy pandas

# List all environments
conda env list

# Activate an environment
conda activate fastapi
conda activate venv

# Deactivate
conda deactivate
```

**Dependencies (Complete Python Bootcamp):**
```bash
pip install -r Complete-Python-Bootcamp/requirements.txt
```

Packages: `ipykernel`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `flask`, `streamlit`, `scikit-learn`, `memory_profiler`

**FastAPI project:**
```bash
cd FastAPI
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Python Fundamentals — With Examples

### 1. Variables & Data Types

Python is dynamically typed — you don't declare types explicitly.

```python
name = "Amit"           # str
age = 25                # int
price = 99.99           # float
is_active = True        # bool
nothing = None          # NoneType

# f-strings (string formatting)
print(f"The price is {price:.2f} dollars")  # The price is 99.99 dollars
```

**Mutability:**
- **Mutable** (can change): `list`, `dict`, `set`
- **Immutable** (cannot change): `str`, `int`, `float`, `tuple`

---

### 2. Control Flow

```python
# if / elif / else
score = 85

if score >= 90:
    print("A grade")
elif score >= 75:
    print("B grade")
else:
    print("C grade")

# for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# while loop
count = 0
while count < 3:
    print(count)
    count += 1

# list comprehension
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

### 3. Data Structures

```python
# List — ordered, mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")

# Tuple — ordered, immutable
coords = (10.5, 20.3)

# Set — unordered, unique values
tags = {"python", "code", "python"}  # {"python", "code"}

# Dictionary — key-value pairs
user = {"name": "Amit", "age": 25}
print(user["name"])       # Amit
user["city"] = "Mumbai"   # add new key
```

---

### 4. Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Amit"))  # Hello, Amit!

# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9
print(power(3, 3))  # 27

# *args and **kwargs
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))  # 10

# Lambda (anonymous function)
double = lambda x: x * 2
print(double(5))  # 10

# map and filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))       # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
```

---

### 5. Scope & Closures

Variable scope determines where a variable is accessible.

```python
x = 99  # global

def func():
    local_var = "only inside"
    print(x)  # can access global

# global keyword
def update():
    global x
    x = 12

update()
print(x)  # 12
```

**Closure** — inner function remembers the outer function's variable:

```python
def func1(num):
    def func2(x):
        return num ** x   # 'num' is captured from outer scope
    return func2

f1 = func1(2)
f2 = func1(3)

print(f1(2))  # 4   (2^2)
print(f2(3))  # 27  (3^3)
```

---

### 6. Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Type or value error: {e}")
else:
    print("No error occurred")
finally:
    print("Always runs")

# Custom exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age
```

---

### 7. Object-Oriented Programming (OOP)

```python
class Car:
    total_car = 0  # class variable

    def __init__(self, brand, model):
        self.__brand = brand   # private attribute
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand}, {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transportation"

    @property
    def model(self):
        return self.__model


# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):          # polymorphism — overrides parent
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.get_brand())    # Tesla
print(my_tesla.fuel_type())    # Electric charge
print(Car.total_car)           # 1

# isinstance checks
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True

# Multiple inheritance
class Battery:
    def battery_info(self):
        return "Battery info"

class Engine:
    def engine_info(self):
        return "Engine info"

class Electric(Battery, Engine, Car):
    pass
```

**OOP Pillars:**
| Concept | Meaning |
|---------|---------|
| Encapsulation | Hide internal data with private (`__`) attributes |
| Inheritance | Child class reuses parent class code |
| Polymorphism | Same method name, different behavior per class |
| Abstraction | Hide implementation details, expose interface |

---

### 8. Decorators

A decorator wraps a function to extend its behavior without modifying it.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)

slow_function(2)  # slow_function took 2.00s
```

---

### 9. Iterators & Generators

```python
# Iterator — manual
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

# Generator — cleaner, memory efficient
def counter(limit):
    for i in range(1, limit + 1):
        yield i

for val in counter(5):
    print(val)  # 1, 2, 3, 4, 5
```

Generators are memory-efficient — they produce one value at a time instead of storing the full list.

---

### 10. Modules & Packages

```python
# Importing standard library modules
import math
import os
import datetime

print(math.sqrt(16))        # 4.0
print(os.getcwd())          # current directory
print(datetime.date.today()) # today's date

# Importing from a custom package
from package.maths import add
from package.subpackages.mult import multiply
```

---

### 11. File Handling

```python
# Write to file
with open("output.txt", "w") as f:
    f.write("Hello, World!")

# Read from file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)

# Append
with open("output.txt", "a") as f:
    f.write("\nNew line added")
```

---

### 12. API Consumption (requests)

```python
import requests

def fetch_user():
    url = "https://api.example.com/user/random"
    res = requests.get(url)
    data = res.json()
    if data["success"]:
        return data["data"]["login"]["username"]
    raise Exception("Failed to fetch user")

if __name__ == "__main__":
    try:
        username = fetch_user()
        print(username)
    except Exception as e:
        print(str(e))
```

---

### 13. FastAPI — Building REST APIs

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas = []

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            return {"deleted": teas.pop(i)}
    return {"error": "Not found"}
```

Run with: `uvicorn main:app --reload`

---

## Learning Path

```
Basics → Control Flow → Data Structures → Functions
    → Scope & Closures → OOP → Exception Handling
        → Modules → File Handling → Advanced Concepts
            → Data Analysis → Databases → Logging
                → Flask → Streamlit → FastAPI
                    → Multithreading & Multiprocessing
```

---

## Author

**Amit Verma** — [beingamitverma@gmail.com](mailto:beingamitverma@gmail.com)
