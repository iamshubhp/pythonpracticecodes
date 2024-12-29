# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA" : "Washington Dc",
            "India" : "New Delhi",
            "Russia" : "Moscow",
            "China" : "Beijing"
           }

# print(dir(capitals)) #prtins all the methods in dictionaries
# print(help(capitals)) # all the methods we can use in the dictionary capital.

# print(capitals.get("Russia"))

# if capitals.get("India"):
#    print("This capital exist")
    
# else:
#    print("It does not exist")

# capitals.update({"Germany" : "Berlin"})
# capitals.pop("China") # removes the inserted key value
# capitals.popitem() # no key required. will remove the latest key added to the dictionary
# capitals.clear() # clears the dictionary

# key = capitals.keys() # keys method prints all the keys in dictionary. keys method is iterable so we can use loops 
# for key in capitals.keys():
    # print(key)

# values = capitals.values() # values method prints all the values of the keys. also iterable.
# for values in capitals.values():
# #   print(values)

items = capitals.items()

for key, value in capitals.items():
    print(f"{key} : {value}")