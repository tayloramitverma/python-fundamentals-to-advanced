# Variables, Data Types, and Mutability in Python

---

## 1. Variables

A variable is a named reference to a value stored in memory. Python is dynamically typed — you don't declare the type; Python infers it at runtime.

```python
name = "Alice"       # str
age = 30             # int
height = 5.7         # float
is_active = True     # bool
```

### Rules for naming variables
- Must start with a letter or underscore (`_`)
- Cannot start with a digit
- Case-sensitive: `name` and `Name` are different
- Cannot use Python keywords (`if`, `for`, `class`, etc.)

```python
_score = 100     # valid
score2 = 99      # valid
2score = 99      # invalid — SyntaxError
```

---

## 2. Data Types

Python has several built-in data types:

| Category   | Type      | Example                        |
|------------|-----------|--------------------------------|
| Text       | `str`     | `"hello"`                      |
| Numeric    | `int`     | `42`                           |
| Numeric    | `float`   | `3.14`                         |
| Numeric    | `complex` | `2 + 3j`                       |
| Boolean    | `bool`    | `True`, `False`                |
| Sequence   | `list`    | `[1, 2, 3]`                    |
| Sequence   | `tuple`   | `(1, 2, 3)`                    |
| Mapping    | `dict`    | `{"key": "value"}`             |
| Set        | `set`     | `{1, 2, 3}`                    |
| None       | `NoneType`| `None`                         |

```python
x = 42
print(type(x))        # <class 'int'>

pi = 3.14
print(type(pi))       # <class 'float'>

greeting = "Hello"
print(type(greeting)) # <class 'str'>

items = [1, 2, 3]
print(type(items))    # <class 'list'>
```

### Type conversion (casting)

```python
x = "10"
y = int(x)      # str → int
z = float(x)    # str → float

print(y + 5)    # 15
print(z + 0.5)  # 10.5
```

---

## 3. Mutable vs Immutable

This is one of the most important concepts in Python.

| Term          | Meaning                                         |
|---------------|-------------------------------------------------|
| **Immutable** | Value **cannot** be changed after creation      |
| **Mutable**   | Value **can** be changed after creation         |

### Immutable Types

`int`, `float`, `str`, `bool`, `tuple`

When you "change" an immutable object, Python actually creates a **new object** and rebinds the variable.

```python
x = 10
print(id(x))   # e.g. 140200001234

x = x + 1
print(id(x))   # different id — new object created!
print(x)       # 11
```

```python
name = "Alice"
# name[0] = "B"   # TypeError: 'str' object does not support item assignment

name = "Bob"       # This is fine — rebinding to a new string object
print(name)        # Bob
```

```python
t = (1, 2, 3)
# t[0] = 99   # TypeError: 'tuple' object does not support item assignment
```

### Mutable Types

`list`, `dict`, `set`

These can be modified **in-place** — the same object in memory changes.

```python
nums = [1, 2, 3]
print(id(nums))   # e.g. 140200005678

nums.append(4)
print(id(nums))   # same id — same object modified!
print(nums)       # [1, 2, 3, 4]
```

```python
person = {"name": "Alice", "age": 25}
person["age"] = 26          # modify existing key
person["city"] = "Delhi"    # add new key
print(person)
# {'name': 'Alice', 'age': 26, 'city': 'Delhi'}
```

---

## 4. Why Mutability Matters

### Shared references with mutable objects

```python
a = [1, 2, 3]
b = a           # b points to the same list object

b.append(4)

print(a)        # [1, 2, 3, 4]  <-- a is also changed!
print(b)        # [1, 2, 3, 4]
```

Both `a` and `b` reference the **same** list. Changing via `b` also affects `a`.

**Fix:** Use `.copy()` to create an independent copy.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)        # [1, 2, 3]   <-- unchanged
print(b)        # [1, 2, 3, 4]
```

### Immutable objects are safe to share

```python
x = "hello"
y = x

y = y + " world"

print(x)        # hello   <-- unchanged
print(y)        # hello world
```

Since strings are immutable, `y = y + " world"` creates a new object — `x` is untouched.

---

## Summary

| Type    | Mutable? | Can modify in-place? | Example          |
|---------|----------|----------------------|------------------|
| `int`   | No       | No                   | `x = 5`          |
| `float` | No       | No                   | `x = 3.14`       |
| `str`   | No       | No                   | `x = "hi"`       |
| `bool`  | No       | No                   | `x = True`       |
| `tuple` | No       | No                   | `x = (1, 2)`     |
| `list`  | Yes      | Yes                  | `x = [1, 2]`     |
| `dict`  | Yes      | Yes                  | `x = {"a": 1}`   |
| `set`   | Yes      | Yes                  | `x = {1, 2}`     |
