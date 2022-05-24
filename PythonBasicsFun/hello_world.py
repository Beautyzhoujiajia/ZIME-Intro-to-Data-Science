# __ is 2 underscores "dunder"
# __name__ is an identifier that stores
# "__main__" if the file was run directly
# or the name of the file if it was imported
print("in hello_world.py __name__:", __name__)
if __name__ == "__main__":
    print("hello world!!")
    print("another print")

# this is a one line comment
"""
this is a 
multi line
comments
"""

# two ways to run a python file (AKA
# also known as module)
# 1. directly 
# example: python hello_world.py
# 2. by importing the module from another module