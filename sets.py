# Sets are used to store multiple items in a single variable.
# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES

# Sets are written with curly brackets { }
fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits) # ignores duplicates

# check if item exists
print("banana" in fruits)

# adding items
fruits.add("orange")
print(fruits)

# adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# removing items
fruits.remove("banana")
print(fruits)

# If you arent sure the item exists use discard()
fruits.discard("kiwi")
print(fruits)

# Set operations (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # combine both (no duplicates)
print(set1.intersection(set2)) # Common elements
print(set1.difference(set2))   # Whats only in set1

"""
MINI CHALLENGE: PARTY GUEST

1. Create two sets:
    - invited_friends = {"Alex", "Sam", "Leo", "Nina"}
    - rsvped = {"Nina", "Sam", "Jordan"}
2. Print:
    - Everyone who was invited (union)
    - Everyone who said theyre coming(rsvped)
    - Who hasnt replied yet (difference)
3. Add two new names to invited_freinds
4. one of the people cancled - remove from rsvped
5. print how many total confirmed guests are attending
6. Check if "Leo" is still coming - print a message depending of result
"""