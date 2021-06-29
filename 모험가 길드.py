# 오름차순
# 공포도 <= 모험가 수 임을 파악하는 문제
n = int(input())
A = list(map(int,input().split()))
A.sort()

num = 0 # 총 모험가 수
count = 0 # 여행의 수
for i in A: #i는 공포도를 의미함
  num += 1
  if(i <= num):
    num = 0
    count +=1

print(count)