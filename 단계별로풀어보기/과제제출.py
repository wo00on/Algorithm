
success_list = []
student_list = list(range(1, 31))

for i in range(28):
    a = int(input())
    success_list.append(a)

    if a not in student_list:
        print(a) 



