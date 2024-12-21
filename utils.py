import os

RESULTS_FOLDER = 'results'


def save_results(file_name, ordinal_number, triangular_number, divisors):
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    file_path = os.path.join(RESULTS_FOLDER, file_name)
    string_lines = [
        f"For ordinal number {ordinal_number} the triangular number is: {triangular_number}",
        f'Found {len(divisors)} divisors:',
        *[str(divisor) for divisor in divisors]
    ]

    print('\n'.join(string_lines))
    with open(file_path, 'w') as file:
        file.write('\n'.join(string_lines))

    print(f"Results successfully saved to {file_path}")