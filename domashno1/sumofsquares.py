n=int(input("How many numbers: "))
list=[]
sum=0
for i in range(n):
    list.append(int(input(f"Enter nummber {i+1}:")))
    sum += list[i]*list[i]
print(sum)