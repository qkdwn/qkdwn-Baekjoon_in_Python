num = []

for i in range(10):
    a = int(input())%42
    if a not in num:
        num.append(a)

print(len(num))