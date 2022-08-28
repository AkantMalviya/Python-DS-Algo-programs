"""
Time Complexity of Insertion Sort Algo
Best case - O(N)
Average Case - O(N^2)
Worst Case - O(N^2)
Space Complexity - O(N)
"""


def insertion_sort(listf1, n):
    for i in range(1, n):
        current = listf1[i]
        for j in range(i, 0, -1):
            if listf1[j - 1] > current:
                listf1[j] = listf1[j - 1]
                listf1[j - 1] = current


if __name__ == "__main__":
    n = int(input("Enter the size of list : "))
    list1 = list()
    for i in range(n):
        el = int(input("Enter element : "))
        list1.append(el)
    print("Entered list :\n", list1)
    insertion_sort(list1, n)
    print("Sorted list :\n", list1)
