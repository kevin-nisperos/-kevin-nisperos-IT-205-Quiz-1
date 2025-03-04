# Python Fundamentals Code

# Variables and Data Types
name = "Kevin"  # String
age = 35  # Integer
height = 5.9  # Float
is_student = True  # Boolean

# Printing output
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Conditional Statements
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Loops
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("Even numbers from 1 to 10:")
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# Function Definition and Calling
def greet(name):
    return f"Hello, {name}! Welcome to Python."

print(greet(name))

# Lists and Basic Operations
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")  # Adding an element
fruits.remove("Banana")  # Removing an element
print("Fruits List:", fruits)

# Dictionary Usage
person = {"name": "Kevin", "age": 34, "city": "Manila"}
print("Person's Name:", person["name"])
person["age"] = 35  # Modifying a value
print("Updated Age:", person["age"])

# File Handling
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
