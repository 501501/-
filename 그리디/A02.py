#방법1 - 직접 푼 방법
s = list(input())
result = 0

for i in s:
    if result == 0:
        result += int(i)
    elif int(i) == 1:
        result += int(i)
    elif int(i) == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)

#방법2 - 답안 예시
data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num
    else:
        result += num

print(result)
