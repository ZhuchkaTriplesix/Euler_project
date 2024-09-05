num = int(input())
nums = []
for i in range(1, num+1):
    if i % 3 == 0 or i % 5 == 0:
        nums.append(i)
print(*nums)
#123