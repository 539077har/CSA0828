def print_numbers_with_skip(m, n, k):
    current_number = m

    while current_number <= n:
        print(current_number, end=" ")
        current_number += k + 1

# Example usage:
start_num = int(input("Enter the starting number (m): "))
end_num = int(input("Enter the ending number (n): "))
skip_count = int(input("Enter the number of elements to skip (k): "))

print("Numbers from", start_num, "to", end_num, "skipping", skip_count, "numbers in between:")
print_numbers_with_skip(start_num, end_num, skip_count)
