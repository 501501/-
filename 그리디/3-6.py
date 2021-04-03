#n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식 사용
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어떨어지는 수가 1이 될 때까지 1씩 빼기)
    target = (n//k) * k
    result += (n-target)
    n = target
    #n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #k로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)
