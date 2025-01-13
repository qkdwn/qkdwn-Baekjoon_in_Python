n = int(input())

current_grade = list(map(int, input().split()))

max_grade = max(current_grade)
sum_grade = 0

for i in range(n):
    sum_grade += current_grade[i] / max_grade * 100
    
new_average = sum_grade / n
print(new_average)