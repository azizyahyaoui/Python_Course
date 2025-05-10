# Python 2025

```
    Yahyaoui Med Aziz  | 02182025
    Editor: Pycharm
    Defintions: ChatGPT
    Other:
    
```
   - 🔗 [devdocs.io](https://www.python.org/downloads/https://devdocs.io/python~3.13/reference/index) 
   - 🔗 [Youtube Video](https://youtu.be/ix9cRaBkVe0)
  


Python is a high-level, interpreted programming language that has become one of the most widely used tools in the world of software development. Known for its simplicity and readability, Python is particularly popular among beginners while also being powerful enough for advanced applications such as web development, data analysis, artificial intelligence, automation, and more. 

The language was created by Dutch programmer Guido van Rossum in December 1989 during his time at Centrum Wiskunde & Informatica (CWI) in the Netherlands. Van Rossum aimed to design a language that was easy to learn, versatile, and capable of addressing the limitations of the ABC programming language, which he had worked on previously. Python’s first version, 0.9.0, was released in February 1991. The name "Python" was inspired not by the snake but by the British comedy series *Monty Python’s Flying Circus*, reflecting Van Rossum's desire to make programming both accessible and enjoyable.

Python's clean syntax relies on indentation rather than brackets or semicolons, promoting code readability and simplicity. These features have made it a favorite for developers across various domains, from scientific research to web development

---

## **Introduction To The Basics🚀**

## **Installing Python 🖥️**
Before getting started, you need to install Python. You can download it from the official Python website:  
🔗 [Download Python](https://www.python.org/downloads/)  

After installation, you can check if Python is installed by running the following command in your terminal or command prompt:  
```sh
python --version
```
or  
```sh
python3 --version
```

---

## **Writing Your First Python Program 🖊️**
You can write Python code in a file with a `.py` extension or run it directly in an interactive shell (REPL).  

Example:  
```python
print("Hello, World!")
```
Run the script by saving it as `hello.py` and executing:  
```sh
python hello.py
```

---

## **Basic Syntax and Concepts 📜**

### **Variables and Data Types**  
Python supports multiple data types such as integers, floats, strings, and booleans.  

```python
# Integer
age = 25

# Floating-point number
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

print(name, "is", age, "years old.")

```

### **Python Type Annotations**  

Python is dynamically typed, meaning you don’t have to explicitly define variable types. However, **type annotations** (introduced in **Python 3.5**) allow you to specify the expected types of variables, function arguments, and return values.  

---

#### **1. Basic Type Annotations**  

#### **1.1 Variable Annotations**
```python
name: str = "Alice"
age: int = 25
height: float = 5.9
is_student: bool = True
```

#### **1.2 Function Annotations**
```python
def add(x: int, y: int) -> int:
    return x + y
```
🔹 `x: int, y: int` → Arguments must be integers  
🔹 `-> int` → Function returns an integer  

#### **1.3 Using `mypy` for Type Checking**
To check for type errors, install **mypy**:
```bash
pip install mypy
```
Run type checking:
```bash
mypy script.py
```

---

#### **2. Type Hints for Collections**  

#### **2.1 Lists, Tuples, Sets, and Dictionaries**
Use **`list`**, **`tuple`**, **`set`**, and **`dict`** for annotations.

```python
numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Alice", "Bob"]
coordinates: tuple[float, float] = (10.5, 20.3)
unique_values: set[int] = {1, 2, 3}
user_ages: dict[str, int] = {"Alice": 25, "Bob": 30}
```

---

#### **3. Using `typing` Module for Advanced Types**
The `typing` module provides **generic types** for better type hints.

#### **3.1 Importing from `typing`**
```python
from typing import List, Tuple, Set, Dict

numbers: List[int] = [1, 2, 3]
coordinates: Tuple[float, float] = (10.5, 20.3)
unique_values: Set[str] = {"apple", "banana"}
user_ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
```

---

#### **4. Optional and Union Types**  

#### **4.1 `Optional` (Nullable Values)**
Use `Optional[T]` when a variable **can be `None`**.
```python
from typing import Optional

def greet(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello!"
```
🔹 Equivalent to `Union[str, None]`  

#### **4.2 `Union` (Multiple Allowed Types)**
Use `Union[T1, T2]` when a variable **can have multiple types**.
```python
from typing import Union

def process_value(value: Union[int, float]) -> float:
    return value * 2.5
```
🔹 Accepts both `int` and `float`, but always returns a `float`.

---

#### **5. Function Annotations with `Callable`**
Use `Callable` to define **functions as parameters**.

```python
from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def multiply(x: int, y: int) -> int:
    return x * y

result = apply_function(multiply, 3, 4)
print(result)  # Output: 12
```
🔹 `Callable[[int, int], int]` → Function takes two `int` arguments and returns an `int`.

---

#### **6. Custom Type Definitions (`TypeAlias`)**
Use `TypeAlias` to create **custom type names**.

```python
from typing import TypeAlias

Coordinates: TypeAlias = tuple[float, float]

def get_location() -> Coordinates:
    return (40.7128, -74.0060)
```
🔹 `Coordinates` is an alias for `tuple[float, float]`.

---

#### **7. `TypedDict` for Structured Dictionaries**  
Use `TypedDict` to specify expected keys and types in dictionaries.

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

person: Person = {"name": "Alice", "age": 25}
```

---

#### **8. Generics in Type Annotations**
Use `TypeVar` to create **generic types**.

```python
from typing import TypeVar

T = TypeVar("T")

def get_first_element(items: list[T]) -> T:
    return items[0]

print(get_first_element([1, 2, 3]))  # Output: 1
print(get_first_element(["Alice", "Bob"]))  # Output: "Alice"
```
🔹 `T` is a placeholder for any type.

---

#### **9. `Any` Type (Disables Type Checking)**
Use `Any` when a variable can be **of any type**.

```python
from typing import Any

def process(value: Any) -> None:
    print(value)

process(123)    # Works
process("hello")# Works
```

---

#### **10. Type Checking in Classes**
Annotate instance variables and methods in classes.

```python
class Car:
    def __init__(self, brand: str, year: int):
        self.brand: str = brand
        self.year: int = year

    def get_info(self) -> str:
        return f"{self.brand} ({self.year})"

car = Car("Tesla", 2023)
print(car.get_info())  # Output: Tesla (2023)
```

---

#### **11. `Literal` for Fixed Values**
Use `Literal` to restrict values to specific constants.

```python
from typing import Literal

def set_status(status: Literal["active", "inactive", "pending"]) -> str:
    return f"Status changed to {status}"

print(set_status("active"))  # ✅ Works
# print(set_status("unknown"))  # ❌ Type error
```

---

#### **Summary Table**
| Concept | Syntax Example |
|---------|--------------|
| **Basic Annotations** | `x: int = 10` |
| **Function Annotations** | `def add(x: int, y: int) -> int:` |
| **Lists, Tuples, Dicts** | `names: list[str]`, `user: dict[str, int]` |
| **Optional Type** | `Optional[str]` (can be `None`) |
| **Union Type** | `Union[int, float]` (multiple types) |
| **Callable Functions** | `Callable[[int, int], int]` |
| **Custom Type Alias** | `Coordinates: TypeAlias = tuple[float, float]` |
| **Typed Dictionary** | `class Person(TypedDict): name: str; age: int` |
| **Generics (`TypeVar`)** | `T = TypeVar('T')` |
| **Disable Type Checking** | `Any` |
| **Restrict Values (`Literal`)** | `Literal["open", "closed"]` |

---


### **3.2 Input and Output**  
Python allows user input using the `input()` function.  

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

### **3.3 Type Casting** 

Type casting in Python refers to converting one data type into another. This can be useful when you need to ensure that data is in the correct format for operations or functions. Here are some common type casting techniques:

1. **Integer Conversion**: `int()`
   - Converts a string or float to an integer.
   ```python
   x = int("10")   # 10
   y = int(10.5)   # 10
   ```

2. **Float Conversion**: `float()`
   - Converts a string or integer to a float.
   ```python
   x = float("10.5")  # 10.5
   y = float(10)      # 10.0
   ```

3. **String Conversion**: `str()`
   - Converts an integer or float to a string.
   ```python
   x = str(10)       # "10"
   y = str(10.5)     # "10.5"
   ```

4. **List Conversion**: `list()`
   - Converts a string or tuple to a list.
   ```python
   x = list("hello")  # ['h', 'e', 'l', 'l', 'o']
   y = list((1, 2, 3)) # [1, 2, 3]
   ```

5. **Tuple Conversion**: `tuple()`
   - Converts a list or string to a tuple.
   ```python
   x = tuple([1, 2, 3])  # (1, 2, 3)
   y = tuple("abc")      # ('a', 'b', 'c')
   ```

6. **Set Conversion**: `set()`
   - Converts a list or string to a set (removes duplicates).
   ```python
   x = set([1, 2, 2, 3])  # {1, 2, 3}
   y = set("hello")       # {'h', 'e', 'l', 'o'}
   ```

#### Type Casting Examples

Here are a few examples demonstrating type casting:

```python
# Example 1: Converting a string to an integer
num_str = "123"
num_int = int(num_str)  # 123

# Example 2: Converting a float to a string
float_num = 45.67
float_str = str(float_num)  # "45.67"

# Example 3: Combining different types
a = "5"
b = 10
result = int(a) + b  # 15
```

#### Notes

- **Invalid Conversions**: Attempting to convert incompatible types will raise a `ValueError`.
  ```python
  invalid_int = int("abc")  # Raises ValueError
  ```

- **Type Checking**: Use `type()` to check the type of a variable.
  ```python
  print(type(num_int))  # <class 'int'>
  ```

Understanding type casting is essential for effective data manipulation in Python.



### **3.4 Operators**  
Python supports arithmetic, comparison, logical, and assignment operators.  

```python
x = 10
y = 5

# Arithmetic Operators
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus

# Comparison Operators
print(x > y)  # True
print(x == y) # False

# Logical Operators
print(x > 5 and y < 10)  # True
print(x > 5 or y > 10)   # True
print(not (x > 5))       # False
```

---

##  **Math Functions in Python 🧮**

Python provides various mathematical functions through the built-in `math` module. These functions help perform complex mathematical operations like exponentiation, logarithms, trigonometry, square roots, and more.

### **1. Importing the `math` Module**
To use math functions, you need to import the `math` module:
```python
import math
```

---

### **2. Basic Math Functions**

#### **2.1 Rounding Functions**
```python
import math

print(math.ceil(4.3))   # 5 (Rounds up)
print(math.floor(4.7))  # 4 (Rounds down)
print(round(4.5))       # 4 (Rounds to the nearest integer)
```

---

### **3. Power and Logarithmic Functions**
#### **3.1 Exponentiation and Square Root**
```python
import math

print(math.pow(2, 3))   # 8.0 (2^3)
print(math.sqrt(25))    # 5.0 (Square root)
```
**Alternative:** You can also use `**` for exponentiation:
```python
print(2 ** 3)  # 8
```

#### **3.2 Logarithmic Functions**
```python
import math

print(math.log(10))       # Natural log (ln) of 10
print(math.log10(100))    # Log base 10
print(math.log2(8))       # Log base 2
```

---

### **4. Trigonometric Functions**
Python provides trigonometric functions like sine, cosine, and tangent.

```python
import math

angle = math.radians(30)  # Convert degrees to radians

print(math.sin(angle))  # 0.5
print(math.cos(angle))  # 0.866
print(math.tan(angle))  # 0.577
```
 **Converting between Degrees and Radians**
```python
print(math.degrees(math.pi))  # 180 degrees
print(math.radians(180))      # 3.14159 radians (π)
```

---

### **5. Constants in `math` Module**
Python's `math` module includes useful mathematical constants:

```python
import math

print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045 "The base of the natural logarithm and exponential function. It is sometimes called Euler's number"
print(math.tau)   # 6.283185307179586 (2π)
print(math.inf)   # Infinity
print(math.nan)   # Not-a-Number (NaN)
```

---

### **6. Factorial and Combinations**
#### **6.1 Factorial**
```python
import math

print(math.factorial(5))  # 120 (5! = 5 × 4 × 3 × 2 × 1)
```

#### **6.2 Combinations and Permutations**
```python
import math

print(math.comb(5, 2))  # 10 (Combinations: 5 choose 2)
print(math.perm(5, 2))  # 20 (Permutations: 5 P 2)
```

---

### **7. Hyperbolic Functions**
```python
import math

print(math.sinh(1))  # 1.175
print(math.cosh(1))  # 1.543
print(math.tanh(1))  # 0.761
```

---

### **8. Greatest Common Divisor (GCD) and Least Common Multiple (LCM)**
```python
import math

print(math.gcd(12, 18))  # 6 (Greatest Common Divisor)
print(math.lcm(12, 18))  # 36 (Least Common Multiple)
```

---

### **9. Absolute Value and Sign Checking**
```python
import math

print(abs(-10))       # 10 (Absolute value)
print(math.copysign(5, -3))  # -5 (Copies sign of second argument)
```

---

### **10. Random Numbers (Using `random` Module)**
Python also has the `random` module for generating random numbers:

```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.random())        # Random float between 0 and 1
print(random.uniform(1, 10))  # Random float between 1 and 10
```

---

## **Conditional Statements in Python 🚦**

Conditional statements in Python allow you to control the flow of your program based on conditions. The most common conditional statements are:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Short-hand `if` (Ternary Operator)

---

### **1. `if` Statement**
The `if` statement executes a block of code only if the condition is `True`.

```python
age = 18

if age >= 18:
    print("You are eligible to vote!")  # This will execute if age is 18 or more.
```

---

### **2. `if-else` Statement**
The `if-else` statement allows you to execute one block of code if the condition is `True`, and another block if it is `False`.

```python
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```
**Output:**  
```
You are not eligible to vote.
```

---

### **3. `if-elif-else` Statement**
The `if-elif-else` statement checks multiple conditions in order.

```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```
**Output:**  
```
Grade: B
```

---

### **4. Nested `if` Statement**
A nested `if` statement means having an `if` inside another `if`.

```python
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number or zero")
```
**Output:**
```
Positive number
Even number
```

---

### **5. Short-Hand `if` (Ternary Operator)**
Python allows writing `if-else` in a single line.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```
**Output:**  
```
Adult
```

---

### **6. Using `and`, `or`, `not` in Conditional Statements**
### **Using `and`**
Both conditions must be `True`.
```python
age = 25
income = 5000

if age > 18 and income > 3000:
    print("Eligible for loan")
```

### **Using `or`**
At least one condition must be `True`.
```python
age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Allowed to enter")
```

### **Using `not`**
Negates the condition.
```python
is_raining = False

if not is_raining:
    print("Go outside!")
```

---

### **7. `pass` Statement**
If you don’t want to write any code inside an `if` block, use `pass` as a placeholder.

```python
age = 20

if age > 18:
    pass  # Placeholder for future code
else:
    print("You are underage.")
```

---

### **8. Example: Checking Even or Odd**
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
**Input:** `7`  
**Output:** `Odd number`

---

## **Python String Methods 📝**

Python provides various built-in methods to manipulate and work with strings.

---

### **1. Changing Case**
#### **1.1 Convert to Uppercase - `upper()`**
```python
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
```

#### **1.2 Convert to Lowercase - `lower()`**
```python
text = "Hello World"
print(text.lower())  # Output: hello world
```

#### **1.3 Capitalize First Letter - `capitalize()`**
```python
text = "hello world"
print(text.capitalize())  # Output: Hello world
```

#### **1.4 Capitalize Each Word - `title()`**
```python
text = "hello world"
print(text.title())  # Output: Hello World
```

#### **1.5 Swap Case - `swapcase()`**
```python
text = "Hello WoRlD"
print(text.swapcase())  # Output: hELLO wOrLd
```

---

### **2. Checking and Finding Substrings**
#### **2.1 Check if String Starts with a Prefix - `startswith()`**
```python
text = "Hello Python"
print(text.startswith("Hello"))  # Output: True
```

#### **2.2 Check if String Ends with a Suffix - `endswith()`**
```python
text = "Hello Python"
print(text.endswith("Python"))  # Output: True
```

#### **2.3 Find Substring Position - `find()`**
Returns the first occurrence index of the substring, or `-1` if not found.
```python
text = "Hello Python"
print(text.find("Python"))  # Output: 6
print(text.find("Java"))    # Output: -1
```

#### **2.4 Find Last Occurrence - `rfind()`**
```python
text = "Hello Python, Python is fun!"
print(text.rfind("Python"))  # Output: 13
```

#### **2.5 Count Occurrences of a Substring - `count()`**
```python
text = "apple banana apple orange apple"
print(text.count("apple"))  # Output: 3
```

---

### **3. Modifying Strings**
#### **3.1 Replace a Substring - `replace()`**
```python
text = "I love Java"
print(text.replace("Java", "Python"))  # Output: I love Python
```

#### **3.2 Remove Leading and Trailing Spaces - `strip()`**
```python
text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
```

#### **3.3 Remove Leading Spaces - `lstrip()`**
```python
text = "   Hello"
print(text.lstrip())  # Output: "Hello"
```

#### **3.4 Remove Trailing Spaces - `rstrip()`**
```python
text = "Hello   "
print(text.rstrip())  # Output: "Hello"
```

---

### **4. Splitting and Joining Strings**
#### **4.1 Split String into a List - `split()`**
```python
text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']
```

#### **4.2 Split by Whitespace - `split()`**
```python
text = "Hello World Python"
print(text.split())  # Output: ['Hello', 'World', 'Python']
```

#### **4.3 Join a List into a String - `join()`**
```python
words = ["Hello", "World", "Python"]
print(" ".join(words))  # Output: "Hello World Python"
```

---

### **5. Checking String Content**
#### **5.1 Check if String Contains Only Digits - `isdigit()`**
```python
text = "12345"
print(text.isdigit())  # Output: True
```

#### **5.2 Check if String Contains Only Alphabets - `isalpha()`**
```python
text = "Python"
print(text.isalpha())  # Output: True
```

#### **5.3 Check if String Contains Only Alphanumeric Characters - `isalnum()`**
```python
text = "Python123"
print(text.isalnum())  # Output: True
```

#### **5.4 Check if String Contains Only Lowercase Letters - `islower()`**
```python
text = "hello"
print(text.islower())  # Output: True
```

#### **5.5 Check if String Contains Only Uppercase Letters - `isupper()`**
```python
text = "HELLO"
print(text.isupper())  # Output: True
```

#### **5.6 Check if String is Title Cased - `istitle()`**
```python
text = "Hello World"
print(text.istitle())  # Output: True
```

---

### **6. String Formatting**
#### **6.1 Using `format()`**
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.
```

#### **6.2 Using f-Strings (Python 3.6+)**
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 25 years old.
```

---

### **7. Centering, Justifying, and Padding**
#### **7.1 Center Align - `center()`**
```python
text = "Python"
print(text.center(20, "-"))  # Output: "-------Python-------"
```

#### **7.2 Left Align - `ljust()`**
```python
text = "Python"
print(text.ljust(10, "*"))  # Output: "Python****"
```

#### **7.3 Right Align - `rjust()`**
```python
text = "Python"
print(text.rjust(10, "*"))  # Output: "****Python"
```

---

### **8. Checking String Prefixes and Suffixes**
#### **8.1 `startswith()`**
```python
text = "Python programming"
print(text.startswith("Python"))  # Output: True
```

#### **8.2 `endswith()`**
```python
text = "Python programming"
print(text.endswith("ing"))  # Output: True
```

---

### **9. Encoding and Decoding Strings**
```python
text = "Hello"
encoded_text = text.encode("utf-8")  # Encoding
print(encoded_text)  # Output: b'Hello'

decoded_text = encoded_text.decode("utf-8")  # Decoding
print(decoded_text)  # Output: Hello
```

---

### **10. String length: `len()`**

```python
text = "hello world"
length = len(text)
print(length)  # 
```

### **11. Example: Using Multiple String Methods**
```python
text = "  hello world! Python is fun.  "

# Apply multiple string methods
formatted_text = text.strip().capitalize().replace("Python", "Coding")

print(formatted_text)
# Output: "Hello world! Coding is fun."
```

---

## **Python Format Specifiers 🎯**

Format specifiers in Python are used to format strings, numbers, and other data types in a structured way. They are mainly used with:  
- **`printf`-style formatting (`%` operator)**
- **`str.format()` method**
- **f-strings (formatted string literals, available from Python 3.6)**  

---

### **1. Using `%` Format Specifiers (Old Style)**
Python provides C-style format specifiers using the `%` operator.

### **Common `%` Format Specifiers**
| Format Specifier | Description | Example |
|-----------------|-------------|---------|
| `%s` | String | `"Hello %s" % "Alice"` → `"Hello Alice"` |
| `%d` | Integer | `"Age: %d" % 25` → `"Age: 25"` |
| `%f` | Floating point (default 6 decimals) | `"PI: %f" % 3.14159` → `"PI: 3.141590"` |
| `%.2f` | Floating point (2 decimal places) | `"PI: %.2f" % 3.14159` → `"PI: 3.14"` |
| `%x` | Hexadecimal (lowercase) | `"Hex: %x" % 255` → `"Hex: ff"` |
| `%X` | Hexadecimal (uppercase) | `"Hex: %X" % 255` → `"Hex: FF"` |
| `%o` | Octal | `"Octal: %o" % 10` → `"Octal: 12"` |
| `%e` | Scientific notation (lowercase) | `"Sci: %e" % 1234.5678` → `"Sci: 1.234568e+03"` |
| `%E` | Scientific notation (uppercase) | `"Sci: %E" % 1234.5678` → `"Sci: 1.234568E+03"` |

### **Example Usage:**
```python
name = "Alice"
age = 25
height = 5.6789

print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))
# Output: Name: Alice, Age: 25, Height: 5.68
```

---

### **2. Using `str.format()` Method**
The `str.format()` method provides more flexibility and readability.

### **Example Usage:**
```python
name = "Bob"
age = 30
salary = 45678.90123

print("Name: {}, Age: {}, Salary: {:.2f}".format(name, age, salary))
# Output: Name: Bob, Age: 30, Salary: 45678.90
```

### **Using Positional Arguments**
```python
print("Hello {0}, you are {1} years old.".format("Alice", 25))
# Output: Hello Alice, you are 25 years old.
```

### **Using Named Arguments**
```python
print("Name: {name}, Age: {age}".format(name="Charlie", age=40))
# Output: Name: Charlie, Age: 40
```

---

### **3. Using f-strings (Python 3.6+)**
f-strings provide the most modern and readable way to format strings.

### **Example Usage:**
```python
name = "David"
age = 28
score = 92.5678

print(f"Name: {name}, Age: {age}, Score: {score:.2f}")
# Output: Name: David, Age: 28, Score: 92.57
```

### **f-strings with Expressions**
```python
x = 5
y = 10
print(f"Sum: {x + y}, Multiplication: {x * y}")
# Output: Sum: 15, Multiplication: 50
```

### **f-strings with Formatting**
```python
pi = 3.1415926535
print(f"Pi: {pi:.3f}")  # Output: Pi: 3.142
print(f"Hex: {255:X}")   # Output: Hex: FF
print(f"Scientific: {1234.5678:E}")  # Output: Scientific: 1.234568E+03
```

---

### **4. Format Specifiers in `str.format()` and f-strings**
| Specifier | Meaning | Example |
|-----------|---------|---------|
| `{:.2f}` | 2 decimal places | `3.14159 → 3.14` |
| `{:.3e}` | Scientific notation | `12345 → 1.235e+04` |
| `{:+d}` | Signed integer | `5 → +5` |
| `{:<10}` | Left align (width 10) | `"Hi"` → `"Hi        "` |
| `{:>10}` | Right align (width 10) | `"Hi"` → `"        Hi"` |
| `{:^10}` | Center align (width 10) | `"Hi"` → `"    Hi    "` |
| `{:b}` | Binary format | `10 → 1010` |
| `{:o}` | Octal format | `10 → 12` |
| `{:x}` | Hexadecimal (lowercase) | `255 → ff` |
| `{:X}` | Hexadecimal (uppercase) | `255 → FF` |

### **Example Usage:**
```python
num = 255

print("Binary: {:b}".format(num))   # Output: Binary: 11111111
print("Octal: {:o}".format(num))    # Output: Octal: 377
print("Hex: {:x}".format(num))      # Output: Hex: ff
print("Right Aligned: {:>10}".format(42))  # Output: '        42'
print("Left Aligned: {:<10}".format(42))   # Output: '42        '
print("Centered: {:^10}".format(42))       # Output: '    42    '
```

---

### **5. Comparing Methods**
| Method | Readability | Performance | Flexibility |
|--------|------------|------------|-------------|
| `%` (Old Style) | ❌ Less readable | ⚡ Fast | ❌ Less flexible |
| `str.format()` | ✅ Readable | 🚀 Good | ✅ Flexible |
| f-strings | ✅✅ Most readable | ⚡⚡ Fastest | ✅✅ Very flexible |

---

## **Python String Indexing 🔢**

In Python, **strings are sequences of characters**, and each character has a unique position (index) within the string. String indexing allows us to access individual characters using their index positions.

---

### **1. Types of String Indexing**
Python supports:
1. **Positive Indexing** (Left to Right, starting from `0`)
2. **Negative Indexing** (Right to Left, starting from `-1`)

---

### **2. Positive Indexing (Left to Right)**
- The first character has an index of `0`.
- The second character has an index of `1`, and so on.

#### **Example:**
```python
text = "Python"

print(text[0])  # P
print(text[1])  # y
print(text[5])  # n
```

#### **String Layout (Positive Indexing)**
```
 P   y   t   h   o   n
 0   1   2   3   4   5
```

---

### **3. Negative Indexing (Right to Left)**
- The last character has an index of `-1`.
- The second last character has an index of `-2`, and so on.

#### **Example:**
```python
text = "Python"

print(text[-1])  # n
print(text[-2])  # o
print(text[-6])  # P
```

#### **String Layout (Negative Indexing)**
```
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

---

### **4. Accessing Characters using Indexing**
#### **Example:**
```python
word = "OpenAI"
print(word[0])   # O
print(word[-1])  # I
print(word[3])   # n
```

---

### **5. IndexError: Out of Range**
If you try to access an index that is out of range, Python will raise an error.

#### **Example:**
```python
text = "Python"

print(text[10])  # ❌ IndexError: string index out of range
```

---

### **6. Using Indexing in a Loop**
You can iterate through a string using indexing.

#### **Example:**
```python
text = "Hello"

for i in range(len(text)):  
    print(f"Index {i}: {text[i]}")
```

#### **Output:**
```
Index 0: H
Index 1: e
Index 2: l
Index 3: l
Index 4: o
```

---

### **7. String Immutability**
Strings in Python are **immutable**, meaning you **cannot** change a character using indexing.

#### **Example:**
```python
text = "Python"
text[0] = "J"  # ❌ TypeError: 'str' object does not support item assignment
```

To modify a string, you need to **reassign** it using string operations.

#### **Correct Way:**
```python
text = "Python"
new_text = "J" + text[1:]  # Replace 'P' with 'J'
print(new_text)  # Jython
```

---

### **8. Practical Example: Reverse a String using Indexing**
```python
text = "Python"
reversed_text = text[::-1]  # Using slicing
print(reversed_text)  # nohtyP
```

---

## **Python Loops 🔄**

Loops in Python allow us to execute a block of code **multiple times**. Python supports two types of loops:

1. **`for` loop** – Used for iterating over **sequences** (lists, tuples, strings, dictionaries, etc.).
2. **`while` loop** – Repeats as long as a condition is `True`.

---

### **1. `for` Loop**
The `for` loop is used to iterate over **iterable objects** like lists, tuples, strings, and ranges.

### **Syntax:**
```python
for variable in iterable:
   ...
    # Code block to execute

```

### **Example: Iterating Over a List**
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

---

### **Using `for` Loop with `range()`**
The `range(start, stop, step)` function generates a sequence of numbers.

```python
for i in range(1, 6):  # Loops from 1 to 5
    print(i)
```
**Output:**
```
1
2
3
4
5
```

### **Using `for` Loop with Strings**
```python
text = "Python"

for char in text:
    print(char)
```
**Output:**
```
P
y
t
h
o
n
```

### **Using `for` Loop with `enumerate()`**
The `enumerate()` function gives both index and value.

```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
```
**Output:**
```
Index 0: red
Index 1: green
Index 2: blue
```

---

### **2. `while` Loop**
A `while` loop runs **as long as a condition is `True`**.

### **Syntax:**
```python
while condition:
   ...
    # Code block to execute
```

### **Example: Counting from 1 to 5**
```python
count = 1

while count <= 5:
    print(count)
    count += 1
```
**Output:**
```
1
2
3
4
5
```

### **Using `while` Loop with `break`**
The `break` statement **exits the loop** when a condition is met.

```python
num = 1

while num <= 10:
    if num == 5:
        break  # Exit the loop at 5
    print(num)
    num += 1
```
**Output:**
```
1
2
3
4
```

### **Using `while` Loop with `continue`**
The `continue` statement **skips the current iteration** and moves to the next one.

```python
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue  # Skip 3
    print(num)
```
**Output:**
```
1
2
4
5
```

---

### **3. `break` and `continue` in Loops**
### **Using `break` in a `for` Loop**
```python
for i in range(1, 6):
    if i == 3:
        break  # Exit at 3
    print(i)
```
**Output:**
```
1
2
```

### **Using `continue` in a `for` Loop**
```python
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3
    print(i)
```
**Output:**
```
1
2
4
5
```

---

### **4. `else` Statement in Loops**
Python allows an `else` block to execute after a loop **completes normally** (without a `break`).

### **Example with `for` Loop**
```python
for i in range(1, 4):
    print(i)
else:
    print("Loop completed!")
```
**Output:**
```
1
2
3
Loop completed!
```

### **Example with `while` Loop**
```python
num = 1

while num < 4:
    print(num)
    num += 1
else:
    print("Loop ended normally!")
```
**Output:**
```
1
2
3
Loop ended normally!
```

---

### **5. Nested Loops**
Loops inside **another loop** are called **nested loops**.

### **Example: Nested `for` Loop**
```python
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```
**Output:**
```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
```

---

### **6. Looping Over a Dictionary**
You can iterate over dictionary **keys**, **values**, or **both**.

### **Example: Iterating Over Keys**
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

for key in person:
    print(key, "->", person[key])
```
**Output:**
```
name -> Alice
age -> 25
city -> New York
```

### **Example: Iterating Over Keys and Values**
```python
for key, value in person.items():
    print(f"{key}: {value}")
```
**Output:**
```
name: Alice
age: 25
city: New York
```

---

### **7. Looping with `zip()`**
The `zip()` function allows **simultaneous iteration** over multiple lists.

### **Example:**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```
**Output:**
```
Alice is 25 years old.
Bob is 30 years old.
Charlie is 35 years old.
```

---

### **8. List Comprehension with Loops**
List comprehensions provide a **concise way** to create lists.

### **Example: Creating a List of Squares**
```python
squares = [x**2 for x in range(1, 6)]
print(squares)
```
**Output:**
```
[1, 4, 9, 16, 25]
```

### **Example: Filtering Even Numbers**
```python
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```
**Output:**
```
[2, 4, 6, 8, 10]
```

---

### **Summary**
| Loop Type | Description |
|-----------|------------|
| `for` loop | Iterates over sequences (lists, strings, ranges, etc.) |
| `while` loop | Runs as long as a condition is `True` |
| `break` | Exits the loop immediately |
| `continue` | Skips the current iteration and moves to the next one |
| `else` with loops | Runs when the loop completes without a `break` |
| Nested loops | Loops inside another loop |

### **Best Practices**
✅ Use `for` loops for **sequences** (lists, ranges, strings).  
✅ Use `while` loops for **conditions** that need checking.  
✅ Use `break` to **exit early** and `continue` to **skip iterations**.  
✅ Use `enumerate()` for **index tracking** in loops.  
✅ Use `zip()` for **parallel iteration** over multiple lists.  
✅ Use **list comprehensions** for concise list creation.

 

#### **For Loop Example**  
```python
for i in range(5):  # Loops from 0 to 4
    print("Iteration:", i)
```

#### **While Loop Example**  
```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```

---

### **3.6 Functions**  
Functions help organize code into reusable blocks.  

```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```

---

### **3.7 Lists (Arrays in other languages)**  
Lists store multiple values in a single variable.  

```python
fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])   # Apple
print(fruits[-1])  # Cherry

fruits.append("Mango")  # Add an element
print(fruits)

for fruit in fruits:
    print(fruit)
```

---

### **3.8 Dictionaries (Key-Value Pairs)**  
Dictionaries store data in key-value pairs.  

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])  # Alice
print(person.get("age"))  # 25

person["age"] = 26  # Updating value
print(person)
```

---

## **Python Collections (Data Structures) 📦**

Python provides several **built-in collection types** that allow you to store and manipulate groups of data efficiently. The four main types of collections in Python are:

1. **List (`list`)** – Ordered, mutable, allows duplicates  
2. **Tuple (`tuple`)** – Ordered, immutable, allows duplicates  
3. **Set (`set`)** – Unordered, mutable, does not allow duplicates  
4. **Dictionary (`dict`)** – Key-value pairs, unordered (before Python 3.7), mutable, unique keys  

---

### **1. List (`list`) – Ordered & Mutable**  
A **list** is an ordered, mutable collection that allows duplicate elements.

### **Creating a List**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
```

#### **Accessing Elements**
```python
print(fruits[0])   # apple
print(fruits[-1])  # cherry (negative index)
```

#### **Modifying Elements**
```python
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

#### **List Operations**
```python
fruits.append("orange")      # Add an element
fruits.insert(1, "grape")    # Insert at index
fruits.remove("apple")       # Remove an element
fruits.pop()                 # Remove last element
fruits.reverse()             # Reverse the list
fruits.sort()                # Sort the list
print(len(fruits))           # Get length
```

#### **List Comprehension**
```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

### **2. Tuple (`tuple`) – Ordered & Immutable**  
A **tuple** is an ordered, immutable collection that **cannot** be changed after creation.

#### **Creating a Tuple**
```python
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
single_element = ("hello",)  # Note the comma for a single-element tuple
```

### **Accessing Elements**
```python
print(fruits[0])  # apple
print(fruits[-1]) # cherry
```

### **Tuple Operations**
```python
print(len(fruits))           # Get length
print(fruits.count("apple")) # Count occurrences
print(fruits.index("banana"))# Find index
```

### **Converting Tuple to List**
```python
fruits_list = list(fruits)
fruits_list.append("orange")
fruits = tuple(fruits_list)
print(fruits)  # ('apple', 'banana', 'cherry', 'orange')
```

---

### **3. Set (`set`) – Unordered, No Duplicates**  
A **set** is an unordered collection that does not allow duplicate values.

### **Creating a Set**
```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

### **Set Operations**
```python
fruits.add("orange")         # Add element
fruits.remove("banana")      # Remove element (error if not found)
fruits.discard("banana")     # Remove element (no error if not found)
fruits.pop()                 # Remove a random element
fruits.clear()               # Empty the set
```

### **Set Union, Intersection, Difference**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # Union -> {1, 2, 3, 4, 5, 6}
print(set1 & set2)  # Intersection -> {3, 4}
print(set1 - set2)  # Difference -> {1, 2}
print(set1 ^ set2)  # Symmetric Difference -> {1, 2, 5, 6}
```

---

### **4. Dictionary (`dict`) – Key-Value Pairs**  
A **dictionary** stores key-value pairs, where **keys must be unique**.

### **Creating a Dictionary**
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

### **Accessing Values**
```python
print(person["name"])  # Alice
print(person.get("age"))  # 25
```

### **Modifying Dictionary**
```python
person["age"] = 26      # Update value
person["job"] = "Engineer"  # Add new key
del person["city"]      # Remove key
print(person)
```

### **Dictionary Methods**
```python
print(person.keys())    # Get all keys
print(person.values())  # Get all values
print(person.items())   # Get all key-value pairs
```

### **Looping Through a Dictionary**
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

---

### **5. Collections Module (`collections`)**
Python's `collections` module provides additional specialized data structures.

### **5.1 `Counter` – Counting Elements**
```python
from collections import Counter

text = "banana"
counter = Counter(text)
print(counter)  # Counter({'a': 3, 'b': 1, 'n': 2})
```

### **5.2 `defaultdict` – Dictionary with Default Values**
```python
from collections import defaultdict

d = defaultdict(int)  # Default value is 0
d["apple"] += 1
print(d)  # defaultdict(<class 'int'>, {'apple': 1})
```

### **5.3 `OrderedDict` – Maintains Insertion Order (Python 3.6+)**
```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

### **5.4 `deque` – Fast List Operations**
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)     # Add to right
dq.appendleft(0) # Add to left
dq.pop()         # Remove from right
dq.popleft()     # Remove from left
print(dq)  # deque([1, 2, 3])
```

---

### **Comparison Table**
| Type       | Ordered? | Mutable? | Allows Duplicates? | Example |
|------------|---------|---------|----------------|---------|
| **List**   | ✅ Yes | ✅ Yes | ✅ Yes | `["apple", "banana"]` |
| **Tuple**  | ✅ Yes | ❌ No | ✅ Yes | `("apple", "banana")` |
| **Set**    | ❌ No  | ✅ Yes | ❌ No  | `{"apple", "banana"}` |
| **Dict**   | ✅ Yes (3.7+) | ✅ Yes | ❌ No (keys) | `{"name": "Alice"}` |

---

### **Summary**
✅ **Lists** – Ordered, mutable, allows duplicates  
✅ **Tuples** – Ordered, immutable, allows duplicates  
✅ **Sets** – Unordered, mutable, no duplicates  
✅ **Dictionaries** – Key-value pairs, unique keys  

### **Best Practices**
✔ Use **lists** when order and mutability are needed  
✔ Use **tuples** when you need immutable sequences  
✔ Use **sets** to store unique items  
✔ Use **dictionaries** for fast lookups with key-value pairs  

---

## **Importing and Using `random` in Python 🎲**

The **`random`** module in Python allows you to generate **random numbers** and perform operations like **shuffling, selecting random items, and simulating randomness** in programs.  

---

### **1. Importing the `random` Module**
To use the `random` module, you need to **import it** first:

```python
import random
```

---

### **2. Generating Random Numbers**
#### **2.1 Generate a Random Float Between `0.0` and `1.0`**
```python
print(random.random())  # Example: 0.723456
```

### **2.2 Generate a Random Integer in a Range**
```python
print(random.randint(1, 10))  # Random integer between 1 and 10 (inclusive)
```

### **2.3 Generate a Random Float in a Range**
```python
print(random.uniform(10, 20))  # Random float between 10 and 20
```

### **2.4 Generate a Random Number with a Step (`randrange`)**
```python
print(random.randrange(0, 100, 5))  # Random number between 0 and 100, step of 5
```

---

### **3. Random Choice from a List**
### **3.1 Pick a Random Element**
```python
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))  # Random fruit from the list
```

### **3.2 Pick Multiple Random Elements (`sample`)**
```python
print(random.sample(fruits, 2))  # Picks 2 unique elements
```

### **3.3 Pick Multiple Elements with Replacement (`choices`)**
```python
print(random.choices(fruits, k=3))  # Picks 3 elements (may repeat)
```

---

### **4. Shuffling a List**
```python
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)  # Shuffles the list in place
print(numbers)  # Example: [3, 1, 5, 4, 2]
```

---

### **5. Random Boolean Value**
```python
print(random.choice([True, False]))  # Output: True or False
```

---

### **6. Seeding the Random Generator (Reproducibility)**
Setting a **seed** makes random results **predictable** (useful for debugging).

```python
random.seed(42)
print(random.randint(1, 10))  # Always produces the same number when run with the same seed
```

---

### **7. Generating Random Bytes**
```python
print(random.randbytes(5))  # Generates 5 random bytes
```

---

### **8. Using `secrets` for Cryptographic Randomness**
For security-sensitive randomness (e.g., passwords, authentication tokens), use the **`secrets`** module.

```python
import secrets

print(secrets.token_hex(16))  # Generates a secure random 16-byte hex token
```

---

### **Conclusion**
| Function | Description |
|----------|-------------|
| `random.random()` | Random float between `0.0` and `1.0` |
| `random.randint(a, b)` | Random integer between `a` and `b` (inclusive) |
| `random.uniform(a, b)` | Random float between `a` and `b` |
| `random.randrange(start, stop, step)` | Random number with step |
| `random.choice(seq)` | Randomly picks an element from a list |
| `random.sample(seq, k)` | Picks `k` unique elements |
| `random.choices(seq, k)` | Picks `k` elements (with replacement) |
| `random.shuffle(seq)` | Shuffles a list in place |
| `random.seed(n)` | Sets a seed for reproducibility |

---

## **Functions in Python 🚀**

A **function** in Python is a reusable block of code that performs a specific task. Functions **help organize code, improve readability, and avoid repetition**.

---

### **1. Defining a Function**
A function is defined using the `def` keyword.

#### **Syntax**
```python
def function_name(parameters):
    """Optional docstring"""
    # Function body
    return value  # Optional return statement
```

#### **Example: Simple Function**
```python
def greet():
    print("Hello, World!")

greet()  # Calling the function
```
**Output:**
```
Hello, World!
```

---

### **2. Function with Parameters**
Parameters allow passing values into a function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```
**Output:**
```
Hello, Alice!
```

---

### **3. Function with Return Value**
A function can return a value using `return`.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

---

### **4. Default Parameters**
You can provide default values for parameters.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Hello, Guest!
greet("Bob")   # Hello, Bob!
```

---

### **5. Keyword Arguments**
You can specify arguments by name.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Alice")  # Named arguments
```
**Output:**
```
My name is Alice and I am 30 years old.
```

---

### **6. `*args` (Variable-Length Arguments)**
Allows a function to accept **multiple positional arguments**.

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))  # Output: 15
```

---

### **7. `**kwargs` (Keyword Arguments)**
Allows a function to accept **multiple keyword arguments**.

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
```
**Output:**
```
name: Alice
age: 25
city: New York
```

---

### **8. Lambda (Anonymous) Functions**
A **lambda function** is a small, anonymous function.

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

👉 **Lambda functions are useful for short, one-time operations.**

---

### **9. Nested Functions**
A function inside another function.

```python
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()
```

---

### **10. Function as an Argument**
Functions can be passed as arguments.

```python
def greet(name):
    return f"Hello, {name}!"

def call_function(func, name):
    print(func(name))

call_function(greet, "Alice")  # Output: Hello, Alice!
```

---

### **11. Recursive Functions**
A function that calls itself.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

### **12. Function Annotations (Type Hints)**
You can specify expected types for parameters and return values.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))  # Output: 8
```

---

### **Summary Table**
| Concept | Example |
|---------|---------|
| Basic Function | `def greet(): print("Hello")` |
| Parameters | `def greet(name):` |
| Return Value | `def add(a, b): return a + b` |
| Default Parameter | `def greet(name="Guest"):` |
| `*args` | `def add(*args): sum(args)` |
| `**kwargs` | `def info(**kwargs): print(kwargs)` |
| Lambda Function | `add = lambda x, y: x + y` |
| Recursive Function | `def factorial(n): return n * factorial(n-1)` |

---

## **Iterables in Python 🔄**

An **iterable** in Python is any object that can be looped over (iterated) using a `for` loop. **Examples** of iterables include **lists, tuples, strings, sets, dictionaries, and even custom objects**.

---

### **1. What is an Iterable?**
An **iterable** is an object that implements the **`__iter__()`** method (returns an iterator) or **`__getitem__()`** (allows indexing).

#### **Example: Lists are Iterables**
```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:  # Iterating over a list
    print(num)
```
✅ Strings, tuples, sets, and dictionaries are also **iterables**.

---

### **2. What is an Iterator?**
An **iterator** is an object that **remembers its state** and produces values **one at a time** using **`__next__()`**.

- **Iterators maintain state** → They do not restart.
- **Iterables can be converted into iterators** using `iter()`.

#### **Example: Converting an Iterable to an Iterator**
```python
numbers = [1, 2, 3]
iterator = iter(numbers)  # Get an iterator from the list

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # ❌ Raises StopIteration (End of iteration)
```

---

#### **3. Checking if an Object is Iterable**
Use `iter()` to check if an object is iterable.

```python
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # Output: True
print(isinstance(100, Iterable))        # Output: False
```

---

### **4. Creating a Custom Iterable (Class-Based)**
You can define **custom iterable objects** by implementing `__iter__()` and `__next__()`.

#### **Example: Custom Iterator**
```python
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):  # Returns the iterator itself
        return self

    def __next__(self):  # Defines how to get the next value
        if self.n <= 0:
            raise StopIteration  # Stop iteration when n reaches 0
        self.n -= 1
        return self.n

count = Countdown(5)
for num in count:
    print(num)  # Output: 4, 3, 2, 1, 0
```

---

### **5. Generators (Efficient Iterators)**
A **generator** is a type of iterator created using the `yield` keyword. **It does not store values in memory**, making it more memory-efficient.

#### **Example: Generator Function**
```python
def countdown(n):
    while n > 0:
        yield n  # Yield instead of return
        n -= 1

gen = countdown(3)
print(next(gen))  # Output: 3
print(next(gen))  # Output: 2
print(next(gen))  # Output: 1
# print(next(gen))  # ❌ Raises StopIteration
```

👉 **Generators are used for streaming large datasets** without loading everything into memory.

---

#### **6. Built-in Functions for Iterables**
Python provides useful functions for working with iterables:

| Function | Description |
|----------|-------------|
| `iter(obj)` | Converts an iterable to an iterator |
| `next(iterator)` | Gets the next value from an iterator |
| `enumerate(iterable)` | Adds an index to an iterable |
| `zip(iter1, iter2)` | Combines multiple iterables |
| `map(func, iterable)` | Applies a function to each element |
| `filter(func, iterable)` | Filters elements based on a condition |

---

### **7. Example: Using `enumerate()`**
Adds an index while iterating.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```
**Output:**
```
1 apple
2 banana
3 cherry
```

---

### **8. Example: Using `zip()`**
Combines multiple iterables.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```
**Output:**
```
Alice is 25 years old.
Bob is 30 years old.
Charlie is 35 years old.
```

---

### **9. Example: Using `map()`**
Applies a function to each element.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

---

### **10. Example: Using `filter()`**
Filters elements based on a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

---

### **Summary**
| Concept | Description |
|---------|-------------|
| **Iterable** | An object that can be looped over (`list`, `tuple`, `string`, etc.) |
| **Iterator** | An object that produces values using `__next__()` |
| **`iter(obj)`** | Converts an iterable into an iterator |
| **`next(iterator)`** | Gets the next item from the iterator |
| **Custom Iterator** | Define `__iter__()` and `__next__()` in a class |
| **Generator (`yield`)** | Memory-efficient iterator function |
| **`map(func, iterable)`** | Applies a function to each element |
| **`filter(func, iterable)`** | Filters elements based on a condition |
| **`zip(iter1, iter2)`** | Combines multiple iterables |

---

## **Membership operators 🔍**

In Python, **membership operators** are used to test whether a value is **present** in a sequence (such as a string, list, tuple, set, or dictionary).

### Python provides two membership operators:
1. **`in`** → Returns `True` if the value is found in the sequence.
2. **`not in`** → Returns `True` if the value is **not** found in the sequence.

---

### Examples:

#### **Using `in`**
```python
# List
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # True

# String
text = "Hello, World!"
print("Hello" in text)  # True

# Dictionary (checks only keys)
person = {"name": "Alice", "age": 25}
print("name" in person)  # True
print("Alice" in person)  # False (checks keys, not values)
```

#### **Using `not in`**
```python
# Tuple
colors = ("red", "green", "blue")
print("yellow" not in colors)  # True

# String
sentence = "Python is awesome!"
print("Java" not in sentence)  # True
```

---

### **Key Points:**
- Works with **lists, tuples, strings, sets, and dictionaries**.
- For dictionaries, `in` checks for **keys, not values**.
- Useful for **filtering and condition checking** in loops and if statements.

---

## **List Comprehension in Python 📝**

**List comprehension** is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable (like a list, tuple, or range) in a **single line of code**.

---

### **Syntax:**  
```python
new_list = [expression for item in iterable if condition]
```
- **`expression`** → The operation or transformation to perform on each item.  
- **`item`** → The current element from the iterable.  
- **`iterable`** → The collection being iterated over (like a list, tuple, or range).  
- **`if condition`** (optional) → A filter that selects which items to include.

---

### **Examples of List Comprehension**

#### **1. Basic Example (Squaring Numbers)**
```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

---

#### **2. Using `if` Condition (Filtering)**
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

---

#### **3. Nested List Comprehension (Flattening a List)**
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

#### **4. Using `if-else` in List Comprehension**
```python
numbers = [1, 2, 3, 4, 5]
even_or_odd = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(even_or_odd)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

#### **5. Creating a List of Tuples**
```python
pairs = [(x, x**2) for x in range(5)]
print(pairs)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
```

---

### **Why Use List Comprehension?**
✅ **More concise** than using `for` loops  
✅ **Faster execution** in many cases  
✅ **Improves readability** (when not overly complex)

---

### **Equivalent `for` Loop vs List Comprehension**
**Using a `for` loop:**
```python
squared = []
for x in range(5):
    squared.append(x**2)
print(squared)  # Output: [0, 1, 4, 9, 16]
```
**Using list comprehension (shorter & faster):**
```python
squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]
```
---

## **Match-Case Statement (Switch) in Python 🎭**

Python introduced the **`match-case`** statement in **Python 3.10** as an alternative to the traditional **if-elif-else** chains. It works similarly to a **switch statement** in other languages like C, Java, and JavaScript.

---

### **Syntax:**
```python
match variable:
    case pattern1:
       ...
        # Code for pattern1
    case pattern2:
       ...
        # Code for pattern2
    case _:
        # Default case (like 'else')
```
- **`match`** → The value being checked.
- **`case`** → The different conditions to match.
- **`_`** (underscore) → Acts as a **default case** (like `else` in if-else).

---

### **Example 1: Simple Match-Case**
```python
def check_status(code):
    match code:
        case 200:
            print("Success ✅")
        case 404:
            print("Not Found ❌")
        case 500:
            print("Server Error 🚨")
        case _:
            print("Unknown Status 🤷‍♂️")

check_status(200)  # Output: Success ✅
check_status(404)  # Output: Not Found ❌
```

---

### **Example 2: Matching Multiple Values**
```python
def check_day(day):
    match day:
        case "Saturday" | "Sunday":
            print("It's the weekend! 🎉")
        case "Monday":
            print("Monday blues! 😴")
        case _:
            print("It's a weekday! 🏢")

check_day("Sunday")  # Output: It's the weekend! 🎉
```

---

### **Example 3: Matching Data Structures (Tuples)**
```python
def get_coordinates(point):
    match point:
        case (0, 0):
            print("Origin 📍")
        case (x, 0):
            print(f"X-axis at {x}")
        case (0, y):
            print(f"Y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")

get_coordinates((0, 5))  # Output: Y-axis at 5
```

---

### **Why Use Match-Case?**
✅ **Cleaner** than long `if-elif-else` chains  
✅ **More readable** for complex pattern matching  
✅ **Introduces structural pattern matching** (useful for tuples, lists, and dictionaries)

---

## **What is a Module in Python? 📦**
A **module** in Python is simply a **file containing Python code** (functions, classes, or variables) that you can **import and reuse** in other programs.  

Modules help organize code, making it more **manageable, reusable, and structured**.

---

### **Types of Modules in Python**  

1. **Built-in Modules** 🏗️ → Already included in Python (e.g., `math`, `random`, `os`)  
2. **User-defined Modules** 📝 → Created by users to organize their own code  
3. **Third-party Modules** 🌍 → Installed via **pip** (e.g., `numpy`, `pandas`, `requests`)  

---

### **1. Using a Built-in Module (Example)**
```python
import math

print(math.sqrt(25))  # Output: 5.0
print(math.pi)        # Output: 3.141592653589793
```

---

### **2. Creating and Importing a User-defined Module**  

#### **Step 1: Create a module (e.g., `my_module.py`)**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

pi_value = 3.14
```

#### **Step 2: Import and use it in another script**
```python
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
print(my_module.pi_value)        # Output: 3.14
```

---

### **3. Installing & Using a Third-Party Module**
To install third-party modules, use `pip`:
```sh
pip install requests
```
Then, you can import and use it:
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200 (if successful)
```

---

### **Importing Modules in Different Ways**  
Python allows different import styles:

1️⃣ **Import the whole module**  
```python
import math
print(math.factorial(5))  # Output: 120
```

2️⃣ **Import specific functions/variables**  
```python
from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
```

3️⃣ **Import with an alias** (Shorter reference)  
```python
import numpy as np
print(np.array([1, 2, 3]))  # Output: [1 2 3]
```

4️⃣ **Import everything (`*`)** ⚠️ **(Not recommended for large modules)**
```python
from math import *
print(sin(90))  # Output: 0.8939966636005579
```

---

### **Why Use Modules? 🤔**
✅ **Code Reusability** – Write once, use anywhere  
✅ **Better Organization** – Keep code structured and modular  
✅ **Easier Maintenance** – Update modules separately  
✅ **Faster Development** – Leverage built-in & third-party tools  

---

## **What is `main()` in Python? 🔍**

In **Java, C, C++**, the `main()` function is the entry point of the program.  
Python **doesn’t require a `main()` function**, but it is often used as a convention.

In Python, we **simulate** `main()` using the special **`if __name__ == "__main__":`** construct.

---

### **2. What is `if __name__ == "__main__"`? 🤔**
This line ensures that a script runs **only when executed directly** and **not when imported as a module**.

```python
def main():
    print("This is the main function")

if __name__ == "__main__":  # Runs only when the script is executed directly
    main()
```
### **🔹 How it Works?**
- If you **run the script directly**, `__name__` is `"__main__"`, so `main()` executes.  
- If you **import the script as a module**, `__name__` is the module name, so `main()` **won’t run automatically**.

---

### **3. What is this `"dunder __"` Thing?**
"Dunder" stands for **"Double UNDERscore"** (`__`). These are **special Python methods and variables** that have a meaning in Python’s internal behavior.

**Examples of dunder methods and variables:**
| **Dunder**      | **What it does** |
|---------------|----------------|
| `__name__`    | Stores the script/module name |
| `__main__`    | The script being run directly |
| `__init__`    | Constructor method for classes |
| `__str__`     | Converts an object to a string |
| `__repr__`    | Official string representation |
| `__len__`     | Defines length for custom objects |
| `__call__`    | Makes an object callable like a function |
| `__getitem__` | Allows indexing into objects |

---

### **4. `main()` in Python vs Java 🚀**
| **Feature**       | **Python** | **Java** |
|----------------|---------|--------|
| **Required?** | ❌ No  | ✅ Yes |
| **Function signature** | `def main():` | `public static void main(String[] args)` |
| **Entry point** | `if __name__ == "__main__":` | `main()` function |
| **Multiple entry points?** | ✅ Yes | ❌ No |

**🔹 Example: Java vs Python**
**Java:**
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello from Java!");
    }
}
```
**Python:**
```python
def main():
    print("Hello from Python!")

if __name__ == "__main__":
    main()
```

---

### **5. Why Use `if __name__ == "__main__"`?**
✅ **Prevents unintended execution** when importing modules  
✅ **Makes Python scripts behave like standalone programs**  
✅ **Improves code organization and readability**  

---

### **6. A Practical Example**  
### **🔹 File: `module.py`**
```python
def greet():
    print("Hello from the module!")

if __name__ == "__main__":
    print("Running module.py directly!")
    greet()
```
### **🔹 File: `main.py`**
```python
import module

print("This is main.py")
```
### **🔹 Output when running `module.py`:**
```
Running module.py directly!
Hello from the module!
```
### **🔹 Output when running `main.py`:**
```
This is main.py
```
🔹 **Notice:** `module.py`'s `print()` didn’t execute when imported.

---

### **7. Takeaways 🎯**
✅ `main()` in Python is **optional** but useful for structuring code  
✅ `"dunder \_\_"` methods are **Python’s internal magic functions**  
✅ `if __name__ == "__main__":` **ensures code runs only when executed directly**  

---

## **Object-Oriented Programming (OOP) in Python 🐍🚀**

OOP (Object-Oriented Programming) is a way to structure code using **objects** and **classes**. Python supports OOP principles such as **Encapsulation, Inheritance, Polymorphism,** and **Abstraction**.

---

### **1. What is a Class and an Object?**
#### **🔹 Class**
A **class** is a blueprint for creating objects. It defines attributes (variables) and methods (functions).

### **🔹 Object**
An **object** is an instance of a class. Each object has its own **data** and can use class **methods**.

---

### **2. Creating a Class and an Object**
```python
class Car:
    def __init__(self, brand, model, year):  # Constructor method
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Creating objects (instances)
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

# Calling a method
car1.display_info()  # Output: 2022 Toyota Corolla
car2.display_info()  # Output: 2023 Honda Civic
```
---

### **3. OOP Pillars in Python**
### **🔹 Encapsulation (Data Hiding) 🔒**
Encapsulation restricts direct access to some object attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (prefix with '__')

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  ❌ AttributeError: Private variable
```
🔹 **Private variables** use `__` (double underscore).  
🔹 Use **getter/setter methods** to access or modify private attributes.

---

### **🔹 Inheritance (Code Reusability) 🧬**
Inheritance allows a class (**child**) to inherit attributes and methods from another class (**parent**).

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("Honk! Honk!")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent constructor
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

car = Car("Tesla", "Model S")
car.display_info()  # Output: Car: Tesla Model S
car.honk()  # Output: Honk! Honk!
```
🔹 **`super()`** calls the parent class constructor.

---

### **🔹 Polymorphism (Multiple Forms) 🔄**
Different classes can have the **same method name** but behave differently.

```python
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.sound())  
# Output:
# Bark
# Meow
```
🔹 Same method **`sound()`** behaves differently for **Dog** and **Cat**.

---

### **🔹 Abstraction (Hiding Complexity) 🎭**
Hides **implementation details** and only shows the **essential features**.

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog = Dog()
print(dog.make_sound())  # Output: Bark
```
🔹 **Abstract classes** can’t be instantiated directly.  
🔹 **Child classes** must implement abstract methods.

---

### **4. Special (Dunder) Methods in OOP 🔥**
Python provides **magic methods** (dunder methods) to modify class behavior.

| **Method** | **Purpose** |
|------------|------------|
| `__init__()` | Constructor (initialize object attributes) |
| `__str__()` | String representation (like `toString()` in Java) |
| `__repr__()` | Official string representation (used in debugging) |
| `__len__()` | Defines behavior for `len(obj)` |
| `__eq__()` | Defines `==` comparison |
| `__add__()` | Defines `+` operator behavior |

### **Example: `__str__()` and `__add__()`**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

    def __add__(self, other):
        return self.age + other.age  # Adding two people's ages

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1)  # Output: Person: Alice, Age: 25
print(p1 + p2)  # Output: 55 (25 + 30)
```
---

### **5. OOP in Real-World Applications 🏆**
✅ **Game Development** – Characters as objects with attributes & behaviors  
✅ **Web Development** – Django & Flask use OOP to define models  
✅ **Data Science** – Pandas & NumPy use OOP for efficient data handling  
✅ **Cybersecurity** – OOP helps structure secure authentication systems  

---

### **6. Key Takeaways 🎯**
✅ **Classes** are blueprints, and **objects** are instances  
✅ **Encapsulation** hides sensitive data using private variables  
✅ **Inheritance** allows code reuse  
✅ **Polymorphism** enables methods with different behaviors  
✅ **Abstraction** hides complexity using abstract classes  

---

## **Multiple and Multilevel Inheritance 🌀**
Python supports both **Multiple Inheritance** and **Multilevel Inheritance**, similar to how Java supports class hierarchies, but with a few differences. Let’s break it down! 🚀

---

### **1️⃣ Multiple Inheritance (Many Parents, One Child)**
🔹 A class **inherits from multiple parent classes**.  
🔹 Unlike Java (which only supports single inheritance for classes), Python allows a class to **inherit from multiple classes**.

### **Example:**
```python
class Father:
    def skills(self):
        return "Coding"

class Mother:
    def hobbies(self):
        return "Painting"

class Child(Father, Mother):  # Inheriting from both Father and Mother
    def talent(self):
        return "Music"

c = Child()
print(c.skills())  # Inherited from Father -> Coding
print(c.hobbies())  # Inherited from Mother -> Painting
print(c.talent())   # Defined in Child -> Music
```
✅ **Key Takeaways**:
- The `Child` class **inherits methods from both `Father` and `Mother`**.
- Python **resolves conflicts** using **Method Resolution Order (MRO)** (left to right).

---

### **2️⃣ Multilevel Inheritance (Chain of Inheritance)**
🔹 A class **inherits from another class**, which in turn **inherits from another class**.  
🔹 This creates a **hierarchical chain**.

### **Example:**
```python
class Grandparent:
    def wisdom(self):
        return "Experience is the best teacher"

class Parent(Grandparent):
    def guidance(self):
        return "Work hard"

class Child(Parent):
    def dream(self):
        return "Become a scientist"

c = Child()
print(c.wisdom())   # Inherited from Grandparent
print(c.guidance()) # Inherited from Parent
print(c.dream())    # Defined in Child
```
✅ **Key Takeaways**:
- `Child` inherits from `Parent`, which inherits from `Grandparent`.
- `Child` gets **all** methods from **both parent and grandparent classes**.

---

### **🧐 Multiple vs. Multilevel: Key Differences**
| Feature | **Multiple Inheritance** | **Multilevel Inheritance** |
|---------|----------------|----------------|
| **Structure** | One class inherits from multiple parents | One class inherits from another, forming a chain |
| **Java Support?** | ❌ Not in Java (only via interfaces) | ✅ Java allows multilevel inheritance |
| **Python Example** | `class C(A, B)` | `class C(B) → class B(A)` |
| **Complexity** | Can lead to **diamond problems** | More structured |

---

### **⚠️ The Diamond Problem in Multiple Inheritance**
🔹 If **two parents** inherit from the **same superclass**, and a child inherits from both, Python uses **MRO (Method Resolution Order)** to resolve conflicts.

### **Example:**
```python
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):  # Inheriting from both B and C
    pass

d = D()
print(d.show())  # B (follows MRO: left to right)
print(D.mro())   # Shows the method resolution order
```
✅ **Python handles this using MRO** (left to right).  
✅ Java **avoids this issue** by **not allowing multiple inheritance** for classes.

---

### **🔹 Summary**
| Type | Definition | Java Equivalent? |
|------|------------|----------------|
| **Multiple Inheritance** | A class inherits from **multiple parents** | ❌ Not supported for classes (only via interfaces) |
| **Multilevel Inheritance** | A class inherits from a class that **inherits from another** | ✅ Java supports it |

Python gives **flexibility** but requires careful **MRO handling** in **Multiple Inheritance**. 🚀

---

## **`@classmethod` in Python 🚀**

The `@classmethod` decorator in Python is used to define a method that belongs to the **class itself**, rather than an instance of the class. It allows you to **access and modify class-level attributes**.

---

### **1. What is `@classmethod`?**
A **class method**:
✅ Takes the **class (`cls`) as its first parameter** instead of `self`.  
✅ Can **modify class attributes** (shared across all instances).  
✅ Can be called using **both the class name and an instance**.  

### **Syntax**
```python
class MyClass:
    @classmethod
    def class_method(cls, params):
        # cls refers to the class itself
        pass
```

---

### **2. Example: Using `@classmethod`**
```python
class Person:
    species = "Human"  # Class attribute

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modifies class attribute

# Calling the class method
Person.set_species("Homo Sapiens")
print(Person.species)  # Output: Homo Sapiens
```
🔹 `cls.species` modifies the shared class attribute.  

---

### **3. Difference Between `@classmethod` and `@staticmethod`**
| Feature | `@classmethod` | `@staticmethod` |
|---------|---------------|----------------|
| **First parameter** | `cls` (class reference) | No `cls` or `self` |
| **Can modify class attributes?** | ✅ Yes | ❌ No |
| **Can modify instance attributes?** | ❌ No | ❌ No |
| **Can be called on class?** | ✅ Yes | ✅ Yes |
| **Can be called on instance?** | ✅ Yes | ✅ Yes |

### **Example: `@staticmethod` vs `@classmethod`**
```python
class Example:
    value = 10

    @classmethod
    def modify_class(cls, new_value):
        cls.value = new_value  # Changes class attribute

    @staticmethod
    def helper_function():
        return "Static method called"

# Using class method
Example.modify_class(50)
print(Example.value)  # Output: 50

# Using static method
print(Example.helper_function())  # Output: Static method called
```

---

### **4. Alternative Constructor Using `@classmethod`**
Class methods are often used as **alternative constructors**.

### **Example: Creating Objects from Different Inputs**
```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, emp_str):
        name, age = emp_str.split("-")
        return cls(name, int(age))  # Creating a new object

# Creating an instance using the class method
emp = Employee.from_string("Alice-30")
print(emp.name, emp.age)  # Output: Alice 30
```

---

### **5. When to Use `@classmethod`?**
✔ When modifying **class-level attributes**.  
✔ When creating **alternative constructors**.  
✔ When you need a method that logically belongs to the class but doesn't require instance data.  

---

### **6. Summary**
| Concept | Explanation |
|---------|------------|
| **`@classmethod`** | Method that operates on the class itself (`cls`) |
| **Can modify class attributes** | ✅ Yes |
| **Can modify instance attributes** | ❌ No |
| **Common Use Cases** | Alternative constructors, shared settings |

---

### **7. Final Thoughts**
✅ `@classmethod` is powerful for **class-wide operations**.  
✅ Use it when you need to **modify class attributes**.  
✅ Prefer `@staticmethod` when you don’t need access to `cls` or instance attributes.  

🚀 **Use `@classmethod` to write cleaner, reusable class logic in Python!** 🐍

---

## **`@property` Decorator in Python 🔹**
The `@property` decorator in Python is used to **define getter methods in a class**, making them **accessible like attributes** instead of calling them as methods. It helps in **encapsulation**, similar to **getters and setters in Java** but in a more Pythonic way. 🚀  

---

### **📌 Why Use `@property`?**
- **Encapsulation** → Controls access to instance variables.  
- **Read-Only Attributes** → Prevents modification of values.  
- **Computed Properties** → Returns **derived values** without exposing internal data.  

---

### **1️⃣ Basic Example: Using `@property` as a Getter**
In Java, we would write:
```java
public class Car {
    private String brand;
    
    public Car(String brand) {
        this.brand = brand;
    }

    public String getBrand() {  // Getter
        return brand;
    }
}
```
But in **Python with `@property`**, it’s much simpler:
```python
class Car:
    def __init__(self, brand):
        self._brand = brand  # Using _brand (a convention for private variables)

    @property
    def brand(self):  # Getter method
        return self._brand

car = Car("Toyota")
print(car.brand)  # Accessing as an attribute, NOT as a method
```
✅ **Key Takeaways**:  
- `brand()` acts like a **getter** but can be accessed like an attribute (`car.brand`).  
- No need to call it as `car.brand()`.  

---

### **2️⃣ Adding a Setter with `@brand.setter`**
If you try to modify `car.brand`, you'll get an error because it's **read-only**. To allow modifications, use `@property` with a **setter**.

### **Example: Using `@property` with a Setter**
```python
class Car:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    @brand.setter  # Setter method
    def brand(self, new_brand):
        if new_brand:
            self._brand = new_brand
        else:
            raise ValueError("Brand cannot be empty!")

car = Car("Toyota")
print(car.brand)  # Toyota

car.brand = "Honda"  # Updating the value using setter
print(car.brand)  # Honda

# car.brand = ""  # ❌ Raises ValueError
```
✅ **How it works**:  
- **Getter (`@property`)** → Retrieves `_brand` when accessing `car.brand`.  
- **Setter (`@brand.setter`)** → Controls how `car.brand = "Honda"` updates `_brand`.  

---

### **3️⃣ Adding a Deleter with `@brand.deleter`**
To **delete an attribute**, use `@property` with `@brand.deleter`.

### **Example:**
```python
class Car:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    @brand.deleter  # Deleter method
    def brand(self):
        print("Deleting brand...")
        del self._brand

car = Car("Toyota")
del car.brand  # Calls deleter
# print(car.brand)  # ❌ AttributeError: 'Car' object has no attribute '_brand'
```
✅ **Key Takeaways**:
- **Getter (`@property`)** → Retrieves `_brand`.  
- **Setter (`@brand.setter`)** → Updates `_brand`.  
- **Deleter (`@brand.deleter`)** → Deletes `_brand`.  

---

### **🔹 `@property` vs Java Getters/Setters**
| Feature | **Java** | **Python (`@property`)** |
|---------|---------|-----------------|
| **Getter** | `getBrand()` | `@property` (`car.brand`) |
| **Setter** | `setBrand("Honda")` | `@brand.setter` (`car.brand = "Honda"`) |
| **Deleter** | `deleteBrand()` | `@brand.deleter` (`del car.brand`) |
| **Encapsulation** | Explicit (`private` fields) | Implicit (Python convention `_var`) |
| **Read-Only Attribute** | No | Yes (`@property` without setter) |

Python’s `@property` **removes boilerplate** and makes **code cleaner** than traditional Java-style getters and setters! 🚀  

---

### **When to Use `@property`?**
✅ **When you need encapsulation** (e.g., prevent direct modification).  
✅ **When computing values dynamically** instead of storing them.  
✅ **When transitioning from an attribute to a method** without breaking existing code.  

---

### **🔹 Example: Using `@property` for Computed Properties**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):  # No need for parentheses!
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.5 (Computed property)
```
✅ **No need to call `c.area()`** → `@property` makes it **act like an attribute**.  

---

### **🚀 Summary**
- `@property` makes a **method behave like an attribute**.
- `@brand.setter` allows **controlled modification** of an attribute.
- `@brand.deleter` allows **deletion** of an attribute.
- Used for **encapsulation** and **computed properties**.
- More **Pythonic** than Java-style getters & setters.

---

## **Decorators in Python✨**

Decorators in Python are **powerful tools** used to modify the behavior of functions or methods **without changing their actual code**. They are heavily used in Python for **logging, authentication, caching, timing functions, and more!** 🚀  

---

### **🔹 What is a Decorator?**
A **decorator** is a function that **wraps another function** to add extra functionality.

🔹 It follows the **principle of higher-order functions**, meaning:  
- Functions can be **passed as arguments**.  
- Functions can **return other functions**.  

---

### **1️⃣ Basic Example of a Decorator**
```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper  # Returning the inner function

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```
**🔍 Output:**
```
Something before the function runs
Hello!
Something after the function runs
```
✅ **Key Takeaways:**
- `@my_decorator` **modifies** the behavior of `say_hello()`.
- `wrapper()` **adds extra behavior** before and after `func()`.

---

### **2️⃣ Equivalent Without `@` Syntax**
The above code is equivalent to:
```python
def say_hello():
    print("Hello!")

decorated_function = my_decorator(say_hello)  # Manually applying the decorator
decorated_function()
```
But using `@my_decorator` is more **Pythonic** and **readable**.  

---

### **3️⃣ Decorator with Arguments**
If a function **takes arguments**, the decorator should handle them.

### **Example:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):  # Accepting arguments
        print("Before function execution")
        result = func(*args, **kwargs)  # Calling the function
        print("After function execution")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))
```
**🔍 Output:**
```
Before function execution
After function execution
8
```
✅ `*args` and `**kwargs` allow **any number of arguments** to be passed.

---

### **4️⃣ Using `functools.wraps` to Preserve Function Metadata**
One issue with decorators is they **override function metadata** (`__name__`, `__doc__`).  
To fix this, use `functools.wraps()`.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        print("Running decorated function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")

print(greet.__name__)  # ✅ Output: greet (not wrapper)
print(greet.__doc__)   # ✅ Output: This function greets the user.
```
✅ `@functools.wraps(func)` ensures the **original function name and docstring remain intact**.

---

### **5️⃣ Real-World Use Cases of Decorators**
### **✅ 1. Logging Decorator**
```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```
**🔍 Output:**
```
Calling multiply with (3, 4) {}
12
```
✅ **Great for debugging!**

---

### **✅ 2. Timing a Function Execution**
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)  # Simulating a slow task
    print("Finished!")

slow_function()
```
**🔍 Output:**
```
Finished!
slow_function took 2.0001 seconds
```
✅ **Perfect for performance measurement!**

---

### **✅ 3. Authorization (Checking Permissions)**
```python
def requires_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied!")
            return
        return func(user)
    return wrapper

@requires_admin
def delete_database(user):
    print(f"Database deleted by {user}")

delete_database("guest")  # ❌ Access Denied
delete_database("admin")  # ✅ Database deleted
```
✅ **Used in security/authentication!**

---

### **6️⃣ Class Decorators (`@classmethod`, `@staticmethod`, `@property`)**
Python has built-in decorators for classes.

### **1. `@classmethod` (Access class itself)**
```python
class Example:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

Example.increment()
print(Example.count)  # ✅ 1
```

---

### **2. `@staticmethod` (Independent method)**
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 4))  # ✅ 7
```

---

### **3. `@property` (Encapsulation)**
```python
class Car:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):  # Getter
        return self._brand

car = Car("Toyota")
print(car.brand)  # ✅ Toyota (accessing without ())
```

---

### **🚀 Summary**
| **Feature** | **Description** |
|------------|----------------|
| **What is a Decorator?** | A function that **modifies another function** without changing its code. |
| **Basic Structure** | `def decorator(func): return wrapper` |
| **Why Use It?** | Adds **logging, authentication, performance tracking, access control, etc.** |
| **`*args, **kwargs`** | Allows **flexible arguments** in decorators. |
| **`functools.wraps`** | Preserves function metadata (`__name__`, `__doc__`). |
| **Built-in Decorators** | `@staticmethod`, `@classmethod`, `@property` |

### **🔥 Common Use Cases**
✅ **Logging (`@log_function_call`)**  
✅ **Performance Timing (`@timer`)**  
✅ **Authorization (`@requires_admin`)**  
✅ **Encapsulation (`@property`)**  

---

## **Exception Handling in Python 🚨**

Exception handling in Python is **crucial** for writing **robust and error-free programs**. It helps prevent unexpected crashes and provides a way to **gracefully handle errors**. 🛠️  

---

### **🔹 What is an Exception?**
An **exception** is an error that **occurs during execution** and interrupts the normal flow of a program.

### **🔍 Example of an Exception**
```python
x = 5 / 0  # ❌ ZeroDivisionError: division by zero
```
This code **crashes** the program because division by zero is not allowed.

---

### **1️⃣ Basic Exception Handling: `try` and `except`**
To handle exceptions, we use **`try`** and **`except`**.

```python
try:
    x = 5 / 0  # Attempting an error
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
```
✅ The program **does not crash** and handles the error **gracefully**.

---

### **2️⃣ Handling Multiple Exceptions**
We can **handle multiple types** of exceptions.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except ValueError:
    print("❌ Invalid input! Please enter a number.")
```
✅ This catches both **ZeroDivisionError** and **ValueError**.

---

### **3️⃣ Using a General `except` Block**
If we don’t know the exact exception type, we can catch **all exceptions**.

```python
try:
    x = int("hello")  # This will cause a ValueError
except Exception as e:
    print(f"❌ An error occurred: {e}")
```
✅ It catches any error and prints the error message.

---

### **4️⃣ Using `else` and `finally`**
- **`else`** → Runs **only if no exception occurs**.  
- **`finally`** → Always **executes, regardless of exceptions**.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
else:
    print(f"✅ Result: {result}")  # Runs if no error
finally:
    print("🛠️ Execution completed.")  # Always runs
```
✅ The `finally` block is useful for **cleaning up resources** (e.g., closing files).

---

### **5️⃣ Raising Exceptions Manually (`raise`)**
We can **force** an exception using `raise`.

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("❌ Amount cannot be negative!")
    print(f"✅ Withdrawn: ${amount}")

withdraw(-100)  # ❌ Raises ValueError
```
✅ `raise` helps enforce **custom validation**.

---

### **6️⃣ Custom Exceptions**
We can define **custom exceptions** by creating a new class.

```python
class NegativeAmountError(Exception):
    """Custom exception for negative amounts"""
    pass

def withdraw(amount):
    if amount < 0:
        raise NegativeAmountError("❌ Cannot withdraw a negative amount!")
    print(f"✅ Withdrawn: ${amount}")

try:
    withdraw(-50)
except NegativeAmountError as e:
    print(e)
```
✅ Useful for **specific business logic errors**.

---

### **7️⃣ Exception Handling in File Operations**
When working with files, **always** handle exceptions.

```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
```
✅ Prevents program crashes if the file is missing.

---

### **🚀 Summary**
| **Concept** | **Explanation** |
|------------|----------------|
| **`try-except`** | Catches and handles exceptions. |
| **Multiple `except` Blocks** | Handles **different exception types**. |
| **General `except`** | Catches **all exceptions** but should be used cautiously. |
| **`else` Block** | Runs **only if no exceptions occur**. |
| **`finally` Block** | **Always executes**, useful for cleanup. |
| **`raise`** | Manually triggers an exception. |
| **Custom Exceptions** | Create **specific error classes**. |

---

### **🔥 Common Exceptions**
| **Exception** | **Description** |
|--------------|----------------|
| `ZeroDivisionError` | Division by zero (`5/0`). |
| `ValueError` | Invalid value (e.g., `int("abc")`). |
| `IndexError` | Accessing out-of-range index. |
| `KeyError` | Missing dictionary key. |
| `TypeError` | Wrong data type used (e.g., `5 + "hello"`). |
| `FileNotFoundError` | File does not exist. |

---

## **File Handling in Python 📂**

File handling in Python allows us to **read**, **write**, **append**, and **manipulate files** on a system. Python provides built-in functions to work with **text files (`.txt`)** and **binary files (`.bin`, images, etc.)**. 🚀  

---

### **1️⃣ Opening a File (`open()`)**
Python's `open()` function is used to open a file.  

#### **🔹 Syntax:**  
```python
file = open("filename", "mode")
```
| **Mode** | **Description** |
|---------|----------------|
| `"r"` | Read (default). File **must** exist. |
| `"w"` | Write. Creates a new file or **overwrites** existing content. |
| `"a"` | Append. Adds content to the file without overwriting. |
| `"x"` | Create. Fails if the file already exists. |
| `"rb"` / `"wb"` | Read/Write **binary** files. |

---

### **2️⃣ Reading a File (`read()`, `readline()`, `readlines()`)**
We can read files **line by line** or **entirely**.

```python
file = open("example.txt", "r")  # Open file in read mode
content = file.read()  # Read full content
print(content)
file.close()  # Always close the file!
```

#### **🔹 Reading Line by Line**
```python
file = open("example.txt", "r")
line1 = file.readline()  # Reads first line
print(line1)
file.close()
```

#### **🔹 Reading All Lines as a List**
```python
file = open("example.txt", "r")
lines = file.readlines()  # Returns a list of lines
print(lines)
file.close()
```
✅ Each line is stored as a **list element**.

---

### **3️⃣ Writing to a File (`write()`)**
If the file **exists**, `"w"` mode **overwrites** it!

```python
file = open("example.txt", "w")
file.write("Hello, Python!\nThis is file handling.")  # Overwrites content
file.close()
```
✅ Always **close** the file after writing.

---

### **4️⃣ Appending to a File (`"a"` Mode)**
To **add** content without deleting existing data:

```python
file = open("example.txt", "a")
file.write("\nAppending a new line!")  # Adds to the file
file.close()
```
✅ `"a"` mode ensures **previous content is not lost**.

---

### **5️⃣ Using `with open()` (Best Practice ✅)**
Using `with` automatically **closes** the file after execution.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to close the file
```
✅ **Safer** and prevents issues like **memory leaks**.

---

### **6️⃣ Checking if a File Exists (`os` Module)**
Before opening a file, check if it exists.

```python
import os

if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File not found!")
```

---

### **7️⃣ Working with Binary Files (`rb`, `wb`)**
Binary files store **images, videos, and other non-text data**.

#### **🔹 Writing a Binary File**
```python
with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print(binary_data)  # Prints raw binary content
```

#### **🔹 Copying a Binary File**
```python
with open("source.jpg", "rb") as source, open("copy.jpg", "wb") as destination:
    destination.write(source.read())
```
✅ This **copies** an image file.

---

### **8️⃣ Deleting a File (`os.remove()`)**
To **delete a file**:

```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File not found!")
```
✅ Avoids errors by **checking existence first**.

---

### **📌 Summary Table**
| **Operation** | **Method** |
|--------------|-----------|
| Open a file | `open("file.txt", "r")` |
| Read full content | `file.read()` |
| Read one line | `file.readline()` |
| Read all lines | `file.readlines()` |
| Write to a file | `file.write("text")` (Overwrites) |
| Append to a file | `file.write("text")` (Adds new content) |
| Best practice for file handling | `with open("file.txt", "r") as file:` |
| Check if file exists | `os.path.exists("file.txt")` |
| Delete a file | `os.remove("file.txt")` |

---

## **Datetime in Python 📆**

Python’s `datetime` module provides powerful tools to **work with dates and times**, making it easy to manipulate, format, and calculate time differences. ⏳✨  

---

### **1️⃣ Importing the `datetime` Module**  
To use date and time features, **import the module**:

```python
import datetime
```

---

### **2️⃣ Getting the Current Date & Time**  
We can retrieve the **current date and time** using `datetime.datetime.now()`.

```python
import datetime

now = datetime.datetime.now()  
print(now)  # Example output: 2025-03-17 14:30:45.678910
```

### **🔹 Extracting Specific Components**
```python
print(now.year)   # 📆 Year (e.g., 2025)
print(now.month)  # 🗓️ Month (e.g., 3 for March)
print(now.day)    # 📅 Day (e.g., 17)
print(now.hour)   # ⏰ Hour (e.g., 14)
print(now.minute) # 🕐 Minute (e.g., 30)
print(now.second) # ⏳ Second (e.g., 45)
```

---

### **3️⃣ Creating a Custom Date & Time**
We can create a **specific date and time** using `datetime.datetime()`.

```python
custom_date = datetime.datetime(2024, 12, 25, 10, 30, 0)  
print(custom_date)  # 🎄 2024-12-25 10:30:00
```

✅ The format is:  
```python
datetime.datetime(year, month, day, hour, minute, second)
```

---

### **4️⃣ Formatting Dates & Times (`strftime()`)**
To display dates in different formats, use `strftime()`.

```python
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Example: 2025-03-17 14:30:45
```

### **🔹 Common Formatting Codes**
| **Code** | **Meaning** | **Example Output** |
|---------|------------|-----------------|
| `%Y` | Full Year | `2025` |
| `%y` | Short Year | `25` |
| `%m` | Month (zero-padded) | `03` |
| `%B` | Month Name | `March` |
| `%d` | Day (zero-padded) | `17` |
| `%A` | Weekday | `Monday` |
| `%H` | Hour (24-hour) | `14` |
| `%I` | Hour (12-hour) | `02` |
| `%p` | AM/PM | `PM` |
| `%M` | Minute | `30` |
| `%S` | Second | `45` |

Example:
```python
print(now.strftime("Today is %A, %B %d, %Y"))  
# Output: Today is Monday, March 17, 2025
```

---

### **5️⃣ Converting Strings to Datetime (`strptime()`)**
We can **parse a date string** into a `datetime` object.

```python
date_string = "2024-07-04 15:45:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # Output: 2024-07-04 15:45:00
```
✅ `strptime()` converts a **formatted string** into a `datetime` object.

---

### **6️⃣ Getting Today’s Date (`date.today()`)**
If we only need the **date (without time)**:

```python
today = datetime.date.today()
print(today)  # Output: 2025-03-17
```

✅ Extracting parts:
```python
print(today.year)  # 2025
print(today.month) # 3
print(today.day)   # 17
```

---

### **7️⃣ Working with Time (`datetime.time`)**
We can also handle **time values separately**.

```python
time_example = datetime.time(14, 30, 45)
print(time_example)  # Output: 14:30:45
```
✅ Extracting parts:
```python
print(time_example.hour)   # 14
print(time_example.minute) # 30
print(time_example.second) # 45
```

---

### **8️⃣ Time Differences (`timedelta`)**
To calculate **date and time differences**, use `datetime.timedelta`.

```python
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # 10 days later
past_date = now - timedelta(weeks=2)    # 2 weeks ago

print(future_date)  # Output: 2025-03-27
print(past_date)    # Output: 2025-03-03
```

### **🔹 Adjusting Time**
```python
new_time = now + timedelta(hours=5, minutes=30)  # Adds 5 hours 30 minutes
print(new_time)
```

---

### **9️⃣ Getting the Current UTC Time**
For **timezone-aware applications**, use `datetime.utcnow()`.

```python
utc_time = datetime.utcnow()
print(utc_time)  # Example: 2025-03-17 12:30:45
```

---

### **🔟 Time Zones (`pytz` Module)**
Python's `datetime` is **not timezone-aware** by default. Use `pytz` to handle time zones.

### **🔹 Install `pytz` (if not installed)**
```bash
pip install pytz
```

### **🔹 Example: Convert to a Specific Time Zone**
```python
import pytz

tz_NY = pytz.timezone("America/New_York")
tz_London = pytz.timezone("Europe/London")

now = datetime.now(pytz.utc)  # Get current UTC time

ny_time = now.astimezone(tz_NY)  
london_time = now.astimezone(tz_London)

print("New York Time:", ny_time)
print("London Time:", london_time)
```

✅ **Useful for international applications! 🌍**

---

### **📌 Summary Table**
| **Operation** | **Method** |
|--------------|------------|
| Get current date & time | `datetime.datetime.now()` |
| Get only today’s date | `datetime.date.today()` |
| Get a custom date | `datetime.datetime(2024, 12, 25, 10, 30, 0)` |
| Format datetime | `strftime("%Y-%m-%d")` |
| Convert string to date | `strptime("2024-07-04", "%Y-%m-%d")` |
| Add/subtract time | `timedelta(days=10, hours=5)` |
| Get UTC time | `datetime.datetime.utcnow()` |
| Handle time zones | `pytz.timezone("America/New_York")` |

---

## **Multithreading in Python 🎛️**

Python provides the `threading` module to execute **multiple tasks simultaneously** within the same process. This is useful for I/O-bound tasks but has limitations for CPU-bound tasks due to the **Global Interpreter Lock (GIL)**.  

---

### **🔹 1️⃣ What is Multithreading?**  
Multithreading allows a program to **run multiple threads** concurrently, enabling tasks like:  
✅ Running background tasks.  
✅ Improving responsiveness in GUI applications.  
✅ Performing I/O operations (file downloads, network requests).  

**⚠️ Python's GIL:** Due to the **Global Interpreter Lock (GIL)**, **threads do not run truly in parallel** for CPU-heavy tasks. Instead, **use multiprocessing** for CPU-bound operations.

---

### **🔹 2️⃣ Creating a Simple Thread**  
A thread is created using the `threading` module.

```python
import threading

def print_hello():
    print("Hello from thread!")

# Create a thread
thread = threading.Thread(target=print_hello)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Main thread finished")
```
### **🛠 Explanation:**  
1️⃣ `threading.Thread(target=function_name)`: Creates a thread.  
2️⃣ `.start()`: Starts execution in parallel with the main thread.  
3️⃣ `.join()`: Waits for the thread to complete before proceeding.  

🔹 **Output:**  
```
Hello from thread!
Main thread finished
```

---

### **🔹 3️⃣ Creating Multiple Threads**  
We can run **multiple threads** in parallel.  

```python
import threading

def print_numbers():
    for i in range(5):
        print(f"Thread {threading.current_thread().name}: {i}")

# Create multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=print_numbers, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads completed")
```

### **🛠 Explanation:**  
- Creates **3 threads** that print numbers.
- Each thread runs **independently**.
- `threading.current_thread().name` prints the thread name.

🔹 **Example Output:**  
```
Thread-1: 0
Thread-2: 0
Thread-3: 0
Thread-1: 1
Thread-2: 1
Thread-3: 1
...
All threads completed
```

---

### **🔹 4️⃣ Using Classes for Threads (`Thread` Subclassing)**  
Instead of using `target=`, we can create a **custom thread class** by subclassing `threading.Thread`.

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"{self.name} is running: {i}")

# Create and start threads
t1 = MyThread()
t2 = MyThread()

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread finished")
```
### **🛠 Explanation:**  
- We define a class `MyThread` that **inherits** from `threading.Thread`.  
- We override the `run()` method (this is executed when `.start()` is called).  
- Threads execute their **own `run()` method**.

---

### **🔹 5️⃣ Thread Synchronization with Locks**  
When multiple threads access **shared resources**, **race conditions** can occur. We use **Locks** to prevent data corruption.  

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Ensures only one thread modifies `counter` at a time
            counter += 1

# Create two threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter:", counter)
```

### **🛠 Explanation:**  
- Without a **lock**, both threads might modify `counter` **simultaneously**, causing data corruption.  
- `with lock:` ensures that only **one thread modifies `counter` at a time**.  

---

### **🔹 6️⃣ Using `ThreadPoolExecutor` for Simplicity**  
Instead of manually creating and managing threads, we can use `concurrent.futures.ThreadPoolExecutor`.

```python
from concurrent.futures import ThreadPoolExecutor

def worker(n):
    print(f"Processing {n}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(worker, range(5))
```

### **🛠 Explanation:**  
- `ThreadPoolExecutor(max_workers=3)`: Creates **3 worker threads**.  
- `.map(worker, range(5))`: Runs the `worker()` function on 5 values using available threads.  

🔹 **Output:**  
```
Processing 0
Processing 1
Processing 2
Processing 3
Processing 4
```

---

### **🔹 7️⃣ Daemon Threads (Background Tasks)**  
A **daemon thread** runs in the background and **exits when the main program ends**.

```python
import threading
import time

def background_task():
    while True:
        print("Running in background...")
        time.sleep(2)

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

time.sleep(5)  # Main thread waits for 5 seconds
print("Main thread exiting...")
```

### **🛠 Explanation:**  
- `.daemon = True`: Makes the thread **exit when the main thread finishes**.  
- Without this, the background task **would run indefinitely**.

---

### **🔹 8️⃣ Multithreading vs. Multiprocessing**  
**Multithreading** is useful for **I/O-bound** tasks (e.g., file handling, API calls).  
**Multiprocessing** is better for **CPU-bound** tasks (e.g., complex calculations, image processing).  

| Feature | Multithreading | Multiprocessing |
|---------|--------------|---------------|
| Execution | Runs multiple **threads** | Runs multiple **processes** |
| Best for | I/O-bound tasks | CPU-bound tasks |
| Parallel execution | 🚫 No (GIL restricts true parallelism) | ✅ Yes |
| Module | `threading` | `multiprocessing` |

✅ **Use `multiprocessing` for CPU-heavy tasks.**  

Example:  
```python
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(3) as pool:
        results = pool.map(square, range(5))
    print(results)
```

🔹 **Output:** `[0, 1, 4, 9, 16]`

---

### **📌 Summary**  
| Concept | Description |
|---------|-------------|
| `threading.Thread(target=function)` | Creates a new thread |
| `.start()` | Starts a thread |
| `.join()` | Waits for the thread to finish |
| `Lock()` | Prevents race conditions |
| `ThreadPoolExecutor` | Manages a pool of threads |
| `daemon=True` | Runs a background thread |

---

## **Database Connection in Python🗄️**

Python supports various databases like **MySQL, PostgreSQL, SQLite, MongoDB**, and more. The most common libraries used for database connections are:

✅ `sqlite3` → Built-in SQLite database (lightweight, no server needed).  
✅ `mysql-connector-python` → For MySQL.  
✅ `psycopg2` → For PostgreSQL.
✅ `pymongo` → For MongoDB.  
✅ `SQLAlchemy` → ORM (Object Relational Mapper) for handling multiple databases easily.  

---

### **🔹 1️⃣ Connecting to SQLite (Built-in Database)**  
SQLite is a lightweight database that requires no installation.  

```python
import sqlite3  

# Connect to (or create) a database file
conn = sqlite3.connect("test.db")  

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Insert a record
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

# Commit and close
conn.commit()
conn.close()
```
✅ If `test.db` doesn't exist, Python creates it.  
✅ `?` is a placeholder to prevent **SQL injection**.  
✅ Always **commit** changes and **close** the connection.

---

### **🔹 2️⃣ Connecting to MySQL (Using `mysql-connector-python`)**  
#### **🔸 Install MySQL Connector:**  
```bash
pip install mysql-connector-python
```

#### **🔸 Python Code for MySQL Connection**
```python
import mysql.connector  

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)

cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 30))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
```
✅ Uses **`%s`** as a placeholder for safe data insertion.  
✅ `.fetchall()` retrieves all records from the table.  

---

### **🔹 3️⃣ Connecting to PostgreSQL (Using `psycopg2`)**  
#### **🔸 Install PostgreSQL Driver:**  
```bash
pip install psycopg2
```

#### **🔸 Python Code for PostgreSQL Connection**
```python
import psycopg2  

conn = psycopg2.connect(
    dbname="test_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INT
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Charlie", 35))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
```
✅ **`SERIAL PRIMARY KEY`** auto-generates unique IDs.  
✅ Uses **`%s`** for safe parameterized queries.  

---

### **🔹 4️⃣ MongoDB Connection in Python 🍃**  

MongoDB is a **NoSQL database** that stores data in **JSON-like documents** instead of tables. Python connects to MongoDB using the **`pymongo`** library.  

---

#### **🔹 1️⃣ Install `pymongo` (MongoDB Driver)**  
```bash
pip install pymongo
```

---

### **🔹 2️⃣ Connecting to MongoDB**  
```python
import pymongo  

# Connect to MongoDB Server (local or remote)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create/Get a database
db = client["test_db"]

# Create/Get a collection (like a table in SQL)
collection = db["users"]

# Insert a document (record)
user_data = {"name": "Alice", "age": 25, "city": "Cairo"}
collection.insert_one(user_data)

print("User added successfully!")
```
✅ **MongoDB creates `test_db` and `users` collection automatically** if they don’t exist.  
✅ **A document is a dictionary (`{}`) instead of a row.**  

---

### **🔹 3️⃣ Inserting Multiple Documents**  
```python
users = [
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Berlin"}
]
collection.insert_many(users)
```
✅ **Equivalent to `INSERT INTO users (...) VALUES (...)` in SQL.**  

---

### **🔹 4️⃣ Querying Data (Find & Filter)**  
#### **🔸 Fetch All Documents**
```python
for user in collection.find():
    print(user)  
```

### **🔸 Fetch Documents with Filters**
```python
user = collection.find_one({"name": "Alice"})
print(user)
```

### **🔸 Fetch Users Older Than 30**
```python
for user in collection.find({"age": {"$gt": 30}}):
    print(user)
```
✅ **`$gt` (greater than), `$lt` (less than), `$eq` (equal), etc., work like SQL comparisons.**  

---

### **🔹 5️⃣ Updating a Document**  
```python
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
```
✅ **Equivalent to `UPDATE users SET age=26 WHERE name='Alice'` in SQL.**  

---

### **🔹 6️⃣ Deleting Data**  
```python
collection.delete_one({"name": "Charlie"})
```
✅ **Equivalent to `DELETE FROM users WHERE name='Charlie'` in SQL.**  

---

### **🔹 7️⃣ Indexing for Fast Queries**  
```python
collection.create_index("name")  # Makes searching by 'name' faster
```
✅ **Works like SQL `CREATE INDEX name_index ON users(name);`**  

---

### **🔹 8️⃣ Handling MongoDB Connection Errors**  
```python
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["test_db"]
    print("Connected to MongoDB!")
except pymongo.errors.ConnectionError as e:
    print(f"Connection Error: {e}")
```
✅ **Always handle errors to prevent crashes!**  

### to keep:

| SQL (Relational DB) | MongoDB (NoSQL) |
|-----------------|----------------------|
| Table | Collection |
| Row | Document |
| Column | Field |
| `SELECT * FROM users` | `collection.find({})` |
| `UPDATE users SET age=30 WHERE name='Bob'` | `collection.update_one({"name": "Bob"}, {"$set": {"age": 30}})` |

✅ **Use MongoDB for unstructured data (JSON-like documents).**  
✅ **Great for high-speed, flexible, and scalable applications.** 

---

### **🔹 5️⃣ Using SQLAlchemy (ORM for Multiple Databases)**  
SQLAlchemy allows **easier** database handling and **works with different databases** (SQLite, MySQL, PostgreSQL).  

#### **🔸 Install SQLAlchemy:**  
```bash
pip install sqlalchemy
```

#### **🔸 Python Code for SQLAlchemy ORM**
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define database (Change to 'mysql://user:pass@localhost/dbname' for MySQL)
DATABASE_URL = "sqlite:///test.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Insert and query data
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Dave", age=40)
session.add(new_user)
session.commit()

# Query Users
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

session.close()
```
✅ Works with **SQLite, MySQL, and PostgreSQL**.  
✅ Uses **ORM (Object Relational Mapping)** for better abstraction.  

---

### **🔹 6️⃣ Handling Errors & Exceptions in Database Operations**
```python
try:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM non_existing_table")  # This will fail
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.close()
```
✅ **Always handle database errors** to avoid crashes.  

---

### **📌 Summary**  
| Database  | Library  | Install Command |
|-----------|---------|----------------|
| SQLite    | `sqlite3` (built-in) | No installation needed |
| MySQL     | `mysql-connector-python` | `pip install mysql-connector-python` |
| PostgreSQL| `psycopg2` | `pip install psycopg2` |
| Multiple DBs | `SQLAlchemy` (ORM) | `pip install sqlalchemy` |

🔹 **Use SQLite for small projects**, **MySQL/PostgreSQL for production**, and **SQLAlchemy for better management**.  

---

## **CRUD Operations in Python (Create, Read, Update, Delete) 📝**

CRUD stands for **Create, Read, Update, Delete**—the fundamental operations for managing data in any application. Here’s how it looks in **SQL (relational databases), MongoDB (NoSQL), and using an ORM (SQLAlchemy)** in Python.

---

### **🗄️ 1️⃣ CRUD in SQLite (Relational Database)**
Using the built-in `sqlite3` module.

```python
import sqlite3  

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()

# ✅ CREATE (INSERT)
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# ✅ READ (SELECT)
def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# ✅ UPDATE
def update_user(id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, id))
    conn.commit()

# ✅ DELETE
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

# Example Usage
create_user("Alice", 25)
create_user("Bob", 30)

print("Users:", read_users())  # Read and display users

update_user(1, 26)  # Update Alice's age
delete_user(2)  # Delete Bob

print("Updated Users:", read_users())  

# Close connection
conn.close()
```

✅ **SQL-based CRUD uses tables, primary keys, and structured data storage.**  

---

### **🍃 2️⃣ CRUD in MongoDB (NoSQL)**
Using `pymongo` for MongoDB.

```python
import pymongo  

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["users"]

# ✅ CREATE
def create_user(name, age):
    collection.insert_one({"name": name, "age": age})

# ✅ READ
def read_users():
    return list(collection.find({}, {"_id": 0}))

# ✅ UPDATE
def update_user(name, new_age):
    collection.update_one({"name": name}, {"$set": {"age": new_age}})

# ✅ DELETE
def delete_user(name):
    collection.delete_one({"name": name})

# Example Usage
create_user("Alice", 25)
create_user("Bob", 30)

print("Users:", read_users())  # Read users

update_user("Alice", 26)  # Update Alice's age
delete_user("Bob")  # Delete Bob

print("Updated Users:", read_users())
```

✅ **MongoDB uses JSON-like documents instead of rows and tables.**  
✅ **Flexible, schema-less, and good for dynamic data storage.**  

---

### **🔹 3️⃣ CRUD Using SQLAlchemy ORM (Relational DB with Python Classes)**
SQLAlchemy allows **object-oriented** database interaction.

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Connection
engine = create_engine("sqlite:///test.db")  # Change this for MySQL/PostgreSQL
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

# Create Table
Base.metadata.create_all(engine)

# ✅ CREATE
def create_user(name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()

# ✅ READ
def read_users():
    return session.query(User).all()

# ✅ UPDATE
def update_user(id, new_age):
    user = session.query(User).filter_by(id=id).first()
    if user:
        user.age = new_age
        session.commit()

# ✅ DELETE
def delete_user(id):
    user = session.query(User).filter_by(id=id).first()
    if user:
        session.delete(user)
        session.commit()

# Example Usage
create_user("Alice", 25)
create_user("Bob", 30)

print("Users:", read_users())  # Read users

update_user(1, 26)  # Update Alice's age
delete_user(2)  # Delete Bob

print("Updated Users:", read_users())
```

✅ **SQLAlchemy makes database interaction more Pythonic using objects instead of raw SQL queries.**  
✅ **Easier to manage complex relationships and data models.**  

---

### **📌 Summary of CRUD in Python**  

| CRUD Operation | SQLite (`sqlite3`) | MongoDB (`pymongo`) | SQLAlchemy ORM |
|---------------|------------------|-----------------|----------------|
| **Create** | `INSERT INTO users (name, age) VALUES (?, ?)` | `collection.insert_one({"name": name, "age": age})` | `session.add(User(name=name, age=age))` |
| **Read** | `SELECT * FROM users` | `collection.find({})` | `session.query(User).all()` |
| **Update** | `UPDATE users SET age=? WHERE id=?` | `collection.update_one({"name": name}, {"$set": {"age": new_age}})` | `user.age = new_age; session.commit()` |
| **Delete** | `DELETE FROM users WHERE id=?` | `collection.delete_one({"name": name})` | `session.delete(user); session.commit()` |

---

## **APIs in Python 🌐**

APIs (Application Programming Interfaces) allow programs to communicate over the web. Python provides several libraries for working with APIs, with **`requests`** being the most popular for making HTTP requests.  

---

### **🔹 1️⃣ Installing Requests Library**  
To handle APIs in Python, install `requests`:  
```bash
pip install requests
```

---

### **🔹 2️⃣ Making a Simple API Request**  
We use `requests.get()` to fetch data from an API.  

```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"  # A test API
response = requests.get(url)

# Convert response to JSON
data = response.json()

print(data)
```

### **🛠 Explanation:**  
✅ `requests.get(url)`: Sends an HTTP GET request.  
✅ `.json()`: Converts response to a Python dictionary.  

🔹 **Example Output:**  
```json
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

---

### **🔹 3️⃣ Handling Query Parameters in GET Requests**  
APIs often require query parameters (e.g., filtering results).  

```python
params = {"userId": 1}  # Filtering by userId
response = requests.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.json())
```
✅ Query parameters are passed using `params={}`.  
✅ Example **URL formed:**  
```
https://jsonplaceholder.typicode.com/todos?userId=1
```

---

### **🔹 4️⃣ Sending Data with POST Requests**  
For sending data (e.g., creating a user), we use `requests.post()`.  

```python
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "New Post",
    "body": "This is a new post.",
    "userId": 1
}

response = requests.post(url, json=data)  # json=data automatically converts it
print(response.json())  # Response from the API
```
✅ `.post(url, json=data)`: Sends a POST request with JSON data.  
✅ The API may return a response indicating the success of the request.  

🔹 **Example Output:**  
```json
{
  "title": "New Post",
  "body": "This is a new post.",
  "userId": 1,
  "id": 101  # New resource ID
}
```

---

### **🔹 5️⃣ PUT and DELETE Requests**  
### **🔸 Updating a resource (PUT request)**  
```python
update_data = {"title": "Updated Title"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print(response.json())
```
✅ `requests.put()` is used to update existing data.  

---

### **🔸 Deleting a resource (DELETE request)**  
```python
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # 200 means successful
```
✅ `requests.delete()` removes a resource.  
✅ `.status_code` helps verify the success (`200 OK`, `204 No Content`).

---

### **🔹 6️⃣ Handling API Authentication**  
Some APIs require authentication using **API keys, tokens, or Basic Auth**.

#### **🔸 Using API Key Authentication**
```python
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get("https://api.example.com/data", headers=headers)
print(response.json())
```
✅ Replace `"YOUR_API_KEY"` with the actual key.

### **🔸 Using Basic Authentication**
```python
from requests.auth import HTTPBasicAuth

response = requests.get("https://api.example.com/data", auth=HTTPBasicAuth("user", "pass"))
print(response.json())
```

---

### **🔹 7️⃣ Handling Errors & Exceptions**  
APIs can fail due to network issues, invalid data, or server errors.  
```python
try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid_url")
    response.raise_for_status()  # Raises an error for 4xx/5xx responses
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
✅ `.raise_for_status()`: Raises an exception for HTTP errors.  

🔹 **Common HTTP Status Codes:** 

| Code | Meaning               |
|------|-----------------------|
| 200  | Success ✅|
| 400  | Bad Request ❌ |
| 401  | Unauthorized 🔒 |
| 403  | Forbidden 🚫 |
| 404  | Not Found ❓ |
| 500  | Internal Server Error 🔥 |

---

### **🔹 8️⃣ Working with JSON APIs**  
Sometimes, API responses contain **deeply nested JSON data**.  
```python
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()  # Convert response to Python objects

# Pretty-print JSON response
print(json.dumps(users, indent=4))  
```
✅ `json.dumps(..., indent=4)`: Formats the JSON output for readability.

---

### **🔹 9️⃣ Streaming Large API Responses**  
For large responses, use `.iter_content()` to process data **chunk by chunk**.  

```python
response = requests.get("https://jsonplaceholder.typicode.com/photos", stream=True)

for chunk in response.iter_content(chunk_size=1024):  
    print(chunk[:100])  # Print only first 100 bytes of each chunk
```
✅ `.stream=True`: Prevents loading everything into memory at once.  
✅ Useful for **downloading files** efficiently.

---

### **🔹 🔟 Making Asynchronous API Calls (Asyncio + Aiohttp)**  
For **faster performance**, use **async programming** with `aiohttp`.  

```python
import aiohttp
import asyncio

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            data = await response.json()
            print(data)

asyncio.run(fetch_data())  
```
✅ **Asynchronous requests** are **non-blocking**, making them faster.  
✅ **`aiohttp`** is best for handling multiple API calls in parallel.

---

### **📌 Summary**  
| HTTP Method | Purpose |
|-------------|---------|
| `GET` | Retrieve data 📩 |
| `POST` | Send data (create new resource) 📤 |
| `PUT` | Update existing resource ✏️ |
| `DELETE` | Remove resource ❌ |

✅ **Common Libraries for APIs in Python:**  
- `requests`: Best for simple HTTP requests.  
- `http.client`: Built-in low-level HTTP client.  
- `aiohttp`: Asynchronous requests for performance.  
- `urllib`: Built-in but less user-friendly than `requests`.

---

## **GUI Development in Python 🎨**  

**PyQt5** is a set of Python bindings for **Qt5**, a powerful cross-platform **GUI framework**. It allows you to create **desktop applications** with a rich user interface.

---

### **1. Installing PyQt5**  
You can install PyQt5 using pip:

```sh
pip install PyQt5 PyQt5-tools
```
- `PyQt5` → The main library  
- `PyQt5-tools` → Contains additional tools like Qt Designer  

---

### **2. Creating a Simple PyQt5 Window**
Let's create a **basic window** using PyQt5.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create the application object
app = QApplication(sys.argv)

# Create a simple window
window = QWidget()
window.setWindowTitle("PyQt5 Window")
window.resize(400, 300)
window.show()

# Run the application loop
sys.exit(app.exec_())
```

### **Explanation**
- `QApplication` → Manages the application.  
- `QWidget` → A basic window component.  
- `window.show()` → Displays the window.  
- `sys.exit(app.exec_())` → Starts the application event loop.

---

### **3. Adding a Button**
Let's add a **button** to the window.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Button Example")
        self.resize(400, 300)

        # Create a button
        button = QPushButton("Click Me", self)
        button.move(150, 130)  # Position the button
        button.clicked.connect(self.on_click)  # Connect button to function

    def on_click(self):
        print("Button clicked!")

# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
```

### **What's New?**
- `QPushButton` → A clickable button.
- `button.clicked.connect(self.on_click)` → Connects the button to a function.

---

### **4. Using Layouts for Better UI**
Instead of manually positioning widgets, use **layouts**.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Layout Example")
        self.resize(400, 300)

        # Create a layout
        layout = QVBoxLayout()

        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")

        # Add buttons to layout
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
```

### **Why Use Layouts?**
✔ Automatically arranges widgets  
✔ Resizes properly when the window changes  
✔ Easy to manage complex UI  

---

### **5. Creating a Form with Input Fields**
Let's create a **form with a text input and a button**.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Form Example")
        self.resize(400, 200)

        layout = QVBoxLayout()

        # Create input field
        self.label = QLabel("Enter your name:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Submit")
        
        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Connect button click event
        self.button.clicked.connect(self.on_submit)

    def on_submit(self):
        name = self.textbox.text()
        self.label.setText(f"Hello, {name}!")

# Run the application
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
```

### **What's New?**
- `QLineEdit` → A text input field.
- `QLabel` → Displays text.
- `self.label.setText(f"Hello, {name}!")` → Updates label on button click.

---

### **6. Using Qt Designer for Drag-and-Drop UI**
Instead of coding the UI manually, you can use **Qt Designer**.

### **Steps to Use Qt Designer**
1. Open Qt Designer:
   ```sh
   pyqt5-tools designer
   ```
2. Design your UI (Add buttons, labels, etc.).
3. Save as `my_ui.ui`.
4. Convert to Python:
   ```sh
   pyuic5 -x my_ui.ui -o my_ui.py
   ```
5. Import and use it in your Python script.

---

### **7. Packaging PyQt5 App into an Executable**
You can package your PyQt5 application into a standalone `.exe` using **PyInstaller**.

### **Install PyInstaller**
```sh
pip install pyinstaller
```

### **Create an Executable**
```sh
pyinstaller --onefile --windowed your_script.py
```
- `--onefile` → Bundles everything into a single file.
- `--windowed` → Hides the terminal (for GUI apps).

---

### **8. Summary**
| Feature | Widget |
|---------|--------|
| **Window** | `QWidget` |
| **Button** | `QPushButton` |
| **Label** | `QLabel` |
| **Text Input** | `QLineEdit` |
| **Layouts** | `QVBoxLayout`, `QHBoxLayout`, `QGridLayout` |
| **Dialogs** | `QMessageBox` |
| **Tables** | `QTableWidget` |

---

PyQt5 is a powerful Python framework for building **desktop applications** with a graphical user interface (GUI). It provides various **widgets** and layout managers to create visually appealing applications.

### **1️⃣ Labels (`QLabel`) 🏷️**
`QLabel` is used to display **text** or **images** in a PyQt5 application. Labels can be static or dynamically updated.

#### **🔹 Creating a Label**
```python
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
label = QLabel("Hello, PyQt5!", window)

window.show()
sys.exit(app.exec_())
```
#### **🔹 Label with HTML Formatting**
```python
label.setText("<h1 style='color:blue;'>Hello, PyQt5!</h1>")
```

---

### **2️⃣ Images (`QPixmap`) 📷**
To display images, PyQt5 provides `QPixmap`, which can be set inside a `QLabel`.

#### **🔹 Displaying an Image in a Label**
```python
from PyQt5.QtGui import QPixmap

label = QLabel()
pixmap = QPixmap("image.png")  # Load image
label.setPixmap(pixmap)
```

---

### **3️⃣ Layout Managers 🧲**
Layout managers control **how widgets are arranged** within a window.

#### **🔹 Common Layouts**
- `QVBoxLayout` → Arranges widgets **vertically**
- `QHBoxLayout` → Arranges widgets **horizontally**
- `QGridLayout` → Arranges widgets **in a grid**

#### **🔹 Example: Vertical Layout**
```python
from PyQt5.QtWidgets import QVBoxLayout

layout = QVBoxLayout()
layout.addWidget(QLabel("First"))
layout.addWidget(QLabel("Second"))
```

---

### **4️⃣ Buttons (`QPushButton`) 🛎️**
`QPushButton` is used to create interactive buttons.

#### **🔹 Creating a Button**
```python
from PyQt5.QtWidgets import QPushButton

button = QPushButton("Click Me")
button.clicked.connect(lambda: print("Button Clicked!"))
```

---

### **5️⃣ Checkboxes (`QCheckBox`) ✅**
Checkboxes allow users to **toggle options on/off**.

#### **🔹 Creating a Checkbox**
```python
from PyQt5.QtWidgets import QCheckBox

checkbox = QCheckBox("Enable feature")
checkbox.setChecked(True)  # Default checked
```

---

### **6️⃣ Radio Buttons (`QRadioButton`) 🔘**
Radio buttons allow **mutually exclusive selections**.

#### **🔹 Creating Radio Buttons**
```python
from PyQt5.QtWidgets import QRadioButton

radio1 = QRadioButton("Option 1")
radio2 = QRadioButton("Option 2")
```

---

### **7️⃣ Line Edits (`QLineEdit`) 💬**
`QLineEdit` is used for **text input fields**.

#### **🔹 Creating a Line Edit Field**
```python
from PyQt5.QtWidgets import QLineEdit

line_edit = QLineEdit()
line_edit.setPlaceholderText("Enter your name")
```

---

### **8️⃣ CSS Styles (`QSS`) 🎨**
PyQt5 supports **Qt Style Sheets (QSS)**, similar to CSS.

#### **🔹 Styling a Button**
```python
button.setStyleSheet("background-color: blue; color: white; font-size: 16px;")
```

#### **🔹 Styling a Label**
```python
label.setStyleSheet("color: red; font-size: 20px;")
```

---

### **9️⃣ Alignment in PyQt5 📏**
Widgets can be aligned within their containers using `setAlignment()`.

#### **🔹 Common Alignment Options**
- `Qt.AlignLeft` → Left alignment
- `Qt.AlignRight` → Right alignment
- `Qt.AlignCenter` → Center alignment
- `Qt.AlignTop` → Top alignment
- `Qt.AlignBottom` → Bottom alignment

#### **🔹 Example: Centering a Label**
```python
from PyQt5.QtCore import Qt

label.setAlignment(Qt.AlignCenter)
```

---

### **🎯 Conclusion**
- PyQt5 provides various **widgets** (`QLabel`, `QPushButton`, etc.) to build UIs.
- **Layout Managers** help organize widgets efficiently.
- **QSS (Qt Style Sheets)** allows UI customization.
- **Alignment** helps position widgets properly.

---

### **9. Next Steps**
✔ Learn about **event handling** (`signals & slots`)  
✔ Use **Qt Designer** for UI design  
✔ Explore **QMainWindow, Menus, and Status Bars**  
✔ Build real-world apps like **calculators, to-do lists, or dashboards**  


---

## **Lambda Expression**

A **lambda expression** in Python is an **anonymous function** (a function without a name) defined using the `lambda` keyword. It can take any number of arguments but only contain a **single expression**.

#### **Syntax:**
```python
lambda arguments: expression
```
Lambda functions are often used for **short, simple operations** where defining a full function with `def` is unnecessary.

#### **Example:**
```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add(5, 3))         # Output: 8
print(add_lambda(5, 3))  # Output: 8
```

---

### **Functional Programming with Lambda in Python**
Like **Java**, Python **supports functional programming**, meaning you can use lambda expressions with **higher-order functions** like `map()`, `filter()`, and `reduce()`.

#### **1. Using `lambda` with `map()`**
Applies a function to **each item** in an iterable.
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

#### **2. Using `lambda` with `filter()`**
Filters elements **based on a condition**.
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

#### **3. Using `lambda` with `reduce()`**
Performs **cumulative computation** (needs `functools.reduce`).
```python
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

---

### **Does Python Have Equivalent Functional Interfaces Like Java?**
Yes, but **Python is dynamically typed** and **not strictly functional** like Java. 

- Java has functional interfaces like `Function<T, R>` and `Predicate<T>`, but Python achieves the same behavior with `lambda`, `map()`, `filter()`, and `functools.reduce()`.  
- Unlike Java, Python does **not require defining** a special interface for functional programming.

#### **Example: Java Lambda vs. Python Lambda**
##### **Java Functional Interface Example:**
```java
import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        Function<Integer, Integer> square = x -> x * x;
        System.out.println(square.apply(5)); // Output: 25
    }
}
```
##### **Equivalent in Python:**
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

### **Key Differences Between Python and Java Lambdas**
| Feature             | Java Lambda Expressions    | Python Lambda Expressions |
|---------------------|--------------------------|--------------------------|
| Type System        | Statically Typed          | Dynamically Typed        |
| Function Scope     | Can be multi-line (with `{}`) | Only single-line expressions |
| Return Statement   | Implicit return           | Implicit return          |
| Functional Interfaces | Requires an interface (e.g., `Function<T, R>`) | No interface needed, just `lambda` |
| Usage in Streams   | Works with Java Streams   | Works with `map()`, `filter()`, `reduce()` |

---

### **When to Use `lambda` in Python?**
✅ **Short, simple functions** where defining `def` is unnecessary.  
✅ **Higher-order functions** like `map()`, `filter()`, and `sorted()`.  
✅ **Sorting with custom keys:**
```python
people = [("Alice", 25), ("Bob", 30), ("Aziz", 26)]
sorted_people = sorted(people, key=lambda person: person[1])  # Sort by age
print(sorted_people)  # Output: [('Alice', 25), ('Aziz', 26), ('Bob', 30)]
```

N.B: 🚫 **Don't use `lambda` for complex logic**, as it reduces readability.


---

## **Python web scraping🕸️🐍**


**Web scraping** is the process of extracting data from websites. In Python, we commonly use **libraries like `BeautifulSoup`, `Requests`, `Scrapy`, and `Selenium`** for this task.

---

### **1️⃣ Basic Web Scraping with `Requests` and `BeautifulSoup`**
🔹 The `requests` library fetches webpage content.  
🔹 The `BeautifulSoup` library parses HTML for easy data extraction.  

### **Installation**
```bash
pip install requests beautifulsoup4
```

### **Example: Scraping Titles from a Website**
```python
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://example.com"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract title
title = soup.title.text
print("Page Title:", title)

# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))
```

---

### **2️⃣ Extracting Specific HTML Elements**
BeautifulSoup provides multiple ways to navigate the HTML structure.

#### **Example: Scraping Blog Post Titles**
```python
html = """
<html>
    <body>
        <h2 class="title">Python Web Scraping</h2>
        <h2 class="title">Learn BeautifulSoup</h2>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Find all <h2> elements with class "title"
titles = soup.find_all("h2", class_="title")
for title in titles:
    print(title.text)
```

---

### **3️⃣ Handling Dynamic Content with Selenium**
Some websites **load content dynamically** using JavaScript. For those, `requests` and `BeautifulSoup` won't work. Instead, we use `Selenium`.

### **Installation**
```bash
pip install selenium
```
🔹 **Download a WebDriver** (e.g., **ChromeDriver** for Chrome) and place it in your system's PATH.

### **Example: Extracting JavaScript-Rendered Content**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver (Make sure chromedriver is installed)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://example.com")

# Extract element text
title = driver.find_element(By.TAG_NAME, "h1").text
print("Title:", title)

# Close the browser
driver.quit()
```

---

### **4️⃣ Scraping Tables & Data with Pandas**
If a website contains tables, **Pandas** can directly read them.

#### **Example: Extracting Table Data**
```python
import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"
tables = pd.read_html(url)

# Print the first table
print(tables[0])
```

---

### **5️⃣ Avoiding Anti-Scraping Measures**
Websites may block scrapers using **CAPTCHAs, rate limits, or IP blocking**. To avoid detection:
✅ **Use Headers & User-Agent Spoofing**  
✅ **Rotate IPs with Proxies**  
✅ **Respect `robots.txt`**  
✅ **Use Delays (`time.sleep()`)**

### **Example: Spoofing User-Agent**
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/110.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response.text)
```

---

### **6️⃣ Advanced Web Scraping with Scrapy**
`Scrapy` is a powerful framework for large-scale web scraping.

#### **Installation**
```bash
pip install scrapy
```

#### **Example: Creating a Scraper**
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }
```
Run the scraper using:
```bash
scrapy runspider myspider.py
```

---

### **🔚 Conclusion**
Python offers multiple ways to scrape the web:
- 🛠 **For simple scraping:** `requests + BeautifulSoup`
- 🚀 **For JavaScript-heavy sites:** `Selenium`
- 📊 **For structured tables:** `pandas`
- 🏗 **For large-scale scraping:** `Scrapy`

---

## **Python Package Installer `pip` 📦**

**`pip` (Python Package Installer)** is the **official package manager** for Python. It allows you to:  
✅ Install packages  
✅ Upgrade packages  
✅ Uninstall packages  
✅ Manage dependencies  

It's similar to **npm** (for Node.js) or **apt/yum** (for Linux).  

---

### **🔹 How to Manage Packages with `pip`**
#### ✅ **1. Check if `pip` is Installed**
Run:  
```bash
pip --version
```
If not installed, install it using:  
```bash
python -m ensurepip --default-pip
```

#### ✅ **2. Install a Package**
```bash
pip install package_name
```
Example:
```bash
pip install requests
```

#### ✅ **3. Install a Specific Version**
```bash
pip install package_name==version
```
Example:
```bash
pip install numpy==1.23.0
```

#### ✅ **4. Upgrade a Package**
```bash
pip install --upgrade package_name
```
Example:
```bash
pip install --upgrade requests
```

#### ✅ **5. Uninstall a Package**
```bash
pip uninstall package_name
```
Example:
```bash
pip uninstall flask
```

#### ✅ **6. List Installed Packages**
```bash
pip list
```

#### ✅ **7. Freeze (Save Installed Packages to a File)**
```bash
pip freeze > requirements.txt
```
This creates a `requirements.txt` file with all installed packages and their versions.

#### ✅ **8. Install from `requirements.txt`**
```bash
pip install -r requirements.txt
```

---

### **🛠️ Bonus: Virtual Environments (`venv`)**
To manage packages per project, use virtual environments:  
```bash
python -m venv myenv
source myenv/bin/activate  # (Linux/macOS)
myenv\Scripts\activate     # (Windows)
pip install flask          # Install packages inside the virtual environment
deactivate                 # Exit virtual environment
```

---

### **🚀 Summary**
- `pip` manages Python packages easily.  
- Use `pip install`, `pip uninstall`, and `pip freeze`.  
- Use `venv` for project-specific environments.  

---

## **Python Package Installer `UV`(2025) 📦⚡**

uv: Python packaging in Rust

uv is an extremely fast Python package installer and resolver, written in Rust, and designed as a drop-in replacement for pip and pip-tools workflows.

uv represents a milestone in our pursuit of a "Cargo for Python": a comprehensive Python project and package manager that's fast, reliable, and easy to use.

As part of this release, we're also taking stewardship of Rye, an experimental Python packaging tool from Armin Ronacher. We'll maintain Rye as we expand uv into a unified successor project, to fulfill our shared vision for Python packaging.

   - 🔗 [@charliermarsh](https://astral.sh/blog/uv) 

---
This a guide to **uv**, the ultra-fast Python package and project manager,
For uv I found this a nice guid Youtyube vedio:

[![UV - A Faster, All-in-One Package Manager to Replace Pip and Venv](https://img.youtube.com/vi/qh98qOND6MI/0.jpg)](https://www.youtube.com/watch?v=qh98qOND6MI)

---

**`uv`** is a next-generation Python package and project manager written in Rust. It serves as a **drop-in replacement** for tools like `pip`, `pip-tools`, `virtualenv`, and `poetry`, offering:

* ✅ **Blazing-fast** dependency resolution and installation
* ✅ **Built-in** virtual environment management
* ✅ **Python version** management
* ✅ **Project initialization** with `pyproject.toml`
* ✅ **Script execution** with inline dependencies
* ✅ **Tool installation** akin to `pipx`

---

### **🔹 Getting Started with `uv`**

#### ✅ **1. Install `uv`**

You can install `uv` using `pip`:

```bash
pip install uv
```

Alternatively, use the official installation script:

* **macOS/Linux**:

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

* **Windows (PowerShell)**:

  ```powershell
  irm https://astral.sh/uv/install.ps1 | iex
  ```

#### ✅ **2. Verify Installation**

```bash
uv --version
```

---

### **📦 Managing Packages with `uv`**

#### ✅ **1. Install a Package**

```bash
uv pip install package_name
```

Example:

```bash
uv pip install requests
```

#### ✅ **2. Install a Specific Version**

```bash
uv pip install package_name==version
```

Example:

```bash
uv pip install numpy==1.23.0
```

#### ✅ **3. Upgrade a Package**

```bash
uv pip install --upgrade package_name
```

Example:

```bash
uv pip install --upgrade requests
```

#### ✅ **4. Uninstall a Package**

```bash
uv pip uninstall package_name
```

Example:

```bash
uv pip uninstall flask
```

#### ✅ **5. List Installed Packages**

```bash
uv pip list
```

#### ✅ **6. Freeze Installed Packages**

```bash
uv pip freeze > requirements.txt
```

#### ✅ **7. Install from `requirements.txt`**

```bash
uv pip install -r requirements.txt
```

#### ✅ **8. Install Editable Package**

```bash
uv pip install -e .
```

---

### **🛠️ Virtual Environments with `uv`**

#### ✅ **1. Create a Virtual Environment**

```bash
uv venv
```

This creates a `.venv` directory in your current project.

#### ✅ **2. Activate the Virtual Environment**

* **macOS/Linux**:

  ```bash
  source .venv/bin/activate
  ```

* **Windows**:

  ```powershell
  .\.venv\Scripts\activate
  ```

#### ✅ **3. Deactivate the Virtual Environment**

```bash
deactivate
```

---

### **🚀 Project Management with `uv`**

#### ✅ **1. Initialize a New Project**

```bash
uv init --python 3.12 my_project
```

This creates a new project with a `pyproject.toml` file and a virtual environment.

#### ✅ **2. Add Dependencies**

```bash
uv add package_name
```

Example:

```bash
uv add fastapi
```

#### ✅ **3. Add Development Dependencies**

```bash
uv add --dev package_name
```

Example:

```bash
uv add --dev pytest
```

#### ✅ **4. Remove Dependencies**

```bash
uv remove package_name
```

#### ✅ **5. Sync Environment**

```bash
uv sync
```

This installs all dependencies specified in `pyproject.toml`.

#### ✅ **6. Lock Dependencies**

```bash
uv lock
```

Generates a lockfile for reproducible installs.

#### ✅ **7. Export Dependencies**

```bash
uv export > requirements.txt
```

---

### **🧪 Running Scripts with `uv`**

#### ✅ **1. Run a Script**

```bash
uv run script.py
```

#### ✅ **2. Run a Script with Inline Dependencies**

Add dependencies at the top of your script:

```python
# requirements: requests
import requests
```

Then run:

```bash
uv run script.py
```

`uv` will install the specified dependencies in an isolated environment before executing the script.

---

### **🐍 Python Version Management with `uv`**

#### ✅ **1. Install a Specific Python Version**

```bash
uv python install 3.12
```

#### ✅ **2. List Installed Python Versions**

```bash
uv python list
```

#### ✅ **3. Use a Specific Python Version**

```bash
uv run --python 3.12 script.py
```

`uv` will automatically download and manage the specified Python version if it's not already installed.

---

### **🔧 Additional `uv` Commands**

* **Build a Package**:

  ```bash
  uv build
  ```

* **Publish to PyPI**:

  ```bash
  uv publish
  ```

* **Manage Cache**:

  ```bash
  uv cache
  ```

* **Display Dependency Tree**:

  ```bash
  uv tree
  ```

* **Run Tools (like `pipx`)**:

  ```bash
  uv tool install ruff
  ruff --version
  ```

---

### **📚 Summary**

* `uv` is a fast, all-in-one Python package and project manager.
* It replaces tools like `pip`, `virtualenv`, and `poetry`.
* Offers seamless project initialization, dependency management, and script execution.
* Manages multiple Python versions effortlessly.

---

## **Python Testing 🧪** 


### Introduction

**What is Testing in Python?**

As other languages testing in Python as alwyas is **writing code to check that your program works as expected**.

Imagine you build a function — how do you know it works? You test it!

You write test code that:
- Runs your function with **specific input**
- Checks if the **output is correct**
- Warns you if something breaks in the future

This makes your code **reliable**, **safe to update**, and helps **prevent bugs**.

---

Before you were a testing wizard, you were a humble peasant using...  
```python
print("It works... I think?")

```
This is the **"medieval testing method"** — just printing stuff to see if it's okay. It works... until it doesn’t 😅.

#### ⚠️ Old-school method
```python
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5?
```

Then came:
```python
assert add(2, 3) == 5
```
Better — but when it fails? Boom 💥 No details. Just a sad `AssertionError`.

That’s why we level up to proper testing with tools like `unittest` and `pytest`.

---


### 🧰 Types of Testing Tools in Python

The two most popular testing tools in Python are:

| Tool      | Description |
|-----------|-------------|
| **`unittest`** | 🏛️ Built-in Python testing framework (inspired by Java's JUnit). Verbose but solid. |
| **`pytest`**   | 🧨 Third-party tool. Simpler syntax, powerful features, preferred by many pros. |

---

### ⚔️ `unittest` vs `pytest`

| Feature              | `unittest`                             | `pytest`                                   |
|----------------------|----------------------------------------|--------------------------------------------|
| **Included in Python?** | ✅ Yes (`import unittest`)              | ❌ No (install via `pip install pytest`)    |
| **Syntax**            | Verbose (uses classes, methods)        | Clean and minimal (uses functions)         |
| **Test discovery**    | Manual (or via CLI flags)              | Automatic (finds all tests easily)         |
| **Assertions**        | Uses special methods like `self.assertEqual()` | Use plain `assert` statements          |
| **Fixtures**          | More boilerplate                       | Cleaner and more flexible                  |
| **Popularity**        | Classic, safe choice                   | Widely preferred in modern projects        |

---

### ✅ Example: Let's Write a Simple Test

#### 🧠 Function to Test
```python
def add(a, b):
    return a + b
```

#### 📦 `unittest` Version
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

#### 🚀 `pytest` Version
```python
def test_add():
    assert add(2, 3) == 5
```

**Which one looks cleaner to you?** Most lean testers go for `pytest`. 😉

---

### 🧠 TL;DR

- **Testing** = making sure your code works, and stays working.
- `unittest`: Built-in, but verbose.
- `pytest`: Cleaner, faster, easier. Recommended for modern Python projects.

---

### ✅ # Basic Beginner Tests (with `pytest`)

#### 🔸 Function to test
```python
def multiply(a, b):
    return a * b
```

### 🔹 Test using `pytest`
```python
def test_multiply():
    assert multiply(2, 5) == 10
```

✅ Run it with:
```bash
pytest test_file.py
```

Pytest will auto-detect all files starting with `test_` or ending with `_test.py`.

---

### 🏰 # Class-based Tests (for grouping related tests)

```python
class TestMath:
    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(5, 2) == 3
```

🔔 No need for inheritance like `unittest.TestCase`!

---

### 🛠️ # Fixtures (for setup/teardown)

Fixtures help you **prepare test data or environments**, like setting up a DB connection or a dummy user.

```python
import pytest

@pytest.fixture
def sample_user():
    return {"username": "Knight", "level": 42}

def test_user_level(sample_user):
    assert sample_user["level"] > 10
```

Fixtures are **reusable** and powerful. You can even make them **scope-based** (`function`, `module`, `session`, etc.).

---

### 🏷️ # Mark & Parametrize (for advanced control)

#### ✔️ Parametrize (run the same test with different inputs)

```python
import pytest

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 6),
    (4, 5, 20),
    (0, 9, 0)
])
def test_multiply(a, b, result):
    assert multiply(a, b) == result
```

This avoids repeating the same test multiple times — **lean testing wins** 🧠.

---

### 🕵️ # Mocking (fake it till you make it)

Useful for simulating:
- APIs
- DB calls
- Time delays
- External resources

#### Example with `unittest.mock`
```python
from unittest.mock import Mock

def get_user_name(api):
    return api.get_name()

def test_get_user_name():
    mock_api = Mock()
    mock_api.get_name.return_value = "Sir Testalot"
    assert get_user_name(mock_api) == "Sir Testalot"
```

Mocking helps isolate what **you** are testing and **fake the rest**.

---

### 🧠 Final Tips

- Use `pytest` for lean, modern testing.
- Stick to **small**, **clear** test cases.
- Prefer **assert** over verbose methods.
- Use **fixtures** for reusable setups.
- Group tests with **classes**.
- Use **parametrize** to test smart, not hard.
- Use **mocking** to avoid testing external chaos.

---

## **QT Designer: A Quick-Start Guide for Python Devs**

### 🧭 Introduction
Qt Designer is a drag-and-drop GUI builder for Qt-based applications. It allows you to create `.ui` files visually, which you can convert into Python code using tools provided by PyQt5, PyQt6, or PySide6.

This guide walks you through:
- Installing and using Qt Designer
- Converting `.ui` and `.qrc` files
- Working with PyQt5, PyQt6, and PySide6
- Power user tips and PyCharm integration

---

### ⚙️ Qt Designer Setup
Qt Designer comes bundled with:
- **PyQt5:** via `pip install pyqt5-tools`
- **PySide6:** via `pip install PySide6`

To open Qt Designer:
```bash
# If using pyqt5-tools:
<path-to-python-scripts>/pyqt5-tools/designer.exe

# If using PySide6 (standalone download or system Qt):
<path-to-qt>/bin/designer.exe
```

---

### 🏗️ Creating UI Files
1. Open Qt Designer
2. Choose a Widget type (MainWindow, Dialog, Widget, etc.)
3. Design your GUI using drag-and-drop
4. Save the file as `your_ui_file.ui`

---

### 🔁 Convert `.ui` to `.py`

### ✅ PyQt5 / PyQt6
```bash
pyuic5 your_ui_file.ui -o your_ui_file.py
# or for PyQt6:
pyuic6 your_ui_file.ui -o your_ui_file.py
```

### ✅ PySide6
```bash
pyside6-uic your_ui_file.ui -o your_ui_file.py
```

Use `where pyside6-uic` (or `Get-Command pyside6-uic` in PowerShell) to find the full path.

---

### 🎨 Convert `.qrc` to `.py`

Use `.qrc` to bundle resources (images, icons):

```xml
<RCC>
  <qresource prefix="/icons">
    <file>myicon.png</file>
  </qresource>
</RCC>
```

### ✅ Convert with PySide6
```bash
pyside6-rcc your_resources.qrc -o your_resources_rc.py
```

Then in Python:
```python
import your_resources_rc  # just import to load resources
```

---

### 🚀 PyCharm Integration

### 🔧 Add External Tool for `.ui` Files
**File > Settings > Tools > External Tools**

#### Convert UI:
- **Name:** Convert UI (PySide6)
- **Program:**
  ```
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python310\Scripts\pyside6-uic.exe
  ```
- **Arguments:**
  ```
  "$FileName$" -o "$FileNameWithoutExtension$_ui.py"
  ```
- **Working Directory:**
  ```
  $FileDir$
  ```

#### Convert QRC:
- **Name:** Convert QRC (PySide6)
- **Program:**
  ```
  C:\Users\<YourName>\AppData\Local\Programs\Python\Python310\Scripts\pyside6-rcc.exe
  ```
- **Arguments:**
  ```
  "$FileName$" -o "$FileNameWithoutExtension$_rc.py"
  ```
- **Working Directory:**
  ```
  $FileDir$
  ```

✅ Now right-click any `.ui` or `.qrc` file and run the External Tool.

---

### 🧪 Quick Python Example (PySide6)
```python
from PySide6.QtWidgets import QApplication, QWidget
from login_window_ui import Ui_Form

app = QApplication([])
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)
window.show()
app.exec()
```

---

### 💡 Tips & Tricks
- 🧠 **Use `$FileDir$` in PyCharm External Tools** to avoid path issues.
- 🚀 Use `.qrc` to cleanly load icons and stylesheets.
- 🧼 Don’t edit the generated UI `.py` files — subclass them if you want logic separation.
- 🔁 Regenerate `.py` every time you update `.ui` or `.qrc`.

---

## Virtual Environments in Python 

In Python, `virtualenv`, `.enve`, and `venv` all relate to managing isolated Python environments, but they differ slightly in terms of their implementation and usage.

### 1. **`virtualenv`**:

* `virtualenv` is a third-party Python package that allows you to create isolated environments for Python projects. It enables you to install dependencies without affecting the system-wide Python installation or other Python projects.
* When you use `virtualenv`, you create a new directory that contains its own Python binary and libraries, so any package you install will only be available in that environment.
* To install `virtualenv`:

  ```bash
  pip install virtualenv
  ```
* To create a virtual environment with `virtualenv`:

  ```bash
  virtualenv myenv
  ```

### 2. **`.enve`**:

* `.enve` is not a standard term in Python. It could be a custom or personal naming convention used by someone to denote an environment directory. However, `.enve` doesn't have a specific meaning in the context of Python's official tools.
* It's possible someone is referring to a hidden environment directory (since directories starting with a dot are hidden in Unix-based systems), but this isn't a standard Python feature.

### 3. **`venv`**:

* `venv` is a built-in Python module introduced in Python 3.3 that creates virtual environments. It's similar to `virtualenv`, but it's included in the standard library, so you don’t need to install anything extra.
* To create a virtual environment with `venv`:

  ```bash
  python -m venv myenv
  ```
* `venv` creates a lightweight environment that includes its own copy of the Python interpreter and a `lib` directory to hold the libraries installed via `pip`. It's the recommended way to manage virtual environments in modern Python projects.

### Key Differences:

* **`virtualenv`** is a third-party tool, while **`venv`** is part of Python's standard library.
* **`venv`** is recommended for most users because it's included with Python 3, whereas **`virtualenv`** is mostly used for legacy projects or if you're using an older version of Python.

In summary:

* Use **`venv`** for standard virtual environments in Python 3.
* **`virtualenv`** can be used if you're working with older Python versions or need specific features not available in `venv`.
* **`.enve`** may refer to a user-specific naming convention, but it's not a standard tool or feature in Python.

---

## Notes:

### The file **`file.cpython-313.pyc`** inside the **`__pycache__`** folder is a **compiled Python bytecode file**. Let’s break it down:  

---

#### **📌 What is `__pycache__`?**
- Python **automatically** creates a folder called `__pycache__` when you run a Python script or import a module.
- Inside it, Python stores **compiled bytecode files (`.pyc`)** to speed up execution in future runs.
- The `__pycache__` folder helps **avoid recompiling the script every time**.

---

#### **📌 What does `student.cpython-313.pyc` mean?**
- **`student`** → The name of your original Python file (`student.py`).
- **`cpython-313`** → The Python implementation and version:
  - `cpython` means it was compiled using **CPython** (the default Python interpreter).
  - `313` means **Python 3.13** was used.
- **`.pyc`** → Stands for **Python Compiled** bytecode.

---

#### **📌 Why does Python create `.pyc` files?**
- Python **compiles** `.py` scripts into bytecode (`.pyc`) to **run faster**.
- Next time you **run or import** the module, Python loads the `.pyc` file instead of recompiling.

---

#### **📌 Can I delete it?**
Yes! 🚀  
- You **can delete** the `__pycache__` folder and `.pyc` files anytime.  
- Python will **regenerate** them when you run the script again.  

---

#### **📌 How to prevent Python from creating `__pycache__`?**
If you **don’t want** Python to create `.pyc` files, set the environment variable:

```bash
export PYTHONDONTWRITEBYTECODE=1
```
Or, in Python scripts:
```python
import sys
sys.dont_write_bytecode = True
```

---

#### **📌 Should I ignore `__pycache__` in Git?**
✅ **Yes**, it's a best practice to ignore it in version control.  
Add this to `.gitignore`:
```
__pycache__/
*.pyc
```

---

### libraries you may find useful in scripting as a pentester


In Python, we can import libraries, which are a collection of files that contain functions. Think of importing a library as importing functions you can use that have been already written for you. For example, there is a "date" library that gives you access to hundreds of different functions for anything date and time-related.

```python

import datetime
current_time = datetime.datetime.now()
print(current_time)

```

We import other libraries using the import keyword. Then in Python, we use that import's library name to reference its functions. In the example above, we import datetime, then access the .now() method by calling library_name.method_name(). Copy and paste the example above into the code editor.

Here are some popular libraries you may find useful in scripting as a pentester:

- Request - simple HTTP library.
- Scapy - send, sniff, dissect and forge network packets
- Pwntools - a CTF & exploit development library.

Many of these libraries are already built into the programming language; however, libraries written by other programmers not already installed in your machine can be installed using an application called pip, which is Python's package manager. Let's say you want to install the "scapy" library (which allows you to craft your own packets in code and send them to other machines); you install it first by running the command pip install scapy, after which in your program you can now import the scapy library.





### 



---

### **Advanced Python Topics to Learn 🚀**

#### **1. Object-Oriented Programming (OOP) - Advanced**
Python supports OOP, but it has some unique features compared to Java.

- **Classes & Objects** (`__init__`, `self`)
- **Encapsulation, Inheritance, Polymorphism**
- **Magic Methods (`__str__`, `__repr__`, `__len__`, `__getitem__`)**
- **Metaclasses (Advanced Class Customization)**
- **Abstract Base Classes (`ABC` module)**
  
👉 **Example: Magic Methods**
```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

p = Person("Alice")
print(p)  # Output: Person: Alice
```

---

#### **2. Functional Programming**
Python supports functional programming concepts like:

- **Lambda functions** (`lambda` keyword)
- **Higher-order functions** (`map()`, `filter()`, `reduce()`)
- **List, Dictionary, and Set Comprehensions**
- **Decorators (`@staticmethod`, `@classmethod`, `@property`)**
- **Generators (`yield`) and Iterators**

👉 **Example: List Comprehension**
```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

👉 **Example: Lambda & Map**
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]
```

---

#### **3. Advanced Data Structures**
Apart from basic lists, tuples, sets, and dictionaries, Python provides:

- **Heap (`heapq` module)**
- **Deque (`collections.deque`)**
- **Defaultdict & OrderedDict (`collections` module)**
- **NamedTuple for lightweight structures**
- **Priority Queue (`queue.PriorityQueue`)**
  
👉 **Example: Using `deque` (Fast Queue Operations)**
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)      # Add to right
dq.appendleft(0)  # Add to left
dq.pop()          # Remove from right
dq.popleft()      # Remove from left
print(dq)  # Output: deque([1, 2])
```

---

#### **4. Multithreading & Multiprocessing**
Python supports concurrent programming for performance optimization.

- **`threading` module** (For I/O-bound tasks)
- **`multiprocessing` module** (For CPU-bound tasks)
- **Global Interpreter Lock (GIL) considerations**
- **AsyncIO for async programming**

👉 **Example: Using Threads**
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

---

#### **5. File Handling & Serialization**
- **Reading/Writing Files (`open()`, `with open() as`)**
- **JSON Handling (`json` module)**
- **Pickle Serialization (`pickle` module)**

👉 **Example: Reading a File**
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

#### **6. Regular Expressions (`re` module)**
Powerful for pattern matching in strings.

- **Finding patterns (`re.findall()`)**
- **Replacing text (`re.sub()`)**
- **Using regex groups (`re.match()`, `re.search()`)**

👉 **Example: Extracting Emails**
```python
import re

text = "Contact me at test@example.com or hello@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)  # Output: ['test@example.com', 'hello@domain.com']
```

---

#### **7. Web Scraping (`BeautifulSoup`, `Scrapy`, `requests`)**
Extracting data from websites.

👉 **Example: Using `requests` & `BeautifulSoup`**
```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Extracts page title
```

---

#### **8. Working with APIs (`requests` & `fastapi`)**
Interacting with REST APIs.

👉 **Example: Fetching Data from an API**
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
print(data["title"])
```

---

#### **9. Database Interaction (`SQLite`, `PostgreSQL`, `MongoDB`)**
- **SQLite (`sqlite3` module)**
- **PostgreSQL (`psycopg2`)**
- **MongoDB (`pymongo`)**

👉 **Example: SQLite Database**
```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
conn.commit()
conn.close()
```

---

#### **10. Testing & Debugging**
- **Unit Testing (`unittest`, `pytest`)**
- **Debugging (`pdb` module)**
- **Performance Profiling (`cProfile`)**

👉 **Example: Using `unittest`**
```python
import unittest

def add(x, y):
    return x + y

class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

---

#### **11. Design Patterns in Python**
Common software design patterns:

- **Singleton**
- **Factory Pattern**
- **Observer Pattern**
- **Decorator Pattern**

👉 **Example: Singleton Pattern**
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True
```

---

#### **12. Python for Data Science & Machine Learning**
- **NumPy** (Numerical computations)
- **Pandas** (Data manipulation)
- **Matplotlib/Seaborn** (Data visualization)
- **Scikit-Learn** (Machine learning)
- **TensorFlow/PyTorch** (Deep learning)

👉 **Example: Using `pandas`**
```python
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
```

---

#### **Final Thoughts**
##### **What Should You Learn Next?**
If you're coming from Java, here’s a suggested path:
1. **Deepen OOP concepts** in Python (since Python's OOP is more flexible).
2. **Understand functional programming** (lambdas, map/filter, decorators).
3. **Learn concurrent programming** (`threading`, `multiprocessing`, `asyncio`).
4. **Explore databases & APIs** (`sqlite3`, `requests`).
5. **Get comfortable with testing & debugging** (`unittest`, `pytest`).
6. **Try advanced topics like web scraping or machine learning.**

Python has a **broad ecosystem**, so choose topics based on your goals (e.g., Web Development, Data Science, Automation).

---

# **N.Q:**

## **🔹 What is `import sys` in Python?**  
The `sys` module in Python provides **access to system-specific parameters and functions**. It allows interaction with the Python interpreter, command-line arguments, and system-level operations.

---

### **🛠️ Common Uses of `sys`**
#### ✅ **1. Access Command-Line Arguments (`sys.argv`)**
```python
import sys

print("Script Name:", sys.argv[0])  # First argument is always the script name
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])  # Other arguments passed
```
Run in terminal:
```bash
python script.py hello world
```
Output:
```
Script Name: script.py
Arguments: ['hello', 'world']
```

---

#### ✅ **2. Exit the Program (`sys.exit()`)**
```python
import sys

if some_error_occurs:
    print("❌ Error occurred!")
    sys.exit(1)  # Exit the script with status code 1 (error)
```

---

#### ✅ **3. Get Python Version (`sys.version`)**
```python
import sys

print("Python Version:", sys.version)
```

---

#### ✅ **4. Modify Module Search Paths (`sys.path`)**
By default, Python searches for modules in **specific directories**.  
You can **add new paths** dynamically:
```python
import sys

sys.path.append("/custom/path/to/modules")
print(sys.path)  # Shows all directories Python searches for imports
```

---

#### ✅ **5. Get System Platform (`sys.platform`)**
```python
import sys

print("Current OS:", sys.platform)
```
Output:
- `"win32"` → Windows  
- `"linux"` → Linux  
- `"darwin"` → macOS  

---

### **🚀 Summary**
- `sys.argv` → Get command-line arguments  
- `sys.exit()` → Exit program  
- `sys.version` → Get Python version  
- `sys.path` → Manage module search paths  
- `sys.platform` → Get OS info  

---

## **PyPI vs PyPy**

**PyPI** and **PyPy** are two distinct concepts in the Python ecosystem, serving entirely different purposes:
### PyPI (Python Package Index)
- **Definition**: PyPI is the official repository for third-party Python software packages. It acts as a central hub where developers can upload, share, and distribute Python libraries and tools.
- **Purpose**:
  - Allows Python developers to find and install pre-built packages using tools like `pip`.
  - Simplifies software distribution and dependency management for Python projects.
- **Usage**:
  - To install a package from PyPI, you typically use the command: `pip install `.
  - It hosts a wide variety of libraries, ranging from web frameworks to data analysis tools.

### PyPy
- **Definition**: PyPy is an alternative implementation of the Python interpreter. Unlike the standard Python interpreter (CPython), PyPy is written in a subset of Python called RPython (Restricted Python).
- **Key Features**:
  - **Speed**: Includes a Just-In-Time (JIT) compiler, making it significantly faster than CPython for many workloads.
  - **Memory Efficiency**: Uses less memory compared to CPython.
  - **Compatibility**: Supports most existing Python libraries.
  - **Stackless Features**: Enables advanced threading capabilities for high-concurrency applications.
- **Use Cases**:
  - Ideal for performance-critical applications where speed and memory efficiency are essential.
  - Useful for research or projects requiring advanced language features or experimentation with dynamic languages.

### Comparison Table

| Feature                  | PyPI                                      | PyPy                                      |
|--------------------------|-------------------------------------------|-------------------------------------------|
| **Type**                 | Repository for Python packages           | Alternative Python interpreter            |
| **Purpose**              | Software distribution                    | Faster execution of Python code           |
| **Written In**           | N/A                                      | RPython (Restricted Python)               |
| **Key Advantage**        | Easy access to third-party libraries      | Speed (via JIT compiler)                  |
| **Usage Example**        | `pip install numpy`                      | Running Python code faster than CPython   |

In summary, PyPI is a repository to find and install Python packages, while PyPy is an optimized interpreter designed to execute Python code more efficiently.