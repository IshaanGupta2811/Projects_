name = input("Enter student name: ")
age = int(input("Enter student age: "))

python_marks = int(input("Enter Python marks: "))
math_marks = int(input("Enter Math marks: "))
english_marks = int(input("Enter English marks: "))
subjects = ("Python", "Math", "English")

student = {
    'Name' : name,
    'Age' : age,
    "Subjects": subjects,
    'marks' : [python_marks,math_marks,english_marks]
}
print("-------------------------------------------")
print("----------Student Report Card--------------")
print("-------------------------------------------")

print("Name : ",name)
print("Age : ",age,"\n")

print("Subject : Marks")
print("-------------------------------------------")

for i in range(len(student["Subjects"])):
    print(student["Subjects"][i], ":", student["marks"][i])

Total=0
for mark in student['marks'] :
    Total= Total + mark

Average = Total/3
print("--------------------------------")
print("Total Marks : ",Total)
print("Average Marks : ",Average)

if(Average>=90):
    print("Grade is A")
elif(Average>=75):
    print("Grade is B")
elif(Average>=60):
    print("Grade is C")
else:
    print("Grade is D")

if Average < 60 :
    print("Result : Fail")
else:
    print("Result : Pass")