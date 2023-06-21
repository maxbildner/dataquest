# ________________________________________________________________________________
# 1) if condition:
print("1) ----------------------------")
if 10 > 2:
    print("yee")  # => "yee"

# ________________________________________________________________________________
# 2) shorthand if
print("")
print("2) ----------------------------")
# if 2 < 10: print("yee")

# ________________________________________________________________________________
# 3) if else
print("")
print("3) ----------------------------")
if 2 > 10:
    print("yee")
else:
    print("else")  # => "else"

# ________________________________________________________________________________
# 4) shorthand if else- python 2.5+ only
# value_when_true if condition else value_when_false
print("")
print("4) ----------------------------")
print("true") if 2 < 10 else print("false")  # => true

# ________________________________________________________________________________
# 5) if elif
print("")
print("5) ----------------------------")
if 2 > 10:
    print("yee")
elif 2 < 10:
    print("elif")  # => "elif"

# ________________________________________________________________________________
# 6) if elif else
print("")
print("6) ----------------------------")
if 2 > 10:
    print("yee")
elif 2 < 10:
    print("elif")  # => "elif"
else:
    print("else")


# ________________________________________________________________________________
# 7) falsey/truthy values
# - objects by default are truthy unless they are empty or the object's bool method returns False

# TRUTHY        FALSEY
# "0"           0
# "-1"          0.0
# 1
# -1
# "a"
# [ 1 ]         [ ]
# { "a": 1 }    { }

print("")
print("7) ----------------------------")
if []:  # falsey
    print("[]")

if {}:  # falsey
    print("{}")

if [1]:  # truthy
    print("[1]")  # => "[1]"

if {1}:  # truthy
    print("{1}")  # => "{1}"

if 1:  # truthy
    print("1")  # => "1"

if 0:  # falsey
    print("0")

# JS
# - all objects are truthy even if they are empty

# ________________________________________________________________________________
# 8) in
# - used to iterate in for loop
# - used to check if a value (or key if dictionary) is present in a sequence (list, string, ...), Set, Dictionary
# __ in sequence/set/dictionary    #=> boolean

print("")
print("8) ----------------------------")
print("Ex1.")
list = ["a", [1], 2]
print("b" in list)  # False
print("a" in list)  # True
print([1] in list)  # True

print("")
print("Ex2.")
str = "abcd"
print("ab" in str)  # True
print("abz" in str)  # False

print("")
print("Ex3.")
set = {"a", "b"}
print("a" in set)  # True
print("z" in set)  # False

print("")
print("Ex4.")
dic = {"a": 2, "b": 3}
print("a" in dic)  # True
print("z" in dic)  # False

# JS
# - for objects, the "in" keyword does NOT check for values, where python DOES
# - Ex JS:
# [3] in [ "a", 2, [3] ]    // false

# ________________________________________________________________________________
# 9) EXPRESSIONS vs STATEMENTS
# EXPRESSIONS
# - expressions evaluate to at least one value
# - expressions are also statements, but not all statements are expressions
print("")
print("9) ----------------------------")
# Ex.
1 + 2
print("ye")
"hi"

# STATEMENTS
# - made up of expressions
x = 10
print("ye")
if 1 < 2: x = "yep"
