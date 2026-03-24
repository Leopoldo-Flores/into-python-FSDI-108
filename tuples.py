# Tuples are just like lists - they can store multiple items
# BUT!!! They are IMMUTABLE (you can't change them after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing items
print(my_tuple[0])
print(my_tuple[2])

# Check if item exists
if "apple" in my_tuple:
    print("Yes, apple is in the tuple")

# Length of a tuple
print(len(my_tuple))

# Single item tuple
# You MUST add a comma at the end or python wont recongize it as a tuple
single = ("grape")
print(type(single)) # this is a string
tuple = ("water",)
print(type(tuple))  # this is a tuple

# Nested tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

"""
MINI CHALLENGE Travel Bag

1. Create a tuple called "travel_bag" with at least 5 items
2. Print the SECOND and FORTH items in your bag
3. Check if "shoes" is in your travel bag - if it is, print "Youre ready to walk"
   Otherwise print "You forgot your shoes"
4. Make a new tuple called "essentials" with 3 must have items
5. combine both tuples into one called "final_bag"
6. print how many total items you now have
7. print the last item in your "final_bag"
"""