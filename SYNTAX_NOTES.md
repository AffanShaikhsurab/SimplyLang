# SimplyLang Programming Language

A lightweight, beginner-friendly scripting language for learning programming
with simple words. The current child-first direction is to start with tiny
visible programs, then grow toward the full text language.

## Table of Contents
- [Variables](#variables)
- [Kid Core](#kid-core)
- [Data Structures](#data-structures)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [I/O Operations](#io-operations)
- [Error Handling](#error-handling)


---

## Kid Core

Use this subset first for ages 7-10:

```simply
show("Hi, I am Robo!")

score is 0
score is score + 1

repeat 3 times
    show("Robo dance!")
.

if score > 2 then
    show("Great job!")
otherwise
    show("Try one more time!")
.
```

Save advanced lists, dictionaries, classes, contracts, and `try/oops` for later
lessons.

---

## Variables


**Examples:**
```simply
Note : Assigning variables .
a is 10 
b is 20 
```

---

## Data Structures

### Arrays
 

**Example:**
```simply
Note : creating arrays  .

array is 1 , 2 , 4 
Note: prinitng .

show("array is " , array)
```

### Dictionaries

**Example:**
```simply

Note : creating dicts .

dict is Name Affan , Age  20 

show("dict is " , dict)

name is Name of dict 

show("Name of dict Name" , name )

Note : Editing dict .

m is "John Doe"

Name of dict is "John Doe"

name is Name of dict 

show("Name of dict Name" , name )
```

---

## Operators
| Type       | Operators          |
|------------|--------------------|
| Arithmetic | `+ - * / % ^`      |
| Comparison | `equals not equals < >` |
| Logical    | `and or not`       |

**Example:**
```simply
result is (10 + 3) * 2    
```

---

## Control Flow

### If-Else
```simply
if a equals b then
 show("a and b are equal" , a)

otherwise 
 show("a and b are different " , b)
```


### Loops
```simply
#Note: This is while loop .

till a < b do show("value of a inside the loop is :" , a) a is a + 5 .

#Note: This is for loop . 

repeat 5 times
show("the value of a is " , a)

```
---

## Functions

**Example:**
```simply

add takes a , b does 
    sum is a + b
    return sum 
.

sum is add(10 , 20 )
show("added sum is " , sum)


Note: direct calling of sum .

show("added sum is " , add(1 , 2)) 
```

---


## I/O Operations

### Printing
```simply
Note: prinitng .
show(<val1>, <val2>, ...)
```

---

## Error Handling

**Example:**
```simply
Note: This is try-oops block .

try
 
   show("the task1 completed successfully")

   Note: this is break statements .

   stop with " something went wrong in task1 "

   show("the task2 completed successfully")

oops 

   show("something went wrong")

. 
```
---

