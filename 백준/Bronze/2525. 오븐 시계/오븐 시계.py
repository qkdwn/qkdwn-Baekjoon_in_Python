h,m =map(int, input().split())
c = int(input())

h += c // 60 #소요시간 c를 60으로 나눈 몫과 나머지
m += c % 60

if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24
    
print(h,m)