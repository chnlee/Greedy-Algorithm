N,K = map(int,input().split())

lst = []

for i in range(N):
  lst.append(int(input()))

lst.sort(reverse = True)
i = 0
count = 0

for i in lst:
  if(K == 0): break
  count += K // i
  K = K % i

print(count)

