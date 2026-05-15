# greet — prints directly, returns nothing
def greet(name):
    print(f"Hello {name}! Welcome to my program.")

greet("User")
greet("Rowland")
greet("Human")

# add_numbers — returns a value, prints nothing
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(2, 2))

# print_list - sends a list as an argument, loops through list and prints each item
hobbies = [
    "Gaming",
    "Coding",
    "Driving",
    "Swimming",
    "Reading"
]

def print_list(hobbies):
    for hobby in hobbies:
        print(f"Rowland likes: {hobby}")

print_list(hobbies)