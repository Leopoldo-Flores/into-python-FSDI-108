"""
A function is a block of code that only runs when its called.
We can pass data to funciton (parameters), and they can return data.

def function_name(parameters):
    # Code block (indented)
    # Preform actions using the parameters
    return value # optional
"""

# Simple function without parameters
def my_function():
    print("This is my function") # this runs when the function is called

my_function()

def other_function():
    print("This is another function")

other_function()
my_function()

# Function with parameters
def print_full_name(first_name, last_name, middle_name):
    print(f"The name is: {first_name} {last_name} {middle_name}")

print_full_name("Leo", "Flores", "J")

# Functions that return values
# instead of just printing, functions can send back (return) data.

def get_full_name(fname, lname):
    return f"{fname} {lname}"    # Sends back the full name as text

# Store the returned value in a variable
full_name = get_full_name("Leo", "Flores")
print(full_name)

# functions with default parameters
# A default paremeter means the function will use that value-
# if no arguement is provided when calling the function

def greet(name="student"):
    print(f"Hello, {name}! Welcome to class")

# Calling with no argument -> use the default
greet()

# Calling with agrument -> overrides the default
greet("Leo")