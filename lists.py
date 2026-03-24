# Lists are used to store MULTIPLE items in a single variable.
# Think of a container that can hold many items
# Lists are written with square brackets [ ] 

my_list = [10, 20, 30, 40, 50]
print(my_list)

# List can contain different data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# You can access list itmes by their INDEX number
# (Indexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # First item (apple)
print(fruits[2]) 

# You can also use a NEGATIVE indexes to count from the end
print(fruits[-2])

# Modifying List Items
fruits[1] = "mango" # change banana -> mango
print(fruits)

# Adding Items
fruits.append("orange") # Adds to the END
print(fruits)

fruits.insert(1, "kiwi") # Adds to a SPECIFIC index
print(fruits)

# Removing Item
fruits.remove("apple") # Removes by value
print(fruits)

fruits.pop()           # Removes last item
print(fruits)

# Looping through a list
for fruit in fruits:
    print(fruit)

# check if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

# List Length
print(len(fruits)) # Number of items in list