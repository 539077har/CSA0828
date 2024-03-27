def sort_numbers(numbers, order):
    sorted_numbers = sorted(numbers, reverse=(order == 'desc'))
    return sorted_numbers

# Example usage:
user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = list(map(int, user_input.split()))

order_choice = input("Enter 'asc' for ascending order or 'desc' for descending order: ").lower()

if order_choice in ['asc', 'desc']:
    sorted_numbers = sort_numbers(user_numbers, order_choice)
    print(f"Sorted numbers in {order_choice} order: {sorted_numbers}")
else:
    print("Invalid choice. Please enter 'asc' or 'desc'.")
