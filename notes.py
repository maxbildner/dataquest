""" comment 1
comment 2
"""

# "everything is an object"

# PYTHON REVIEW NOTES / CHEAT SHEET
# 1) Multi Variable Assigment
# - don't have to define variable type like in other languages
# - assigning multple values to multiple variables:
print("------- 1)")
a, b, c = 1, 2, 3
print(a)  # => 1
print(b)  # => 2
print(c)  # => 3
# JS multi variable assigment
# [ a, b, c ] = [ 1, 2, 3 ]


# 2) Variable Naming- same as JS
# - A to Z, or 0 to 9, or "_"
# - first character must start with letter or "_", no special characters
# JS also first char must begin with letter or "_", no special characters
print("------- 2)")
_apple = 2  # GOOD
print(_apple)


# 3) CONSTANTS
# - convention is to use all caps (can use lowercase)
# - lets others know this variable shouldn't be changed (but in reality we can reassign with no errors!)
print("------- 3)")
PRICE = 5
PRICE = 2
print(PRICE)  # => 2
# JS uses "const" keyword to declare a constant, and re-assigning a constant will cuase a TypeError!


# 4) Strings are immutable
# JS strings are also immutable
print("------- 4)")
apple = "apple"
# apple[0] = "Z" #=> TypeError 'str' object does not support item assignment


# 5) DATA TYPES - PRIMITIVE DATA TYPES
# - Integers - signed integers
#     -5
# - Float - decimal points accurate to 15 decimal places
#     -5.0
# - Strings - single or double quotation marks
#     "apple"
#     'apple'
# - Boolean
#     True
#     False
# JS numbers are all floating point! (64-bit)
print("------- 5)")
num1 = -5
print(type(num1))  # => <type 'int'>

num2 = 5.0
print(type(num2))  # => <type 'float'>


# 6) None
# JS has "null" or "undefined" data types, but python does not! python has "None" datatype
print("------- 6)")
print(type(None))  # => <type 'NoneType'>


# 7) DATA TYPES - SEQUENCES - LIST
# - Sequences = list, arrays, tuple, range
# - can store different datatypes (unlike array)
# - mutable (unlike tuple)
# - JS does NOT support negative indexing like in python!
# - JS length: arr.length    python length: len(arr)
print("------- 7)")
list1 = ["a", "b", 4]
print(list1[-1])  # => 4
print(len(list1))  # => 3
