
line = []

for _ in range(9):
    a = int(input())
    line.append(a)

print(max(line))
print(line.index(max(line))+1)
    
