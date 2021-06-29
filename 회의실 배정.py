n = int(input())

lst = [[int(x) for x in input().split()] for y in range(n)]

lst.sort()
print(lst)
x = 0
count = 1
for i in range(1,n):
  if(lst[i][0] >= lst[x][1]):
    x = i
    count += 1
    print(lst[i])
print(count)
