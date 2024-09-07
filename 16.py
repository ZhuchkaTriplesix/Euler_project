"""215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 21000?"""

def sum_of_digits(n):
    digits = str(n)
    total_sum = sum(int(digit) for digit in digits)
    return total_sum

power_of_two = 2 ** 1000

result = sum_of_digits(power_of_two)

print(result)
