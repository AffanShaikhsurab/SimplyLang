# Simply Programming Language Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Syntax](#basic-syntax)
3. [Variables and Data Types](#variables-and-data-types)
4. [Mathematical Operations](#mathematical-operations)
5. [Data Structures](#data-structures)
6. [Functions](#functions)
7. [Control Structures](#control-structures)
8. [Error Handling](#error-handling)

## Introduction
Simply is a programming language designed to make coding accessible and intuitive, using natural language-like syntax for better readability and understanding.

## Basic Syntax
- Statements end with a period (.)
- Comments start with "Note:" and must end with a period
- Code blocks are defined using periods
- The language uses natural English-like expressions

### Comments
Comments in Simply use a natural language format:
```simply
Note: This is a single line comment that must end with a period.
Note: Comments make code more readable and help explain complex logic.
Note: Multiple comments can be used to provide detailed explanations.
```

## Variables and Data Types
### Variable Assignment
Variables are assigned using the 'is' keyword:
```simply
a is 10
b is 20
```

### Supported Data Types
1. Numbers (Integers)
2. Strings (Text enclosed in quotes)
3. Arrays
4. Dictionaries

## Mathematical Operations
The language supports basic mathematical operations:
```simply
Note: Perform subtraction of two variables and store in c.
c is a - b
Note: Add 10 to the element variable.
elememt + 10
```

## Data Structures
### Arrays
Arrays are created using comma-separated values:
```simply
array is 1, 2, 4
```

Accessing array elements:
```simply
Note: Access the first element of the array.
elememt is array[0]
```

### Dictionaries
Dictionaries are created using key-value pairs:
```simply
dict is Name Affan, Age 20
```

Accessing and modifying dictionary values:
```simply
Note: Access the value associated with the Name key.
name is Name of dict
Note: Modify the value of the Name key.
Name of dict is "John Doe"
```

## Functions
### Function Definition
Functions are defined using 'takes' and 'does' keywords:
```simply
add takes a, b does
    sum is a + b
    return sum
.
```

### Function Calls
Functions can be called directly or with variable assignment:
```simply
sum is add(10, 20)
show("added sum is", add(1, 2))
```

## Control Structures
### While Loop
While loops use the 'till' and 'do' keywords:
```simply
till a < b do
    show("value of a inside the loop is:", a)
    a is a + 5
.
```

### For Loop
For loops use the 'repeat' keyword:
```simply
repeat 5 times
    show("the value of a is", a)
.
```

### Conditional Statements
If-else statements use 'if', 'then', and 'otherwise' keywords:
```simply
if a equals b then
    show("a and b are equal", a)
otherwise
    show("a and b are different", b)
.
```

## Error Handling
### Try-Oops Blocks
Error handling uses 'try' and 'oops' keywords:
```simply
try
    show("the task1 completed successfully")
    stop with "something went wrong in task1"
    show("the task2 completed successfully")
oops
    show("something went wrong")
.
```

### Break Statement
Use 'stop with' to break execution:
```simply
stop with "something went wrong in task1"
```

## Built-in Functions
### show()
The 'show' function is used for output:
```simply
show("array is", array)
show("Name of dict Name", name)```
