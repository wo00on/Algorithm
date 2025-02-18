numbers = []

for _ in range(10):
    a = int(input())
    namugi = a % 42
    numbers.append(namugi)

numbers = list(set(numbers))

print(len(numbers))




    



#
#
# print(numbers)