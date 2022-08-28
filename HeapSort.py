'''
Time Complexity of Merge Sort Algo
Best case - O(N*log(N))
Average Case - O(N*log(N))
Worst Case - O(N*log(N))
Space Complexity - Depends
'''

'''
Heap Sort Algorithm
1. first we create a max heap by heapify method 
2. then we swap first element of heap to last element of heap in array
3. and leave the last element or delete
4. than again convert it to max heap 
than again perfrom step 2
'''
# Creats max heap
def heapify(list1, n, parent_indx):
    largest = parent_indx
    left = 2 * parent_indx + 1
    right = 2 * parent_indx + 2
    if left < n and list1[left] > list1[largest]:
        largest = left
    if right < n and list1[right] > list1[largest]:
        largest = right
    if largest != parent_indx:
        list1[largest], list1[parent_indx] = list1[parent_indx], list1[largest]
        heapify(list1, n, largest)


def heap_sort(list1, n):
    # pi means parent node index
    # this creates our max heap by heapify method
    for pi in range(n // 2 - 1, -1, -1):
        heapify(list1, n, pi)
    # le means last element of array or max heap
    for le in range(n - 1, 0, -1):
        list1[le], list1[0] = list1[0], list1[le]
        heapify(list1, le, 0)


if __name__ == "__main__":
    n = int(input("Enter size of list/Array : "))
    list1 = list()
    for i in range(n):
        el = int(input("Enter Array Elements : "))
        list1.append(el)
    print("Entered Array : ", list1)
    heap_sort(list1, n)
    print("Sorted Array : ", list1)
