"""
Time Complexity of Selection Sort Algo
Best case - O(N^2)
Average Case - O(N^2)
Worst Case - O(N^2)
Space Complexity - O(N)
"""


def selection_sort(listf1, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if listf1[j] < listf1[min_index]:
                min_index = j
        if i != min_index:
            listf1[i], listf1[min_index] = listf1[min_index], listf1[i]


if __name__ == "__main__":
    n = int(input("Enter the size of list : "))
    list1 = list()
    for i in range(n):
        el = int(input("Enter element : "))
        list1.append(el)
    print("Entered list :\n", list1)
    selection_sort(list1, n)
    print("Sorted list :\n", list1)
