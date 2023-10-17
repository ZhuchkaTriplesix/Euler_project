def fibonacci(num):
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


fib10 = []
for i in range(1, 12):
    fib10.append(fibonacci(i))
fib10.pop(0)
print(*fib10)
