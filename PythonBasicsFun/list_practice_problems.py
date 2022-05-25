import random

# 1D PRACTICE PROBLEM 
# Write code that generates 20 random numbers between 1 and 10 inclusive 
# and puts them in a 1D list. 
random.seed(0)
numbers = []
for i in range(20):
    rand_num = random.randrange(1, 11) # [1, 11) -> [1, 10]
    numbers.append(rand_num) # append adds an element to the end of list
print(numbers)

# The program then does the following using the list:
# 1. Prints the numbers all one line, each number separated by a space
def pretty_print(numbers):
    for num in numbers:
        print(num, end=" ")
    print()
pretty_print(numbers)
# 2. Sorts the list using a list method
# numbers.sort() # inplace sort (modifies the list)
# pretty_print(numbers)
# use the built-in sorted function (doesn't modify the list
# produces a new list)
sorted_numbers = sorted(numbers)
pretty_print(sorted_numbers)

# 3. Prints the largest and smallest number in the list
print("min:", min(numbers), "max:", max(numbers))
# Hint: can you take advantage of the current ordering of your list?
print("min:", sorted_numbers[0], "max:", sorted_numbers[-1])

# 4. Determines the number of times a user-specified number is in the list
user_num = int(input("Enter a number in [1, 10]: "))
count = 0
for num in numbers:
    if num == user_num:
        count += 1
print("there are", count, "of", user_num, "in the list")
# 5. Removes all instances of a user-specified number in the list. 
# If the number is not in the list print the message: "Sorry, your number is not here!"
# Note: for practice with functions, try solving this problem using functions :)
user_num = int(input("Enter a number in [1, 10] to remove: "))
if user_num not in numbers:
    print("Sorry, your number is not here!")
else: #user_num in numbers
    while user_num in numbers:
        numbers.remove(user_num)

print(sorted(numbers))
print()


# 2D LIST PRACTICE PROBLEMS
# Write code that generates 50 random numbers 
# between 1 and 10 inclusive and puts them in a 2D list 
# that is 10x5 (e.g. 10 rows and 5 columns). The program 
# then does the following using the list:
# 2D list is a nested list
# or in other words it is 1D where each element is a list
table = []
for _ in range(10):
    row = []
    for _ in range(5):
        rand_num = random.randint(1, 10)
        row.append(rand_num)
    table.append(row)
print(table)

# 1. Prints the numbers in a nice grid format (like a table)
for row in table:
    for value in row:
        print(value, end="\t")
    print()

# 2. Prints the largest and smallest number in the list
# assume the first element in the first nested list is the smallest and largest number
smallest = table[0][0]
largest = table[0][0]
for row in table:
    if min(row) < smallest:
        smallest = min(row)
    if max(row) > largest:
        largest = max(row)
print("smallest:", smallest, "largest:", largest)

# 3. Determines the number of times a user-specified number 
# is in the list
# user_num = int(input("Enter a number in [1, 10]: "))
# count = 0
# for row in table:
#     for num in row:
#         if num == user_num:
#             count += 1
# print("there are", count, "of", user_num, "in the list")

# 4. Removes all instances of a user-specified number in the list.
# If the number is not in the list print the message: 
# "Sorry, your number is not here!"
user_num = int(input("Enter a number in [1, 10] to remove: "))
found = False 
for row in table:
    while user_num in row:
        found = True
        row.remove(user_num)

if not found:
    print("Sorry, your number is not here!")
else:
    print(table)

# Note: for practice with functions, try solving this 
# problem using functions :)