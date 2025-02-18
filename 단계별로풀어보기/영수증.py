X = int(input())   #총 금액
N = int(input())   #물건의 종류 수 
sum = 0

for _ in range(N):
    a, b = map(int, input().split())  #a가격, b개수
    sum += a * b

if sum == X:
    print('Yes')

else :
    print('NO')
    

#
money = int(input())
n = int(input())
s = 0
for i in range(n):
    a, b = map(int, input().split())
    s += a * b
if s == money:
    print("Yes")
else:
    print("No")