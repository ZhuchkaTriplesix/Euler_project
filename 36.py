def is_palindrome(s):
    return s == s[::-1]


def find_palindromic_numbers(limit):
    palindromic_numbers = []

    for num in range(1, limit):
        decimal_str = str(num)
        binary_str = bin(num)[2:]

        if is_palindrome(decimal_str) and is_palindrome(binary_str):
            palindromic_numbers.append(num)

    return palindromic_numbers


def sum_of_palindromic_numbers(limit):
    palindromic_numbers = find_palindromic_numbers(limit)
    return sum(palindromic_numbers)



limit = 1_000_000
result = sum_of_palindromic_numbers(limit)
print(f"Сумма всех чисел меньше {limit}, являющихся палиндромами в десятичной и двоичной системах: {result}")
