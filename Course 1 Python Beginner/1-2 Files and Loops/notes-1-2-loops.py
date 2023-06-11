# ________________________________________________________________________________
# - there is no C++ style loops- Ex. for (int i = 0; i < n; i++){ }

# 1) LOOPS- for ___ in SEQUENCE:
#   __ = iterator variable can be named anything (only accessible within this for loop)
#   - if looping over sequence (list, string), iterator refers to ELEMENT in current iteration
#   - CAN guarantee loop order

# Ex1. list
print("1) ----------------------------")
print("Ex1.")
fruits = ["apple", "mango", "pear"]
for item in fruits:
    print(item)  # => "apple", "mango", "pear"

# Ex2. string
# - CAN guarantee loop order
print("")
print("Ex2.")
name = "abcd"
for char in name:
    print(char)  # => "a", "b", "c", "d"

# JS
# - __ iterator variable refers to the stringified KEY (PROPERTY) in the iterable NOT the element
# - CAN guarantee loop order for iterable (array, string)
# Ex1.
# let fruits = ["apple", "mango", "pear"]
# for (const key in fruits) {
#   console.log(key); //=> "0", "1", "2"
# }

# ________________________________________________________________________________
# 2) LOOPS- for ___ in DICTIONARY:
#   - if looping over dictionary, iterator refers to KEY (PROPERTY) in current iteration
#   - can NOT guarantee loop order (like in looping an object in JS)

# Ex1. dictionary
print("")
print("2) ----------------------------")
print("Ex.")
pantry = {"apple": 2, "mango": 4, "pear": 1}
for item in pantry:
    print(item)  # => "mango", "pear", "apple"


# JS
# Ex.
# let pantry = {"apple": 2, "mango": 4, "pear": 1};
# for (let key in pantry){
#   console.log(key) //=> "apple", "mango", "pear"
# }

# ________________________________________________________________________________
# 3) range(start, end, step) => sequence
# params:
#   start (int) = optional, number referring where to start, default 0
#   end (int) = number referring where to end (exclusive)
#   step (int) = optional, number referring to the incrementation of the sequence, default 1
# returns (sequence) = list of numbers
print("")
print("3) ----------------------------")
print("Ex1. default step 1")
x = range(3, 6)
print(x)  # [ 3, 4, 5 ]

print("")
print("Ex2. custom step 2")
x = range(3, 6, 2)
print(x)  # [ 3, 5 ]

print("")
print("Ex3. only 1 param- end")
x = range(4)
print(x)  # [ 0, 1, 2, 3 ]

print("")
print("Ex4. negative param- end")
x = range(-3)
print(x)  # []

print("")
print("Ex5. 0 param- end")
x = range(0)
print(x)  # []

print("")
print("Ex6. negative param- end")
x = range(-2, 4)
print(x)  # [ -2, -1, 0, 1, 2, 3 ]

print("")
print("Ex7. descending numbers")
x = range(4, 1, -1)
print(x)  # [ 4, 3, 2 ]


# ________________________________________________________________________________
# 4) LOOPS- for ___ in range(start, end):
# - can use this to create C++ style for loops
# - https://stackoverflow.com/questions/9450446/how-do-i-use-a-c-style-for-loop-in-python
print("")
print("4) ----------------------------")
print("Ex1. loop 4 times from 0 to 3 (inclusive), in steps of 1")
for i in range(0, 4):
    print(i)  # 0, 1, 2, 3


# ________________________________________________________________________________
# 5) LOOPS- WHILE
print("")
print("5) ----------------------------")
print("Ex1. loop 4 times from 0 to 3 (inclusive) in steps of 1")
i = 0
while i < 4:
    print(i)
    i += 1
