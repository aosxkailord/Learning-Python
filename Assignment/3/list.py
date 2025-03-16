# List Basics

#Create and modify
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#Slicing
print(my_list[1:3])


# Tuples Basics

#Create (immutable)
my_tuple = (1, 2, 3)
print(my_tuple[0])

#Tuple unpacking
a, b, c = my_tuple
print(a, b, c)


# Tuples vs List

#Lists are mutable
my_list1 = [1, 2]
my_list1[0] = 10
print(my_list1)         # [10, 2]

#Tuples are immutable
my_tuple1 = (1, 2)
my_tuple1[0] = 10
print(my_tuple1)         # Error: 'tuple' object does not support item assignment