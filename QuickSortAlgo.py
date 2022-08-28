'''
Time Complexity of Quick Sort Algo
Best case - O(N*log(N))
Average Case - O(N*log(N))
Worst Case - O(N^2)
Space Complexity - O(N)
'''


def partition(list,low,high):
    pivot = high
    high-=1
    while low < high:
        while list[low] < list[pivot] and low <= pivot :
            low+=1
        while list[high] > list[pivot] and high >= 0  :
            high-=1
        if low < high :
            list[low] , list[high] = list[high], list[low]
    if list[low] > list[pivot]:
         list[low], list[pivot] = list[pivot] , list[low]
    return low

def quicksort(list,low,high):
    if low < high : 
        pi = partition(list,low,high)
        quicksort(list,low,pi-1)
        quicksort(list,pi+1,high)

if __name__ == "__main__":
        size = int(input("Enter size of the list : "))
        list1 = []
        for i in range(size):
            el = int(input("Enter elements :"))
            list1.append(el)
        print("Entered list :\n",list1)
        low = 0 
        high = size-1
        quicksort(list1,low,high)
        print("Sorted list : \n",list1)
