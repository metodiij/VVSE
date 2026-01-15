class Student:
    def __init__(self, name, gender,points):
        self.name = name
        self.gender =gender
        self.points = points

    def grade(self):
        grade = 2 + (self.points/100)*4
        return grade
    


n= int(input("How many students: "))
students=[]
for i in range(n):
    data=input("Enter name,gender,points(with spaces in between): ").split()
    name = data[0]
    gender = data[1]
    points = int(data[2])
    students.append(Student(name,gender,points))
boyscount=0
girlscount=0
totalall=0
totalboys=0
totalgirls=0
for student in students:
    totalall+=student.grade()
    if student.gender == "M":
        boyscount+=1
        totalboys +=student.grade()
    if student.gender == "W":
        girlscount += 1
        totalgirls += student.grade()

average=round(totalall/n, 2)
if(boyscount>0):
    b_average = round(totalboys/boyscount,2)
else:
    b_average = 0
if(girlscount>0):
    g_average = round(totalgirls/girlscount,2)
else:
    g_average=0

print("Average: ", average)
print("Average for boys: ", b_average)
print("Average for girls: ", g_average)