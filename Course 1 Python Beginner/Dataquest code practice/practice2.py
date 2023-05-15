
# Practice #1- modify a list of a lists to make one columns strings become integers
# Practice #1, Method #1 using csv reader
'''
import csv
f = open('crypto_prices.csv','r')   # takes in file string name, returns file pointer
reader_object = csv.reader(f)       # takes in file pointer, returns list reader object
lol = list(reader_object)           # takes in reader object, returns list of lists
lol = lol[1:]                       # removes header, updates lol
for each in lol:                    # loops through each row in lol
    each[1] = int(each[1])
print(lol)
'''
# Practice #1, Method 2: not using csv reader
'''
f = open('crypto_prices.csv')       # open file, default is 'r' read
raw_data = f.read()                 # read in file contents, store in variable
list_data = raw_data.split('\n')    # create list separated by \n
lol = []                            # creates empty list of lists (lol)
for each in list_data:              # loops over each item in list_data
    lol.append(each.split(','))     # splits each item by ',' and appends to lol
header = lol[0]                     # creates header list
lol = lol[1:]                       # removes header from lol
for each in lol:                    # loops through each item in lol
    each[1] = int(each[1])          # changes price str item to int
print(lol)
'''
# Practice #2- add a column to a list of lists (lol)
# Method 1:
'''
import csv
f = open('crypto_prices.csv')
list_object = csv.reader(f)
lol = list(list_object)
lol = lol[1:]                       # [ ['bitcoin', 3000], ['ETH', 130], ['BTH', 100] ]
rating = ['buy', 'sell', 'sell']
i = 0
for row in lol:
    row.append(rating[i])
    i += 1
print(lol)
'''
# Practice #2, Method 2
'''
lol = [ ['bitcoin', 3000], ['ETH', 130], ['BTH', 100] ]
rating = ['buy', 'sell', 'sell']
i = 0                               # counter variable i created
for each in lol:                    # loops over each item in lol
    each.append(rating[i])          # append rating at index i to each list
    i += 1                          # increase counter i by 1
print(lol)
'''
# Practice #3.1- refer to last row within a list of lists of unknown length
# Practice #3.2- refer to last row, last item within a list of lists of unknown length
# Method 1:
'''
lol = [ ['bitcoin', 3000], ['ETH', 130], ['BTH', 100] ]
idx_last_row = len(lol)-1           # index value of last row
last_row = lol[idx_last_row]        # len(lol) = 3, so to get last index value, - 1
last_row_last_item = lol[idx_last_row][len(last_row)-1] 
'''
# Practice #4.1- create dictionary with one column of a list of lists as the key, and another column
# of that same list of lists, as the dictionary value/element
'''
lol = [ ['bitcoin', 3000, 'buy'], ['ETH', 130, 'sell'], ['BTH', 100, 'sell'] ]
ratings = {}                        # create empty dictionary
for each in lol:
    ratings[each[0]] = each[2]      # sets crypto name as key and crypto rating as value
'''
# Practice #5.1- write function that can calculate the min and max values for any list thats passed in
# must be able to take in a list of any type of number
# Method 1:
'''
prices = [.10, .2, .300, .4]
def min_max(list_name):                 # takes in list, returns min and max values
    max_value = list_name[0]               # sets max value = first item in list
    min_value = list_name[0]               # sets min value = first item in list
    for each in list_name:              # loops through each item in the list
        if each > max_value:            # 1st pass, -300 > -300 FALSE, so max_value remains -300
            max_value = each
        if each < min_value:            # 1st pass, -300 < -300 FALSE, so min_value remains -300
            min_value = each
    return min_value, max_value         # returns tuple, note variables in function don't exist outside
(min_value, max_value) = min_max(prices)    # calls function, stores tuple in min and max variables
print(min_value,max_value)
'''
# Practice #5.2- write function that can calculate the min and max values for any list of lists
# that's passed in. Funciton takes in list of list, and index that refers to column
# returns min and max values for that column
'''
lol = [ ['AAPL', 142, 1.3 ], ['TSLA', 300, .9], ['MSFT', 100, .5] ]  # Name, Price, Beta
def min_max(lol, i):                    # takes in list of list, and index that refers to column
    min_value = lol[0][i]               # sets min = first item, value at ith position
    max_value = lol[0][i]               # sets max = first item, value at ith position
    for each in lol:                    # loops through each row in lol
        if each[i] < min_value:
            min_value = each[i]
        if each[i] > max_value:
            max_value = each[i]
    return min_value, max_value         
min_price, max_price = min_max(lol,1)
print(min_price,max_price)
'''
# Practice #5.3- write function that can calculate the min and max values for any dictionary 
# that's passed in. Funciton takes in a dictionary, and returns min and max values
'''
prices = {
    'AAPL':0,
    'BTC':.2,
    'XRP':.3,
    'TSLA':.400
}
def min_max(dictionary):
    min_value = 0
    max_value = 0
    i = 0
    for each in dictionary:
        if dictionary[each] < min_value or i == 0 :
            min_value = dictionary[each]
        if dictionary[each] > max_value or i == 0:
            max_value = dictionary[each]
        i += 1
    return min_value, max_value
print(min_max(prices))
'''
# Practice #6.1- write function that takes in a dictionary, and returns a list of lists
# where each row refers to the key and value from that dictionary (CODE NOT FINISHED)
'''
prices = {
    'AAPL':-400,
    'BTC':-300,
    'XRP':-200,
    'TSLA':.1
}
def dict_to_list(dictionary):
    lol = []
    key = []
    value = []
    for each in dictionary:             # each refers to key in dictionary
        key.append(each)                # key = ['AAPL', 'BTC', 'XRP', 'TSLA']
        value.append(dictionary[each])  # value = [-400, -300, -200, .1]
    lol.append()
'''
# Practice #7.1- count the # of times each element occurs in a list, then add it to a dictionary
# output should be {lab: 1, corgi: 2, pitbull: 1}
'''
pets = ['lab', 'corgi', 'corgi', 'pitbull']
breed_counts = {}
for pet in pets:                    # loops through pets, 1st pass pet = 'lab'
    if pet in breed_counts:
        breed_counts[pet] += 1
    else:
        breed_counts[pet] = 1
print(breed_counts)
'''
# Practice #7.2- count the # of times each element occurs in a list of lists, then add it to a dictionary
'''
stocks = [ ['AAPL', 140, 1.13, 'hold'], ['TSLA', 333, .55, 'sell'], ['NVDA', 135, 2.65, 'sell'] ]
ratings = {}                        # dictionary, key = rating (ex. sell), value = count
for stock in stocks:                # loops through stocks, stock = 1 row
    if stock[3] in ratings:         # 1st pass- if 'hold' in ratings
        ratings[stock[3]] += 1
    else:
        ratings[stock[3]] = 1
print(ratings)
'''
# Practice #7.3- write function, takes in list, and what you want to count, returns num items of that input
'''
breeds = ['corgi', 'corgi', 'lab', 'pitbull']
def counts (lst,input):
    num = 0
    for each in lst:
        if each == input:
            num += 1
    return(num)
print(counts(input='corgi',lst = breeds))
'''




