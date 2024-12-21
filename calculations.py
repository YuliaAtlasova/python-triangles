def calculate_triangular_number(number):
    return number * (number + 1) // 2


def find_divisors(number):
    divisors = []
    for i in range (1, number+1):
        if (number % i) == 0:
            divisors.append(i)
    return divisors
