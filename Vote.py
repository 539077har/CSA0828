def check_eligibility(age):
    if age < 0:
        return "Age cannot be negative."
    elif isinstance(age, int) or isinstance(age, float):
        if age >= 18:
            return "You are eligible to vote."
        else:
            years_left = 18 - age
            return f"You are allowed to vote after {years_left} years."
    else:
        return "Invalid input. Please enter a valid age."

if __name__ == "__main__":
    try:
        age = float(input("Enter your age: "))
        print(check_eligibility(age))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
