"""
Time Complexity of Bubble Sort Algo
Best case - O(N^2)
Average Case - O(N^2)
Worst Case - O(N^2)
Space Complexity - O(N)
"""


def bubble_sort(listf1, n):
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if listf1[j] > listf1[j + 1]:
                listf1[j], listf1[j + 1] = listf1[j + 1], listf1[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    n = int(input("Enter the size of list : "))
    list1 = list()
    for i in range(n):
        el = int(input("Enter element : "))
        list1.append(el)
    print("Entered list :\n", list1)
    bubble_sort(list1, n)
    print("Sorted list :\n", list1)
