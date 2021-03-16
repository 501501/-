#방법1 (min() 함수 이용)
n, m = map(int, input().split()) #n:행 m:열
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)