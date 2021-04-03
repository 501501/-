#방법1 (단순한 방법)
n, m, k = map(int, input().split()) #n:배열의 크기, m:숫자가 더해지는 횟수, k:연속으로 k번까지 가능
data = list(map(int, input().split())) #n개의 수를 공백으로 구분하여 입력받기

data.sort()
first = data[n-1] #제일 큰 수
second = data[n-2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second #두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)

#방법2 (수열 이용)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first #가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)