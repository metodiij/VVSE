numbers = []
n = int(input("Enter how many elements there are:"))
for i in range(n):
    numbers.append(int(input("Enter element" + {i+1}+  ":")))
numbers.sort()
print("Sorted list:", numbers)
