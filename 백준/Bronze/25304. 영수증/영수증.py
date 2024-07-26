sum = int(input()) #총가격
num = int(input()) #개수
result = 0

for i in range(num):
    a, b = map(int,input().split())
    result += a*b
    
if result == sum:
    print("Yes")
else:
    print("No")