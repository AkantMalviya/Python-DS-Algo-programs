def BinarySearchRecursive(list,first,last,val):
    if first <= last :
        mid = ( first + last ) // 2
        if list[mid] == val:
            return mid
        else :
            if list[mid]<val:
                return BinarySearchRecursive(list,mid+1,last,val)
            else :
                return BinarySearchRecursive(list,first,mid-1,val)
    else :
        return -1

size = int(input("Enter length of list : "))
list1 = list()
for i in range(size):
    el  = int(input("Enter Elements : "))
    list1.append(el)
val = int(input("Enter search value : "))
first = 0 
last = size-1
index = BinarySearchRecursive(list1,first,last,val)
if index == -1 :
     print("Value not found")
else :
     print(f"Value found at {index+1}th Position")