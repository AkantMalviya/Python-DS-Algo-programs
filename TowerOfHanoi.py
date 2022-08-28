"""
Program to calculate total moves that solve Tower of hanoi problem
Recursive representation
"""


# Recursive_Method For Tower of Hanoi
def TowerOfHanoi(n, A, B, C):
    if n == 0:
        print(f"No Disk in Tower {A}")
        return
    if n == 1:
        print(f"Move Disk {n} From {A} to {C}")
    else:
        TowerOfHanoi(n - 1, A, C, B)
        print(f"Move Disk {n} From {A} to {C}")
        TowerOfHanoi(n - 1, B, A, C)


start = "A"
temp = "B"
dest = "C"
print("<\tTower of Hanoi(Recursive Algorithm)>")
n = int(input("Enter Number of Disk in Tower A "))
print("Total moves required : ", pow(2, n) - 1)
TowerOfHanoi(n, start, temp, dest)
