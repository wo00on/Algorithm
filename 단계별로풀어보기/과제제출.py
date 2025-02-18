
success_list = []
student_list = list(range(1, 31))

for i in range(28):
    a = int(input())
    success_list.append(a)

    
for student in student_list:
    if student not in success_list:
        print(student)
       

"""
students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    students.remove(applied) #소거

print(min(students))
print(max(students))
"""
