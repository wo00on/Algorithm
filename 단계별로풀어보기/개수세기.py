"""N = int(input())
line = list(map(int, input().split()))
a = map(int, input())


for i in range (line):
    if a == i:
        print(i)
                
##############################################"""
N = int(input())
line = list(map(int, input().split()))
a = int(input())

print(line.count(a))
    