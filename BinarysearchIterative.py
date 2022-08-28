"""
Time Complexity of Binary Search Algo
Best case - O(1)
Worst Case - O(log2N)
Space Complexity - O(1)
"""


def BinarySearch(list,size,val):
    first = 0 
    last = size-1
    while first <= last: 
        mid = int((first+last)//2)
        if val == list[mid]:
            return mid
        else :
            if list[mid] < val:
                first = mid + 1
            else:
                last = mid - 1 
    return -1

size = int(input("Enter length of list : "))
list1 = list()
for i in range(size):
    el  = int(input("Enter Elements : "))
    list1.append(el)
val = int(input("Enter search value : "))
index = BinarySearch(list1,size,val)
if index == -1 :
     print("Value not found")
else :
     print(f"Value found at {index+1}th Position")