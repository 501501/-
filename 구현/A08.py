# 방법 1
s = input()
length = len(s)
s_num = 0
result = ""
ascii_result = []

for i in range(length):
    # 숫자인 경우
    if str.isdigit(s[i]):
        s_num += int(s[i]) # 숫자 합
    # 알파벳인 경우
    else:
        ascii_result.append(ord(s[i])) # 아스키코드 값으로 변환 후 저장

ascii_result.sort() # 아스키코드 값 기준 오름차순 정렬

for i in ascii_result:
    result += chr(i) # 아스크코드 값을 문자로 변경 후 문자열 합치기

if s_num != 0: # 문자열에 숫자가 하나라도 존재하는 경우
    result += str(s_num) # 문자열 끝에 숫자 결과값 합치기
print(result)

# 방법 2
"""data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))"""
