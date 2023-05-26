""" 
Multi Line Comments
line 2
"""

# PYTHON REVIEW NOTES / CHEAT SHEET

# ________________________________________________________________________________
# 1) COMPILED vs INTERPRETED
# PYTHON- Usually Interpreted
# JS- Usually Interpreted


# ________________________________________________________________________________
# 2) STATICALLY vs DYNAMICALLY Typed Language
# PYTHON- Dynamically Typed
# JS- Dynamically Typed
#
# DYNAMICALLY TYPED Language =
#   - perform type checking at run-time
#   - no need to declare variables before you use them
# STATICALLY TYPED Language =
#   - perform type checking at compile-time
#   - must declare variables before you use them
# TYPE CHECKING
#   - verifiying if the data types are compatible with the operands being used on them


# ________________________________________________________________________________
# 3) STRONGLY vs WEAKLY Typed Language
# PYTHON- Strongly
# JS- Weakly
#
# STRONGLY = does NOT allow implicit conversion between unrelated data types
# WEAKLY = DOES allow implicit conversion between unrelated data types
# Python Ex.
print("------- 3)")
# 1 + "2"  # TypeError!


# ________________________________________________________________________________
# 4) OBJECTS
# PYTHON- OBJECTS
#   - everything is an object

# JAVASCRIPT- OBJECTS
#   - almost everything is an object
#   - 7 primitive data types (number, string, boolean, null, undefined, symbol, bigInt) are NOT objects
#   - JS objects are more like Python classes intead of like python dictionaries
#   - JS objects are a storage of key:value pairs
#   - JS objects are also called "dictionaries"
# https://jfine-python-classes.readthedocs.io/en/latest/javascript-objects.html#:~:text=JavaScript%20objects%20are%20like%20Python,a%20superclass%20of%20its%20type).
# https://stackoverflow.com/questions/20987485/what-are-the-differences-between-python-dictionaries-vs-javascript-objects
# https://dev.to/justforaday__/javascript-vs-python-object-1c03#:~:text=So%20Python%20has%20mutable%20and,is%20mutable%2C%20int%20is%20immutable.&text=In%20JS%2C%20we%20also%20say,%2C%20number%2C%20boolean%20and%20symbol.


# ________________________________________________________________________________
# 5) DATA TYPES
# PYTHON- DATA TYPES
#   - 5 Main Types:
#     - Numeric
#       - Integer (ex. 13, -1), Float (ex. 1.0), Complex (ex. 3j)
#     - Dictionary (ex. { 5: True, "a": 2 })
#     - Boolean (ex. True, False)
#     - Set (ex. { "apple", 2, "mango" } )
#     - Sequence
#       - String (ex. "ye", 'ye'), List (ex. [1, "a", [3]] ), Tuple (ex. (1, "a", [ "b", 2 ]) )
# https://www.theengineeringprojects.com/2020/06/how-to-use-data-types-in-python.html
# https://www.geeksforgeeks.org/python-data-types/


# ________________________________________________________________________________
# 6) PRIMITIVE vs NON-PRIMITIVE DATA TYPES
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
# 7) IMMUTABLE DATA TYPES
# PYTHON- IMMUTABLE DATA TYPES
#   - objects that cannot be changed after creation:
#     - 1 Int (ex. 5, -5)
#     - 2 Float (ex. -5.0)
#     - 3 Complex (ex. 3j)
#     - 4 Tuple (ex. (1, "a", [ "b", 2 ]) )
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
# 8) Variable Declaration / Assignment
# PYTHON
# - no need to declare variable data types like in C++ (ex. int myNum;)
# - no declaration needed before assignment!
# - no keywords (ex. let, var, const) when declaring like in JS
#
# JS
# - no need to declare variable before assignment but you can!
# - keywords (ex. let, var, const) to control variable scope


# ________________________________________________________________________________
# 9) Variable Naming- same as JS
# - A to Z, or 0 to 9, or "_"
# - first character must start with letter or "_", no special characters
# JS also first char must begin with letter or "_", no special characters
print("------- 9)")
_apple = 2  # GOOD
print(_apple)


# ________________________________________________________________________________
# 10) Multi Variable Assignment
# - don't have to define variable type like in other languages
# - assigning multiple values to multiple variables:
print("------- 10)")
a, b, c = 1, 2, 3
print(a)  # => 1
print(b)  # => 2
print(c)  # => 3
# JS multi variable assigment
# [ a, b, c ] = [ 1, 2, 3 ]

# Assign the same value to multiple variables
# https://note.nkmk.me/en/python-multi-variables-values/#:~:text=You%20can%20assign%20the%20same,variables%20with%20the%20same%20value.&text=After%20assigning%20the%20same%20value,to%20one%20of%20the%20variables


# ________________________________________________________________________________
# 11) CONSTANT VARIABLES
# - convention is to use all caps (can use lowercase)
# - lets others know this variable shouldn't be changed (but in reality we can reassign with no errors!)
print("------- 11)")
PRICE = 5
PRICE = 2
print(PRICE)  # => 2
# JS uses "const" keyword to declare a constant, and re-assigning a constant will cuase a TypeError!


# ________________________________________________________________________________
# 12) NONE Data Type- None
# JS has "null" or "undefined" data types, but python does not! python has "None" datatype
print("------- 12)")
print(type(None))  # => <type 'NoneType'>


# ________________________________________________________________________________
# 13) Function Hoisting
# PYTHON- functions are NOT hoisted
# JS- functions declarations ARE hoisted (function expressions/arrow functions are not)
# https://i.redd.it/1x4ho2qngv421.jpg


# ________________________________________________________________________________
# 14) DETERMINE VALUE's DATA TYPE
# type( __ )
# Ex.
print("------- 14)")
print(type([1, 2, "a"]))  # => <type 'list'>

# JS- typeof [1, 2, "a"] // "object"


# ________________________________________________________________________________
# 15) LIST DATA TYPE
# - Sequences = list, arrays, tuple, range
# - 1) supports NEGATIVE INDEXING to refer to elements starting from end of list
#   - JS does NOT support negative indexing like in python! (won't get error)
# - 2) will get ERROR if you try to index an element out of range/doesn't exist
#   - JS will NOT get error if indexing an element out of range/doesn't exist (will get undefined)
# - 3) len( list ) method to get length of list in O(1) time
#   - JS arr.length
# Ex.
print("------- 15)")
list1 = ["a", "b", 4]
print(list1[-1])  # => 4
print(list1[-2])  # => "b"
print(len(list1))  # => 3

# - lists can store different datatypes (unlike array)
# - mutable (unlike tuple)


# ________________________________________________________________________________
# 16) LIST MANIPULATION- ADDING ITEM
# list.append( item ) #=> None
# - adds item to end of list
# - param: item to addd (only 1 param!)
# - return: None
# - will get error if you try adding more than one param
# Ex.
print("------- 16)")
list1 = [1, 2]
list1.append("a")
print(list1)  # => [ 1, 2, "a" ]

# JS array.push(item, item2, ...) => (num) length of new array


# ________________________________________________________________________________
# 17) LIST MANIPULATION- COMBINING LISTS
# - use + plus operator
# - listA + listB   #=> listC
# - returns new list where items from listB are spread onto the end of listA

# Ex.
print("------- 17)")
listA = [1, 2]
listB = ["a", 4]
listC = listA + listB
print(listA, listB, listC)  # => ([1, 2], ['a', 4], [1, 2, 'a', 4])

# JS- adding two lists converts them both to strings, then concatenates listB to the end of listA
# Ex.
# let listA = [ 1, 2 ];
# let listB = [ "a", 4 ];
# console.log(listA + listB); //=> "1,2a,4"

# JS- use array1.concat(iterable) //=> new array
#   - use above for similar behavior to python +


# ________________________________________________________________________________
# 18) LIST MANIPULATION- SLICING
# - use colon :
# - start (inclusive) : end idx (exclusive) : step (int, optional defaults to 1)
# - returns new list of sliced items
print("------- 18)")
# Ex 1.
list1 = ["a", "b", "c", "d"]
print(list1[0:3])  # => ["a", "b", "c"]

# Ex 2.
list1 = ["a", "b", "c", "d"]
print(list1[1:-1])  # => ["b", "c"]

# Ex 3.
print(list1[1:])  # => ["b", "c", "d"]

# Ex 4.
print(list1[:-1])  # => ["a", "b", "c"]

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# JS- will get ERROR if you try to use colon to slice an array index
#   - use array.slice(startIncl, endExcl)
