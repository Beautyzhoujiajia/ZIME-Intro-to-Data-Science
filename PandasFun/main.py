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

# let's start DataFrames
# we can make a DataFrame from a 2D list
# let's have a pop_df w/3 columns
# 1 for City
# 1 for Population
# 1 for Class (small, medium, or large city)
# task: make a 2D list to store this tabular data
pop_data = [
    ["Shanghai", 24.8, "Large"],
    ["Beijing", 21.1, "Large"],
    ["Hangzhou", 7.9, "Medium"],
    ["Zibo", 2.6, "Small"]
]
header = ["City", "Population", "Class"]
pop_df = pd.DataFrame(pop_data, columns=header)
pop_df = pop_df.set_index("City")
print(pop_df) # nicely pretty prints!!

# indexing/slicing
# grab a column by its label (to get a Series)
pop_ser3 = pop_df["Population"]
print(pop_ser3)
# grab a column by its position (to get a Series)
print(pop_df.iloc[:, 0])
# grab a single value
print(pop_df["Population"]["Shanghai"])
print(pop_df.iloc[0, 0])
# use .loc[] to mix label and position based indexing
print(pop_df.loc["Shanghai", "Population"])

# let's do a join demo!!
# let's create a file called regions.csv
# and we will open this file with pandas
# to store its data in a DataFrame
regions_df = pd.read_csv("regions.csv", index_col=0)
print(regions_df)
# then we will join it with pop_df
merged_df = pop_df.merge(regions_df, on=["City"], how="outer")
print(merged_df)

# groupby demo
# let's say we want to compute the average population by Class
grouped_by_class = merged_df.groupby("Class")
print(grouped_by_class["Population"].mean())

# to wrap up...
# let's save our merged_df to a file
merged_df.to_csv("merged.csv")

#warm up
large_df = grouped_by_class.get_group("Large")
print(large_df)

large_df = merged_df(merged_df["class"] == "Large")
print(large_df)
#value_counts
print(len(merged_df["class"].value_counts()))
print(merged_df["class"].unique())
#append
new_row_ser = pd.Series([18.8,"Large","S"],name="Guangzhou",index=merged_df.columns)
merged_df = merged_df.append(new_row_ser)
print(merged_df)
#sort_values
merged_df = merged_df.sort_values("population",ascending=False)
print(merged_df)

