n = int(input())

a = list(map(int, input().split()))

a.sort()
result = 0
for i in range(n):
  result += a[i] * (n-i)

print(result)