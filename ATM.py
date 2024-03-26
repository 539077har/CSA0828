def calculate_total(denominations, notes):
    total = 0
    for denom, note in zip(denominations, notes):
        total += denom * note
    return total

if __name__ == "__main__":
    denominations = []
    notes = []

    for i in range(4):
        denom = int(input(f"Enter the {i+1}st Denomination: "))
        notes_count = int(input(f"Enter the {i+1}st Denomination number of notes: "))
        denominations.append(denom)
        notes.append(notes_count)

    total_amount = calculate_total(denominations, notes)
    print("Total Available Balance in ATM:", total_amount)
