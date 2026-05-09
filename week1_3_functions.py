# write 3 functions: one that adds two numbers, one that reverses a string, one that finds the max in a list

# Function 1
def adding():
    number1 = int(input("Enter the 1st number: "))
    number2 = int(input("Enter the 2nd number: "))
    sum_of_num = number1 + number2
    return f"The sum is {sum_of_num}"
print(adding())

# Function 2
def reversestring():
    clientword = input("Enter a single word: ")
    reverseword = clientword[::-1]
    return reverseword
print(reversestring())

# Function 3
def findmax():
    numbers = [int(x) for x in input("Enter multiple numbers: ").split()]
    max_num = max(numbers)
    return max_num
print(findmax())




