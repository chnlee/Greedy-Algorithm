#1
A = input()
B = []
for i in A:
  i = int(i)
  B.append(i)
if(B[0]+B[1]>B[0]*B[1]):
  result = B[0]+B[1]
else:
  result = B[0]*B[1]
i = 2
for k in range(len(A)-2):
  if(result+B[i]> result*B[i]):
    result += B[i]
  else:
    result *= B[i]
  i += 1
print(result)
#2
A = input()

result = int(A[0])

for i in range(1, len(A)):
  num = int(A[i])
  if (num <=1 or result <= 1):
    result += num

  else:
    result *= num

print(result)
