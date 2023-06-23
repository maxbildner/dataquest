# ________________________________________________________________________________
# 1) dictionaries
print("1) ----------------------------")
# - 1.1) keys must be hashable- strings, integers, floats, boolean, tuple (if values are only immutables), none

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
prices = {}
prices['btc'] #=> ERROR- KeyError: 'btc'

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
# 2) 
print("")
print("2) ----------------------------")


