from calculations import calculate_triangular_number, find_divisors
from utils import save_results


def calculate_triangular_number_and_divisors(number):
    triangular_number = calculate_triangular_number(number)
    divisors = find_divisors(triangular_number)
    save_results('triangular_for_ordinal_number.txt', number, triangular_number, divisors)


def find_triangular_number_with_amount_of_divisors(required_divisors, max_iterations=1000):
    for ordinal_number in range(1, max_iterations + 1):
        triangular_number = calculate_triangular_number(ordinal_number)
        divisors = find_divisors(triangular_number)

        if len(divisors) >= required_divisors:
            save_results('triangular_with_required_divisors.txt', ordinal_number, triangular_number, divisors)
            return

    print(f'Required amount of divisors is too big. The program stopped after {max_iterations} iterations.')


def main():
    print("Choose an option:")
    print("1. Calculate triangular number and find its divisors.")
    print("2. Find triangular number with a required amount of divisors.")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        number = int(input("Enter ordinal number: "))
        calculate_triangular_number_and_divisors(number)

    elif choice == "2":
        divisors = int(input("Enter required divisor amount: "))
        max_iter_input = input("Enter maximum iterations (press Enter for default 1000): ").strip()
        max_iter = int(max_iter_input) if max_iter_input else 1000
        find_triangular_number_with_amount_of_divisors(divisors, max_iter)

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == '__main__':
    main()
