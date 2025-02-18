N = int(input())
line = list(map(int, input().split()))
a = int(input())
count=0


for i in line:
    if a == i:
        count+=1
print(count)
                
##############################################

N = int(input())
line = list(map(int, input().split()))
a = int(input())

print(line.count(a))
