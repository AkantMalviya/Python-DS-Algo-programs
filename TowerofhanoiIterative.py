"""
Program to calculate moves that solve Tower of hanoi problem
Iterative representation
"""
print("<\tTower of Hanoi (Iterative Method)>")
n = int(input("Enter the number of disk in tower A"))
start = "A"
temp = "B"
dest1 = "C"
total_moves = (pow(2, n) - 1)
if n % 2 == 0:
    dest1, temp = temp, dest1

for i in range(1, total_moves + 1):
    if n == 0:
        print("No Disk in Tower A")
        break
    if n == 1:
        print(f"Move Disk {1} From {start} to {dest1}")
        break
    if i % 3 == 1:
        print(f"Move Disk {1} From {start} to {dest1}")
    if i % 3 == 2:
        print(f"Move Disk {1} From {start} to {temp}")
    if i % 3 == 0:
        print(f"Move Disk {1} From {temp} to {dest1}")
