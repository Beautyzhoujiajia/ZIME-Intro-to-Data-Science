import pandas as pd # by convention

# pandas is short for "panel data"
# it is built on top of numpy (is short for "numerical python")
# 2 main reasons to use pandas for data science
# 1. label-based indexing (in addition to position-based indexing)
# 2. really great builtin functionality for indexing, cleaning,
# computing statistics, etc.

# there are 2 main objects in pandas
# 1. Series: 1D data
# 2. DataFrame: 2D data

# let start with Series
populations = [24.8, 21.1, 7.9, 2.6] # 1D data
cities = ["Shanghai", "Beijing", "Hangzhou", "Zibo"] # data's labels
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)

# we can name a Series
# this is really helpful if we are going to
# insert this Series as a column in a DataFrame
pop_ser.name = "Population"
print(pop_ser)

# indexing/slicing
# we can use a label to get a value
print(pop_ser["Beijing"])
print(pop_ser[["Beijing", "Zibo"]])
print("**")
print(pop_ser["Beijing": "Zibo"]) # inclusive of stop
# we can still do position-based indexing (use .iloc[])
print(pop_ser.iloc[1])
print(pop_ser.iloc[[1, 3]])
print(pop_ser.iloc[1: 3]) # exclusive of stop

# summary statistics
print("average population:", pop_ser.mean())
print("standard deviation population:", pop_ser.std())

# we can add new data to a Series
# very similar to how you add a new key:value pair to a dictionary
# dog_ages = {}
# dog_ages["rex"] = 5
# print(dog_ages)
pop_ser["Liuzhou"] = 2.1
print(pop_ser, len(pop_ser), pop_ser.shape)

# we can create an empty Series
pop_ser2 = pd.Series(dtype=float)
pop_ser2["Liuzhou"] = 2.1
print(pop_ser2)