def linearsearchrec(list, size, value):
    if size<0:
        return -1
    if list[size]==value:
        return size
    return linearsearchrec(list,size-1,value)    

size = int(input("Enter length of list : "))
list1 = list()
for i in range(size):
    el  = int(input("Enter Elements : "))
    list1.append(el)
val = int(input("Enter search value : "))
index = linearsearchrec(list1,size-1,val)
if index == -1 :
    print("Search Value not found")
else :
    print(f"Value found at {(index+1)}th Position")