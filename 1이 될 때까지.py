N, M = map(int, input().split())

count  = 0
while(N>=M):
  while (N % M != 0):
    N -= 1
    count += 1
  N = N // M
  count += 1

while(N>1):
  N -= 1
  count +=1
 # count += (N-1)
print(count)