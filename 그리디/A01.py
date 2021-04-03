#방법1 (내림차순 정렬) -직접 푼 방법
n = int(input()) #인원 수
k = list(map(int, input().split())) #공포도

result = 1
li = [] #인덱스 리스트
x = 0 #인덱스 번호
k.sort(reverse=True) #내림차순 정렬

while True:
    if n == 1 | k[0] == n : #인원 수가 1이거나 최고 공포도와 인원 수가 같은 경우
        break

    li.append(x)
    x += k[x]
    result += 1

    if x+k[x] == n:
        break

print(result)

#방법2 (오름차순 정렬) -교재 예시
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i : #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그룹에 포함된 모험가의 수 초기화

print(result)
