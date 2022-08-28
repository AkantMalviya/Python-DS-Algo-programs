#Divide and Conquar Merge sort Algorithm
'''
Time Complexity of Merge Sort Algo
Best case - O(N*log(N))
Average Case - O(N*log(N))
Worst Case - O(N*log(N))
Space Complexity - Depends
'''
def mergesort(list):
    if len(list) > 1 : 
        left_arr = list[:len(list)//2]
        right_arr = list[len(list)//2:]
        #recursion
        mergesort(left_arr)
        mergesort(right_arr)
        #merge
        i = 0 #leftarray index
        j = 0 #rightarray index
        k = 0 #merged list index
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j] :
                list[k] = left_arr[i]
                i+=1
            else:
                list[k] = right_arr[j]
                j+=1
            k+=1
        #for single element left in both array merged into list
        while i<len(left_arr):
            list[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            list[k] = right_arr[j]
            j+=1
            k+=1    


if __name__ == "__main__":
    size = int(input("Enter the size of the list : "))
    list1 = []
    for i in range(size): 
        el = int(input("Enter Elemnets : "))
        list1.append(el)
    print("Entered list : \n",list1)
    mergesort(list1)
    print("Sorted list : \n",list1)