count = 1
d = 1
while d < 20:
    if count % d == 0:
        d += 1
    else:
        count += 1
        d = 1
print(count)
