# if -> checks a condition
# elif -> (else if) checks another conditoin if the first is False
# else -> runs if all other conditions are False

# if file or varible is mostly typed out hit TAB to automatically fill it out
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# Short Hand IF Statements

if x > 5: print("x is greater than 5")

# short hand if...else

print("Even") if x % 2 == 0 else print("Odd")

# Nested If statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining Condition
age = 18

if age >= 18 and age <=21:
    print("You are between 18 and 21 years old!")

"""
MINI CHALLENGE

1. ask user to enter today's temperature in ferenheit and store it in a variable called temperature
2. use if-elif-else statements to classify the temperature:
    If temp >= 86, print "It's hot outside!"
    If temp >= 68, and temp < 86, print "The weather is nice."
    If temp >= 50 and temp < 68, print "It's a bit chilly"
    otherwise, print "Its Cold." (else)
3. Create a variable called jacket:
    Set it to True if temp < 59, otherwise False.
4. Bonus: If jacket is True, print "Better wear a jacket!", otherwise print "No jecket needed"

"""