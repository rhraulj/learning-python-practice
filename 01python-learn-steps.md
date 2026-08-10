# 🟢 Part 1 — Basic Python

## 1. Python Introduction

---

## 1. What is Python?

Python is a **high-level, general-purpose programming language**. It was created by **Guido van Rossum** and first released in 1991.

Python is designed with a focus on:

* Readable syntax
* Simplicity
* Productivity
* Code maintainability
* Large standard library
* Extensive third-party ecosystem

Example:

```python
print("Hello, Python!")
```

Python code is generally easier to read compared with many lower-level or more syntax-heavy languages.

Python supports multiple programming styles, including:

* Procedural programming
* Object-oriented programming
* Functional programming

---

## 2. Why Python?

Python is popular because it provides a good balance between **simplicity and power**.

### Main reasons

**Simple syntax**

```python
name = "Rahul"
print(name)
```

The syntax is relatively close to natural language.

**Less code**

Many tasks can be accomplished with fewer lines of code compared with languages such as Java or C++.

**Large standard library**

Python includes many built-in modules for working with:

* Files
* Dates and times
* JSON
* Regular expressions
* Operating-system functionality
* Networking
* Mathematics
* Databases and more

**Large ecosystem**

Python has thousands of third-party packages available through the Python Package Index (PyPI).

**Cross-platform**

Python programs can generally run on:

* Windows
* Linux
* macOS

with little or no modification.

**Easy to learn but powerful**

Python is suitable for beginners while also providing advanced features such as:

* Decorators
* Generators
* Context managers
* Async programming
* Metaclasses
* Type hints

---

## 3. Python Use Cases

Python is a general-purpose language, so it is used in many areas.

### Common uses

* Automation
* Scripting
* Backend development
* Testing
* Command-line applications
* Desktop applications
* Data processing
* Scientific computing
* System administration
* Networking
* DevOps tooling
* Artificial intelligence and machine learning
* Education

For example, Python can be used to automate file operations:

```python
import os

for filename in os.listdir("documents"):
    print(filename)
```

Python itself is the programming language. Frameworks and libraries built around Python are separate technologies.

---

## 4. Python Versions

Python has gone through multiple major versions.

The two historically important versions are:

```text
Python 2
Python 3
```

Python 2 is a legacy version and reached its official end of life in 2020. Modern Python development uses **Python 3**.

Python 3 uses version numbers such as:

```text
Python 3.10
Python 3.11
Python 3.12
Python 3.13
Python 3.14
```

The exact version available depends on when Python is installed.

You can check your installed version from the terminal:

```bash
python --version
```

or, on systems where Python 3 is invoked separately:

```bash
python3 --version
```

You can also check from Python:

```python
import sys

print(sys.version)
```

Different Python versions can introduce:

* New language features
* Performance improvements
* Bug fixes
* Security fixes
* Standard-library changes

For modern learning and development, use a currently supported **Python 3** release.

---

## 5. Python Installation

Python must be installed on your computer before you can normally execute Python programs locally.

After installation, the Python interpreter becomes available through the operating system's terminal or command prompt.

You can verify the installation with:

```bash
python --version
```

For example:

```text
Python 3.x.x
```

Depending on the operating system, the command may instead be:

```bash
python3 --version
```

### Python installation usually provides

* Python interpreter
* Standard library
* Package-management tool such as `pip`
* Python command-line interface

A code editor is separate from Python.

For example:

```text
VS Code
PyCharm
Sublime Text
```

are development tools/editors. They provide an environment for writing code, while Python is the language runtime used to execute that code.

---

## 6. Python Interpreter

The **Python interpreter** is the program that executes Python code.

For example:

```python
print("Hello")
```

When this code is executed, the Python runtime processes it and produces:

```text
Hello
```

A simplified view is:

```text
Python source code
       ↓
Python interpreter/runtime
       ↓
Execution
       ↓
Result
```

Python implementations have different internal architectures. In the commonly used **CPython** implementation, Python source code is compiled into bytecode and then executed by the Python virtual machine.

Therefore, saying:

> "Python is interpreted"

is useful as a beginner-level description, but the actual execution process is more sophisticated than simply executing source-code lines one by one.

---

## 7. Python REPL

REPL stands for:

```text
R → Read
E → Evaluate
P → Print
L → Loop
```

It is an interactive Python environment.

Running:

```bash
python
```

can open the Python interactive interpreter.

You can then enter Python expressions:

```python
>>> 10 + 20
30

>>> 5 * 4
20

>>> print("Hello")
Hello
```

The REPL reads your input, evaluates it, displays the result when appropriate, and waits for another instruction.

### REPL is useful for

* Quickly testing Python expressions
* Experimenting with syntax
* Checking how functions behave
* Testing small pieces of code
* Learning Python interactively

It is different from writing a complete Python program in a `.py` file.

---

## 8. Running Python Programs

A Python program can be written in a `.py` file.

For example:

```text
hello.py
```

Contents:

```python
print("Hello, Python!")
print("This is my first program.")
```

Run it from the terminal:

```bash
python hello.py
```

or:

```bash
python3 hello.py
```

The Python interpreter loads the program and executes it.

There are therefore two common ways to work with Python:

### Interactive execution

```text
Terminal → Python REPL → Individual instructions
```

### Script execution

```text
.py file → Python interpreter → Program execution
```

---

## 9. `.py` Files

A Python source-code file normally has the extension:

```text
.py
```

Examples:

```text
main.py
calculator.py
student.py
bank.py
employee.py
```

A `.py` file contains Python source code.

Example:

```python
# calculator.py

a = 10
b = 20

result = a + b

print(result)
```

Running:

```bash
python calculator.py
```

produces:

```text
30
```

A project can contain many Python files:

```text
my_project/
│
├── main.py
├── calculator.py
├── student.py
└── utilities.py
```

Later, these files can be organized into modules and packages.

---

## 10. Python Execution Flow

At a simplified level, when you execute:

```bash
python program.py
```

the process looks like:

```text
program.py
     ↓
Python reads/parses the source
     ↓
Python compiles it to bytecode
     ↓
Python runtime executes the bytecode
     ↓
Output / result / exception
```

For example:

```python
print("First")
print("Second")
print("Third")
```

The statements execute in their defined program flow:

```text
First
Second
Third
```

Later, execution flow becomes more complex because of:

* Conditions
* Loops
* Functions
* Exceptions
* Classes
* Generators
* Async operations

For now, the important concept is that Python processes a program according to its syntax and control flow.

---

## 11. Python Syntax

**Syntax** means the rules that determine how Python code must be written.

For example, this is valid:

```python
print("Hello")
```

This is invalid because the closing parenthesis is missing:

```python
print("Hello"
```

Python reports an error instead of executing invalid syntax.

Another example:

```python
name = "Rahul"
```

is valid.

But:

```python
name =
```

is incomplete syntax.

Syntax includes rules related to:

* Keywords
* Indentation
* Parentheses
* Colons
* Strings
* Operators
* Expressions
* Statements
* Blocks
* Function definitions
* Classes

Correct syntax is necessary for Python to understand the program.

---

## 12. Indentation

Indentation means the spaces placed at the beginning of a line.

Python uses indentation to define **code blocks**.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The indentation before:

```python
print("Adult")
```

indicates that this statement belongs to the `if` block.

Without correct indentation:

```python
age = 20

if age >= 18:
print("Adult")
```

Python raises an indentation-related error.

### Standard practice

Python code normally uses **4 spaces** for each indentation level.

Example:

```python
if condition:
    statement1()
    statement2()
```

Nested code:

```python
if condition:
    if another_condition:
        print("Both conditions are true")
```

Indentation is one of the major characteristics that distinguishes Python syntax from languages that commonly use `{}` to define blocks.

---

## 13. Comments

A comment is text in source code intended for human readers rather than normal program execution.

A single-line comment begins with:

```python
#
```

Example:

```python
# Store the student's age
age = 20
```

Python does not execute the comment as a Python statement.

Multiple comments can be written:

```python
# Student information
name = "Rahul"
age = 20
city = "Ahmedabad"
```

Comments are useful for:

* Explaining non-obvious code
* Documenting decisions
* Adding notes
* Temporarily disabling code

Example:

```python
price = 100

# Apply a 10% discount
discount = price * 0.10
final_price = price - discount
```

Comments should generally add useful information rather than describe extremely obvious code.

---

## 14. Docstrings

A **docstring** is a string used to document a Python module, function, class, or method.

Example:

```python
def calculate_total():
    """Calculate and return the total amount."""
    return 100
```

The text:

```python
"""Calculate and return the total amount."""
```

is the function's docstring.

A module can also have a docstring:

```python
"""Utilities for calculating student marks."""

print("Student utilities")
```

### Comment vs docstring

Comment:

```python
# Calculate total
```

Docstring:

```python
"""Calculate and return the total."""
```

A docstring is associated with a Python object and can be accessed programmatically.

For example:

```python
def greet():
    """Display a greeting."""
    print("Hello")


print(greet.__doc__)
```

Output:

```text
Display a greeting.
```

Docstrings become particularly important when writing reusable functions, classes, and packages.

---

## 15. Keywords

**Keywords** are reserved words that have special meaning in Python's syntax.

Examples include:

```text
if
else
elif
for
while
in
is
def
class
return
import
from
try
except
finally
raise
with
as
and
or
not
True
False
None
```

Because they have special meanings, they cannot normally be used as ordinary identifiers.

This is invalid:

```python
class = "Python"
```

because `class` is a keyword.

This is valid:

```python
course = "Python"
```

You can inspect the keywords of the Python version you're using:

```python
import keyword

print(keyword.kwlist)
```

The exact keyword list can change as Python evolves.

---

## 16. Identifiers

An **identifier** is a name used to identify something in Python.

Identifiers are used for things such as:

* Variables
* Functions
* Classes
* Modules
* Objects

Example:

```python
student_name = "Rahul"
student_age = 20
```

Here:

```text
student_name
student_age
```

are identifiers.

### Basic rules

An identifier can contain:

* Letters
* Digits
* Underscores

It cannot start with a digit.

Valid:

```python
name
student_name
student2
_age
total_marks
```

Invalid:

```python
2student
student-name
student name
```

Also, Python identifiers are **case-sensitive**:

```python
name = "Rahul"
Name = "Riya"
```

These are two different identifiers.

Similarly:

```python
age
Age
AGE
```

are different names.

Keywords cannot be used as normal identifiers:

```python
class = "Student"  # Invalid
```

---

## 17. Naming Conventions

Naming conventions are recommended practices for choosing readable and consistent names.

### Variables

Python commonly uses **snake_case**:

```python
student_name = "Rahul"
total_marks = 450
account_balance = 5000
```

### Functions

Functions also commonly use snake_case:

```python
calculate_total()
get_student_name()
calculate_average()
```

### Classes

Classes commonly use **PascalCase**:

```python
class Student:
    pass

class StudentRecord:
    pass
```

### Constants

Constants are commonly written in uppercase:

```python
MAX_MARKS = 100
PI = 3.14159
DEFAULT_TIMEOUT = 30
```

### Private/internal names

A leading underscore is commonly used to indicate an internal name:

```python
_internal_value = 10
```

This is primarily a convention; a single leading underscore does not make the variable truly private.

### Good naming

```python
student_age = 20
total_price = 500
number_of_students = 30
```

Poor naming:

```python
x = 20
tp = 500
n = 30
```

Short names such as `x`, `i`, and `n` can be perfectly appropriate in small contexts, but descriptive names are generally better for meaningful application logic.

---

## 18. PEP 8 Basics

**PEP 8** is the widely used Python style guide.

PEP stands for:

**Python Enhancement Proposal**

PEP 8 provides recommendations for writing readable and consistent Python code.

### Indentation

Use 4 spaces:

```python
if age >= 18:
    print("Adult")
```

### Spaces around operators

Preferred:

```python
total = price + tax
```

Less readable:

```python
total=price+tax
```

### Naming

Use snake_case for variables and functions:

```python
student_name = "Rahul"

def calculate_total():
    pass
```

Use PascalCase for classes:

```python
class StudentRecord:
    pass
```

### Blank lines

Separate logical sections of code:

```python
name = "Rahul"
age = 20

print(name)
print(age)
```

### Imports

Imports are normally placed near the beginning of the file:

```python
import os
import sys

print("Program started")
```

### Line length

Traditional PEP 8 guidance recommends keeping lines to a reasonable length, historically **79 characters for code**. Modern tooling and project conventions may use different limits, so consistency within a project is important.

### Readability

PEP 8 is ultimately about making code easier for humans to read and maintain.

For example:

```python
total = price + tax
```

is easier to read than:

```python
t=price+tax
```

---

# Quick Summary

| Topic                  | Core idea                                                           |
| ---------------------- | ------------------------------------------------------------------- |
| **What is Python**     | High-level, general-purpose programming language                    |
| **Why Python**         | Readable, productive, powerful, large ecosystem                     |
| **Use cases**          | Automation, scripting, backend, testing, scientific computing, etc. |
| **Python versions**    | Modern development uses Python 3                                    |
| **Installation**       | Installs the Python runtime and related tools                       |
| **Interpreter**        | Runtime that executes Python programs                               |
| **REPL**               | Interactive Read-Evaluate-Print-Loop environment                    |
| **Running programs**   | Execute `.py` files using Python                                    |
| **`.py` files**        | Standard Python source-code files                                   |
| **Execution flow**     | Source → parsing/compilation → runtime execution                    |
| **Syntax**             | Rules for writing valid Python                                      |
| **Indentation**        | Defines code blocks                                                 |
| **Comments**           | Human-readable notes in source code                                 |
| **Docstrings**         | Documentation associated with Python objects                        |
| **Keywords**           | Reserved words with special language meaning                        |
| **Identifiers**        | Names used for variables, functions, classes, etc.                  |
| **Naming conventions** | Recommended patterns for readable names                             |
| **PEP 8**              | Python style and readability guidelines                             |

This completes the **Python Introduction** section. The next logical section is **Variables & Data Types**, where Python's objects, values, variable references, `int`, `float`, `str`, `bool`, `None`, `type()`, and `isinstance()` can be covered.

