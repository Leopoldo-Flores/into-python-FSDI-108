print("Hello World from Python!") # No semicolons needed
print(2)
print(5 + 3)
print(True)

# shortcuts
# Save file- ctrl + s 
# Run last command in terminal - up arrow

# COMMENTS adsfjasdlf
# jalsdfldsf

""" 
This is a comment
    this too
asdfasdf
"""

# Variables and concatenation
name = "Leo"
age = 23
print(name) # prints the variable value

# concatenation (joining stings with +)
# concatination cant combine string and integer
# Fix it- cast age to string using str()
print("My name is " + name + " and I am " + str(age) + " years old.")

name = "Michale"
age = 30
middle_name = "Javier"
last_name = "Flores"
found = False  # Boolean variable

print(name)
print("My name is " + name + " and I am " + str(age) + " years old.")
print("Did he show up to class? " + str(found))

# MINI CHALLENGE
"""
Write a short story using variables.
Steps:
1. Declasre and intitialize variables (strings and numbers)
2. use print() and concatenation to tell the story
3. Run the program in the terminal
"""

# F-string
# Cleaner way to format strings
work = "sdgku"
job = "professor"
# start with f"", variable in {}
print(f"I work at {work} my job is {job}!")

# Multi-line f-string
print(f"""
my name is {name} {middle_name} {last_name}
I like python!
    Type    indentations   
""")

# type function
print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(found))  #<class 'bool'>

# casting (changing data types)
print(20 + int("20"))
print(20 + age)
print(20 + 2.98)

# User input
# input() lets the user type values into the terminal
user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

# input() always returns a string
print(input("Enter your age: "))

# Example: converting input to int
new_age = int(input("Enter your age: "))
print(age + new_age)

# MINI CHALLENGE 2
"""
Pizza Calculator
    - Ask how many slices of pizza and how many people # 2 variables
    - Use math operators to calculate slices per person # divide the 2 variables
    - Show to result with an f-string
"""

"""
pushing to gitrepo
1. git init
2. git add .
3. git commit -m "Initial commit"
4. git push
"""

