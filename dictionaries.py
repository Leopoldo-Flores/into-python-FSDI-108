# Dictionaries store data in KEY:VALUE pairs.
# Written with curly brackets {}

student = {
    "name" : "Leo",
    "age" : 23,
    "major" : "Computer Science"
}
print(student)

# Accessing Items
print(student["name"]) # Access by KEY
print(student.get("major")) # another way to access

# Adding Items
student["graduation_year"] = 2025
print(student)

# Changeing Values
student["age"] = 25
print(student)

# Removing Items
student.pop("major") # Removes Key:Value
print(student)

# Check IF a key exists
if "name" in student:
    print("Key 'name' exists in the dictionary!")

# Nested Dictionary
studnets = {
    "student1" : {"name": "Leo", "age": 22},
    "student2" : {"name": "Alex", "age": 21}
}
print(studnets["student2"]["age"]) # Access nested value


"""
MINI CHALLENGE - Student Report Card
You need to store and analyze a student's grades.

1. create a dictionary called "report_card" with keys:
    - "name"
    - "subject"
    - "grades" (use a tuple with 3 numbers)
# EXAMPLE: {"name:"Leo",... "grades":(90,85,88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum()  and len())
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above-> print "EXCELLENT!"
   If between 70 and 89 -> print "Good Job"
   otherwise - print "Needs Improvement"
6. remove the "subject" key and print the updated dictionary

"""