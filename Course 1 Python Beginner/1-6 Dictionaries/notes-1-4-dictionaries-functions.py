# ________________________________________________________________________________
# 1) dictionaries
print("1) ----------------------------")
# - 1.1) keys must be hashable- strings, numbers, boolean, none, tuples (if values are only immutables)

# - 1.2) if you try creating a key using an undefined variable, that variable is NOT coerced into a string! (ERROR)
#   dic = { a: 1 } # ERROR- NameError: name 'a' is not defined

# - 1.3) can NOT use dot . notation to create, update, or get key/value pairs
#   dic = { "b": 2}
#   dic.a = 1  # ERROR- AttributeError: 'dict' object has no attribute 'a'
#   dic.b      # ERROR- AttributeError: 'dict' object has no attribute 'b'

prices = {}
prices['btc'] = 3000
prices['btc']           #=> 3000

# - 1.4) can NOT refer to an undefined key in a dictionary. will get ERROR
try:
  prices = {}
  prices['btc'] #=> ERROR
except Exception as err:
  print(type(err).__name__  , err) #=> KeyError 'btc'

# - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# - like JS duplicate keys will overwrite each other


# JS
# - 1.1) keys can ONLY be strings. primitive keys are implicitly coerced to strings.
#   obj = { null: 1 }  //=> { "null": 1 }

# - 1.2) if you try creating a key using an undefined variable, that variable IS implicitly coerced into a string!
#   obj = { a: 1 } //=> { "a": 1 }

# - 1.3) CAN use dot . notation to create, update, or get key/value pairs
#   obj = { "b": 2}
#   obj.a = 1   //=> { "a": 1, "b": 2 }   same as obj['a'] = 1
#   obj.b       //=> 2                    same as obj['b']

# - 1.4) CAN refer to an undefined key in a dictionary. will get undefined
#   prices = {}
#   prices['btc']   //=> undefined

# ________________________________________________________________________________
# 2) FUNCTIONS
print("")
print("2) ----------------------------")
# - 2.1) functions are NOT hoisted
# - 2.2) indentation inside function can be 2+ spaces, but must be consistent for each code block
# - 2.3) if no return value, default return is None
# - 2.4) variables defined in function are function scoped (ie not accessible outside function)
print("")
print("Ex1.")
try:
  def test():
      x = 10

  test()
  print(x) # ERROR
except Exception as err:
  print(type(err).__name__, err) # NameError name 'x' is not defined

# - 2.5) function POSITIONAL arguments must be called in order

# - 2.6) function KEYWORD arguments (aka NAME arguments) can be called out of order
print("")
print("Ex2.")
def print_name_age(name, age):
  print("hello " + name + "! you are " + str(age) + " years old")

print_name_age(age=12, name="harry") #=> 'hello harry! you are 12 years old'

# - 2.7) calling a function with more parameters than defined, results in ERROR!
print("")
print("Ex3.")
try:
  def test(x):
    print(x)

  test(1, 2)
except Exception as err:
  print(type(err).__name__, err) #=> TypeError test() takes 1 positional argument but 2 were given

# - 2.8) calling a function with less parameters than defined, results in ERROR!
print("")
print("Ex3.")
try:
  def test(x):
    print('hi')

  test()
except Exception as err:
  print(type(err).__name__, err) #=> TypeError test() missing 1 required positional argument: 'x'



# JS
# - function declarations ARE HOISTED (but not function expressions)
# - if no return value, default return is undefined
# - functions do NOT have Keyword/Named arguments!, but we can mimic this by using object destructuring
# - calling a function with more parameters than defined, does NOT result in error
# - calling a function with less parameters than defined, does NOT result in error

