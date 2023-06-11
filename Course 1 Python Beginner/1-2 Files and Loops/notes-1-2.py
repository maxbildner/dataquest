# ________________________________________________________________________________
# - there is no C++ style loops- Ex. for (int i = 0; i < n; i++){ }

# 1) LOOPS- for ___ in ...
# __ = iterator variable only accessible within this for loop
#      - you can call this anything you want
#      - if looping over sequence (list, string), iterator refers to ELEMENT in current iteration
#      - if looping over dictionary, iterator refers to KEY (PROPERTY) in current iteration
# ... = sequence variable you want to loop over

# ex1. list
# - CAN guarantee loop order
print("------- 1)")
print("ex1.")
fruits = ["apple", "mango", "pear"]
for item in fruits:
    print(item)  # => "apple", "mango", "pear"


# ex2. dictionary
# - can NOT guarantee loop order (like in looping an object in JS)
print("")
print("ex2.")
pantry = {"apple": 2, "mango": 4, "pear": 1}
for item in pantry:
    print(item)  # => "mango", "pear", "apple"


# ex3. string
# - CAN guarantee loop order
print("")
print("ex3.")
name = "abcd"
for char in name:
    print(char)  # => "a", "b", "c", "d"


# JS
# - the __ is refers to the stringified KEY (PROPERTY) in the sequence NOT the element
# - can loop over object, array, string
# - CAN guarantee loop order
# Ex1.
# let fruits = ["apple", "mango", "pear"]
# for (const key in fruits) {
#   console.log(key); //=> "0", "1", "2"
# }

# Ex2.
# let pantry = {"apple": 2, "mango": 4, "pear": 1};
# for (let key in pantry){
#   console.log(key) //=> "apple", "mango", "pear"
# }

# ________________________________________________________________________________
# 2) LOOPS- for ___ in range(start, end)
# https://stackoverflow.com/questions/9450446/how-do-i-use-a-c-style-for-loop-in-python

# ________________________________________________________________________________
# 3) LOOPS- while
