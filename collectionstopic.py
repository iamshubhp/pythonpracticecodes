# collection = single "variable" used to store multiple values
#  List  = [] ordered and changeable. Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#  Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# --------------------------------------------------------------------------------------------------

# Lists[]

# fruits = ["apple", "banana", "cherry", "orange", "apple"]

# print(help(fruits))  # this open up the methods with discriptions
# print(dir(fruits))  # dictionary to get all the methods we can use for collections
# print(len(fruits)) # Length of the list
# print("pineapple" in the list) # Checks if the element is in the list or not
# fruits[1] = "pineapple"
# fruits.append("pineapple") # adds another value to the collection fruits
# fruits.remove("apple")
# fruits.insert(0, "pineapple") # adds the value at the mentioned index
# fruits.sort()
# fruits.reverse()
# fruits.clear() clears the elements in the list

# for fruit in (fruits):
#     print(fruit)

# --------------------------------------------------------------------------------------------------

# Sets{}

# fruits = {"apple", "banana", "cherry", "orange"}

# print(dir(fruits))
# print(help(fruits))  # this open up the methods with discriptions
# we cannot use index function on the sets as they are unordered
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() # removes whichever element is first as it is unordered everytime

# print(fruits)

# --------------------------------------------------------------------------------------------------

# tuples()

# fruits = ("apple", "banana", "cherry", "orange")

# print(dir(fruits))
# print(help(fruits))  # this open up the methods with discriptions
# print(fruits.index("apple"))
# print(fruits.count("orange"))  # counts the elements

# for fruit in fruits:
# print(fruit)
