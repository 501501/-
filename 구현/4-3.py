n = input()
row = int(n[1])
column = ord(n[0]) - ord('a') + 1
result = 0
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

for i in steps:
    c = column + i[0]
    r = row + i[1]

    if r < 1 or c < 1 or r > 8 or c > 8:
        continue

    result += 1

print(result)
