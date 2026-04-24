# SEA Lang Documentation 🌊

**Version 1.0** | A Family-Friendly Programming Language Built on Python

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Language Syntax](#language-syntax)
4. [Data Types](#data-types)
5. [Operators](#operators)
6. [Control Flow](#control-flow)
7. [Functions](#functions)
8. [Built-in Functions](#built-in-functions)
9. [String Formatting](#string-formatting)
10. [Error Handling](#error-handling)
11. [Examples](#examples)
12. [Migration Guide](#migration-guide)

---

## Introduction

### What is SEA Lang?

**SEA Lang** is a human-centric programming language that makes Python accessible to everyone. It provides two syntax styles:

- **Natural Language Style**: Use readable phrases like `is equal to`, `plus`, `times`
- **Symbol Style**: Use traditional operators like `=`, `+`, `*`

Mix and match styles in the same program for maximum flexibility!

### Philosophy

SEA Lang removes barriers to coding by:
- Eliminating mathematical jargon
- Providing readable, self-documenting code
- Offering a gentle roadmap from natural language to logical thinking
- Leveraging Python's full power without its complexity

### Key Features

✅ **Dual-Mode Syntax** - Use words or symbols, your choice  
✅ **No Math Required** - Complex operations in plain English  
✅ **Onion Parsing** - Nested functions handled automatically  
✅ **Full Python Power** - Everything Python can do, SEA can do  
✅ **Flexible Indentation** - Combines readability with structure  

---

## Getting Started

### Installation

1. Ensure Python 3.6+ is installed on your system
2. Place `sea.py` in your project directory
3. Create `.sea` files with your code

### Running SEA Code

```bash
python sea.py
# Then enter the path to your .sea file when prompted
```

### Your First Program

Create a file named `hello.sea`:

```
write "Hello, World!"
```

Run it:
```bash
python sea.py
# Enter: hello.sea
```

---

## Language Syntax

### Comments

Single-line comments start with `#`:

```
# This is a comment
write "Hello"  # This is an inline comment
```

### Basic Structure

SEA code is line-based. Each line is a statement:

```
variable is equal to 5
write variable
```

### Statement Termination

Statements end with a period `.` or newline:

```
x is equal to 10.
y is equal to 20
```

---

## Data Types

### Numbers

#### Integers
```
count is equal to 42
count = 42  # Both syntaxes work
```

#### Floats
```
pi is equal to 3.14
temperature = -273.15
```

#### Scientific Notation
```
large_number is equal to 1.5e10
small_number = 3.2e-5
```

### Strings

Enclose text in double or single quotes:

```
name is equal to "Alice"
greeting = 'Hello, World!'
message is equal to "She said \"Hello\""
```

### Booleans

```
is_active is equal to true
is_ready = false
condition is equal to Nothing
```

### Collections

#### Lists

```
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, true]
```

#### Dictionaries

```
person = {"name": "John", "age": 30}
```

---

## Operators

### Assignment Operators

| Natural Language | Symbol |
|------------------|--------|
| `is equal to` | `=` |
| `plus equal to` | `+=` |
| `minus equal to` | `-=` |
| `times equal to` | `*=` |
| `over equal to` | `/=` |
| `mod equal to` | `%=` |
| `to power of equal to` | `**=` |

### Arithmetic Operators

| Natural Language | Symbol | Example |
|------------------|--------|---------|
| `plus` | `+` | `5 plus 3` = `5 + 3` |
| `minus` | `-` | `10 minus 2` = `10 - 2` |
| `times` | `*` | `4 times 5` = `4 * 5` |
| `over` | `/` | `20 over 4` = `20 / 4` |
| `mod` | `%` | `10 mod 3` = `10 % 3` |
| `to power of` | `**` | `2 to power of 3` = `2 ** 3` |

### Comparison Operators

| Natural Language | Symbol | Example |
|------------------|--------|---------|
| `equal to` | `==` | `x equal to 5` = `x == 5` |
| `not equal to` | `!=` | `x not equal to 5` = `x != 5` |
| `greater than` | `>` | `x greater than 5` = `x > 5` |
| `less than` | `<` | `x less than 5` = `x < 5` |
| `greater than or equal to` | `>=` | `x >= 5` |
| `less than or equal to` | `<=` | `x <= 5` |

### Logical Operators

| Natural Language | Symbol | Example |
|------------------|--------|---------|
| `and` | `and` | `x and y` |
| `or` | `or` | `x or y` |
| `not` | `not` | `not x` |

### Bitwise Operators

| Natural Language | Symbol |
|------------------|--------|
| `bitwise and` | `&` |
| `bitwise or` | `\|` |
| `bitwise xor` | `^` |
| `bitwise not` | `~` |
| `left shift` | `<<` |
| `right shift` | `>>` |

### Membership Operators

```
element in list      # Check if in collection
element not in list  # Check if not in collection
```

### Identity Operators

```
x is y          # Same object?
x is not y      # Different objects?
```

---

## Control Flow

### Conditional Statements

#### if...else

**Natural Language:**
```
n is equal to 10
if n greater than 5:
    write "n is greater than 5"
else:
    write "n is 5 or less"
```

**Symbol Style:**
```
n = 10
if n > 5:
    write "n is greater than 5"
else:
    write "n is 5 or less"
```

#### if...else if...else

```
score = 85
if score greater than or equal to 90:
    write "Grade A"
else if score greater than or equal to 80:
    write "Grade B"
else if score greater than or equal to 70:
    write "Grade C"
else:
    write "Grade F"
```

### Loops

#### while Loop

```
count is equal to 0
while count less than 5:
    write count
    count plus equal to 1
```

#### for Loop

```
for i in [1, 2, 3, 4, 5]:
    write i
```

#### approches Loop (Counting Loop)

SEA's special counting loop syntax:

```
approches 5 times:
    write "This runs 5 times"
```

#### Loop Control

```
while true:
    value = input "Enter a number: "
    if value equal to "quit":
        break.
    write value

for i in range 10:
    if i equal to 5:
        continue
    write i
```

---

## Functions

### Function Definition

**Natural Language:**
```
GET_SQUARE n:
    square_of_n is equal to n to power of 2
    return square_of_n
```

**Symbol Style:**
```
def square(n):
    result = n ** 2
    return result
```

### Function Calls

```
result = GET_SQUARE 5
write result  # Output: 25
```

### Multiple Parameters

```
GET_SUM a, b:
    total is equal to a plus b
    return total

sum_result = GET_SUM 10, 20
write sum_result  # Output: 30
```

### Functions Without Return

```
GREET name:
    write "Hello, {name}!"

GREET "Alice"  # Output: Hello, Alice!
```

---

## Built-in Functions

### Input/Output

| Natural Language | Python | Description |
|------------------|--------|-------------|
| `write` | `print()` | Display output |
| `display` | `print()` | Display output |
| `output` | `print()` | Display output |
| `input` / `scan` / `get` / `read` | `input()` | Get user input |

### Type Conversion

```
write int "42"           # Convert to integer
write float "3.14"       # Convert to float
write str 42             # Convert to string
write bool 1             # Convert to boolean
```

### List Operations

```
numbers = [1, 2, 3, 4, 5]
length = len numbers     # Get length
maximum = max numbers    # Get maximum
minimum = min numbers    # Get minimum
```

### String Operations

```
text = "Hello World"
upper = text.upper()
lower = text.lower()
substring = text[0:5]    # Get first 5 chars
```

### Range Function

```
for i in range 10:
    write i  # 0 through 9

for i in range 1, 6:
    write i  # 1 through 5
```

---

## String Formatting

SEA automatically converts `{}` placeholders to f-string format:

### Variable Substitution

```
name = "Alice"
age = 30
write "My name is {name} and I'm {age} years old"
# Output: My name is Alice and I'm 30 years old
```

### Expression Evaluation

```
x = 5
y = 3
write "The sum is {x plus y}"
# Output: The sum is 8
```

### Multiple Placeholders

```
write "First: {a}, Second: {b}, Third: {c}"
```

---

## Error Handling

### try...except

**Natural Language:**
```
while true:
    try:
        n is equal to float input "Enter a number: "
        result = n to power of 2
        write "Square: {result}"
        break.
    except ValueError:
        write "Please enter a valid number"
    except:
        write "An error occurred"
```

**Symbol Style:**
```
while true:
    try:
        n = float(input("Enter a number: "))
        print(n ** 2)
        break
    except ValueError:
        print("Invalid input")
```

### Exception Types

Common exceptions in SEA:

- `ValueError` - Invalid value (e.g., wrong type)
- `NameError` - Variable not defined
- `IndexError` - List index out of range
- `KeyError` - Dictionary key not found
- `TypeError` - Wrong type for operation
- `ZeroDivisionError` - Division by zero
- `FileNotFoundError` - File doesn't exist

---

## Examples

### Example 1: Simple Calculator

```
# Simple SEA Calculator

write "=== Simple Calculator ==="
write ""

a is equal to float input "Enter first number: "
operation is equal to input "Enter operator (+, -, *, /): "
b is equal to float input "Enter second number: "

if operation equal to "+":
    result is equal to a plus b
else if operation equal to "-":
    result is equal to a minus b
else if operation equal to "*":
    result is equal to a times b
else if operation equal to "/":
    result is equal to a over b
else:
    write "Invalid operator"
    ...

write "Result: {result}"
```

### Example 2: Fibonacci Sequence

```
# Generate Fibonacci sequence

GET_FIBONACCI n:
    if n less than or equal to 1:
        return n
    else:
        return GET_FIBONACCI n minus 1 plus GET_FIBONACCI n minus 2

limit is equal to int input "How many Fibonacci numbers? "

for i in range limit:
    write GET_FIBONACCI i
```

### Example 3: List Processing

```
# Process a list of numbers

numbers = [10, 25, 15, 30, 5]

write "Original list: {numbers}"
write "Sum: {sum numbers}"
write "Average: {sum numbers over len numbers}"
write "Max: {max numbers}"
write "Min: {min numbers}"

for num in numbers:
    if num greater than 15:
        write "{num} is greater than 15"
```

### Example 4: String Manipulation

```
# String processing example

text = input "Enter text: "

write "Length: {len text}"
write "Uppercase: {text.upper()}"
write "Lowercase: {text.lower()}"

if "hello" in text.lower():
    write "Contains 'hello'"
```

### Example 5: Dictionary Usage

```
# Working with dictionaries

person is equal to {"name": "John", "age": 30, "city": "New York"}

write "Person: {person}"
write "Name: {person['name']}"
write "Age: {person['age']}"

person["age"] = 31
write "Updated: {person}"
```

---

## Migration Guide

### From Python to SEA

#### Variables

**Python:**
```python
x = 5
y = 10
```

**SEA:**
```
x is equal to 5
y is equal to 10
```

#### Arithmetic

**Python:**
```python
result = a + b * c
```

**SEA:**
```
result is equal to a plus b times c
```

#### Conditionals

**Python:**
```python
if x > 5 and y < 20:
    print("Condition met")
```

**SEA:**
```
if x greater than 5 and y less than 20:
    write "Condition met"
```

#### Loops

**Python:**
```python
for i in range(5):
    print(i)
```

**SEA:**
```
for i in range 5:
    write i
```

#### Functions

**Python:**
```python
def square(n):
    return n ** 2
```

**SEA:**
```
GET_SQUARE n:
    return n to power of 2
```

---

## Best Practices

### 1. Code Organization

- Start with imports and constants
- Define functions before main logic
- Use meaningful variable names
- Keep functions focused and single-purpose

### 2. Readability

- Use natural language for clarity when appropriate
- Use symbols when code gets long
- Add comments for complex logic
- Consistent indentation (4 spaces recommended)

### 3. Error Handling

- Always handle user input with try...except
- Use specific exception types
- Provide helpful error messages
- Validate data before processing

### 4. Performance

- Avoid unnecessary loops
- Use built-in functions (they're faster)
- Cache repeated calculations
- Profile before optimizing

---

## Troubleshooting

### Common Issues

**Issue: "No such file or directory"**
- Ensure the .sea file exists in the correct path
- Check file name spelling and extension

**Issue: "SyntaxError in generated code"**
- Check for mismatched quotes in strings
- Verify correct syntax for operators
- Look for unbalanced parentheses

**Issue: "NameError: name not defined"**
- Ensure variable is created before use
- Check spelling of variable names
- Verify scope (functions can't access outer variables without proper declaration)

**Issue: "Indentation Error"**
- Ensure consistent indentation (spaces, not tabs)
- All code inside if/for/while must be indented
- Use exactly 4 spaces for each level

---

## Support & Resources

- **Examples**: See `main.sea` for a working example
- **Syntax**: Refer to the Operators and Control Flow sections
- **Issues**: Debug using the generated Python code for detailed error messages

---

## Version History

- **v1.0** (April 2026) - Initial release with core features
  - Natural language and symbol syntax support
  - Full Python integration
  - Basic error handling
  - Function definitions and calls

---

## License

SEA Lang is created as a family-friendly educational tool.

**Happy Coding! 🌊**
