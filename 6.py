array = []
for i in range(1, 101):
    array.append(i)
summ = [i ** 2 for i in array]
summm = 0
for i in array:
    summm += i
result = summm ** 2 - sum(summ)
print(result)
