"""
A while loop repeats a block of code as long as a condition is TRUE.
Be careful - if the condition never becomes FALSE, you'll get an INFINITE loop

while condition:
    # Code block runs as long as condition is True
"""

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1 # Assignment operator which adds 1 and loop stops at =5

# using BREAK to stop the loop

number = 0

while True:   # infinite loop
    print(number)
    number += 1
    if number == 3:
        break  # stops the loop when it reaches 3

# using CONTINUE to SKIP an iteration
count = 0 

while count < 5:
    count += 1
    if count == 3:
        continue  # SKIP
    print(count)

print("________________________")
# else with while loop
# The else block runs when the loop condition becomes False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished!")

"""
MINI CHALLENGE: PASSWORD CHECKER
1. Ask the user to enter a password
2. Check if it's correct (password: "secret123")
3. If it's wrong, print "Wrong! Try again." and ask again
4. When they enter the correct password, print "Access granted!"
"""

# solution
password = ""   # empty string
while password != "secret123":   # Keeps looping while password is wrong
    password = input("Enter the password: ") 
    if password != "secret123":     # If wrong
        print("Wrong! Try again.")

# once they enter correct password, while condition becomes false, so loop stops
print("Access granted!")
