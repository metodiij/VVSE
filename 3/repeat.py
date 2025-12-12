n = int(input("How many elements:"))
list=[]
for i in range(n):
    list.append(int(input("Enter element {i+1}")))

duplicates = False
for j in range(len(list)):
    if list.count(list[i])>1:
        duplicates=True

if duplicates:
    print("There are duplicates")
else:
    print("There are no duplicates")
            
