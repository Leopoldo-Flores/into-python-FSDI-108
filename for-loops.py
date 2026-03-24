"""
A for loop in python is a control structure that lets you repeat a block of code for 
each item in a sequence (such as list, string, tuple, range of numbers ect...)

for variable in sequence:
    # Code block runs for each item in the sequence
"""

# Basic example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for letter in "Leopoldo":
    print(letter)

print("_______________________________________")

# range() generates a sequence of numbers
for x in range(5): # Index by 0
    print(x)

print("_______________________________________")
# Start and end range
for x in range(2, 6): 
    print(x)

print("_______________________________________")

# Step
for x in range(0, 10, 2):
    print(x)

"""
MINI CHALLENGE
1. Ask the user to enter a number and store it in a variable called num.
2. Use a for loop with range(1, 11) to repeat 10 times (from 1 to 10).
3. Inside the loop, multiply num by the current loop value(i)
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")