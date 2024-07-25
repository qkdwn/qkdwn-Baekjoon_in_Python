hour, minute = map(int, input().split())
add = int(input())

h = (hour + ((minute + add)//60)) % 24
m = (minute + add) % 60

print(h,m)