import random

# Place holder to store the list elements
list_elements = []

# Creates a list with 10 random two digit numbers
for i in range(10):
    list_elements.append(random.randrange(10, 99))
print("List to be sorted: {}".format(list_elements))

# Bubble sort: Compares adjacent elements
for i in range(len(list_elements)):
    for j in range(len(list_elements)-i-1):
        if list_elements[j] > list_elements[j+1]:
            list_elements[j + 1], list_elements[j] = list_elements[j], list_elements[j+1]
print("Sorted Lits: {}".format(list_elements))



