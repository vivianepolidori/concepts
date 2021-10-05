list1 = ['banana', 2020, 'apple', 2019]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = ['a', 'b', 'c', 'd']

# Accessing values in lists.

print("list1[0]: ", list1[0])
print("list2[1:5]", list2[1:5])

# Updating values without append.

print("Current value at [1]:", list1[1])
list1[1] = 2021
print("Current value at [1]:", list1[1])

# To remove a list element, you can use either the del statement if you know
# exactly which element(s) you are deleting or the remove() method
# if you do not know.

print(list1)
del list1[2]
print("After deleting value at index 2: ")
print(list1)

# Basic List Operations
# Length
x = len([1, 2, 3])
print(x, "\n")

# Concatenation
x = [1, 2, 3] + [4, 5, 6]
print(x, "\n")

# Repetition
x = ['Hi!'] * 4
print(x, "\n")

# Membership
x = 3 in [1, 2, 3]
print(x, "\n")

# Iteration
for x in [1, 2, 3]:
    print(x)
    
# Reversing a list
print(list1[::-1])

# List comprehension, get only the int values
int_values = [ x for x in list1 if type(x) == int]

# get list element and its position in the same loop
for position, value in enumerate(list1):;
    # Python >= 3.8
    print(f"{position=}, {value=}")
