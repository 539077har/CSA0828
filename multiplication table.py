def print_multiplication_table(m, n):
    print(f"Multiplication table for {m} up to {n}:")

    for i in range(1, n + 1):
        result = m * i
        print(f"{m} x {i} = {result}")

# Example usage:
member_m = int(input("Enter the member (m) for the multiplication table: "))
limit_n = int(input("Enter the limit (n) for the multiplication table: "))

print_multiplication_table(member_m, limit_n)
