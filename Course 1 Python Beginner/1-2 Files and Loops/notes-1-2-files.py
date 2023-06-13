# ________________________________________________________________________________
# 1) open(file, mode)
#    - file (string) = relative or absolute path to file
#    - mode (string) = optional mode of working with the file, default "r" for read
#      "r" read,   "w" write,  "a" append,   "x" create
#    - returns (file object)
#      - file object doesn't have actual file contents, but acts like a placeholder to file contents
print("1) ----------------------------")
print("Ex1.")
f = open("../../datasets/BalanceSheetSummaries.csv", "r")
print(type(f))  # <type 'file'>
print(
    f
)  # <open file '../../datasets/BalanceSheetSummaries.csv', mode 'r' at 0x7fed38026ed0>


# ________________________________________________________________________________
# 2) file.read(n)
#    - file = file object
#    - n (int) = optional number of bytes or characters? to read from file. default is entire file
#    - returns (string) representation of opened file
#    - if csv file, returned string will most likely contain '\n' new line characters
print("")
print("2) ----------------------------")
print("Ex1.")
f = open("../../datasets/BalanceSheetSummaries.csv", "r")
data = f.read(5)
print(len(data))  # 5
print(data)  # 'Fund '


# ________________________________________________________________________________
# 3) string.split(delimeter)
#    - delimeter (string) = what to split/separate string by (ex. ",", "\n")
#    - returns (list) of items split by the delimeter
#    - will get error if you pass in empty string '' delimeter
print("")
print("3) ----------------------------")
print("Ex1.")
fruits = "apple,pear,mango"
print(fruits.split(","))  # [ 'apple', 'pear', 'mango' ]

# JS- SAME!
# - except you CAN pass in empty string delimeter

print("")
print("Ex2.")
f = open("../../datasets/BalanceSheetSummaries.csv", "r")
data = f.read(1000)
banks = data.split("\n")
print(banks)
