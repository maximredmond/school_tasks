# Task 1
def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    return product

# Task 2
def iterate_and_sum():
    previous_num = 0
    for current_num in range(10):
        result = current_num + previous_num
        print(f"Current Number: {current_num}, Previous Number: {previous_num}, Sum: {result}")
        previous_num = current_num

# Task 3
def even_index_chars(input_string):
    return input_string[::2]

# Task 4
def remove_chars(input_string, n):
    return input_string[n:]

# Task 5
def is_first_last_same(num_list):
    return num_list[0] == num_list[-1] if len(num_list) > 0 else False

# Task 6
def print_divisible_by_five(num_list):
    for num in num_list:
        if num % 5 == 0:
            print(num)

# Task 7
def count_emma(input_string):
    return input_string.count("Emma")

# Task 8
def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

# Task 9
def combine_odd_even(list1, list2):
    result_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
    return result_list

# Task 10
def extract_digits_reverse(num):
    return [int(digit) for digit in str(num)[::-1]]

# Task 11
def calculate_income_tax(income):
    tax = 0
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.10
    else:
        tax = (10000 * 0.10) + (income - 20000) * 0.20
    return tax

# Task 12
def print_multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()

# Task 13
def print_half_pyramid(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Task 14
def exponent(base, exp):
    return base ** exp
