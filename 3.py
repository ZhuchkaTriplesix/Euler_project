num = 600851475143
count = 1
while num != 1:
    count += 1
    if num % count == 0:
        num /= count

print(count)
