n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

for i in range(m):
    i,j = map(int,input().split())
    tmp = numbers[i-1:j]
    tmp.reverse()
    numbers[i-1:j] = tmp
    
for i in range(n):
    print(numbers[i], end=" ")