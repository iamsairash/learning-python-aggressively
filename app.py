# letters = ["a", "b", "c"]

# print(enumerate(letters))

# for letter in enumerate(letters):
#     i, l = letter  # unpacking the tuple
#     print(i, l)

#############################################################33
# sort using lamda

# items = [("product1", 10), ("product2", 8), ("product3", 4)]

# items.sort(key=lambda item: item[1]) #### it'll use lamda means annonymous fn, where parameter is item and it return item[1] and the item is each element of items list

# print(items)

#############################################################33

#### map functions

# items = [("product1", 10), ("product2", 5), ("product3", 8)]

#### to get only the price in seperate list

# prices = []

# for item in items:
#     prices.append(item[1])

# print(prices)

#### but we can do same thing using map function in more cleaner way

# prices_obj = map(lambda item: item[1], items)

#### prices_obj is iterable that have price of each item

# prices = list(prices_obj)
# print(prices)


#######################filter function#########################

# items = [("product1", 10), ("product2", 5), ("product3", 8)]

# #### to filter the item with price greater than or equal to 8, we can use filter funtion

# items_obj = filter(
#     lambda item: item[1] >= 8, items
# )  #### it'll return filter object which is itrable

# filterredList = list(items_obj)
# print(filterredList)


################### list comprehension #######################

# items = [("product1", 10), ("product2", 5), ("product3", 8)]

# #### we can use list comprehension to map or filter lists, it is more cleaner and preffered way

# prices = [
#     item[1] for item in items
# ]  ## return item[1] from item(which is a tuple) and the item is each elelment of list items

# ### also to fiter that

# filtered_item = [
#     item for item in items if item[1] >= 8
# ]  # it'll return item where the price is greater that equal to 8

####################### zip function #########################################

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# zipped_obj = zip(
#     list1, list2
# )  ### return zip obj which is again iterable, each obj/item is a tuple like (1, 4) (2, 5) (3, 6)
# print(zipped_obj)

# for item in zipped_obj:
#     print(item)


####################### tuple #########################################

# point = (1, 2)  ### this is a tuple

# point = ()  ##empty tuple

# ## concatenat tuple

# point = (1, 2) + (3, 4)
# print(point)


# point = (1, 2) * 4
# print(point)  #### (1,2,1,2,1,2,1,2)

# point = tuple("Hello")  ### converts any iterable to tuple
# print(point)


# point = 4, 5  ## this is also a tuple

# point = (4,)  ## as there is comma thisi also a tuple

# print(point)


# x = 4
# y = 5

# # the RHS, are tuple with values above, and in LHS, it is unpacking the tuple
# x, y = y, x

# print(x)
# print(y)

# ## by same logic like above we can define multiple variable in one line

# a, b, c = 7, 8, 9
# ## again RHS is a tuple and in LHS, it is unpacking the tuple


####################### array #########################################

# from array import array

# numbers = array("i", [1, 2, 3])  ## this is an array of time singed int
# # use it in large list

## "i" for sign int
## "I" for unsigned int
## "f" for float
## "d" for double
## google it for more


################ set #################### set contains unique elements

# numbers = [1, 1, 2, 2, 3, 4]

# first_set = set(numbers)
# print(first_set)

# second_set = {4, 5, 6}

# print(first_set | second_set)  ## union
# print(first_set & second_set)  ## intersection
# print(first_set - second_set)  ## minus like in set
# print(first_set ^ second_set)  ## common el. remove


########################## dictionries ###########################

# point = {"x": 1, "y": 2}

point = dict(x=1, y=2, z=3, s=4)  ## this looks more cleaner

# print(point2)
# print(point2["y"])

# point2["z"] = 30
# print(point2)

# print(point["a"]) ## we get KeyErro: 'a' as there is not "a" key in poit dict

## we can use
# print(point.get("a"))  ### return none as there is no "a"

# ## we can ser default value

# print(point.get("a", 0))  ### if a xaina vane then return 0

## loop in dict
# for x in point:
#     print(x)  ## the x the key of dict
#     print(x, point[x])

## another way to iterate
# for x in point.items():
#     print(x)  ## here we get tuple of each key value pair ('x', 1) and all

# ## we can unpack those tuple
# for key, val in point.items():
#     print(key, val)


#### dict comprehension ####
# values = [x for x in range(1, 20)]  ## list comprehension
# print(values)

# values = {x: x + 2 for x in range(1, 20)}
# print(values)


#### tuple #####
# from sys import getsizeof

# values = (x * 2 for x in range(500000000000))
# print(getsizeof(values))  ## it is generator obj, it is iterable

# # for val in values:
# #     print(val)

# """
# This is a generator object, and it is iterable.

# Generators are lazy iterables — meaning they **generate a new value on the fly** during each iteration, rather than storing all values in memory at once (like a list or tuple would).

# Because of this, the memory size of the generator object remains very small (usually around 200 bytes), no matter how large the range is.

# This makes generators **much more memory efficient**, especially when working with large sequences of data (e.g., millions or billions of items).

# Only one item is held in memory at any point in time during iteration.
# """
# values = [x * 2 for x in range(1000000)]
# print(getsizeof(values))  # This will use LOTS of memory


############# unpacking operator #################

## this is quite similar to ... spread operator in js

# numbers = [1, 2, 3, 4]
# # print(*numbers)

# list1 = [1, 2]
# list2 = [3, 4]
# # print(*list1, "hello", *list2)

# combined = [*list1, *list2, *"hello"]
# ## this will take out each element from the iterable and put them in list

# print(combined)


# point = 1, 2, 3
# print(*point)  ## just a tuple ko example

#### dict ####
## we have to use ** as unpacking operator in ditc
# first = {"x": 1}
# second = {"x": 10, "y": 2}

# combined = {**first, **second, "z": 20}
# print(combined)


### this is a common interview question
## find the char with multiple occurance in the sentence

# sentence = "this is a common inverview question"

# char_frequency = {}

# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True
# )
# # print(char_frequency_sorted)
# print("The char with multiple occurence is : ", char_frequency_sorted[0])
