def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return x * y // find_gcd(x, y)

def find_lcm_of_numbers(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = find_lcm(lcm, numbers[i])
    return lcm

def find_gcd_of_numbers(numbers):
    gcd = numbers[0]
    for i in range(1, len(numbers)):
        gcd = find_gcd(gcd, numbers[i])
    return gcd

if __name__ == "__main__":
    try:
        N = int(input("N value: "))
        if N <= 0:
            print("N should be a positive integer.")
        else:
            numbers = []
            for i in range(1, N + 1):
                num = int(input(f"Number {i}: "))
                numbers.append(num)

            lcm = find_lcm_of_numbers(numbers)
            gcd = find_gcd_of_numbers(numbers)

            print("LCM =", lcm)
            print("GCD =", gcd)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
