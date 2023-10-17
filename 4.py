def palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False


x = 999 ** 2

d = []
for i in range(10000, x + 1):
    flag = palindrome(i)
    if not flag:
        continue
    else:
        d.append(i)
print(max(d))
