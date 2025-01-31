a = int(input())  # 첫 번째 숫자 입력
b = input()        # 두 번째 숫자 입력 (문자열로 받기)

# 각 자리 수에 대해 곱셈
a1 = a * int(b[2])  # 3의 자리
a2 = a * int(b[1])  # 2의 자리
a3 = a * int(b[0])  # 1의 자리
a4 = a * int(b)     # 전체 숫자

# 결과 출력
print(a1)
print(a2)
print(a3)
print(a4)