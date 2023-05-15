'''prices = [1, 2, 3, 4, 5, 6]
slices = prices[len(prices)-2:len(prices)]
print(slices)
'''
'''
data = (open("crypto_prices.csv","r")).read()
split_data = data.split("\n")
print(split_data)
'''
'''
fruit = ["kiwi", 'lichi', 'pear']
for scoobydoobabadooThisIsATempVariable in fruit:
    print(scoobydoobabadooThisIsATempVariable)
'''
'''
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])
'''
'''
crypto_prices = ["bitcoin,3000", "ETH,120", "XRP,.44"]
final_list = []
for tempVariable in crypto_prices:
    split_list = tempVariable.split(",")
    final_list.append(split_list)
print(final_list)
'''
'''
f = open("crypto_prices.csv","r")
data = f.read()
split_data = data.split("\n")
final_list = []
for tempVariable in split_data:
    split_list = tempVariable.split(",")
    final_list.append(split_list)
print(final_list[0][0])
'''
# cities_list = [five_elements[0][0], five_elements[1][0], five_elements[2][0], five_elements[3][0], five_elements[4][0]]

'''
f = open("crypto_prices.csv","r")
data = f.read()
split_data = data.split("\n")
final_list = []
for tempVariable in split_data:
    split_list = tempVariable.split(",")
    final_list.append(split_list)
crypto_names = []
for row in final_list:
    crypto_name = row[0]
    crypto_names.append(crypto_name)
print(crypto_names)
'''
'''
f = open("crime_rates.csv")
data = f.read()
split_data = data.split("\n")
final_list = []
for tempVariable in split_data:
    split_list = tempVariable.split(",")
    final_list.append(split_list)
#print(final_list)

int_crime_rates = []
for rows in final_list:
    crime_rate = int(rows[1])
    int_crime_rates.append(crime_rate)
'''
''' 
crime_rates = [1, 2, 3]
first_500 = (crime_rates[0] > 500)
first_749 = (crime_rates[0] >= 749)
first_last = (crime_rates[0] >= crime_rates[len(crime_rates)-1])
'''
# create a new list that contains all prices above 400 using a for loop and if statement
'''
prices = [1, 300, 500, 800, 1000]
new_prices = []
for np in prices:
    if np > 400:
        new_prices.append(np)
print(new_prices)
'''
# find the largest integer in a data set
'''
price = [1, 3, 2, 13, 5]
highest_price = 0
for temp in price:
    if temp > highest_price:
        highest_price = temp
print(highest_price)
'''
# challenge for course 1.4
# 1 Open a file and read in the data, and split the data so u can manipulate it
# 2 create a new list that contains only the first five elements of the data set
'''
f = open('unisex_names_table.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = []
counter = 0
for temp in names_list:
    if counter < 5:
        first_five.append(temp)
    counter += 1
print(first_five)
'''
# creates new list of split split items
'''
f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for temp in names_list:
    comma_list = temp.split(',')
    nested_list.append(comma_list)
print(nested_list[0:4])
'''
'''
numerical_list = []
names = []
quantity = []
i = 0 # counter
for temp in nested_list:
    names.append(temp[0])
    quantity.append(float(temp[1]))
    new_list = [names[i], quantity[i]]
    numerical_list.append(new_list) 
    i += 1
print(numerical_list[0:5])
'''
# new list that contains only names of those with 1000 or greater shared names
'''
# The last value is ~100 people
# numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for temp in numerical_list:
    if (temp[1] >= 1000):
        thousand_or_greater.append(temp[0])
print(thousand_or_greater[0:10])
'''
'''
prices = [1, 2, 3, 4, 5]
last_price = prices[1:(len(prices)-1)]
print(last_price)
weather[len(weather)-1] gives you the last item in a list called weather. 
[1:len(weather)-1] gives you all the items in weather from the second item to the last item
'''
#combining lists
'''
btc_jan = [20000, 15000, 12000, 8000]
btc_nov = [6000, 5000, '$3000']
btc_combined = btc_jan + btc_nov
print(btc_combined)
'''
# Referring to the last three, two, and one items in a list
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_three = list1[len(list1)-3:len(list1)]
last_two = list1[len(list1)-2:len(list1)]
last_one = list1[len(list1)-1]
print(last_three, last_two, last_one)
'''
# open a file, read in the data, split it, split it again and store the split split list
'''f = open('crypto_prices.csv','r')
str_data = f.read()
split_data = str_data.split('\n')   # output: ['bitcoin,3000', 'ETH,130', 'BTH, 100']
split_split_data = []
for temp in split_data:
    split_split_data.append(temp.split(','))
print(split_split_data)             # output: [ ['bitcoin', '3000'], ['ETH', '130'], ['BTH', '100'] ]
'''
# access elements in a list of lists using double bracket notation [][]
'''
f = open('crypto_prices.csv', 'r')
str_data = f.read()
split_data = str_data.split('\n')
split_split_data = []
for temp in split_data:
    split_split_data.append(temp.split(','))
# first_item = split_split_data[0] 
# first_item_first_value = first_item[0]
# print(first_item)                   # output: 'bitcoin,3000'
# print(first_item_first_value)       # output: 'bitcoin'
# first_item_first_value = split_split_data[len(split_split_data)-1][len(split_split_data)-1]
# print(first_item_first_value)
list = [['1', '2'], ['3', '4'], ['5', '6']]
last_item = list[len(list)-1]
# print(last_item) # ['5', '6']
last_last = last_item[len(last_item)-1]
# print(last_last) # ['6']
print(list[len(list)-1][len(list[len(list)-1])-1]) ###############!!!!!!!! last item last item generic formula
'''
# modifies list_list to make value at 1 index str to int ####### Good Practice!!!
'''
f = open('crypto_prices.csv','r')
str_list = f.read()                         # output: ['bitcoin,3000\nETH,130\nBTH,100']
split_list = str_list.split('\n')           # output: ['bitcoin,3000', 'ETH,130', 'BTH,100']
list_list = []
for temp in split_list:
    list_list.append(temp.split(','))       # output: [ ['bitcoin','3000'], ['ETH','130'], ['BTH','100'] ]
    for temp in list_list:
        temp[1] = int(temp[1])
print(list_list) 
# instead of nested for loop, can do two individual for loops to get same result
for temp in list_list:
    temp[1] = int(temp[1])                  # output: [ ['bitcoin', 3000], ['ETH', 130], ['BTH', 100] ]
print(list_list)
# create new list to make value 1 index str to int
'''
# dictionaries
'''
students = {
    "Tom": 60,
    "Jim": 70,
}
students["Ann"] = 85
students['Tom'] = 80
students['Jim'] += 5
print(students)
'''
# GOOD PRACTICE- count the # of times each element occurs in this list and add it to a dictionary
'''
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] += 1
    else:
        pantry_counts[item] = 1
'''
# Good Practice!!!! With Making/Calling Functions
'''
crypto = [ ['bitcoin',3000], ['ETH',130], ['BTH',100] ]
def check_price(crypto_name):      # returns price of crypto, takes in name
        for temp in crypto:
                if temp[0] == crypto_name:
                        return temp[1]
print(check_price('scooby'))
'''
# Good Practice!!!! With Functions
# Example of functions with multiple arguments and calling them with inputs 
# non-sequential using named arguments
'''
stocks = [ ['AAPL', 150, 'hold'], ['MSFT', 100, 'buy'], ['TSLA', 333, 'sell'] ]
crypto = [ ['BTC',3000,'buy'], ['ETH',130,'sell'], ['BTH',100,'sell'] ]
# returns rating of asset, takes in asset class, asset name 
def check_rating(asset_class, asset_name):      
        for temp in asset_class:
                if temp[0] == asset_name:
                        return temp[2]
print(check_rating(asset_name='ETH', asset_class=crypto)) 
'''
'''
AAPL = [150, 'hold', .14]   		# price, rating, short-interest (i.e. %float short)
TSLA = [333, 'sell', .12]
def check_detail(ticker, index):        # takes in ticker, position of detail i want to lookup, returns detail
        return ticker[index]
print(check_detail(index = 1, ticker = TSLA))
print(TSLA[1]) # same result
'''
# from mission 6 optional arguments
# this exercise was hard, easier way?
# movie_data is a list of lists containing all movie_metadata
'''
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False): # default is False header row
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)] #slices input list to remove header
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt
def feature_counter(input_lst,input_str,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)] #slices input list to remove header
    for each in input_lst:
        if each[6] == input_str: #6 corresponds to location
            num_elt = num_elt + 1
    return num_elt
num_of_us_movies = feature_counter(movie_data,'USA', True)
'''
#  Mission #7 for Functions
'''
def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
def summary_statistics(input_lst):   #input_lst is a list of lists
    num_japan_films = feature_counter(input_lst,6,'Japan')
    num_color_films = feature_counter(input_lst,2,'Color')
    num_films_in_english = feature_counter(input_lst,5,'English')
    dictionary = {
        'japan_films':num_japan_films,
        'color_films':num_color_films,
        'films_in_english':num_films_in_english
    }
    return dictionary
summary = summary_statistics(movie_data)
'''
# Practice opening, reading, parsing, converting str to int
'''
1) open file, read in data and store
2) parse data/split data by \n and store in list
3) make list of list (separate by ",") and store 
4) remove header row and store in new list
5) convert the last item of each item in the list from a str to int (store in another list)
6) write function that takes in name of crypto you want to find price for, returns price
7) create separate dictionary for crypto with names as keys, prices as values
'''
'''
f = open('crypto_prices.csv','r')               #step 1
data = f.read()                         
str_data = data.split('\n')                     #step 2
lol_wHeader = []                                        # lol = list of list with header
for each in str_data:                           #step 3
       lol_wHeader.append(each.split(','))
lol_woutHeader= lol_wHeader[1:len(lol_wHeader)] #step 4 lol without header
for each in lol_woutHeader:                     #step 5 modify lolwoutheader to int
        each[1] = int(each[1])
def price_lookup1(name):                        #step 6 function to lookup price
        for each in lol_woutHeader:
                if each[0] == name:
                        return each[1]

crypto_dict = {}                                #step 7 create dictionary
for each in lol_woutHeader:
        crypto_dict[] = lol_woutHeader[]
'''
# can functions return 2 values? Yes
'''
portfolio = [ ['AAPL', 150, 1.13], ['TSLA', 333, .55], ['NVDA', 135, 2.65] ]
def lookup(lst, ticker):   # takes in portfolio list of list, and ticker. returns price and beta
        for each in lst:
                if ticker in each:
                        return each[1], each[2]         # you can return multiple values separated by ,
print(lookup(portfolio, 'TSLA'))
'''    
# Course 1_1_10 Guided Project Explore US Births
'''
# takes in a string representing the csv file name
def read_csv(file_name):
    f = open(file_name)
    raw_data = f.read()
    
    # dataH = data as a string that is split by '\n' includes Header
    dataH = raw_data.split('\n')
    # string_list is list without Header
    string_list = dataH[1:len(dataH)]
    final_list = []
    
    # iterates through string list without header
    for each in string_list: 
        int_fields = []
        # splits each element in string list by , to make list of list
        string_fields = each.split(',')
        
        # creates new list of lists that are int's not str's
        for each in string_fields:
            int_fields.append(int(each))
        
        final_list.append(int_fields)
        
    return final_list
cdc_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')
print(cdc_list[0:10])
'''
# Sample code for objective 3 in mission 10 of first course
'''
# takes in list of list that is the final_list we created above^
def month_births(lol):
    # dictionary where key = month and value/element = total births in that month
    births_per_month = {}
    
    for each in lol:
        # each[1] corresponds to month in each
        # each[4] corresponds to births in each
        
        # extracts month and births
        month = each[1]
        num_births = each[4]
        
        # if month value is already a key in dictionary, then add its associated births
        if month in births_per_month:
            births_per_month[month] += num_births
        else:
            births_per_month[month] = num_births
    
    return births_per_month
cdc_month_births = month_births(cdc_list)
cdc_month_births
'''
# Note how functions dow_births() and month_births() share alot of similarities
# we can combine them to create one generic function
# takes in data = list of lists, and column =  column # that we want to calculate totals
'''
def calc_counts(data, column):
    # generic dictionary to contain columns for year, month, dom, or dow
    dictionary = {}
    
    for each in data:
        # each[0] corresponds to year
        # each[1] corresponds to month
        # each[2] corresponds to date of month
        # each[3] corresponds to date of week
        # each[4] corresponds to number of births 
    
        if each[column] in dictionary:
            dictionary[each[column]] += each[4]
        else:
            dictionary[each[column]] = each[4]
            
    return dictionary
cdc_year_births = calc_counts(cdc_list,0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)
'''
# using modules
'''
import csv
f = open('crypto_prices.csv')
csvreader = csv.reader(f)
my_data = list(csvreader)
print(my_data)
'''
# practice with modules (step 1, course 2, mission 1)
# Import a Math module, assign it an alias, use module functions/constants to calculate stuff
'''
import math as m
neg = -1.5
pos = 1.5
sqrt_pi = m.sqrt(pi)
print(sqrt_pi)
floor = m.floor(neg)    # returns largest integer NOT greater than num, num = -1.5, so floor = -2
print(floor)
floor = m.floor(pos)    # returns largest integer NOT greater than num, num = 1.5, so floor = 1   
print(floor)
ceiling = m.ceil(neg)   # returns smallest integer NOT less than num, num = -1.5, so ceiling = -1
print(ceiling)
ceiling = m.ceil(pos)   # returns smallest integer NOT less than num, num = 1.5, so ceiling = 2
print(ceiling)
'''
# practice with list function
# list() takes in 1 argument that is an iterable (string, dictionary/set, or iterator object)
'''
vowels = 'aeiou'
# print(list(vowels))                       # ['a', 'e,', 'i', 'o', 'u']
# print(list(['a', 'e,', 'i', 'o', 'u']))   # ['a', 'e,', 'i', 'o', 'u']
# lol = [ ['AAPL', 142], ['TSLA', 300] ]    # [ ['AAPL', 142], ['TSLA', 300] ]
counts = {
    'corgi':2,
    'lab':1,
    'pitbull':1
}
print(list(counts))                         # converts dictionary keys to list: ['corgi', 'lab', 'pitbull']
'''
# practice with list function
'''
# vowel string
vowels = 'aeiou'
print(list(vowels))
# output: ['a', 'e', 'i', 'o', 'u']
# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(list(vowelList))
# output: ['a', 'e', 'i', 'o', 'u']
'''
# practice with CSV module- create lists of lists using csv reader
# import csv module, open a file, create a variable that contains file object using reader() function, then convert to list
'''import csv
f = open('crypto_prices.csv', 'r')  # takes in csv file as string, and mode, returns file pointer
file_object = csv.reader(f)         # reader() takes in file pointer, returns csv reader object
data = list(file_object)            # list() takes in file object, returns list of lists
'''
# practice with classes
# create class called "Scoobydoo", 
# initialize function of class, takes in self and a list of lists (lol), has attribute called "speak" which = 'scoobydoo'
# initialize a variable with class type Scoobydoo, and run the speak attribute
'''
import csv
class Scoobydoo:
    def __init__(self,lst):
        self.speak = 'scoobydoo'
fpointer = open('crypto_prices.csv')
fobject = csv.reader(fpointer)
lol = list(fobject)
doggo = Scoobydoo(lol)
print(doggo.speak)                  # prints 'scoobydoo'
'''
# more practice with classes
'''
import csv
class Dataset:
    def __init__(self,data):        # special function that only runs ONCE upon initition/creation of an object of this type class
        self.data = 'scoobydoo'     # creates attribute called "data", which can be applied to any object of class Dataset 

f = open('crypto_prices.csv')
csvreader = csv.reader(f)           # accesses csv module, reader method, returns file object
crypto_data = list(csvreader)       # creates variable nfl_data that contains list of lists separated by \n and ,
temp = Dataset(crypto_data)         # creates instance of Dataset class, crypto lol is passed in (and self)
dataset_data = temp.data            # dataset_data = 'scoobydoo'       
'''
# step 1, course 2, mission 2, objective 3
# passing additional arguments to the initializer example
'''
import csv
class Dataset:
    def __init__(self,data):
        self.data = data
f = open('nfl.csv')
csvreader = csv.reader(f)       # accesses csv module, reader method, returns file object
nfl_data = list(csvreader)      # creates variable nfl_data that contains list of lists separated by \n and ,
temp = Dataset(nfl_data)
dataset_data = temp.data
'''
# GOOD PRACTICE!! CONVERTS STRS OF LIST OF LIST TO FLOATS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Method 1: the hard way using 2 counter variables
'''
str_list = ['1', '2', '3']
strlol = [ ['1', '2', '3'], ['4', '5', '6'] ]
i = 0
for each in str_list:
    str_list[i] = float(each)
    i += 1
print(str_list)
i = 0
for row in strlol:
    j = 0
    for each in row:
        strlol[i][j] = float(strlol[i][j])
        j += 1
    i += 1
print(strlol)
'''
# method 2: the slightly easier way only using one counter variable
'''
str_list = ['1', '2', '3']
strlol = [ ['1', '2', '3'], ['4', '5', '6'] ]
for row in strlol:
    i = 0
    for each in row:
        row[i] = float(row[i])
        i += 1
print(strlol)
'''
# Practice adding another column to a list of lists !!! GOOD PRACTICE!!!!!!!!!!!!!!!!!!!!!!!!!
'''
list1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15] ]
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11, 12]
# [13, 14, 15]
column1 = [1, 4, 7, 10, 13]
# want to create another column = [0, 2.5, 5.5, 8.5, 11.5]
avgp = [0]
i = 0
for each in column1[0:4]:   
        avgp.append((column1[i] + column1[i + 1])/2)
        i += 1
i = 0
for each in list1:
        each.append(avgp[i])
        i += 1
'''
# Step 1, Course 2, Mission 2 Classes, Objective 4 Adding addition behavior
# Note nfl_data is already loaded
'''
class Dataset:                          # creates class called Dataset 
    def __init__(self, data):           # creates method within that class 
        self.data = data                # self refers to the object being acted upon (ex. nfl_dataset)

    # Your method goes here
    def print_data(self, num_rows):     # creates another method callsed print_data
        print(self.data[:num_rows])     # takes in data and the num of rows you want to print out

nfl_dataset = Dataset(nfl_data)         # creates an instance of the Dataset class and initializes it with nf_data. 

nfl_dataset.print_data(5)               # apply that method (print method) to the nfl_dataset object
                                        # no need to pass in self, it is automatically passed in
'''
# Step 1, Course 2, Mission 2 Classes, Objective 5 Enhancing the Initializer
# Practice
# create class called Dataset, that upon initialization has a header and nonheader/data attribute
'''
import csv
f = open('crypto_prices.csv')
fobject = csv.reader(f)
raw_data = list(fobject)
class Dataset:
    def __init__(self,data):
        self.header = data[0]
        self.data = data[1:]
crypto_data = Dataset(raw_data)
print(crypto_data.header)
print(crypto_data.data)
'''
# Step 1, Course 2, Mission 2 Classes, Objective 5 Enhancing the Initializer
# Note nfl_data is already loaded
'''
class Dataset:
    def __init__(self, data):           #__init__ method is automatically called once whenever an object is created of this Dataset class
        self.data = data                # self refers to the object we are acting upon (ie nfl_header below), data is our list of lists
        self.header = self.data[0]      # data[0] refers to the header row of the data 
        self.data = data[1:]            # data[1:] refers to all the rows except the header
nfl_dataset = Dataset(nfl_data)         # create object called nfl_dataset that is of the Dataset class

nfl_header = nfl_dataset.header         # stores header in nfl_header
'''
# enumerate function practice- loop through a list using enumerate() and create two new lists that contain indexes and values
'''
prices = [3800, 150]
idx = []
p = []
for index, price in enumerate(prices):
    idx.append(index)
    p.append(price)
print(idx, p)
'''
# enumerate function 
'''
pets = ['harry', 'bleu', 'red']
pets_object = enumerate(pets)           # returns enumerate object NOT a list (contains pairs)
print(list(pets_object))                # convert enumerate object into list (contains pairs)
'''
# enumerate function practice 2
'''
for index, value in enumerate(['harry', 'bleu']):
        print(index, value)
# output:
# 0 harry
# 1 bleu
portfolio = [ ['ticker', 'price', 'beta'], ['AAPL', 150, 1.13], ['TSLA', 333, .55], ['NVDA', 135, 2.65] ]
'''
# practice with the "not in" phrase
'''
attendance = ['max', 'harry', 'billy', 'bob']
if 'stewart' not in attendance:
    print('Stewart playing hookie!')
'''
# practice with the "not in" phrase
'''
pets = ['scooby', 'bleu']
if 'harry' not in pets:
        print('not there!')
# list1 = [ ['name', 'price'], ['aapl', 150], ['tsla', 333] ]
'''
# Step 1, Course 2, Mission 2 Classes, Objective 6 Grabbing Column Data
# Note nfl_data is already loaded
'''
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    def column(self, label):        # method named column, takes in self object and str header
        if label not in self.header:
            return None
        
        index = 0
        # loops through header to see find index value of passed in label (of header)
        for idx, element in enumerate(self.header): # header list is passed in enumerate
            if label == element:
                index = idx
        
        column = []
        for each in self.data:
            column.append(each[index])
        return column                  
nfl_dataset = Dataset(nfl_data) # initialize nfl_dataset (creates object class Dataset)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
'''
# 1 Create a class Dataset, that upon initialization has a header and data attrtibute that store a header and rest of data
# 2 Create a method within that Dataset class that returns a column of data given the header label you want
'''
import csv
f = open('crypto_prices.csv')
fobject = csv.reader(f)
raw_data = list(fobject)
class Dataset:
    def __init__(self,lol):
        self.header = lol[0]
        self.data = lol[1:]
    
    def column(self,label):     # label = string that corresponds to the header column you want to extract
        if label not in self.header:
            return None

        # we need to find the index that corresponds to that label
        index = 0
        for idx, value in enumerate(self.header):
            if label == value:
                index = idx
        
        column = []
        for each in self.data:
            column.append(each[index])
        
        return column
crypto = Dataset(raw_data)
name_column = crypto.column('crypto_name')
price_column = crypto.column('price')
print(name_column)
print(price_column)
'''
# practice using the set() function
'''
pantry = ['apple', 'mango', 'mango', 'mango', 'coconut', 'coconut']
unique_fruit = set(pantry)              # takes in list, returns unique items as a set (not indexable)
print(unique_fruit)
'''
# practice using the set() function
'''
pets = ['labrador', 'corgi', 'corgi']
unique_breeds = set(pets)
print(type(unique_breeds))
'''
# Step 1, Course 2, Mission 2 Classes, Objective 7 Count Unique Method
# Note nfl_data is already loaded
'''
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # Add your count unique method here
    def count_unique(self, label):
        column_to_count = self.column(label)        # method within a method
    
        total_unique = len(set(column_to_count))
        
        return total_unique
nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')         # Total years should = # of unique years in dataset
'''
# sets practice
'''
pets = {'harry', 'bleu'}
str1 = 'harry'
print(list(pets))
print(list(str1))
'''
# add() method practice- adds a unique item to a set, if it already exists, then it won't add
'''
pets = {'corgi','corgi','lab','lab'}             # output will be {'corgi', 'lab'}
pets.add('corgi')                                # can only use add() to SETS NOT LISTS/INTS/STRS/FLTS...
print(pets)                                      # output will be {'corgi', 'lab'}
'''
# remove() method practice- removes a unique item from a set, if not in the set, will get error
'''
pets = {'corgi', 'lab', 'corgi'}                # output = {'corgi', 'lab'}
print(pets)
pets.remove('corgi')
print(pets)
'''
# list() practice
# convert the keys of a dictionary to a list
'''
dictionary1 = {
    'btc':3800,
    'eth':150
}
keys = list(dictionary1)
print(keys)
'''
# try except practice- what will the output be of the following?
'''
prices = ['1', '2', '', '4']
for each in prices:
    try:
        print(int(each))
    except Exception as exc:
        print('there was an error')
        print(type(exc))
# print(prices)
# print(type(prices))
'''
# try except practice- analyze this dataset, and convert str prices to floats, convert any missing data to 0's
'''
stocks = [ ['AAPL', 150, 'hold'], ['MSFT', '', 'buy'], ['TSLA', 333, 'sell'] ]
prices = []
for stock in stocks:
    try:
        stock[1] = float(stock[1])
    except Exception as exc:
        stock[1] = 0
    prices.append(stock[1])

print(stocks)
print(prices)
'''
# Step 1, Course 2, Mission 3 Error Handling, Objective 9 Convert Birth Years to Integers
# note legislators list of list has already been loaded
# list1 = [ ['1992-03-01', 'max'], ['1991-05-18', 'seani'] ]
'''
for row in legislators: 
    birthday = row[0]
    bithyear = birthday.split('-')[0]  # splits birthday into list, grabs 0 index (year)
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)
''' 
# modulus practice to find even/odd number
'''
def odd_num(l,u):
    all_num = list(range(l,u+1))
    odds = []
    for each in all_num:
        if each % 2 == 0:
            pass
        else:
            odds.append(each)
    return odds
print(odd_num(1,10))
'''
# Practice with enumerate function and what is or is not an iterable
# animals = ['dog', 'cat', 'dragon']    # list with many items OK
# animals = ['abcd']                    # list with 1 item OK
# animals =  'abcd'                     # string OK
# animals = [1,2,3]                     # list with many int items OK
# animals = [123]                       # list with 1 int item OK
# animals = 123                         # NOT an iterable        
# animals = {1, 2, 3}                   # set with many items OK
# animals = {1}                         # set with 1 item OK
# animals = {'dog':10, 'cat':2}         # dictionary with many items OK
# animals = {'dog':10}                  # dictionary with 1 item OK   
'''
animals = ['dragon', 'puppy', 'dog']
print(enumerate(animals))
print(type(enumerate(animals)))
#output:
#<enumerate object at>
#<class 'enumerate'>
'''
# More Practice with enumerate function
'''
animals = ['dragon', 'puppy', 'dog']
for index, animal in enumerate(animals):
    print("index =", index, " animal =", animal)
'''
# Using enumerate to loop through TWO lists
'''
animals = ['dragon', 'puppy', 'dog']
cuteness = [2, 10, 9]
for index, animal in enumerate(animals):
    print('animal: ', animal)
    print('cuteness: ', cuteness[index])
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 3 Adding Columns Practice
# Objective: using enumerate(), add the ratings list to the stocks list of lists as a column
'''
stocks = [ ['AAPL', 140], ['TSLA', 300] ]   
ratings = ['hold', 'sell']
for index, stock in enumerate(stocks):      # loops through each row in stocks
    stock.append(ratings[index])            # appends the item in ratings that has
                                            # the same index as the current stock to each stocks
print(stocks)
'''
# practice- given two lists, create a new list of lists that contains both lists as individual rows for that lol
# manually
'''
stocks = ['BTC','AAPL', 'TSLA']
prices = [3800, 150, 300]
lol = stocks
lol[0] = [ stocks[0], prices[0] ]
lol[1] = [ stocks[1], prices[1] ]
lol[2] = [ stocks[2], prices[2] ]
print(lol)
'''
# practice- same as above, but with loop !!!!! GOOD PRACTICE !!!!!!!!!!!!!!!!!!!!!!!!!!
'''
stocks = ['BTC','AAPL', 'TSLA']
prices = [3800, 150, 300]
i = 0
for stock in stocks:
    stocks[i] = [ stocks[i], prices[i] ]
    i += 1
print(stocks)
'''
# list comprehension practice- write a condensed for loop that creates a new list of Price to EPS given a list of lists
# note* eps can't be 0
'''
stocks = [ ['AAPL', 140, 2.95], ['TSLA', 300, 1], ['NVDA', 136, 1.65] ] # ticker, price, EPS
pe_ratios = []
# the following list comprehension below is equal to the loop below, but with a try exception incase there
pe_ratios = [ stock[1]/stock[2] for stock in stocks ]
print(pe_ratios)
# for stock in stocks:
#    pe_ratios.append(stock[1]/stock[2])
#print(pe_ratios)

# the following loop below is equal to the loop above, but with a try exception incase an eps is 0
#for stock in stocks:
#    try:
#        pe_ratios.append(stock[1]/stock[2])
#    except Exception:
#        pe_ratios.append(0)
#print(pe_ratios)
'''
# list comprehension practice
'''
prices = [10, 20, 30]
output = [each*2 for each in prices]
print(output)
'''
# practice with None object and is None syntax
# write function that takes in list and finds the min and maximum value in a list
'''
numbers = [0, -20, -30]
def min_max(lst):
    min_value = None
    max_value = None
    for each in lst:
        if min_value is None or each < min_value:       # None comparison must come first!
            min_value = each
        if max_value is None or each > max_value:       # None comparison must come first!
            max_value = each
    return min_value,max_value
print(min_max(numbers))
'''
# None Practice
'''
stews_attendance = None
if stews_attendance is None:
    print('True')
'''
# practice with None object and is None syntax
# find the maximum value in a list of negative numbers
'''
values = [-20, -500, -30]
max_value = None
for i in values:
    if max_value is None or i > max_value:
        max_value = i
print(max_value)
'''
# create a function that takes in a list of lists, returns a new list of their PE ratios
# function should handle cases where inputs are None or 0
'''
stocks = [ ['AAPL', 140, 2.95], ['TSLA', 300, None], ['NVDA', 136, 1.65] ]
def pe_ratios(lol):
    pe_list = []
    for stock in lol:
        try:
            pe_list.append(round(stock[1]/stock[2],2))
        except Exception:
            pe_list.append('None')
    return pe_list
print(pe_ratios(stocks))
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 7 Comparing with None
# practice using is not None syntax to compare a value to None
# create a list that has booleans that correspond to another lists' items
'''
values = [ None, 10, 20 ]
checks = []
for each in values:
	if each is not None and each > 10:
		checks.append(True)
	else:
		checks.append(False)
print(checks)
'''
# items() method practice- loop through a dictionary and create two new lists, one containing the keys, another containing the values
'''
pe_ratios = {
    'NVDA': 19.77,
    'AAPL': 12.49,
    'AMZN': 96.95
}
stocks = []
pes = []
for stock, pe in pe_ratios.items():
    stocks.append(stock)
    pes.append(pe)
print(stocks)
print(pes)
'''
# items() method practice
'''
pe_ratios = {
    'NVDA': 19.77,
    'AAPL': 12.49,
    'AMZN': 96.95
}
print(pe_ratios.items())            # output: dict_items([('NVDA', 19.77), ('AAPL', 12.49), ('AMZN', 96.95)])
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 8 Highest Female Name Count
# dictionary contains keys of females, values # of times the names occured after 1940
# objective: max_value should contain the largest value in name_counts
'''
name_counts = {
    'Kristen':2,
    'Maxine':1,
    'Nancy':3
}
max_value = None
for n in name_counts:           # n refers to the key name, or 'Kristen' on first loop pass
    count = name_counts[n]      # name_counts[n] on first pass = 2
    if max_value is None or count > max_value:
        max_value = count
print(max_value)
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 9 Items Method
# objective: use items() method to iterate through the keys and values in assets
# print each riskiness
'''
assets = {
	'crypto': 10,
	'stocks': 6,
	'bonds': 4
}
for asset, riskiness in assets.items():
	print(riskiness)
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 10 Finding most common female names
# objective: create a list (top_female_names) that is a list of the most common female names in
    # a dictionary (name_counts dictionary)
# name_counts dictionary already laoded in
'''
top_female_names = []
# method 1 below:
for n in name_counts:               # n refers to key name ex. 'Kristen'
    if name_counts[n] == 2:         # name_counts[n] refers to value at key n
        top_female_names.append(n)  # appends key n to top_female_names list
# method 2 below:
for name, counts in name_counts.items():    # name referes to key, counts refers to value
    if counts == 2:
        top_female_names.append(name)
'''
# appending item to dictionary practice
'''
assets = {
	'BTC': 3000,
	'AAPL': 140,
	'TSLA': 300
}
assets['MSFT'] = 100
print(assets)
'''
# Step 1, Course 2, Mission 4 List Comprehensions, Objective 11 Finding most common male names
# objective: create a list (top_male_names) that is a list of the most common male names in
    # a dictionary (male_name_counts dictionary)
# legislators list of list already loaded in
# gender column indexed = 3
# year column indexed = 7
# first name column indexed = 1
'''
top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == 'M' and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] += 1
        else:
            male_name_counts[row[1]] = 1
highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count
for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)
'''
# practice with sum() function
'''
set1 = {1,2,3}
list1 = [1,2,3]
print(sum(set1))
print(sum(list1))
'''
# practice with scopes. note how variables defined in a function/class aren't accessible outside
'''
class Dataset:
    def __init__(self,data): # takes in data list
        self.data = data
    test1 = 10
list1 = [1,2,3,4]
scooby = Dataset(list1)
print(test1)
'''
# pracetice with scopes. note how if a variable/object isn't defined locally, python will look outside to define it
'''
price = 3800
def add_stuff(num):
	return (num + price)		# note how price isn’t defined, so price will = 3800 (global scope)
print(add_stuff(200))
print(price)
'''
# question 1 for step 1, course 2, mission 6. why is scoobydoo not being accepted/defined?
''''
class Dataset:
    def __init__(self,data): # takes in data list
        self.data = data
    scoobydoo = "scoobydoo2"
    def scooby(self):  # method takes in data list, returns "scoobydoo"
        print(scoobydoo)
list1 = [1,2,3]
pet = Dataset(list1)
pet.scooby()
'''
# More pracetice with scopes- functions within functions and which variables are used
'''
two = 4
def add_stuff (num):            # takes in a number, adds 2 to it by calling another function that adds 2 to it, returns result
    two = 2                     # Note!!! how two variable is re-defined within function and overrides global scope above!!!
    def add2(num):              # takes in a number, adds 2 to it, returns result
        new_num = num + two     # TWO WILL REFER TO 2 NOT 4 IN THE OUTER GLOBAL SCOPE!
        return new_num
    new_num = add2(num)
    return new_num
price = 1
new_price = add_stuff(price)
print(new_price)
'''
# Scope Inheritance Limitations:
'''
a = 2
def alter_a():
    a = a + 1
    return a
alter_a()
'''
# practice with global scopes
'''
a = 4
def alter_a():
    global a
    a = 2
    return a
print(alter_a())
print(a)
'''
# practice with global scopes- what will be the output of the following code below?
'''
def new_function():
    global b
    b = 20
print(b)
'''

