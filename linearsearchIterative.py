"""
Time Complexity of Linear Search Algo
Best case - O(1)
Worst Case - O(N)
Space Complexity - O(1)
"""


def linearsearch(size, list, val):
    for i in range(size):
        if val == list[i]:
            return i
    else:
        return -1


size = int(input("Enter length of list : "))
list1 = list()
for i in range(size):
    el = int(input("Enter Elements : "))
    list1.append(el)
val = int(input("Enter search value : "))
index = linearsearch(size, list1, val)
position = index + 1
print("Position of Value : ", position)
