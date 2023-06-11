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
