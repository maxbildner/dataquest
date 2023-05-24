""" comment 1
comment 2
"""

# "everything is an object"

# PYTHON REVIEW NOTES / CHEAT SHEET

# 1) OBJECTS
# PYTHON- OBJECTS
#   - everything is an object

# JAVASCRIPT- OBJECTS
#   - almost everything is an object
#   - primitive data types (number, string, boolean, null, undefined, symbol) are NOT objects
#   - JS objects are more like Python classes intead of like python dictionaries
#   - JS objects are a storage of key:value pairs
#   - JS objects are also called "dictionaries"
# https://jfine-python-classes.readthedocs.io/en/latest/javascript-objects.html#:~:text=JavaScript%20objects%20are%20like%20Python,a%20superclass%20of%20its%20type).
# https://stackoverflow.com/questions/20987485/what-are-the-differences-between-python-dictionaries-vs-javascript-objects
# https://dev.to/justforaday__/javascript-vs-python-object-1c03#:~:text=So%20Python%20has%20mutable%20and,is%20mutable%2C%20int%20is%20immutable.&text=In%20JS%2C%20we%20also%20say,%2C%20number%2C%20boolean%20and%20symbol.


# ________________________________________________________________________________
# 2) PRIMITIVE vs NON-PRIMITIVE DATA TYPES
# PYTHON- PRIMITIVE DATA TYPE
#   - no such thing as a "primitive" like in other languages (Java, JavaScript)
# https://www.quora.com/Does-Python-have-primitive-types
# https://stackoverflow.com/questions/46683060/are-python-primitives-objects-or-primitves-like-an-object
# https://blog.varunramesh.net/posts/no-more-primitives/

# JAVASCRIPT- PRIMITIVE vs NON-PRIMITIVE DATA TYPES
#   - PRIMITIVE DATA TYPE
#     - contain a single value (ex. "yes", 13, 13.0, True)
#     - the basic building blocks for other data types
#     - immutable (once a value is created, it cannot be changed)
#     - 7 Primitive Types:
#       - Number, String, Boolean, Undefined, Null, Symbol, BigInt
#   - NON-PRIMITIVE DATA TYPE
#     - objects
# https://www.freecodecamp.org/news/python-vs-javascript-what-are-the-key-differences-between-the-two-popular-programming-languages/#:~:text=Python%20has%20four%20primitive%20data,%2C%20and%20null%20(source).
# https://www.edureka.co/blog/data-types-in-javascript/#difference-1
# https://res.cloudinary.com/practicaldev/image/fetch/s--FFnTzQrh--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tiq8n9z3hsbimcdy17kb.png


# ________________________________________________________________________________
# 3) DATA TYPES
# PYTHON- DATA TYPES
#   - 5 Main Types:
#     - Numeric
#       - Integer (ex. 13, -1), Float (ex. 1.0), Complex
#     - Dictionary
#     - Boolean (ex. True, False)
#     - Set
#     - Sequence
#       - String, List, Tuple
# https://www.theengineeringprojects.com/2020/06/how-to-use-data-types-in-python.html
# https://www.geeksforgeeks.org/python-data-types/


# ________________________________________________________________________________
# 4) IMMUTABLE DATA TYPES
# PYTHON- IMMUTABLE DATA TYPES
#   - objects that cannot be changed after creation:
#     - 1 Int (ex. 5, -5)
#     - 2 Float (ex. -5.0)
#     - 3 Tuple
#     - 4 Complex
#     - 5 String (ex. "ye", 'ye')
#     - 6 Bytes
#     - 7 Frozen Set
#   - attempting to change the value of an immutable datatype DOES result in an error! Ex:
#     fruit = "mango"
#     fruit[0] = "ZZZ"  # TypeError 'str' object does not support item assignment
# https://www.tutorialspoint.com/Which-data-types-are-immutable-in-Python

# JAVASCRIPT- IMMUTABLE DATA TYPES
# - all 7 primitive data types:
#   - Number (all are floating point), String, Boolean, Undefined, Null, Symbol, BigInt
# - attempting to change the value of an immutable datatype does NOT result in an error! Ex:
#   let fruit = "mango"
#   fruit[0] = "Z" # No Error!
# https://developer.mozilla.org/en-US/docs/Glossary/Immutable
# https://javascript.plainenglish.io/javascript-mutable-vs-immutable-1efb662d78c8


# ________________________________________________________________________________
# 5) MUTABLE DATA TYPES
# PYTHON- MUTABLE DATA TYPES
# - List, Set, Dictionary, ByteArray, Array
# https://www.scientecheasy.com/2023/01/mutable-and-immutable-in-python.html/


# ________________________________________________________________________________
# 6) NONE- None
# JS has "null" or "undefined" data types, but python does not! python has "None" datatype
print("------- 6)")
print(type(None))  # => <type 'NoneType'>


# ________________________________________________________________________________
# 7) LIST DATA TYPE
# - Sequences = list, arrays, tuple, range
# - lists can store different datatypes (unlike array)
# - mutable (unlike tuple)
# - JS does NOT support negative indexing like in python!
# - JS length: arr.length    python length: len(arr)
print("------- 7)")
list1 = ["a", "b", 4]
print(list1[-1])  # => 4
print(len(list1))  # => 3


# ________________________________________________________________________________
# 8) Variable Naming- same as JS
# - A to Z, or 0 to 9, or "_"
# - first character must start with letter or "_", no special characters
# JS also first char must begin with letter or "_", no special characters
print("------- 2)")
_apple = 2  # GOOD
print(_apple)


# ________________________________________________________________________________
# 9) Multi Variable Assignment
# - don't have to define variable type like in other languages
# - assigning multiple values to multiple variables:
print("------- 1)")
a, b, c = 1, 2, 3
print(a)  # => 1
print(b)  # => 2
print(c)  # => 3
# JS multi variable assigment
# [ a, b, c ] = [ 1, 2, 3 ]

# Assign the same value to multiple variables
# https://note.nkmk.me/en/python-multi-variables-values/#:~:text=You%20can%20assign%20the%20same,variables%20with%20the%20same%20value.&text=After%20assigning%20the%20same%20value,to%20one%20of%20the%20variables


# ________________________________________________________________________________
# 10) CONSTANTS
# - convention is to use all caps (can use lowercase)
# - lets others know this variable shouldn't be changed (but in reality we can reassign with no errors!)
print("------- 3)")
PRICE = 5
PRICE = 2
print(PRICE)  # => 2
# JS uses "const" keyword to declare a constant, and re-assigning a constant will cuase a TypeError!


# ________________________________________________________________________________
# 11) Function Hoisting
# PYTHON- functions are NOT hoisted
# JS- functions declarations ARE hoisted (function expressions/arrow functions are not)
# https://i.redd.it/1x4ho2qngv421.jpg
