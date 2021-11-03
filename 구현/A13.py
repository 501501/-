from itertools import combinations

# 도시의 크기 N
# 폐업시키지 않을 치킨집 최대 개수 M
n, m = map(int, input().split())

# 도시 정보
city = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    city[i] = list(map(int, input().split()))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        # 집 위치
        if city[i][j] == 1:
            house.append([i, j])
        # 치킨 집 위치
        if city[i][j] == 2:
            chicken.append([i, j])

# 치킨 집 조합
comb = list(combinations(chicken, m))

distance = []
result = []
for i in range(len(comb)):
    for h in house:
        d = []
        for j in range(m):
            d.append(abs(h[0] - comb[i][j][0]) + abs(h[1] - comb[i][j][1]))
        distance.append(min(d))

distance_sum = 0
for i in range(len(distance)):
    distance_sum += distance[i]
    if (i+1) % len(house) == 0:
        result.append(distance_sum)
        distance_sum = 0

print(min(result))

