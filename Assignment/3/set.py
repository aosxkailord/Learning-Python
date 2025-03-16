# Set Basics
#Create from list
my_set = set([1, 2, 2, 3, 3, 3])
print(my_set)

#Add/Remove elements
my_set.add(4)
my_set.remove(2)
print(my_set)       # {1, 3, 4}


# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # {3}

# Difference
print(set_a - set_b)  # {1, 2}


#Set Methods

# Check membership
print(3 in {1, 2, 3})  # True

# Update with another set
my_set = {1, 2}
my_set.update({3, 4})
print(my_set)  # {1, 2, 3, 4}