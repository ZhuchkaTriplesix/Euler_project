def sum_of_digits(n):
    digits = str(n)
    total_sum = sum(int(digit) for digit in digits)
    return total_sum

power_of_two = 2 ** 1000

result = sum_of_digits(power_of_two)

print(result)
