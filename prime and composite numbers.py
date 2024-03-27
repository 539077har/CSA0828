def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes_and_composites(numbers):
    prime_count = 0
    composite_count = 0

    for num in numbers:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1

    return prime_count, composite_count

# Example usage:
user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = list(map(int, user_input.split()))

prime_count, composite_count = count_primes_and_composites(user_numbers)

print(f"Prime numbers: {prime_count}")
print(f"Composite numbers: {composite_count}")
