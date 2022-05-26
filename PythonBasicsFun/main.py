import hello_world

# lets start with lists
# they can grow and shrink in size
# they can have mixed types
# they also are objects
# they have attributes (AKA fields) and methods
# recall method invocation syntax: <object reference>.<method name>()

nums = [8, 2, 4, 3, 1]
print(nums)

# built-in functions
print("number of elements:", len(nums)) # length
print("sum:", sum(nums))
print("min:", min(nums))

# list methods
nums.append(100)
print(nums)
first_elem = nums.pop(0) # index to remove
print(nums)
print("first elem:", first_elem)
nums.remove(100) # first occurence of 100 to remove
print(nums)

# 2D lists
# AKA nested lists
matrix = [[0, 1, 2], [3, 4, 5]] # 2x3 grid, matrix, table, etc.
# 2 "rows" (lists)
# each "row" has 3 elements (columns)
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

def add_one(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] += 1

print("matrix before:", matrix)
add_one(matrix)
print("matrix after:", matrix)
# objects are pass by object reference in python
# which means that references are copied by value
# and with a copy of the reference, you can modify the object
# the reference refers to
# https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

def clear_out(table):
    table = []

print("matrix before:", matrix)
clear_out(matrix)
print("matrix after:", matrix) 
