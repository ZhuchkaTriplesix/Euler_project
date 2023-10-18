digit = 1
num = 1


def is_simple(num):
    count = 0
    flag = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        flag = 1
    return flag


while num < 10001:
    if is_simple(digit) == 1:
        digit += 1
        num += 1
    else:
        digit += 1

print(num, ":", digit)
