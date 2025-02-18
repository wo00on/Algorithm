T = int(input())

for _ in range(T):
    char = input()*3
    print(char[0] + char[-1])

    

####################################

T = int(input())  # 입력 횟수 입력받기
results = []  # 결과를 저장할 리스트

for _ in range(T):
    char = input() * 3  # 문자열 3번 반복
    results.append(char[0] + char[-1])  # 처음과 마지막 문자 저장

print("\n".join(results))  # 한 번에 출력