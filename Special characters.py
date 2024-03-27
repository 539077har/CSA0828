def count_special_characters(text):
    special_chars = "!@#$%^&*()-_+=[]{}|;:,.<>?/"
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count

def main():
    text = input("Enter a string: ")
    special_count = count_special_characters(text)
    print("Number of special characters:", special_count)

if __name__ == "__main__":
    main()
