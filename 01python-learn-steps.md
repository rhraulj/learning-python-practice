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

# 🟢 Part 1 — Basic Python

## 2. Variables & Data Types

---

## 1. Variables

A **variable** is a name that refers to a value/object in Python.

Example:

```python
name = "Rahul"
age = 25
```

Here:

```text
name → "Rahul"
age  → 25
```

A useful way to think about Python variables is:

> A variable is a name/reference associated with an object.

Python variables don't have a fixed data type declaration like some statically typed languages.

For example:

```python
x = 10
```

Later:

```python
x = "Python"
```

This is valid because `x` can refer to different objects during program execution.

---

## 2. Variable Assignment

Assignment means associating a variable name with a value.

```python
age = 25
name = "Rahul"
price = 99.50
```

The `=` operator is the **assignment operator**.

It does not mean "equals" in the mathematical sense. It means:

> Evaluate the expression on the right and assign/reference the resulting object using the name on the left.

Example:

```python
x = 10
```

Then:

```python
print(x)
```

Output:

```text
10
```

You can assign the result of an expression:

```python
total = 100 + 50
print(total)
```

Output:

```text
150
```

You can also assign one variable to another:

```python
x = 10
y = x

print(y)
```

Output:

```text
10
```

### Important

This:

```python
x = 10
```

is assignment.

This:

```python
x == 10
```

is comparison and asks whether `x` is equal to `10`.

---

## 3. Multiple Assignment

Python allows multiple variables to be assigned in a single statement.

```python
name, age, city = "Rahul", 25, "Ahmedabad"
```

This is equivalent to:

```python
name = "Rahul"
age = 25
city = "Ahmedabad"
```

You can also assign the same value to multiple variables:

```python
x = y = z = 100
```

Now all three names refer to the value `100`.

### Swapping variables

Python makes swapping particularly simple:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

This works through Python's iterable unpacking mechanism.

### Unpacking

```python
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

The number of variables must normally match the number of values being unpacked.

---

## 4. Constants

A **constant** is a value that is intended not to change during a program.

Python does not have a built-in keyword such as `const` that makes a variable immutable.

Instead, Python uses a naming convention:

```python
PI = 3.14159
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
```

Uppercase names communicate:

> "This value is intended to be treated as a constant."

However, Python does not prevent reassignment:

```python
MAX_USERS = 100

MAX_USERS = 200
```

This is technically allowed.

Therefore:

```python
MAX_USERS = 100
```

is a **convention**, not an enforced constant.

### `Final`

Python's type-hinting system also provides `Final`:

```python
from typing import Final

MAX_USERS: Final = 100
```

Static type checkers can use this information to detect reassignment, but Python itself does not automatically prevent the reassignment at runtime.

---

## 5. Dynamic Typing

Python is **dynamically typed**.

This means the type of an object is determined at runtime, and variable names do not need to be declared with a fixed type.

Example:

```python
x = 10
```

Here `x` refers to an integer object.

Later:

```python
x = "Hello"
```

Now `x` refers to a string object.

And:

```python
x = 3.14
```

Now it refers to a float object.

The variable itself isn't permanently declared as an `int`, `str`, or `float`.

A useful mental model is:

```text
x ──→ 10
```

Then:

```text
x ──→ "Hello"
```

Then:

```text
x ──→ 3.14
```

The name `x` can be rebound to different objects.

### Dynamic typing vs static typing

Python:

```python
x = 10
x = "Hello"
```

Languages with static typing may require something like:

```text
int x = 10
```

and generally won't allow `x` to later hold a string without an explicit compatible type design.

Dynamic typing makes Python flexible, but it also means type-related errors can appear during execution.

---

## 6. Type Checking

Type checking means determining the type of an object/value.

The most common tools are:

```python
type()
```

and:

```python
isinstance()
```

Example:

```python
age = 25

print(type(age))
```

Output:

```text
<class 'int'>
```

You can also use:

```python
print(isinstance(age, int))
```

Output:

```text
True
```

Python also performs type-related checks when operations are executed.

For example:

```python
x = 10
y = "20"

print(x + y)
```

This raises a `TypeError` because Python does not automatically treat the string `"20"` as the integer `20` for this operation.

---

# 7. Type Conversion

**Type conversion** means converting a value from one data type to another.

Common conversion functions include:

```python
int()
float()
str()
bool()
complex()
```

### String to integer

```python
age = "25"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

### Integer to float

```python
x = 10

y = float(x)

print(y)
```

Output:

```text
10.0
```

### Number to string

```python
age = 25

text = str(age)

print(text)
print(type(text))
```

Output:

```text
25
<class 'str'>
```

### Float to integer

```python
x = 10.9

y = int(x)

print(y)
```

Output:

```text
10
```

`int()` truncates the fractional portion when converting a floating-point number. It does not round `10.9` to `11`.

### Invalid conversion

```python
x = "hello"

print(int(x))
```

This raises:

```text
ValueError
```

because `"hello"` cannot be interpreted as an integer.

---

# 8. `int`

`int` represents **integers**, meaning whole numbers without a fractional component.

Examples:

```python
age = 25
temperature = -10
score = 0
```

All are integers.

```python
print(type(25))
```

Output:

```text
<class 'int'>
```

Python integers can represent arbitrarily large integers, limited mainly by available memory.

For example:

```python
large_number = 999999999999999999999999999999
print(large_number)
```

### Integer operations

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3
1
1000
```

Here:

* `+` → addition
* `-` → subtraction
* `*` → multiplication
* `//` → floor division
* `%` → remainder
* `**` → exponentiation

---

# 9. `float`

`float` represents **floating-point numbers**, generally numbers containing a fractional part.

Examples:

```python
price = 99.99
temperature = 36.5
percentage = 75.0
```

Check the type:

```python
print(type(99.99))
```

Output:

```text
<class 'float'>
```

### Arithmetic

```python
a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Floating-point numbers have finite precision.

For example:

```python
print(0.1 + 0.2)
```

may produce:

```text
0.30000000000000004
```

This happens because many decimal fractions cannot be represented exactly in binary floating-point format.

For financial calculations where exact decimal arithmetic matters, Python provides the `decimal` module.

---

# 10. `complex`

`complex` represents **complex numbers**.

A complex number has:

```text
real part + imaginary part
```

Python uses `j` for the imaginary component.

Example:

```python
z = 3 + 4j

print(z)
print(type(z))
```

Output:

```text
(3+4j)
<class 'complex'>
```

You can access the components:

```python
z = 3 + 4j

print(z.real)
print(z.imag)
```

Output:

```text
3.0
4.0
```

Complex numbers support arithmetic:

```python
a = 2 + 3j
b = 1 + 2j

print(a + b)
print(a * b)
```

They are commonly used in mathematical, engineering, and scientific applications.

---

# 11. `bool`

`bool` represents a logical value.

There are only two Boolean values:

```python
True
False
```

Notice that they start with capital letters.

Example:

```python
is_logged_in = True
is_admin = False
```

Check the type:

```python
print(type(True))
```

Output:

```text
<class 'bool'>
```

Boolean values are commonly produced by comparisons:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

Another example:

```python
x = 10
y = 20

print(x > y)
```

Output:

```text
False
```

Boolean values are heavily used with:

* `if`
* `while`
* `and`
* `or`
* `not`
* Comparisons

### Boolean conversion

Python can convert other values to Boolean using `bool()`:

```python
print(bool(1))
print(bool(0))
print(bool("Hello"))
print(bool(""))
```

Output:

```text
True
False
True
False
```

This introduces the concept of **truthy** and **falsy** values, which becomes important when learning conditions.

---

# 12. `str`

`str` represents **strings**, which are sequences of text characters.

Examples:

```python
name = "Rahul"
city = 'Ahmedabad'
message = "Welcome to Python"
```

Strings can use:

```python
"double quotes"
'single quotes'
```

Triple quotes can be used for multi-line strings:

```python
message = """This is
a multi-line
string."""
```

Check the type:

```python
name = "Rahul"

print(type(name))
```

Output:

```text
<class 'str'>
```

### Strings can contain numbers

```python
x = "100"
```

This is a string, not an integer.

```python
print(type(x))
```

Output:

```text
<class 'str'>
```

Therefore:

```python
"10" + "20"
```

produces:

```text
1020
```

because both are strings and `+` concatenates them.

But:

```python
10 + 20
```

produces:

```text
30
```

because both are integers.

### String conversion

```python
age = 25

message = "Age: " + str(age)

print(message)
```

Output:

```text
Age: 25
```

Strings will be covered in much greater depth in the dedicated **Strings** section.

---

# 13. `None`

`None` represents the absence of a value.

It is a special singleton object of type `NoneType`.

Example:

```python
result = None

print(result)
```

Output:

```text
None
```

Check its type:

```python
print(type(None))
```

Output:

```text
<class 'NoneType'>
```

`None` is commonly used when:

* A value doesn't exist
* A value hasn't been assigned yet conceptually
* A function has no meaningful return value
* You need to represent "nothing" or "no result"

Example:

```python
user_name = None
```

Later:

```python
user_name = "Rahul"
```

### `None` vs `0`

They are not the same.

```python
x = 0
y = None
```

`0` is an integer value.

`None` represents the absence of a value.

### Checking for `None`

Use:

```python
if value is None:
    print("No value")
```

rather than:

```python
if value == None:
    print("No value")
```

`is None` is the standard and preferred form for checking the singleton `None`.

---

# 14. `type()`

`type()` is a built-in Python function that can be used to determine an object's type.

Example:

```python
x = 100

print(type(x))
```

Output:

```text
<class 'int'>
```

More examples:

```python
print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))
print(type(None))
print(type(2 + 3j))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
<class 'complex'>
```

You can also use `type()` with a variable:

```python
value = "Python"

print(type(value))
```

### Important

`type()` tells you the **exact type** of an object.

For inheritance and more flexible type checks, `isinstance()` is usually preferred.

---

# 15. `isinstance()`

`isinstance()` checks whether an object is an instance of a particular class or type.

Syntax:

```python
isinstance(object, type)
```

Example:

```python
age = 25

print(isinstance(age, int))
```

Output:

```text
True
```

Another example:

```python
name = "Rahul"

print(isinstance(name, str))
```

Output:

```text
True
```

If the type doesn't match:

```python
age = 25

print(isinstance(age, str))
```

Output:

```text
False
```

### Multiple types

You can check multiple types by providing a tuple:

```python
value = 10

print(isinstance(value, (int, float)))
```

Output:

```text
True
```

This means:

> Is `value` either an `int` or a `float`?

### `type()` vs `isinstance()`

Consider:

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
```

Then:

```python
print(type(dog) is Dog)
```

gives:

```text
True
```

And:

```python
print(isinstance(dog, Dog))
```

also gives:

```text
True
```

But:

```python
print(isinstance(dog, Animal))
```

gives:

```text
True
```

because `Dog` inherits from `Animal`.

Whereas:

```python
print(type(dog) is Animal)
```

gives:

```text
False
```

So:

* `type()` is useful when you need the exact type.
* `isinstance()` is generally better for checking whether an object belongs to a type hierarchy.

---

# Quick Summary

| Topic                   | Core idea                                                         |
| ----------------------- | ----------------------------------------------------------------- |
| **Variables**           | Names that refer to objects                                       |
| **Variable assignment** | Associates a name with an evaluated value/object                  |
| **Multiple assignment** | Assign multiple names/values in one statement                     |
| **Constants**           | Values intended not to change; uppercase naming is the convention |
| **Dynamic typing**      | Names don't have fixed declared types                             |
| **Type checking**       | Determining/checking an object's type                             |
| **Type conversion**     | Converting a value to another type                                |
| **`int`**               | Integer numbers                                                   |
| **`float`**             | Floating-point numbers                                            |
| **`complex`**           | Complex numbers using `j` for the imaginary part                  |
| **`bool`**              | `True` or `False`                                                 |
| **`str`**               | Text/string data                                                  |
| **`None`**              | Represents absence of a value                                     |
| **`type()`**            | Returns an object's type                                          |
| **`isinstance()`**      | Checks whether an object is an instance of a type                 |

### One important Python concept

The most useful mental model to retain is:

```python
x = 10
```

doesn't mean that `x` permanently **is an integer variable**.

Instead, Python creates/uses an integer object and makes the name `x` refer to it:

```text
x ─────→ 10 (int)
```

Then:

```python
x = "Python"
```

rebinds the name:

```text
x ─────→ "Python" (str)
```

This relationship between **names, objects, values, and types** becomes increasingly important as you move into Python's intermediate and advanced concepts.
# 🟢 Part 1 — Basic Python

## 3. Operators

Operators are symbols or keywords that perform operations on values or objects.

For example:

```python
a = 10
b = 5

print(a + b)
```

Here, `+` is an **operator**, while `a` and `b` are **operands**.

Python provides several categories of operators.

---

# 1. Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Meaning           | Example   | Result     |
| -------- | ----------------- | --------- | ---------- |
| `+`      | Addition          | `10 + 3`  | `13`       |
| `-`      | Subtraction       | `10 - 3`  | `7`        |
| `*`      | Multiplication    | `10 * 3`  | `30`       |
| `/`      | Division          | `10 / 3`  | `3.333...` |
| `//`     | Floor division    | `10 // 3` | `3`        |
| `%`      | Modulus/remainder | `10 % 3`  | `1`        |
| `**`     | Exponentiation    | `10 ** 3` | `1000`     |

### Addition

```python
a = 10
b = 5

print(a + b)
```

Output:

```text
15
```

`+` can also concatenate strings:

```python
first_name = "Rahul"
last_name = "Patel"

print(first_name + " " + last_name)
```

Output:

```text
Rahul Patel
```

### Subtraction

```python
print(10 - 3)
```

Output:

```text
7
```

### Multiplication

```python
print(10 * 3)
```

Output:

```text
30
```

It can also repeat strings:

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

### Division `/`

The `/` operator always produces a floating-point result:

```python
print(10 / 2)
```

Output:

```text
5.0
```

Even when the mathematical result is a whole number, the result is a `float`.

### Floor division `//`

Floor division performs division and returns the floor of the result:

```python
print(10 // 3)
```

Output:

```text
3
```

With negative numbers, remember that floor means moving toward negative infinity:

```python
print(-10 // 3)
```

Output:

```text
-4
```

because:

```text
-10 / 3 = -3.333...
floor = -4
```

### Modulus `%`

Returns the remainder:

```python
print(10 % 3)
```

Output:

```text
1
```

Common uses include checking divisibility:

```python
number = 10

print(number % 2 == 0)
```

Output:

```text
True
```

### Exponentiation `**`

Used for powers:

```python
print(2 ** 3)
```

Output:

```text
8
```

Equivalent to:

```text
2 × 2 × 2 = 8
```

---

# 2. Comparison Operators

Comparison operators compare values and produce a Boolean result:

```text
True
```

or:

```text
False
```

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `5 == 5` |
| `!=`     | Not equal to             | `5 != 3` |
| `>`      | Greater than             | `5 > 3`  |
| `<`      | Less than                | `5 < 3`  |
| `>=`     | Greater than or equal to | `5 >= 5` |
| `<=`     | Less than or equal to    | `5 <= 3` |

### Equal `==`

```python
print(10 == 10)
```

Output:

```text
True
```

Important:

```python
=
```

means assignment, while:

```python
==
```

means comparison.

### Not equal `!=`

```python
print(10 != 5)
```

Output:

```text
True
```

### Greater than `>`

```python
print(10 > 5)
```

Output:

```text
True
```

### Less than `<`

```python
print(10 < 5)
```

Output:

```text
False
```

### Greater than or equal `>=`

```python
print(10 >= 10)
print(10 >= 5)
```

Both produce:

```text
True
```

### Less than or equal `<=`

```python
print(5 <= 5)
print(5 <= 10)
```

Both produce:

```text
True
```

Comparisons are fundamental to conditions:

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# 3. Assignment Operators

Assignment operators assign values to variables.

The basic assignment operator is:

```python
=
```

Example:

```python
x = 10
```

Python also provides **augmented assignment operators**.

| Operator | Example   | Equivalent             |      |                       |
| -------- | --------- | ---------------------- | ---- | --------------------- |
| `=`      | `x = 5`   | Assign                 |      |                       |
| `+=`     | `x += 5`  | `x = x + 5`            |      |                       |
| `-=`     | `x -= 5`  | `x = x - 5`            |      |                       |
| `*=`     | `x *= 5`  | `x = x * 5`            |      |                       |
| `/=`     | `x /= 5`  | `x = x / 5`            |      |                       |
| `//=`    | `x //= 5` | `x = x // 5`           |      |                       |
| `%=`     | `x %= 5`  | `x = x % 5`            |      |                       |
| `**=`    | `x **= 5` | `x = x ** 5`           |      |                       |
| `&=`     | `x &= 5`  | Bitwise AND assignment |      |                       |
| `        | =`        | `x                     | = 5` | Bitwise OR assignment |
| `^=`     | `x ^= 5`  | Bitwise XOR assignment |      |                       |
| `<<=`    | `x <<= 2` | Left-shift assignment  |      |                       |
| `>>=`    | `x >>= 2` | Right-shift assignment |      |                       |

### Example

```python
x = 10

x += 5

print(x)
```

Output:

```text
15
```

This:

```python
x += 5
```

is equivalent to:

```python
x = x + 5
```

Another example:

```python
x = 10

x *= 3

print(x)
```

Output:

```text
30
```

---

# 4. Logical Operators

Logical operators are used to combine or modify Boolean conditions.

Python has three logical operators:

```text
and
or
not
```

---

## `and`

`and` returns a truthy result only when both operands are truthy.

For Boolean values:

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

Output:

```text
True
False
False
False
```

Example:

```python
age = 25
has_license = True

print(age >= 18 and has_license)
```

Output:

```text
True
```

Both conditions are true.

---

## `or`

`or` is true when at least one operand is truthy.

```python
print(True or False)
print(False or True)
print(False or False)
```

Output:

```text
True
True
False
```

Example:

```python
is_admin = False
is_manager = True

print(is_admin or is_manager)
```

Output:

```text
True
```

---

## `not`

`not` reverses a Boolean value.

```python
print(not True)
print(not False)
```

Output:

```text
False
True
```

Example:

```python
is_logged_in = False

print(not is_logged_in)
```

Output:

```text
True
```

### Important: `and` and `or` return operands

Python's `and` and `or` don't necessarily return `True` or `False`. They return one of their operands.

Example:

```python
print(10 and 20)
```

Output:

```text
20
```

And:

```python
print(0 and 20)
```

Output:

```text
0
```

Similarly:

```python
print(10 or 20)
```

Output:

```text
10
```

This behavior becomes important when working with Python's truthiness and default-value patterns.

---

# 5. Bitwise Operators

Bitwise operators work with the **individual bits of integers**.

The main bitwise operators are:

| Operator | Name        |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left shift  |            |
| `>>`     | Right shift |            |

Consider:

```text
5 = 0101
3 = 0011
```

### Bitwise AND `&`

```python
print(5 & 3)
```

Binary operation:

```text
0101
0011
----
0001
```

Result:

```text
1
```

### Bitwise OR `|`

```python
print(5 | 3)
```

```text
0101
0011
----
0111
```

Result:

```text
7
```

### Bitwise XOR `^`

XOR produces `1` when the corresponding bits are different.

```python
print(5 ^ 3)
```

```text
0101
0011
----
0110
```

Result:

```text
6
```

### Bitwise NOT `~`

```python
print(~5)
```

Output:

```text
-6
```

Python integers use a signed representation consistent with two's-complement-style bitwise semantics, so `~x` follows the relationship:

```text
~x == -(x + 1)
```

Therefore:

```text
~5 = -6
```

### Left shift `<<`

Moves bits to the left:

```python
print(5 << 1)
```

Binary:

```text
0101 → 1010
```

Result:

```text
10
```

For positive integers, shifting left by one position is equivalent to multiplying by 2.

### Right shift `>>`

Moves bits to the right:

```python
print(10 >> 1)
```

Result:

```text
5
```

Bitwise operations are commonly used in areas such as:

* Low-level programming
* Permissions/flags
* Binary data processing
* Networking
* Compression
* Performance-sensitive algorithms

---

# 6. Membership Operators

Membership operators check whether a value exists inside a collection or sequence.

Python has:

```text
in
not in
```

### `in`

```python
names = ["Rahul", "Riya", "Amit"]

print("Riya" in names)
```

Output:

```text
True
```

Because `"Riya"` exists in the list.

### `not in`

```python
names = ["Rahul", "Riya", "Amit"]

print("John" not in names)
```

Output:

```text
True
```

### Strings

Membership also works with strings:

```python
text = "Python Programming"

print("Python" in text)
```

Output:

```text
True
```

And:

```python
print("Java" in text)
```

Output:

```text
False
```

### Dictionaries

Membership testing on a dictionary checks **keys** by default:

```python
student = {
    "name": "Rahul",
    "age": 25
}

print("name" in student)
```

Output:

```text
True
```

But:

```python
print("Rahul" in student)
```

produces:

```text
False
```

because `"Rahul"` is a value, not a key.

---

# 7. Identity Operators

Identity operators determine whether two references point to the **same object**.

Python has:

```text
is
is not
```

### `is`

```python
a = None
b = None

print(a is b)
```

Output:

```text
True
```

Both names refer to the singleton `None` object.

### `is not`

```python
a = None
b = 10

print(a is not b)
```

Output:

```text
True
```

### `==` vs `is`

This distinction is extremely important.

`==` checks **value equality**.

`is` checks **object identity**.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Why?

Both lists contain the same values:

```text
a → [1, 2, 3]
b → [1, 2, 3]
```

so:

```python
a == b
```

is `True`.

But they are separate list objects, so:

```python
a is b
```

is `False`.

### Common use of `is`

The standard way to check for `None` is:

```python
if value is None:
    print("No value")
```

rather than:

```python
if value == None:
    print("No value")
```

---

# 8. Operator Precedence

When an expression contains multiple operators, Python follows rules that determine which operators are evaluated first.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

It does **not** calculate:

```text
(10 + 5) * 2 = 30
```

Instead, multiplication has higher precedence:

```text
10 + (5 * 2)
10 + 10
20
```

### Parentheses

Parentheses can explicitly control evaluation:

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

### Simplified precedence order

From higher to lower precedence:

```text
1. Parentheses / grouping
2. Exponentiation **
3. Unary +, -, ~
4. *, /, //, %
5. +, -
6. <<, >>
7. &
8. ^
9. |
10. Comparisons, in, is
11. not
12. and
13. or
14. Conditional expression
15. Assignment expressions
```

There are additional details and special cases, but this ordering covers the operators introduced here.

### Example

```python
result = 10 + 2 * 3 ** 2

print(result)
```

Evaluation:

```text
3 ** 2 = 9
2 * 9 = 18
10 + 18 = 28
```

Result:

```text
28
```

When readability matters, parentheses are often preferable even when they aren't technically necessary:

```python
result = 10 + (2 * (3 ** 2))
```

---

# 9. Chained Comparisons

Python allows multiple comparisons to be written together.

For example:

```python
age = 25

print(18 <= age <= 60)
```

Output:

```text
True
```

This is equivalent in meaning to:

```python
print(18 <= age and age <= 60)
```

but the chained form is cleaner.

### Another example

```python
x = 10

print(5 < x < 20)
```

Output:

```text
True
```

This means:

```text
5 < x
and
x < 20
```

Both comparisons must be true.

### Three-way comparison

```python
x = 15

print(10 < x < 20)
```

Output:

```text
True
```

### Chaining different comparison operators

Python allows comparison chains such as:

```python
a = 10
b = 20
c = 30

print(a < b < c)
```

Output:

```text
True
```

Conceptually:

```python
a < b and b < c
```

### Important detail

A chained comparison is not simply treated as a series of independent comparisons with repeated evaluation of the middle expression. Python evaluates the middle expressions appropriately and effectively combines the comparisons with `and` semantics.

For normal use, think:

```python
10 < x < 20
```

as:

```python
10 < x and x < 20
```

---

# Quick Summary

| Operator category       | Operators                  | Purpose                     |
| ----------------------- | -------------------------- | --------------------------- |
| **Arithmetic**          | `+ - * / // % **`          | Mathematical operations     |
| **Comparison**          | `== != > < >= <=`          | Compare values              |
| **Assignment**          | `= += -= *= /= //= %= **=` | Assign/update values        |
| **Logical**             | `and or not`               | Combine logical conditions  |
| **Bitwise**             | `& \| ^ ~ << >>`           | Operate on integer bits     |
| **Membership**          | `in`, `not in`             | Check membership            |
| **Identity**            | `is`, `is not`             | Check object identity       |
| **Precedence**          | —                          | Determines evaluation order |
| **Chained comparisons** | `a < b < c`                | Combine comparisons cleanly |

### The three distinctions worth remembering

```python
=
```

**Assignment**

```python
==
```

**Value equality**

```python
is
```

**Object identity**

For example:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

These three concepts are fundamental to understanding Python expressions correctly.
# 🟢 Part 1 — Basic Python

## 4. Strings

A **string** is a sequence of characters used to represent text in Python.

Examples:

```python
name = "Rahul"
city = "Ahmedabad"
message = "Welcome to Python"
```

The type of a string is `str`:

```python
text = "Python"

print(type(text))
```

Output:

```text
<class 'str'>
```

Strings can contain letters, numbers, spaces, symbols, and Unicode characters.

---

# 1. Creating Strings

Strings can be created by placing text inside quotes.

```python
name = "Rahul"
city = 'Ahmedabad'
message = "Hello, Python!"
```

You can also create an empty string:

```python
text = ""
```

An empty string has a length of zero:

```python
print(len(text))
```

Output:

```text
0
```

Numbers inside quotes are still strings:

```python
age = "25"

print(type(age))
```

Output:

```text
<class 'str'>
```

So:

```python
25
```

is an integer, while:

```python
"25"
```

is a string.

---

# 2. Single, Double, and Triple Quotes

Python supports several ways of writing strings.

### Single quotes

```python
name = 'Rahul'
```

### Double quotes

```python
name = "Rahul"
```

Both create the same `str` type.

```python
a = "Python"
b = 'Python'

print(a == b)
```

Output:

```text
True
```

### Choosing between single and double quotes

Quotes are especially useful when the string itself contains a quote.

For example:

```python
message = "It's a beautiful day"
```

Or:

```python
message = 'He said "Hello"'
```

This avoids needing an escape character.

### Triple quotes

Triple single quotes:

```python
message = '''Hello
Python
World'''
```

Triple double quotes:

```python
message = """Hello
Python
World"""
```

Triple-quoted strings can span multiple lines.

They are also commonly used for **docstrings**:

```python
def greet():
    """Return a greeting message."""
    return "Hello"
```

---

# 3. String Indexing

A string is a sequence, so each character has a position called an **index**.

Python uses **zero-based indexing**.

Consider:

```python
text = "Python"
```

Its indexes are:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

You can access a character using square brackets:

```python
print(text[0])
```

Output:

```text
P
```

```python
print(text[3])
```

Output:

```text
h
```

### Negative indexing

Python also supports negative indexes:

```text
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

For example:

```python
print(text[-1])
```

Output:

```text
n
```

And:

```python
print(text[-2])
```

Output:

```text
o
```

### Invalid index

```python
text = "Python"

print(text[10])
```

This raises:

```text
IndexError
```

because index `10` doesn't exist.

---

# 4. String Slicing

**Slicing** extracts a portion of a string.

Basic syntax:

```python
string[start:stop]
```

The `start` index is included, but the `stop` index is excluded.

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

Indexes:

```text
P y t h o n
0 1 2 3 4 5
```

`0:3` means indexes `0`, `1`, and `2`.

### Omitting start

```python
print(text[:3])
```

Output:

```text
Pyt
```

This means start from the beginning.

### Omitting stop

```python
print(text[3:])
```

Output:

```text
hon
```

This means continue until the end.

### Copying the whole string

```python
print(text[:])
```

Output:

```text
Python
```

### Slicing with a step

Syntax:

```python
string[start:stop:step]
```

Example:

```python
text = "Python"

print(text[::2])
```

Output:

```text
Pto
```

It takes every second character.

### Reverse a string

A common slicing technique:

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

The `-1` step moves through the string backwards.

---

# 5. String Concatenation

**Concatenation** means joining strings together.

The `+` operator can concatenate strings:

```python
first_name = "Rahul"
last_name = "Patel"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Rahul Patel
```

The operands must be compatible.

This produces an error:

```python
age = 25

print("Age: " + age)
```

because `age` is an integer.

Convert it first:

```python
print("Age: " + str(age))
```

Output:

```text
Age: 25
```

For modern Python code, f-strings are often more convenient for combining text with values.

---

# 6. String Repetition

The `*` operator can repeat a string.

```python
text = "Python "

print(text * 3)
```

Output:

```text
Python Python Python
```

Another example:

```python
print("-" * 20)
```

Output:

```text
--------------------
```

The repetition count must be an integer.

```python
"Hello" * 3
```

is valid, while:

```python
"Hello" * 2.5
```

raises a `TypeError`.

---

# 7. String Immutability

Python strings are **immutable**.

This means that once a string object is created, its individual characters cannot be changed.

For example:

```python
text = "Python"

text[0] = "J"
```

This raises:

```text
TypeError
```

You cannot modify the existing string character-by-character.

Instead, you create a new string:

```python
text = "Python"

text = "J" + text[1:]

print(text)
```

Output:

```text
Jython
```

String methods also generally return new strings rather than modifying the original.

```python
text = "python"

new_text = text.upper()

print(text)
print(new_text)
```

Output:

```text
python
PYTHON
```

The original `text` remains unchanged.

This is an important consequence of string immutability.

---

# 8. Escape Characters

An **escape sequence** allows special characters to be represented inside strings.

Escape sequences begin with a backslash:

```text
\
```

### Newline `\n`

```python
print("Hello\nPython")
```

Output:

```text
Hello
Python
```

### Tab `\t`

```python
print("Hello\tPython")
```

Output:

```text
Hello    Python
```

### Single quote `\'`

Useful inside a single-quoted string:

```python
text = 'It\'s Python'
```

### Double quote `\"`

```python
text = "He said \"Hello\""
```

### Backslash `\\`

To represent an actual backslash:

```python
path = "C:\\Users\\Rahul"
```

### Common escape sequences

| Sequence | Meaning         |
| -------- | --------------- |
| `\n`     | New line        |
| `\t`     | Tab             |
| `\\`     | Backslash       |
| `\'`     | Single quote    |
| `\"`     | Double quote    |
| `\r`     | Carriage return |
| `\b`     | Backspace       |

---

# 9. Raw Strings

A **raw string** treats backslashes mostly as literal characters rather than interpreting them as escape sequences.

An `r` or `R` is placed before the string:

```python
text = r"Hello\nPython"

print(text)
```

Output:

```text
Hello\nPython
```

Without the `r`:

```python
text = "Hello\nPython"

print(text)
```

Output:

```text
Hello
Python
```

Raw strings are particularly useful for things such as:

* Regular expressions
* Windows-style paths
* Strings containing many backslashes

Example:

```python
path = r"C:\Users\Rahul\Documents"
```

The backslashes are treated as literal backslashes.

### Important limitation

Raw strings do not mean that *every* character loses special meaning. In particular, a raw string cannot end with a single backslash:

```python
r"C:\Users\"
```

This is invalid because the final backslash escapes the closing quote at the lexical level.

---

# 10. String Methods

Strings provide many built-in methods for common text operations.

Examples include:

```python
upper()
lower()
strip()
split()
join()
replace()
find()
count()
startswith()
endswith()
```

Methods are called using dot notation:

```python
text.upper()
```

Most string methods return a **new string** or another result because strings are immutable.

For example:

```python
text = "python"

result = text.upper()

print(result)
```

Output:

```text
PYTHON
```

The original string remains:

```text
python
```

---

# 11. `upper()`

`upper()` returns a new string with applicable letters converted to uppercase.

```python
text = "Hello Python"

print(text.upper())
```

Output:

```text
HELLO PYTHON
```

The original is unchanged:

```python
text = "Hello Python"

result = text.upper()

print(text)
print(result)
```

Output:

```text
Hello Python
HELLO PYTHON
```

---

# 12. `lower()`

`lower()` returns a lowercase version of the string.

```python
text = "Hello Python"

print(text.lower())
```

Output:

```text
hello python
```

It is commonly used when performing case-insensitive comparisons:

```python
name = "RAHUL"

if name.lower() == "rahul":
    print("Match")
```

Output:

```text
Match
```

---

# 13. `strip()`

`strip()` removes whitespace from the beginning and end of a string.

```python
text = "   Python   "

print(text.strip())
```

Output:

```text
Python
```

It does not remove spaces from the middle:

```python
text = "   Hello Python   "

print(text.strip())
```

Result:

```text
Hello Python
```

### `lstrip()`

Removes whitespace from the left:

```python
text = "   Python"

print(text.lstrip())
```

### `rstrip()`

Removes whitespace from the right:

```python
text = "Python   "

print(text.rstrip())
```

`strip()` can also remove specified characters from both ends:

```python
text = "---Python---"

print(text.strip("-"))
```

Output:

```text
Python
```

It removes characters from the ends, not arbitrary occurrences throughout the string.

---

# 14. `split()`

`split()` divides a string into a list of substrings.

```python
text = "Python is easy"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

By default, whitespace is used as the separator.

### Using a specific separator

```python
data = "apple,banana,orange"

items = data.split(",")

print(items)
```

Output:

```text
['apple', 'banana', 'orange']
```

You can also limit the number of splits:

```python
text = "one-two-three-four"

print(text.split("-", 2))
```

Output:

```text
['one', 'two', 'three-four']
```

---

# 15. `join()`

`join()` combines multiple strings into one string using a separator.

Example:

```python
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is easy
```

Here:

```python
" ".join(words)
```

uses a space as the separator.

### Comma-separated values

```python
items = ["apple", "banana", "orange"]

result = ", ".join(items)

print(result)
```

Output:

```text
apple, banana, orange
```

### Important

The elements being joined must be strings.

This will fail:

```python
numbers = [1, 2, 3]

print(", ".join(numbers))
```

because the list contains integers.

Convert them first:

```python
numbers = [1, 2, 3]

result = ", ".join(str(number) for number in numbers)

print(result)
```

Output:

```text
1, 2, 3
```

---

# 16. `replace()`

`replace()` replaces occurrences of one substring with another.

```python
text = "I like Java"

result = text.replace("Java", "Python")

print(result)
```

Output:

```text
I like Python
```

The original string isn't changed:

```python
text = "I like Java"

text.replace("Java", "Python")

print(text)
```

Output:

```text
I like Java
```

Because strings are immutable, you need to store the returned string if you want to use the modified version:

```python
text = text.replace("Java", "Python")
```

You can also specify how many occurrences to replace:

```python
text = "apple apple apple"

print(text.replace("apple", "orange", 2))
```

Output:

```text
orange orange apple
```

---

# 17. `find()`

`find()` searches for a substring and returns its first index.

```python
text = "Hello Python"

print(text.find("Python"))
```

Output:

```text
6
```

Because:

```text
H e l l o   P y t h o n
0 1 2 3 4 5 6 ...
```

If the substring isn't found, `find()` returns:

```text
-1
```

Example:

```python
print(text.find("Java"))
```

Output:

```text
-1
```

You can also specify a starting position:

```python
text = "Python Python"

print(text.find("Python", 1))
```

This searches starting from index `1`.

### `find()` vs `index()`

`find()` returns `-1` if the substring doesn't exist.

`index()` raises a `ValueError` instead.

---

# 18. `count()`

`count()` returns the number of occurrences of a substring.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

Another example:

```python
text = "Python Python"

print(text.count("Python"))
```

Output:

```text
2
```

It can also search within a specified range:

```python
text = "banana"

print(text.count("a", 0, 4))
```

The search range follows normal Python slicing-style boundaries: start is included and stop is excluded.

---

# 19. `startswith()`

`startswith()` checks whether a string begins with a particular substring.

It returns a Boolean.

```python
text = "Python Programming"

print(text.startswith("Python"))
```

Output:

```text
True
```

Example:

```python
print(text.startswith("Java"))
```

Output:

```text
False
```

You can specify a starting position:

```python
text = "Hello Python"

print(text.startswith("Python", 6))
```

Output:

```text
True
```

---

# 20. `endswith()`

`endswith()` checks whether a string ends with a particular substring.

```python
filename = "report.pdf"

print(filename.endswith(".pdf"))
```

Output:

```text
True
```

Another example:

```python
filename = "image.png"

print(filename.endswith(".pdf"))
```

Output:

```text
False
```

It can also accept multiple suffixes:

```python
filename = "photo.jpg"

print(filename.endswith((".jpg", ".png", ".gif")))
```

Output:

```text
True
```

---

# 21. String Formatting

String formatting means inserting values into text in a structured way.

Instead of:

```python
name = "Rahul"
age = 25

message = "My name is " + name + " and I am " + str(age) + " years old."

print(message)
```

modern Python provides cleaner formatting techniques.

The main approaches include:

* f-strings
* `str.format()`
* Older `%` formatting

The most commonly preferred modern approach is the **f-string**.

---

# 22. f-Strings

An **f-string** is a string prefixed with `f` or `F`.

It allows expressions to be placed inside `{}`.

Example:

```python
name = "Rahul"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)
```

Output:

```text
My name is Rahul and I am 25 years old.
```

You can put expressions inside the braces:

```python
a = 10
b = 20

print(f"Total: {a + b}")
```

Output:

```text
Total: 30
```

### Formatting numbers

```python
price = 99.5678

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 99.57
```

Here:

```text
:.2f
```

means format the number as a floating-point value with two digits after the decimal point.

### Expressions

```python
name = "Rahul"

print(f"Name length: {len(name)}")
```

Output:

```text
Name length: 5
```

f-strings are concise, readable, and powerful.

---

# 23. `format()`

The `format()` method provides another way to insert values into strings.

Example:

```python
name = "Rahul"
age = 25

message = "My name is {} and I am {} years old.".format(name, age)

print(message)
```

Output:

```text
My name is Rahul and I am 25 years old.
```

### Positional arguments

You can specify positions:

```python
message = "{0} is {1} years old.".format("Rahul", 25)

print(message)
```

Output:

```text
Rahul is 25 years old.
```

### Named arguments

```python
message = "My name is {name} and I am {age}.".format(
    name="Rahul",
    age=25
)

print(message)
```

Output:

```text
My name is Rahul and I am 25.
```

### Formatting numbers

```python
price = 99.5678

print("Price: {:.2f}".format(price))
```

Output:

```text
Price: 99.57
```

`format()` is still useful, especially when formatting templates or working with code that predates f-strings.

---

# 24. String Interpolation

**String interpolation** means inserting values or expressions into a string.

For example:

```python
name = "Rahul"
age = 25

message = f"{name} is {age} years old."

print(message)
```

Here:

```text
{name}
{age}
```

are placeholders whose values are inserted into the resulting string.

Python supports several historical and modern approaches to interpolation.

### f-string

```python
name = "Rahul"

print(f"Hello, {name}")
```

### `format()`

```python
name = "Rahul"

print("Hello, {}".format(name))
```

### `%` formatting

Older Python code may contain:

```python
name = "Rahul"
age = 25

print("Name: %s, Age: %d" % (name, age))
```

Output:

```text
Name: Rahul, Age: 25
```

The `%` style is an older formatting mechanism. For modern Python code, f-strings are generally the clearest choice when the string and values are known at the same point.

---

# Quick Summary

| Topic                           | Core idea                                           |
| ------------------------------- | --------------------------------------------------- |
| **Creating strings**            | Use quotes to create `str` objects                  |
| **Single/double/triple quotes** | Different ways of defining strings                  |
| **Indexing**                    | Access individual characters using indexes          |
| **Slicing**                     | Extract portions of strings                         |
| **Concatenation**               | Join strings using `+`                              |
| **Repetition**                  | Repeat strings using `*`                            |
| **Immutability**                | Existing string objects cannot be modified          |
| **Escape characters**           | Represent special characters such as `\n` and `\t`  |
| **Raw strings**                 | Treat backslashes mostly as literal characters      |
| **String methods**              | Built-in operations for manipulating/searching text |
| **`upper()`**                   | Convert applicable letters to uppercase             |
| **`lower()`**                   | Convert applicable letters to lowercase             |
| **`strip()`**                   | Remove characters/whitespace from both ends         |
| **`split()`**                   | Divide a string into a list                         |
| **`join()`**                    | Combine strings using a separator                   |
| **`replace()`**                 | Replace substring occurrences                       |
| **`find()`**                    | Find the first occurrence's index                   |
| **`count()`**                   | Count occurrences                                   |
| **`startswith()`**              | Check beginning of a string                         |
| **`endswith()`**                | Check ending of a string                            |
| **String formatting**           | Insert values into text                             |
| **f-strings**                   | Modern, concise formatting using `{}`               |
| **`format()`**                  | Formatting using placeholders and `.format()`       |
| **String interpolation**        | General concept of inserting values into strings    |

### Core string model

A useful representation is:

```python
text = "Python"
```

```text
 P   y   t   h   o   n
 ↑   ↑   ↑   ↑   ↑   ↑
 0   1   2   3   4   5
```

And remember that strings are immutable:

```python
text = "Python"

# text[0] = "J"     ❌
text = "Jython"      # ✅ creates/references a new string
```

This combination of **sequence behavior + indexing/slicing + immutability + string methods + formatting** forms the foundation for working with text in Python.
